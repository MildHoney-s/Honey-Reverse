default persistent.shoot_highscore = 69

init python:
    import random
    import time
    import renpy.store as store
    random.seed(time.perf_counter_ns())

    class shooter_clock(renpy.Displayable):
        def __init__(self):
            super(renpy.Displayable,self).__init__()
            self.start = 0
            self.current = 0

        def render(self,width,height,st,at):
            self.current += 1

            renpy.redraw(self, 0)
            return renpy.Render(0, 0)

    class shooter_enemy(renpy.Displayable):
        def __init__(self, images, x, y, z):
            super(renpy.Displayable, self).__init__()
            self.image = random.choice(images)
            self.x = x
            self.y = y
            self.z = z
            self.yzoom = .01
            self.stat = "_idle"
            self.time = 0
            self.parent = None

        def change(self, stat):
            self.stat = stat
            self.time = 0

        def shoot(self):
            renpy.play("minigames/shooting/gun_1.ogg", "sound")
            self.change("_shooting")
            self.parent.got_shot()

        def render(self, width, height, st, at):
            if self.yzoom < 1:
                self.yzoom += .2
            else:
                self.yzoom = 1
            self.time += 1
            if self.image == "shooting_villager" and self.time > 300:
                self.change("hidden")
            elif self.stat == "_idle":
                if self.time > 300 and self.image != "shooting_villager":
                    self.shoot()
            elif self.time > 100 and self.stat == "_shooting":
                self.change("_idle")
            elif self.time > 100 and self.stat == "_dead":
                self.change("hidden")

            img = self.image + self.stat
            if self.stat == "hidden":
                return renpy.Render(0, 0)
            t = Transform(img, xanchor=0.5, yanchor=0.5, zoom=self.z, yzoom=self.yzoom, nearest=True)
            child_render = renpy.render(t, width, height, st, at)
            cw, ch = child_render.get_size()

            rv = renpy.Render(cw, ch)
            rv.blit(child_render, (0, 0))

            renpy.redraw(self, 0)
            return rv


    class shooter_handler:
        def __init__(self, enemies):
            self.enemies = enemies
            self.active_enemies = []
            self.stat = "start"
            self.clock = shooter_clock()
            self.health = 5
            self.bullets = 8
            self.kills = 0
            self.combo_kills = 0
            self.original_spawn = self.spawn
            self.shoot_cooldown = 0
            self.spawn_interval = 0.8  # Spawn every 1 second initially
            self.time_elapsed = 0  # Tracks time passed

        def increase_difficulty(self):
            # Increase difficulty by reducing spawn interval
            self.time_elapsed += 1
            if self.time_elapsed % 20 == 0:  # Every 30 seconds
                self.spawn_interval = max(0.1, self.spawn_interval - 0.15)  # Reduce spawn interval but not below 0.5

        def start(self):
            self.stat = "playing"

        def cooldown(self):
            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1

        def restart(self):
            self.kills = 0
            self.health = 5
            self.bullets = 8
            self.active_enemies = []
            self.stat = "playing"
            self.combo_kills = 0
            self.spawn = self.original_spawn
            self.time_elapsed = 0

        def spawn(self):
            if self.stat == "dead":
                return

            # Remove hidden enemies from the active list
            self.active_enemies = [i for i in self.active_enemies if i.stat != "hidden"]

            # Spawn only if fewer than the maximum number of active enemies
            if len(self.active_enemies) < 5:
                # Fixed weights for enemies: 5 for thieves, 2 for villagers (2:3 ratio)
                if self.time_elapsed > 45:
                    weights = [10 if enemy[0][0] == "shooting_thief" else 0 for enemy in self.enemies]
                elif self.time_elapsed > 30:
                    weights = [5 if enemy[0][0] == "shooting_thief" else 1 for enemy in self.enemies]
                else:
                    weights = [4 if enemy[0][0] == "shooting_thief" else 2 for enemy in self.enemies]

                # Select an enemy based on the fixed weights
                e = random.choices(self.enemies, weights=weights, k=1)[0]

                # Create the enemy instance
                enemy = shooter_enemy(*e)

                # Avoid spawning on the same position
                for i in self.active_enemies:
                    if i.x == enemy.x and i.y == enemy.y:
                        return

                # Add the enemy to the active list
                enemy.parent = self
                self.active_enemies.append(enemy)

        def shoot(self, enemy):
            if self.stat != "playing" or self.shoot_cooldown > 0:
                renpy.play("minigames/shooting/empty.ogg", "sound")
                self.combo_kills = 0

            elif self.bullets > 0:
                tag = f"shooter_bullets_{random.randint(0,10000)}"
                x, y = renpy.get_mouse_pos()
                Show("shooter_bullets", x=x, y=y, z=8, tag=tag, _tag=tag)()
                self.bullets -= 1
                renpy.play("minigames/shooting/gun_2.ogg", "sound")
                if self.combo_kills >= 20:
                    self.shoot_cooldown = 8
                else:
                    self.shoot_cooldown = 10

                if not enemy:
                    return
                if enemy.stat != "_dead":
                    renpy.play("minigames/shooting/kill.ogg", "sfx1")
                    enemy.change("_dead")
                    if enemy.image == "shooting_villager":
                        self.kills -= 2
                        self.combo_kills = 0
                    else:
                        self.kills += 1
                        self.combo_kills += 1
                        if self.kills > persistent.shoot_highscore:
                            persistent.shoot_highscore = self.kills
                        if (self.combo_kills%10) == 0 and self.health < 20:
                            self.health += 1
            else:
                renpy.play("minigames/shooting/empty.ogg", "sound")

        def got_shot(self):
            if self.stat == "playing":
                self.health -= 1
                if self.health < 1:
                    self.stat = "dead"
                    renpy.play("minigames/shooting/hurt.ogg", "sfx1")
                    for enemy in self.active_enemies:
                        if enemy.stat != "_dead":
                            enemy.change("hidden")
                    self.spawn = lambda: None

        def reload(self):
            if self.bullets == 0:
                renpy.play("minigames/shooting/reload.ogg", "sound")
                self.bullets = 8

