""" todo
- serving animations
- client cap
- animations
- swap demon
- effects
- stat improvement and training
"""


init python:
    from copy import copy
    class summontry_demon:
        def __init__(self, name, image, stats, mana):
            self.name = name
            self.image = image
            self.stats = stats

            self.x = 0
            self.y = 0

            self.mana = mana

    class summontry_client:
        def __init__(self, name, image, stats, pos, mana = None):
            self.name = name
            self.image = image
            self.stats = stats

            self.chant_delay = 10
            self.chant_duration = 10
            self.serve_duration = 10

            self.mana = mana or random.randint(80, 100)
            self.x, self.y = pos
            self.parent = None
            self.demon = None
            self.stat = "idle"

            self.selected_stat = None

    class summontry_handler:
        def __init__(self, demons, clients):
            self.demons = demons
            self.clients = clients
            self.hovered_client = None
            self.holding = None
            self.stat = "start"
            self.client_cap = 3
            self.holding_pos = (-200,-200)
            self.mana = 0
            self.missed = 0
            self.time = 0
            self.stat = "start"
            self.tonights_gain = 0
            self.spawn_timer = 0  # Timer for spawning clients
            self.spawn_sequence = iter(clients)  # Create an iterator for the clients
            self.current_client = None  # To keep track of the current client in sequence
            self.mana_gain_timers = {}
            self.spawn_positions = [
            (-475,95),
            (-475, -211),
            (460, -100),
            (460, 185),
            (460, -370)
            ]
            self.occupied_positions = [None] * len(self.spawn_positions)

        def clicked_portal(self, client):
            renpy.play("summontry/rotate_up.ogg", "sound")

            if client.demon:
                if self.holding:
                    # Swap demons between the client and the holding slot
                    old_demon = client.demon
                    client.demon = self.holding
                    # Dynamically set serve duration based on demon-client stat comparison
                    client.serve_duration = self.calculate_serve_duration(client, self.holding)
                    client.stat = "serving"
                    self.holding = old_demon
                    self.demons.append(old_demon)



                    self.holding = None
                    return
                else:
                    # Pick up the demon from the client
                    self.holding = client.demon
                    client.demon = None
                    client.waiting_duration = client.serve_duration
                    client.stat = "waiting"
                    return

            if not self.holding:
                # Just hover over the client, no demon in hand
                self.hovered_client = client
                return

            # Place the demon onto the client
            client.demon = self.holding
            client.serve_duration = self.calculate_serve_duration(client, self.holding)
            if client.stat == "waiting":
                client.serve_duration = client.waiting_duration
            client.stat = "serving"

            self.mana_gain_timers[client] = 5

            self.holding = None


        def calculate_serve_duration(self, client, demon):
        
            ##Calculates the serve duration based on the demon's stats and the client's selected stat.
            ##Better matches result in shorter serve durations.

            # Assume the client's selected stat is a tuple (stat_name, required_value)
            client_stat_name, client_required_value = client.selected_stat

            # Get the demon's stat for the selected stat
            demon_stat_value = demon.stats.get(client_stat_name, 0)

            # Compare the demon's stat to the client's requirement and adjust serve duration
            if demon_stat_value >= client_required_value:
                # Good match: shorter serving time (e.g., between 10-15 seconds)
                return random.randint(30, 40)
            elif demon_stat_value < client_required_value:
                # Bad match: longer serving time (e.g., between 20-30 seconds)
                return random.randint(15, 25)
            
        def clicked_out(self):
            self.hovered_client = None
            if not self.holding:
                return
            renpy.play("summontry/rotate_up.ogg", "sound")
            self.holding_pos = (-200,-200)
            self.demons.append(self.holding)
            self.holding = None
        def update_holding(self):
            self.holding_pos = renpy.get_mouse_pos()
        def clicked_demon(self, demon):
            if self.stat in ["start", "day"]:
                return
            if self.holding:
                self.demons.append(self.holding)
            self.holding_pos = (-200,-200)
            self.holding = demon
            self.demons.remove(demon)
        def calculate(self, client):
            for key, value in client.demon.stats.items():
                if key == client.selected_stat[0]:
                    demon_stat_value = client.demon.stats[key]
                    client_stat_value = client.selected_stat[1]

                    # Compare the demon's stat to the client's selected stat
                    if demon_stat_value >= client_stat_value:
                        
                        gain_amount = 11
                        
                        # Adjust this if needed
                    elif demon_stat_value < client_stat_value:
                        
                        gain_amount = 7
                        
                        
                    
                    # Other operations (sound effects, etc.)
                    renpy.play("summontry/bubble_7.ogg", "sound")
                    spawn_mana(client.x, client.y, gain_amount, self)
                    
                    
                    
        def gain_mana(self, amount):
            self.mana += amount
        def tick(self):
            if self.time > 1:
                self.time -= 1
            else:
                self.end_night()
                return

            self.spawn()

            for i in self.clients:
                if i.stat == "idle":
                    pass
                elif i.stat == "ready":
                    i.chant_delay -= 1
                    if i.chant_delay <= 0:
                        i.stat = "chanting"
                        renpy.play("summontry/fail.ogg", "sound")
                elif i.stat == "chanting":
                    i.chant_duration -= 1
                    if i.chant_duration <= 0:
                        i.stat = "idle"
                        renpy.play("summontry/shed.ogg", "sound")
                        self.release_slot(i)
                elif i.stat == "serving":
                    i.serve_duration -= 1
                    
                    # Decrease demon's mana while serving
                    if i.demon:
                        i.demon.mana -= 1  # Decrease mana each tick
                        if i.demon.mana < 0:
                            i.demon.mana = 0  # Ensure mana doesn't go below zero
                        
                        # Check if the demon's mana has reached 0
                        if i.demon.mana == 0:
                            # Return the demon to the bench
                            self.demons.append(i.demon)
                            i.demon = None
                            
                            # Set client to "waiting" when demon's mana is 0
                            i.waiting_duration = i.serve_duration  # Set remaining time as waiting_duration
                            i.stat = "waiting"
                            renpy.play("summontry/return_bench.ogg", "sound")  # Play a sound when the demon returns to the bench
                            continue  # Skip further processing for this client as the demon is no longer serving
                    self.mana_gain_timers[i] -= 1  # Decrease the timer
                    if self.mana_gain_timers[i] <= 0:
                        self.calculate(i)  # Gain 10 mana every 5 seconds (adjust as needed)
                        self.mana_gain_timers[i] = 5 
                    
                    
                    if i.serve_duration < 0:
                        self.demons.append(i.demon)
                        i.demon = None
                        i.waiting_duration = i.serve_duration  # Set remaining time to waiting_duration
                        i.stat = "waiting"
                elif i.stat == "waiting":
                    i.waiting_duration -= 1
                    if i.waiting_duration <= 0:
                        i.stat = "idle"  # Set to idle when waiting time runs out
                        self.release_slot(i)

            # Call to regenerate mana for demons on the bench
            self.regenerate_mana_for_bench()
            
            # Continue the spawning process
            

        def regenerate_mana_for_bench(self):
            for demon in self.demons:
                # Regenerate mana if demon is on the bench
                demon.mana += 3  # Increase mana by 1 each tick
                if demon.mana > 100:  # Ensure mana doesn't exceed maximum
                    demon.mana = 100



        def spawn(self):
            """Handles client spawning."""
            if self.spawn_timer > 0:
                self.spawn_timer -= 1
                return

            # Find an available spawn position (None means unoccupied)
            available_index = None
            for i, client in enumerate(self.occupied_positions):
                if client is None:
                    available_index = i
                    break

            if available_index is None:
                # No available position; return early
                return

            try:
                self.current_client = next(self.spawn_sequence)
            except StopIteration:
                # Reset the iterator if all clients have been used
                self.spawn_sequence = iter(self.clients)
                self.current_client = next(self.spawn_sequence)

            if self.current_client.stat == "idle":
                self.current_client.chant_delay = 15
                self.current_client.chant_duration = 10
                self.current_client.selected_stat = key, value = random.choice(list(self.current_client.stats.items()))
                self.current_client.stat = "ready"

                # Assign the client to the available spawn position
                self.current_client.x, self.current_client.y = self.spawn_positions[available_index]
                self.occupied_positions[available_index] = self.current_client  # Mark the position as occupied
                renpy.play("summontry/locked.ogg", "sound")

            # Reset spawn timer
            self.spawn_timer = 2

        def release_slot(self, client):
            """Frees up the position when a client finishes serving."""
            for i, pos_client in enumerate(self.occupied_positions):
                if pos_client == client:
                    self.occupied_positions[i] = None
                    break


        def hovered(self, client):
            self.hovered_client = client
        def unhovered(self):
            self.hovered_client = None
        def reset(self):
            self.hovered_client = None
            self.time = 90
            self.tonights_gain = 0
            self.missed = 0
            self.stat = "start"
        def start(self):
            self.time = 90
            self.stat = "night"
        def end_night(self):
            """Ends the night cycle and resets all client states."""
            if self.holding:
                self.holding_pos = (-200, -200)
                self.demons.append(self.holding)
                self.holding = None

            for i, client in enumerate(self.clients):
                if client.stat in ["serving", "ready", "chanting", "waiting"]:
                    client.stat = "idle"
                    if client.demon:
                        self.demons.append(client.demon)
                        client.demon = None
                    self.release_slot(client)
            self.stat = "day"

