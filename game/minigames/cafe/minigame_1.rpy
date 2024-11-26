init python:
    from copy import copy
    left_time = 10
    init_time = 60
    sign_name = "______"

    name_colors = {
        "Mild-R": "#afefdb",
        "Tsururu": "#4ddbf4",
        "Debirun": "#433ed5"
    }

    stat_colors = {
        "Lovely": "#FF69B4",
        "Sexy": "#DC143C",
        "Joy": "#FFFF00"
    }
    # Maid Class
    class cafe_maid:
        def __init__(self, name, image, stats, stamina):
            self.name = name
            self.image = image
            self.stats = stats
            self.stamina = stamina
            self.x = 0
            self.y = 0

    # Client Class
    class cafe_client:
        def __init__(self, name, image, stats, pos, stamina=None):
            self.name = name
            self.image = image
            self.stats = stats
            self.chant_delay = 15
            self.chant_duration = 10
            self.serve_duration = 10
            self.stamina = stamina or random.randint(80, 100)
            self.x, self.y = pos
            self.parent = None
            self.maid = None
            self.stat = "idle"
            self.selected_stat = None
            self.wait_counter = 0

    # Game Handler
    class cafe_handler:
        def __init__(self, maids, clients,chant_delay=15,chant_duration=10):
            self.maids = maids
            self.clients = clients
            self.hovered_client = None
            self.holding = None
            self.stat = "start"
            self.chant_delay = chant_delay
            self.chant_duration = chant_duration
            self.holding_pos = (-200, -200)
            self.stamina = 0
            self.time = 0
            self.tonights_gain = 0
            self.spawn_timer = 0
            self.spawn_sequence = iter(clients)
            self.current_client = None
            self.stamina_gain_timers = {}
            self.spawn_positions = [(-650, 275), (-570, -125), (600, 275), (530, -125)]
            self.occupied_positions = [None] * len(self.spawn_positions)
            self.clients_left_count = 0

        def clicked_portal(self, client):
            renpy.play("minigames/cafe/rotate_up.ogg", "sound")
            if client.maid:
                if self.holding:
                    client_stat_name, client_required_value = client.selected_stat
                    maid_stat_value = self.holding.stats.get(client_stat_name, 0)
                    old_maid = client.maid
                    client.maid = self.holding
                    client.serve_duration = client.serve_duration
                    if maid_stat_value >= client_required_value:
                        if "_idle" in client.image:
                            client.image = client.image[:-5]
                            client.image = "{}_happy".format(client.image)
                            client.serve_duration += 5
                    else:
                        if "_happy" in client.image:
                            client.image = client.image[:-6]
                            client.image = "{}_idle".format(client.image)
                            client.serve_duration -= 5
                    client.stat = "serving"
                    self.holding = old_maid
                    self.maids.append(old_maid)
                    self.holding = None
                else:
                    self.holding = client.maid
                    client.maid = None
                    client.waiting_duration = client.serve_duration
                    client.stat = "waiting"
            elif self.holding:
                client.maid = self.holding
                client.serve_duration = self.calculate_serve_duration(client, self.holding)
                if client.stat == "waiting":
                    client.serve_duration = client.waiting_duration
                client.stat = "serving"
                self.stamina_gain_timers[client] = 5
                self.holding = None
            else:
                self.hovered_client = client

        def calculate_serve_duration(self, client, maid):
            client_stat_name, client_required_value = client.selected_stat
            maid_stat_value = maid.stats.get(client_stat_name, 0)
            if "_angry" in client.image:
                client.image = client.image[:-6]
            if "_idle" in client.image:
                client.image = client.image[:-5]
            if "_happy" in client.image:
                client.image = client.image[:-6]
            if maid_stat_value >= client_required_value:
                if client.stat != "waiting":
                    client.image = "{}_happy".format(client.image)
                    return random.randint(18, 25)
                client.image = "{}_happy".format(client.image)
            else:
                if client.stat != "waiting":
                    client.image = "{}_idle".format(client.image)
                    return random.randint(25, 30)
                client.image = "{}_idle".format(client.image)

        def clicked_out(self):
            self.hovered_client = None
            if not self.holding:
                return
            renpy.play("minigames/cafe/rotate_up.ogg", "sound")
            self.holding_pos = (-200, -200)
            self.maids.append(self.holding)
            self.holding = None

        def update_holding(self):
            self.holding_pos = renpy.get_mouse_pos()

        def clicked_maid(self, maid):
            if self.stat in ["start", "day"]:
                return
            if self.holding:
                self.maids.append(self.holding)
            self.holding_pos = (-200, -200)
            self.holding = maid
            self.maids.remove(maid)

        def calculate(self, client):
            for key, value in client.maid.stats.items():
                if key == client.selected_stat[0]:
                    maid_stat_value = client.maid.stats[key]
                    client_stat_value = client.selected_stat[1]
                    gain_amount = 6 if maid_stat_value >= client_stat_value else 3
                    renpy.play("minigames/cafe/bubble_7.ogg", "sound")
                    spawn_stamina(client.x, client.y, gain_amount, self)

        def gain_stamina(self, amount):
            self.stamina += amount

        def tick(self):
            if self.time > 1:
                self.time -= 1
            else:
                self.end_night()
                return

            self.spawn()

            for client in self.clients:
                if client.stat == "ready":
                    client.chant_delay -= 1
                    if client.chant_delay <= 0:
                        client.stat = "chanting"
                        renpy.play("minigames/cafe/fail.ogg", "sound")
                elif client.stat == "chanting":
                    if "_idle" in client.image:
                        client.image = client.image[:-5]
                    if "_happy" in client.image:
                        client.image = client.image[:-6]
                    if "_angry" not in client.image:
                        client.image = "{}_angry".format(client.image)
                    client.chant_duration -= 1
                    if client.chant_duration <= 0:
                        client.stat = "idle"
                        renpy.play("minigames/cafe/shed.ogg", "sound")
                        if "_angry" in client.image:
                            client.image = client.image[:-6]
                        self.clients_left_count += 1
                        self.release_slot(client)
                elif client.stat == "serving":
                    client.serve_duration -= 1
                    if client.maid:
                        client.maid.stamina -= 2
                        if client.maid.stamina <= 0:
                            client.maid.stamina = 0
                            self.maids.append(client.maid)
                            client.maid = None
                            client.waiting_duration = client.serve_duration
                            client.stat = "waiting"
                            # renpy.play("minigames/cafe/return_bench.ogg", "sound")
                            continue
                    self.stamina_gain_timers[client] -= 1
                    if self.stamina_gain_timers[client] <= 0:
                        self.calculate(client)
                        self.stamina_gain_timers[client] = 5
                    if client.serve_duration <= 0:
                        self.maids.append(client.maid)
                        client.maid = None
                        client.waiting_duration = client.serve_duration
                        client.stat = "waiting"
                elif client.stat == "waiting":
                    client.waiting_duration -= 1
                    client.wait_counter += 1
                    if client.waiting_duration <= 0:
                        if "_idle" in client.image:
                            client.image = client.image[:-5]
                        if "_happy" in client.image:
                            client.image = client.image[:-6]
                        client.stat = "idle"  # Set to idle when waiting time runs out
                        self.release_slot(client)
                    elif client.wait_counter > left_time:
                        client.stat = "idle"  # Set to idle when waiting time runs out
                        self.clients_left_count += 1
                        self.release_slot(client)

            self.regenerate_stamina_for_bench()

        def regenerate_stamina_for_bench(self):
            for maid in self.maids:
                maid.stamina += 1
                if maid.stamina > 100:
                    maid.stamina = 100

        def spawn(self):
            if self.spawn_timer > 0:
                self.spawn_timer -= 1
                return

            available_index = next((i for i, client in enumerate(self.occupied_positions) if client is None), None)
            if available_index is None:
                return

            try:
                self.current_client = next(self.spawn_sequence)
            except StopIteration:
                self.spawn_sequence = iter(self.clients)
                self.current_client = next(self.spawn_sequence)

            if self.current_client.stat == "idle":
                self.current_client.chant_delay = self.chant_delay
                self.current_client.chant_duration = self.chant_duration
                self.current_client.selected_stat = key, value = random.choice(list(self.current_client.stats.items()))
                self.current_client.stat = "ready"
                self.current_client.x, self.current_client.y = self.spawn_positions[available_index]
                self.occupied_positions[available_index] = self.current_client
                renpy.play("minigames/cafe/locked.ogg", "sound")

            self.spawn_timer = 2

        def release_slot(self, client):
            for i, pos_client in enumerate(self.occupied_positions):
                client.wait_counter = 0
                if pos_client == client:
                    self.occupied_positions[i] = None


        def hovered(self, client):
            self.hovered_client = client

        def unhovered(self):
            self.hovered_client = None

        def reset(self):
            if self.holding:
                self.holding_pos = (-200, -200)
                self.maids.append(self.holding)
                self.holding = None

            for client in self.clients:
                if client.stat in ["serving", "ready", "chanting", "waiting"]:
                    client.stat = "idle"
                    if client.maid:
                        self.maids.append(client.maid)
                        client.maid = None
                    self.release_slot(client)
            for maid in self.maids:
                maid.stamina = 100
            self.hovered_client = None
            self.stat = "start"
            self.stamina = 0
            self.time = 60
            self.tonights_gain = 0
            self.spawn_timer = 0
            self.current_client = None
            self.clients_left_count = 0


        def start(self):
            self.time = init_time
            self.stat = "night"

        def end_night(self):
            if self.holding:
                self.holding_pos = (-200, -200)
                self.maids.append(self.holding)
                self.holding = None

            for client in self.clients:
                if "_idle" in client.image:
                    client.image = client.image[:-5]
                if "_happy" in client.image:
                    client.image = client.image[:-6]
                if "_angry" in client.image:
                    client.image = client.image[:-6]
                if client.stat in ["serving", "ready", "chanting", "waiting"]:
                    client.stat = "idle"
                    if client.maid:
                        self.maids.append(client.maid)
                        client.maid = None
                    self.release_slot(client)

            for maid in self.maids:
                maid.stamina = 100
            self.stat = "day"