screen shooter():
    modal True
    style_prefix "shooter"
    default shooter_game = shooter_handler([
        [["shooting_thief", "shooting_villager"], 550, 335, .25],
        [["shooting_thief", "shooting_villager"], 650, 800, .25],
        [["shooting_thief", "shooting_villager"], 510, 1100, .25],
        [["shooting_thief", "shooting_villager"], 1230, 950, .25],
        [["shooting_thief", "shooting_villager"], 960, 575, .125],
    ])

    button:
        background None
        action Function(shooter_game.shoot, None)
    fixed:
        xysize 1920,1080
        for i in shooter_game.active_enemies:
            button:
                padding .0,.0 pos i.x,i.y background None anchor .5,1.0
                add i
                action Function(shooter_game.shoot, i)

    if shooter_game.stat == "start":
        button:
            align .5,.5
            text "Start"
            action Function(shooter_game.start)
        imagebutton auto "images/tutorial/howtoplay_button_%s.png":
            focus_mask True
            action Show("tutorial_popup",tutorial="shoot")

    elif shooter_game.stat == "playing":
        timer shooter_game.spawn_interval repeat True action Function(shooter_game.spawn)

        # Increase difficulty over time
        timer 1.0 repeat True action Function(shooter_game.increase_difficulty)

        # Shoot Cooldown logic
        timer 0.1 repeat True action Function(shooter_game.cooldown)
        hbox:
            align .0,1.0 spacing 10 offset 20,-20
            for i in range(shooter_game.health):
                add "shooting_heart" at zoom(.25, True)
        if shooter_game.bullets > 0:
            hbox:
                align 1.0,1.0 spacing 10 offset -20,-20
                for i in range(shooter_game.bullets):
                    add "shooting_ammo" at zoom(.175, True)
        else:
            button:
                align 1.0,1.0 offset -20,-20
                text "Reload"
                action Function(shooter_game.reload)
        key "K_r" action Function(shooter_game.reload)

    elif shooter_game.stat == "dead":
        vbox:
            align .5,.5 spacing 10
            if tokens > 3:
                button:
                    background "#006"
                    insensitive_background "#eae4e4"
                    hover_background "#00a"
                    padding 20,20
                    align (0.5, 0.5)
                    text "Restart use 3 coins"
                    action [Function(shooter_game.restart),SetVariable("tokens",tokens-3)]
            button:
                background "#006"
                insensitive_background "#eae4e4"
                hover_background "#00a"
                padding 20,20
                align (0.5, 0.5)
                text "Exit" style "exitshooter_text"
                action Return(shooter_game.kills)

        imagebutton auto "images/tutorial/howtoplay_button_%s.png":
            focus_mask True
            action Show("tutorial_popup",tutorial="shoot")

    vbox:
        spacing -30
        align (0.5, 0.01)
        text "HIGH SCORE\n" style "highscore_text" align (0.5, 0.5)
        text str(persistent.shoot_highscore):
            align (0.5, 0.5)
            style "highscore_text"
    vbox:
        align (0.04,0.02)
        spacing 20
        hbox:
            text "SCORE : " style "score_text"
            text str(shooter_game.kills) style "score_text"
        hbox:
            text "COMBO " style "combo_text"
            text str(shooter_game.combo_kills) style "combo_text"
    hbox:
        spacing 25
        align (0.975,0.03)
        add "doll_coin" size (100,100)
        text "{}".format(tokens) size 80 offset (0, 10) color "#abaeaeff"

style shooter_text:
    font "ARCADE_N.ttf"
    size 40
    color "#f6a330"
    outlines [ (3, "#ffffff", 0, 0) ]
    bold True

style score_text:
    font "ARCADE_N.ttf"
    size 25
    color "#df6507"
    outlines [ (2, "#ecdda8", 0, 0) ]

style combo_text:
    font "ARCADE_N.ttf"
    size 25
    color "#227114"
    outlines [ (2, "#c2f09a", 0, 0) ]

style highscore_text:
    font "ARCADE_N.ttf"
    size 40
    color "#ed412e"
    outlines [ (4, "#efe66c", 0, 0) ]

style exitshooter_text:
    font "ARCADE_N.ttf"
    size 40
    color "#ef3232"
    outlines [ (3, "#84260f", 0, 0) ]

style shooter_button:
    background Frame("shooting_shooter_frame", 6,6) padding (20,20)
    outlines [ (8, "#ffffff", 0, 0) ]

screen shooter_bullets(x,y,z,tag):
    add "shooting_ammo_effect" pos x,y anchor .5,.5 at zoom(.1, True)
    timer 1 repeat True action Hide(tag)

label shooting_game_center:
    $ default_mouse = "shooter"
    $ quick_menu = False
    show shooting_bg at truecenter:
        zoom 1.25 ypos 605
    call screen shooter
    $ default_mouse = ""
    $ quick_menu = True
    jump act2_3_shot_3
