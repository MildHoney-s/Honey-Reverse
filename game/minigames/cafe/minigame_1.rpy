init python:
    from copy import copy
    init_time = 5

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
            self.chant_delay = 10
            self.chant_duration = 10
            self.serve_duration = 10
            self.stamina = stamina or random.randint(80, 100)
            self.x, self.y = pos
            self.parent = None
            self.maid = None
            self.stat = "idle"
            self.selected_stat = None

    # Game Handler
    class cafe_handler:
        def __init__(self, maids, clients):
            self.maids = maids
            self.clients = clients
            self.hovered_client = None
            self.holding = None
            self.stat = "start"
            self.client_cap = 3
            self.holding_pos = (-200, -200)
            self.stamina = 0
            self.missed = 0
            self.time = 0
            self.tonights_gain = 0
            self.spawn_timer = 0
            self.spawn_sequence = iter(clients)
            self.current_client = None
            self.stamina_gain_timers = {}
            self.spawn_positions = [(-475, 95), (-475, -211), (460, -100), (460, 185), (460, -370)]
            self.occupied_positions = [None] * len(self.spawn_positions)

        def clicked_portal(self, client):
            renpy.play("minigames/cafe/rotate_up.ogg", "sound")
            if client.maid:
                if self.holding:
                    old_maid = client.maid
                    client.maid = self.holding
                    client.serve_duration = self.calculate_serve_duration(client, self.holding)
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
            if maid_stat_value >= client_required_value:
                return random.randint(30, 40)
            else:
                return random.randint(15, 25)

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
                    gain_amount = 11 if maid_stat_value >= client_stat_value else 7
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
                    client.chant_duration -= 1
                    if client.chant_duration <= 0:
                        client.stat = "idle"
                        renpy.play("minigames/cafe/shed.ogg", "sound")
                        self.release_slot(client)
                elif client.stat == "serving":
                    client.serve_duration -= 1
                    if client.maid:
                        client.maid.stamina -= 1
                        if client.maid.stamina <= 0:
                            client.maid.stamina = 0
                            self.maids.append(client.maid)
                            client.maid = None
                            client.waiting_duration = client.serve_duration
                            client.stat = "waiting"
                            renpy.play("minigames/cafe/return_bench.ogg", "sound")
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
                    if client.waiting_duration <= 0:
                        client.stat = "idle"  # Set to idle when waiting time runs out
                        self.release_slot(client)

            self.regenerate_stamina_for_bench()

        def regenerate_stamina_for_bench(self):
            for maid in self.maids:
                maid.stamina += 3
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
                self.current_client.chant_delay = 15
                self.current_client.chant_duration = 10
                self.current_client.selected_stat = key, value = random.choice(list(self.current_client.stats.items()))
                self.current_client.stat = "ready"
                self.current_client.x, self.current_client.y = self.spawn_positions[available_index]
                self.occupied_positions[available_index] = self.current_client
                renpy.play("minigames/cafe/locked.ogg", "sound")

            self.spawn_timer = 2

        def release_slot(self, client):
            for i, pos_client in enumerate(self.occupied_positions):
                if pos_client == client:
                    self.occupied_positions[i] = None

        def hovered(self, client):
            self.hovered_client = client

        def unhovered(self):
            self.hovered_client = None

        def reset(self):
            self.hovered_client = None
            self.time = init_time
            self.tonights_gain = 0
            self.missed = 0
            self.stat = "start"

        def start(self):
            self.time = init_time
            self.stat = "night"

        def end_night(self):
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
            self.stat = "day"

screen cafe_hire_screen(maid_list):
    style_prefix "cafe"
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
                            bar value i.stamina range 100 xysize 150,36 right_bar "stamina_bar_back" left_bar "stamina bar" align .5,.5
                add i.image align (0.5, 0.0) xsize 156 ysize 120 