screen summontry_hire_screen(demon_list):
    style_prefix "summontry"
    hbox align (0.5, 0.5) spacing 20:
        for i in demon_list:
            vbox spacing -90 box_reverse True align (0.5, 0.5):
                button:
                    padding 10,10 background "#000a"
                    action Return(i)
                    frame:
                        padding 20,90,20,20 background "#000a"
                        vbox:
                            text i.name color "#ffb300" size 40
                            vbox:
                                for key,value in i.stats.items():
                                    text "[key]: [value]"
                            bar value i.mana range 100 xysize 150,36 right_bar "mana_bar_back" left_bar "mana bar" align .5,.5
                add i.image align (0.5, 0.0)

screen minigame_1(g):
    add "images/minigame_shop_bg.png"
    style_prefix "summontry"
    
    button:
        background None
        action Function(g.clicked_out)

    for i in g.clients:
        fixed fit_first True:
            align (.5,.5) offset i.x,i.y
            
            # Only show the button if the client's status is in ["waiting", "ready", "chanting", "serving"]
            if i.stat in ["waiting", "ready", "chanting", "serving"]:
                vbox:
                    align .5,.5

                    # Timer as text (in seconds) placed ABOVE the button for specific states
                    if i.stat == "waiting":
                        text "[i.waiting_duration]s" size 20 color "#080808"
                    elif i.stat == "chanting":
                        text "[i.chant_duration]s" size 20 color "#080808"
                    elif i.stat == "ready":
                        text "[i.chant_delay]s" size 20 color "#080808"
                    elif i.stat == "serving":
                        text "[i.serve_duration]s" size 20 color "#080808"
                    
                    # Button containing client image on the left and demon (if placed) on the right
                    button:
                        xsize 312  # Set button width
                        ysize 120  # Set button height
                        align .5,.5
                        background "#0000"  # Transparent background

                        hbox:
                            spacing 0
                            # Display client's image on the left half of the button
                            add i.image xsize 156 ysize 120  # Left half for client image (156px wide)
                            
                            # Display demon on the right half if a demon is placed
                            if i.demon:
                                vbox:
                                    # Demon image on the right half
                                    add i.demon.image xsize 156 ysize 120  # Right half for demon image

                                    # Display demon mana bar below the demon image
                                    bar value i.demon.mana range 100 xysize 150,36 right_bar "mana_bar_back" left_bar "mana bar" align .5,.5

                        hovered Function(g.hovered, i)
                        unhovered Function(g.unhovered)
                        action Function(g.clicked_portal, i)

                    # Display client stats below the image and demon
                    vbox:
                        align .2,.1  # Align below the button
                        spacing 5
                        for stat_name, stat_value in i.stats.items():
                            text "[stat_name]: [stat_value]" size 20 color "#080808"  # Show each stat with a label

    # Demon display and interaction at the bottom of the screen
    hbox:
        align (0.5, 1.0) yoffset -20
        for i in g.demons:
            vbox:
                button:
                    add i.image
                    hovered Function(g.hovered, i)
                    unhovered Function(g.unhovered)
                    action Function(g.clicked_demon, i)
                bar value i.mana range 100 xysize 150,36 right_bar "mana_bar_back" left_bar "mana bar" align .5,.5

    # Adjusted mana bottle and text at the top-left
    text str(g.mana) size 60 align .0,.0 offset 130,10  # Adjusted position for text

    # Handling the held item (demon or client)
    if g.holding:
        timer .02 repeat True action Function(g.update_holding)
        add g.holding.image offset g.holding_pos

    # Time bar during night state
    if g.stat == "night":
        bar value g.time range 90 xysize 900,10 align (0.5, 0.0) yoffset 10
        text ("[g.time]") align (0.5, 0.05)
        timer 1 repeat True action Function(g.tick)

    # Start screen with button to start the game
    elif g.stat == "start":
        button:
            align (0.5, 0.5) padding 20,20 background "#e66f0ecc"
            text "Let's start."
            action Function(g.start)

    # Day state with Finish button
    elif g.stat == "day":
        button:
            align (0.5, 0.5) padding 20,20 background "#e66f0ecc"
            text "Finish , Today Gain : [g.mana]"
            action [SetVariable("money",money + g.mana),Return()]
    
    if g.hovered_client and type(g.hovered_client) is summontry_demon:
        vbox spacing -90 box_reverse True align (0.5, 0.5):
            frame:
                padding 10,10 background "#e66f0ecc"
                frame:
                    padding 20,90,20,20 background "#e66f0ecc"
                    vbox:
                        text g.hovered_client.name color "#ffb300" size 40
                        vbox:
                            for key,value in g.hovered_client.stats.items():
                                text "[key]: [value]"
                        bar value g.hovered_client.mana range 100 xysize 150,36 right_bar "mana_bar_back" left_bar "mana bar" align .5,.5
            add g.hovered_client.image align (0.5, 0.0)