screen cafe_hire_screen(maid_list):
    style_prefix "cafemini"
    hbox align (0.5, 0.5) spacing 20:
        for i in maid_list:
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
                            bar value i.stamina range 100 xysize 130,26 right_bar "cafe_empty_stamina_bar" left_bar "cafe_full_stamina_bar" align .5,.5
                add i.image align (0.5, 0.0) xsize 130 ysize 130

image frame = Transform("images/minigames/cafe/tsuru_portrait.png",alpha=0.0)
screen minigame_1(g,force_lose = False):
    add "images/minigames/cafe/cafe_bg.png"
    style_prefix "cafemini"

    button:
        background None
        action Function(g.clicked_out)

    for i in g.clients:
        #if g.stat == "night":
            #add "frame1" xysize 305,160 align (.5,.5) offset i.x-11,i.y-5
        fixed fit_first True:
            align (.5,.5) offset i.x,i.y
            # Only show the button if the client's status is in ["waiting", "ready", "chanting", "serving"]
            if i.stat in ["waiting", "ready", "chanting", "serving"]:
                if i.stat is "chanting":
                    add "frame3" xysize 302,161 offset 20,-30
                elif i.stat is "waiting":
                    add "frame4" xysize 302,161 offset 20,-30
                else:
                    add "frame1" xysize 302,161 offset 20,-30
                vbox:
                    xpos 27 ypos -42
                    # Timer as text (in seconds) placed ABOVE the button for specific states
                    if i.stat == "waiting":
                        text "[i.waiting_duration]" size 20 color "#ff6200d9" ypos -15 outlines [ (1, "#ffffff", 0, 0) ]
                    elif i.stat == "chanting":
                        text "[i.chant_duration]" size 20 color "#ff0000" ypos -15 outlines [ (1, "#ffffff", 0, 0) ]
                    elif i.stat == "ready":
                        text "[i.chant_delay]" size 20 color "#d6c540f7" ypos -15 outlines [ (1, "#514f4f", 0, 0) ]
                    elif i.stat == "serving":
                        text "[i.serve_duration]" size 20 color "#ffffff" ypos -15 outlines [ (1, "#514f4f", 0, 0) ]

                    # Button containing client image on the left and maid (if placed) on the right
                    button:
                        xsize 312  # Set button width
                        ysize 120  # Set button height
                        align .5,.5
                        background "#0000"  # Transparent background

                        hbox:
                            spacing 15

                            # Display maid on the right half if a maid is placed
                            if i.maid:
                                vbox:
                                    # maid image on the right half
                                    add i.maid.image xsize 130 ysize 130  # Right half for maid image

                                    # Display maid stamina bar below the maid image
                                    bar value i.maid.stamina range 100 xysize 130,26 right_bar "cafe_empty_stamina_bar" left_bar "cafe_full_stamina_bar" align .5,.5
                            # Display client's image on the left half of the button
                            else:
                                vbox:
                                    add "frame" xsize 130 ysize 130
                            add i.image xsize 130 ysize 130  # Left half for client image (156px wide)
                            #text str(i.wait_counter)

                        hovered Function(g.hovered, i)
                        unhovered Function(g.unhovered)
                        action Function(g.clicked_portal, i)

                    # Display client stats below the image and maid
                    vbox:
                        xalign 0.77
                        ypos -100
                        for stat_name, stat_value in i.stats.items():
                            text "[stat_name]: [stat_value]" size 20 color "#FFFFFF" xalign 0.5  # Show each stat with a label


    # maid display and interaction at the bottom of the screen
    hbox:
        align (0.5, 1.0) yoffset -20
        for i in g.maids:
            vbox:
                if g.stat != "day":
                    button:
                        add i.image xsize 130 ysize 130
                        hovered Function(g.hovered, i)
                        unhovered Function(g.unhovered)
                        action Function(g.clicked_maid, i)
                    bar value i.stamina range 100 xysize 130,26 right_bar "cafe_empty_stamina_bar" left_bar "cafe_full_stamina_bar" align .5,.5

    # Adjusted stamina bottle and text at the top-left
    add "cafe_corner" xysize (495,184) align .005,.01
    add "gui/honey_revense_logo.png" xysize (180,180) align .007,.012
    add "cafe_coin" xysize (75, 75) align .13,.015
    add "cafe_exit" xysize (75, 75) align .13,.11
    text str(g.stamina) size 60 align .13,.015 offset 150,10  # Adjusted position for text
    text str(g.clients_left_count)+"/3" size 60 align .13,.11 offset 130,10

    # Handling the held item (maid or client)
    if g.holding:
        timer .02 repeat True action Function(g.update_holding)
        add g.holding.image offset g.holding_pos xsize 130 ysize 130

    if g.clients_left_count >= 3:
        if force_lose:
            timer 0.01 action Return()
        timer 0.01 action Function(g.end_night)
        vbox spacing -90 box_reverse True align (0.5, 0.5):
            frame:
                add "summary" xysize (500,750) align .5,.5
                hbox:
                    align (0.5, 0.5)
                    text "You Failed"
                hbox:
                    spacing 100
                    align (0.5, 0.6)
                    text "Client left"
                    text "[g.clients_left_count]"
                button:
                    align (0.5,0.765)
                    text "Click To Restart"
                    action [Function(g.reset),Function(g.start)]
        imagebutton auto "images/tutorial/howtoplay_button_%s.png":
            focus_mask True
            action Show("tutorial_popup")

    # Time bar during night state
    elif g.stat == "night":
        # bar value g.time range 90 xysize 900,10 align (0.5, 0.0) yoffset 10
        bar value g.time range 60 xysize 800,128 right_bar "test_bar" left_bar "bar" align (0.5, 0.0) yoffset 10
        text ("[g.time]") align (0.5, 0.065) color "#ffffff"
        timer 1 repeat True action Function(g.tick)

    # Start screen with button to start the game
    elif g.stat == "start":
        button:
            align (0.5, 0.5) padding 20,20 background "#e66f0ecc"
            insensitive_background "#eae4e4"
            hover_background "#e7802ccc"
            text "Let's start." color "#eae4e4"
            action Function(g.start)

        imagebutton auto "images/tutorial/howtoplay_button_%s.png":
            focus_mask True
            action Show("tutorial_popup")

    # Day state with Finish button
    elif g.stat == "day":
        vbox spacing -60 box_reverse True align (0.5, 0.5):
            frame:
                add "summary" xysize (500,750) align .5,.5
                hbox:
                    spacing 100
                    align (0.5, 0.45)
                    text "Client left"
                    text "[g.clients_left_count]"
                hbox:
                    spacing 100
                    align (0.5, 0.55)
                    text "Total Recive"
                    text "[g.stamina]"
                hbox:
                    spacing 100
                    align (0.5, 0.65)
                    text "Total Money"
                    if sign_name is povname:
                        text "[money]"
                    else:
                        text "[g.stamina+money]"
                button:
                    align (0.5,0.765)
                    text "Sign Here {}".format(sign_name)
                    if sign_name is not povname:
                        action [SetVariable("sign_name",povname),SetVariable("money",money + g.stamina)]
        if sign_name is povname:
            timer 1.2 action [SetVariable("sign_name","_____"),Return()]

    if g.hovered_client and type(g.hovered_client) is cafe_maid and g.stat == 'night':
        vbox spacing -90 box_reverse True align (0.5, 0.5):
            frame:
                add "status" xysize (450,675) align (1.0,0.1)
                vbox:
                    spacing 52
                    align (0.86, 0.42)
                    $ name_color = name_colors.get(g.hovered_client.name, "#ffb300")
                    text g.hovered_client.name color name_color size 40
                    for key,value in g.hovered_client.stats.items():
                        $ stat_color = stat_colors.get(key, "#ffb300")
                        text "[key]: {color=#fff}[value]{/color}" color stat_color
                add g.hovered_client.image align (0.918, 0.12) xsize 156 ysize 156