screen minigame_1(g):
    add "images/minigame_shop_bg.png"
    style_prefix "cafe"

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

                    # Button containing client image on the left and maid (if placed) on the right
                    button:
                        xsize 312  # Set button width
                        ysize 120  # Set button height
                        align .5,.5
                        background "#0000"  # Transparent background

                        hbox:
                            spacing 0
                            # Display client's image on the left half of the button
                            add i.image xsize 156 ysize 120  # Left half for client image (156px wide)

                            # Display maid on the right half if a maid is placed
                            if i.maid:
                                vbox:
                                    # maid image on the right half
                                    add i.maid.image xsize 156 ysize 120  # Right half for maid image

                                    # Display maid stamina bar below the maid image
                                    bar value i.maid.stamina range 100 xysize 150,36 right_bar "stamina_bar_back" left_bar "stamina bar" align .5,.5

                        hovered Function(g.hovered, i)
                        unhovered Function(g.unhovered)
                        action Function(g.clicked_portal, i)

                    # Display client stats below the image and maid
                    vbox:
                        align .2,.1  # Align below the button
                        spacing 5
                        for stat_name, stat_value in i.stats.items():
                            text "[stat_name]: [stat_value]" size 20 color "#080808"  # Show each stat with a label

    # maid display and interaction at the bottom of the screen
    hbox:
        align (0.5, 1.0) yoffset -20
        for i in g.maids:
            vbox:
                button:
                    add i.image xsize 156 ysize 120 
                    hovered Function(g.hovered, i)
                    unhovered Function(g.unhovered)
                    action Function(g.clicked_maid, i)
                bar value i.stamina range 100 xysize 150,36 right_bar "stamina_bar_back" left_bar "stamina bar" align .5,.5

    # Adjusted stamina bottle and text at the top-left
    text str(g.stamina) size 60 align .0,.0 offset 130,10  # Adjusted position for text

    # Handling the held item (maid or client)
    if g.holding:
        timer .02 repeat True action Function(g.update_holding)
        add g.holding.image offset g.holding_pos xsize 156 ysize 120 

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
            text "Finish , Today Gain : [g.stamina]"
            action [SetVariable("money",money + g.stamina),Return()]

    if g.hovered_client and type(g.hovered_client) is cafe_maid:
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
                        bar value g.hovered_client.stamina range 100 xysize 150,36 right_bar "stamina_bar_back" left_bar "stamina bar" align .5,.5
            add g.hovered_client.image align (0.5, 0.0) xsize 156 ysize 120

init:
    style cafe_text:
        align (.5,.5)
    style cafe_frame:
        align (.5,.5)
    style cafe_button:
        align (.5,.5)

init python:
    import random

    # Sample data for names and stats
    names = ["Dana", "Inari", "Ririn", "Keiko", "Aiko", "Sora", "Shiri", "Hina"]
    default_possible_stats = {
        "Love": (0, 100),
        "Joy": (0, 100),
        "Athletics": (0, 100),
    }
    # Sample positions following your previous example
    positions = [
        (-318, 332),  # Position for Dana
        (-697, 133),  # Position for Inari
        (-687, -303),  # Position for Ririn
        (-148, -104),  # Position for Keiko
        (407, -278),  # Position for Aiko
        (347, 142),  # Position for Sora
        (604, 259),  # Position for Shiri
        (376, -105),  # Position for Hina
    ]

    # Function to generate a random client with a random number of stats
    def generate_random_client(max_stats=3, stat_ranges=None):
        name = random.choice(names)
        image = f"{name.lower()}_portrait"  # Assuming the image name follows this pattern
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
    def generate_random_clients(num_clients=1, max_stats=3, stat_ranges=None):
        return [generate_random_client(max_stats, stat_ranges) for _ in range(num_clients)]

init:
    default tsuru_working = cafe_maid(
        name="Tsuru",
        image="tsuru_portrait",
        stats={
            "Athletics": 6,
            "Love": 15,
            "Joy": 17,
        },
        stamina=100,
        )

    default mild_working = cafe_maid(
        name="Mild",
        image="mild_portrait",
        stats={
            "Athletics": 5,
            "Love": 20,
            "Joy": 18,
        },
        stamina=120,
    )

    default debirun_working = cafe_maid(
        name="Debirun",
        image="del_portrait",
        stats={
            "Athletics": 5,
            "Love": 20,
            "Joy": 18,
        },
        stamina=120,
    )

    default custom_stat_ranges = {
        "Love": (0, 60),         # Custom max for Love
        "Joy": (0, 40),          # Custom max for Joy
        "Athletics": (0, 70),    # Custom max for Athletics
    }

    default minigame1_act1_1 = cafe_handler(
        [tsuru_working],  # Fixed clients
        generate_random_clients(1, max_stats=2, stat_ranges=custom_stat_ranges)  # Generate 1 random client with up to 2 stats
    )

    default minigame1_act1_2_shot_3 = cafe_handler(
        [mild_working, debirun_working],  # Fixed clients
        generate_random_clients(2, max_stats=3)  # Generate 2 random clients with up to 3 stats
    )

    default minigame1_act1_2_shot_4 = cafe_handler(
        [mild_working, tsuru_working, debirun_working],  # Fixed clients
        generate_random_clients(1)  # Generate 1 random client with up to 3 stats (default)
    )