init:
    style summontry_text:
        align (.5,.5)
    style summontry_frame:
        align (.5,.5)
    style summontry_button:
        align (.5,.5)

init:
    default dana = summontry_client(
        name = "Dana",
        image = "dana_portrait",
        stats = {
            "Love": 33,           
        },
        pos = (-318,332),
        )
    default inari = summontry_client(
        name = "Inari",
        image = "inari_portrait",
        stats = {
            "Athletics": 30,
        },
        pos = (-697,133),
        )
    default ririn = summontry_client(
        name = "Ririn",
        image = "ririn_portrait",
        stats = {

            "Love": 5,
 
        },
        pos = (-687,-303),
        )
    default keiko = summontry_client(
        name = "Keiko",
        image = "keiko_portrait",
        stats = {
            "Joy": 45,
 
        },
        pos = (-148,-104),
        )
    default aiko = summontry_client(
        name = "Aiko",
        image = "aiko_portrait",
        stats = {
            "Joy": 23,
        },
        pos = (407,-278),
        )
    default sora = summontry_client(
        name = "Sora",
        image = "sora_portrait",
        stats = {
            "Athletics": 21,

        },
        pos = (347,142),
        )
    default shiri = summontry_client(
        name = "Shiri",
        image = "shiri_portrait",
        stats = {
            "Athletics": 62,

        },
        pos = (604,259),
        )
    default hina = summontry_client(
        name = "Hina",
        image = "hina_portrait",
        stats = {
            "Joy": 23,
        },
        pos = (376,-105),
        )
    default all_clients = [dana, inari, ririn, keiko, aiko, sora, shiri]

    default tsuru_working = summontry_demon(
        name = "Tsuru",
        image = "tsuru_portrait",
        stats = {
            "Athletics": 6,
            "Love": 15,
            "Joy": 17,
        },
        mana = 100,
        )

    default summontry = summontry_handler([tsuru_working], all_clients)