init:
    style cafemini_text:
        font "cafe.ttf"
        align (.5,.5)
    style cafemini_frame:
        align (.5,.5)
    style cafemini_button:
        align (.5,.5)


init python:
    import random

    # Sample data for names and stats
    names = ["client1","client2","client3","client4"]
    default_possible_stats = {
        "Sexy": (10, 30),
        "Joy": (10, 30),
        "Lovely": (10, 30),
    }
    # Sample positions following your previous example
    positions = [
        (-318, 332),  # Position for Dana
        (-697, 133),  # Position for Inari
        (-687, -303),  # Position for Ririn
        (-148, -104),
        (-318, 332),  # Position for Dana
        (-697, 133),  # Position for Inari
        (-687, -303),  # Position for Ririn
        (-148, -104),  # Position for Keiko  # Position for Keiko
    ]

    # Function to generate a random client with a random number of stats
    def generate_random_client(max_stats=3, stat_ranges=None):
        name = random.choice(names)
        image = f"{name.lower()}"  # Assuming the image name follows this pattern
        # Use provided stat ranges or fall back to defaults
        stats_range = stat_ranges if stat_ranges else default_possible_stats
        # Get the total number of possible stats
        total_possible_stats = len(stats_range)
        # Ensure max_stats does not exceed available stats
        if max_stats > total_possible_stats:
            max_stats = total_possible_stats
        # Randomly choose how many stats to include (1 to max_stats)
        num_stats = random.randint(1, max_stats)
        # Randomly select stats from the possible stats
        selected_stats = random.sample(list(stats_range.keys()), k=num_stats)
        # Create stats dictionary with random values
        stats = {}
        for stat in selected_stats:
            min_val, max_val = stats_range[stat]
            stats[stat] = random.randint(min_val, max_val)  # Ensure values respect the max limits
        pos = random.choice(positions)  # Random position from the predefined list
        return cafe_client(name=name, image=image, stats=stats, pos=pos)

    # Function to generate a list of random clients
    def generate_random_clients(num_clients=4, max_stats=1, stat_ranges=None):
        return [generate_random_client(max_stats, stat_ranges) for _ in range(num_clients)]

