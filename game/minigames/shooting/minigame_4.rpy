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
        def __init__(self, images, x, y, z, ):
            super(renpy.Displayable,self).__init__()
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

        def render(self,width,height,st,at):
            if self.yzoom < 1:
                self.yzoom += .2
            else:
                self.yzoom = 1
            self.time += 1
            # time before enemy fire
            if self.stat == "_idle":
                if self.time > 500 and self.image == "shooting_villager":
                    # self.change("hidden")
                    pass
                elif self.time > 500 and self.image != "shooting_villager":
                    self.shoot()
            elif self.time > 100 and self.stat == "_shooting":
                self.change("_idle")
            elif self.time > 100 and self.stat == "_dead":
                self.change("hidden")
            img = self.image + self.stat
            if self.stat == "hidden":
                return renpy.Render(0, 0)
            t = Transform(img, xanchor=0.5, yanchor=0.5, zoom = self.z, yzoom = self.yzoom, nearest = True)
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

            self.original_spawn = self.spawn

        def start(self):
            self.stat = "playing"

        def restart(self):
            # handle global money in game
            if store.money >= 0:
                store.money -= 10

                self.kills = 0
                self.health = 5
                self.bullets = 8
                self.active_enemies = []
                self.stat = "playing"

                self.spawn = self.original_spawn
            else:
                store.money += 10

        def spawn(self):
            if self.stat == "dead":
                return
            for i in self.active_enemies:
                if i.stat == "hidden":
                    self.active_enemies.remove(i)
            if len(self.active_enemies) < 3:
                weights = [1] * (len(self.enemies) - 1) + [0.1]
                e = random.choices(self.enemies, weights=weights, k=1)[0]
                enemy = shooter_enemy(*e)
                for i in self.active_enemies:
                    if i.x == enemy.x:
                        if i.y == enemy.y:
                            return
                enemy.parent = self
                self.active_enemies.append(enemy)

        def shoot(self, enemy):
            if self.stat != "playing":
                return

            if self.bullets > 0:
                tag = f"shooter_bullets_{random.randint(0,10000)}"
                x, y = [*renpy.get_mouse_pos()]
                Show("shooter_bullets", x = x, y = y, z = 8, tag = tag, _tag = tag)()
                self.bullets -= 1
                renpy.play("minigames/shooting/gun_2.ogg", "sound")
                if not enemy:
                    return
                if not enemy.stat == "_dead":
                    renpy.play("minigames/shooting/kill.ogg", "sfx1")
                    enemy.change("_dead")
                    if enemy.image == 'shooting_villager':
                        self.kills -= 2
                    else:
                        self.kills += 1
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
            renpy.play("minigames/shooting/reload.ogg", "sound")
            self.bullets = 8

screen shooter():
    modal True
    style_prefix "shooter"
    default g = shooter_handler([
        [["shooting_thief", "shooting_villager"], 550, 335, .25],
        [["shooting_thief", "shooting_villager"], 650, 800, .25],
        [["shooting_thief", "shooting_villager"], 510, 1100, .25],
        [["shooting_thief", "shooting_villager"], 1230, 950, .25],
        [["shooting_thief", "shooting_villager"], 960, 575, .125],
    ])
    # add g.clock
    button:
        background None
        action Function(g.shoot, None)
    fixed:
        xysize 1920,1080
        for i in g.active_enemies:
            button:
                padding .0,.0 pos i.x,i.y background None anchor .5,1.0
                add i
                action Function(g.shoot, i)

    if g.stat == "start":
        button:
            align .5,.5
            text "Start"
            action Function(g.start)

    elif g.stat == "playing":
        timer 1 repeat True action Function(g.spawn)
        hbox:
            align .0,1.0 spacing 10  offset 20,-20
            for i in range(g.health):
                add "shooting_heart" at zoom(.25, True)
        if g.bullets > 0:
            hbox:
                align 1.0,1.0 spacing 10 offset -20,-20
                for i in range(g.bullets):
                    add "shooting_ammo" at zoom(.175, True)

        else:
            button:
                align 1.0,1.0  offset -20,-20
                text "Reload"
                action Function(g.reload)
        key "K_r" action Function(g.reload)

    elif g.stat == "dead":
        hbox:
            align .5,.5 spacing 10
            if money > 0:
                button:
                    padding 20,20
                    text "Restart"
                    action Function(g.restart)
            button:
                padding 20,20
                text "Done"
                action Return(g.kills)

    vbox:
        text str(g.kills)

style shooter_button:
    background Frame("shooting_shooter_frame", 6,6) padding (20,20)

screen shooter_bullets(x,y,z,tag):
    add "shooting_ammo_effect" pos x,y anchor .5,.5 at zoom(.1, True)
    timer 1 repeat True action Hide(tag)

label shooter_example:
    $ default_mouse = "shooter"

    show shooting_bg at truecenter:
        zoom 1.25 ypos 605
    $ quick_menu = False
    call screen shooter
    $ quick_menu = True

    # jump act1_1_shot_1