init:
    default tsuru_working = cafe_maid(
        name="Tsururu",
        image="tsuru_portrait",
        stats={
            "Lovely": 22,
            "Sexy": 11,
            "Joy": 17,
        },
        stamina=120,
        )

    default mild_working = cafe_maid(
        name="Mild-R",
        image="mild_portrait",
        stats={
            "Lovely": 14,
            "Sexy": 23,
            "Joy": 13,
        },
        stamina=120,
    )

    default debirun_working = cafe_maid(
        name="Debirun",
        image="del_portrait",
        stats={
            "Lovely": 14,
            "Sexy": 8,
            "Joy": 28,
        },
        stamina=120,
    )

    default custom_stat_ranges_1 = {
        "Sexy": (10, 22),         # Custom max for Sexy
        "Joy": (16, 22),          # Custom max for Joy
        "Lovely": (14, 22),    # Custom max for Lovely
    }

    default custom_stat_ranges_2 = {
        "Sexy": (12, 25),         # Custom max for Sexy
        "Joy": (18, 29),          # Custom max for Joy
        "Lovely": (17, 26),    # Custom max for Lovely
    }

    default minigame1_act1_1 = cafe_handler(
        [tsuru_working],  # Fixed clients
        generate_random_clients(10, max_stats=1)  # Generate 1 random client with up to 2 stats
    )

    default minigame1_act1_1_2 = cafe_handler(
        [mild_working, tsuru_working],  # Fixed clients
        generate_random_clients(10, max_stats=1,stat_ranges=custom_stat_ranges_1)  # Generate 1 random client with up to 3 stats (default)
    )

    default minigame1_act1_2_shot_3 = cafe_handler(
        [mild_working, debirun_working],  # Fixed clients
        generate_random_clients(10, max_stats=1,stat_ranges=custom_stat_ranges_1),  # Generate 2 random clients with up to 3 stats
        chant_delay = 10,chant_duration=10
    )

    default minigame1_act1_2_shot_4 = cafe_handler(
        [mild_working, tsuru_working, debirun_working],  # Fixed clients
        generate_random_clients(10, max_stats=1,stat_ranges=custom_stat_ranges_2),  # Generate 1 random client with up to 3 stats (default)
        chant_delay = 10,chant_duration=7
    )

    default minigame1_act2_2 = cafe_handler(
        [mild_working, tsuru_working, debirun_working],  # Fixed clients
        generate_random_clients(10, max_stats=1),  # Generate 1 random client with up to 3 stats (default)
        chant_delay = 5,chant_duration=5
    )
