init python:
    import random
    import time
    random.seed(time.time())
    def get_pixel(image, x, y):
        img = renpy.load_surface(image)
        return img.get_at((x, y))

    class doll_bar(renpy.Displayable):
        def __init__(self, image):
            super(renpy.Displayable,self).__init__()
            self.image = image
            self.x = 0
            self.y = 0
            self.x_direction = 8
            self.y_direction = 8
            self.x_moving = False
            self.y_moving = False
            self.limit = 450
            self.speed = 8

        def render(self,width,height,st,at):
            if self.y > self.limit:
                self.y_direction = -self.speed
            elif self.y < -self.limit:
                self.y_direction = self.speed

            if self.x > self.limit:
                self.x_direction = -self.speed
            elif self.x < -self.limit:
                self.x_direction = self.speed
            if self.y_moving:
                self.y += self.y_direction
            if self.x_moving:
                self.x += self.x_direction

            t = Transform(self.image, xanchor=0.5, yanchor=0.5)
            child_render = renpy.render(t, width, height, st, at)
            cw, ch = child_render.get_size()

            rv = renpy.Render(cw, ch)
            rv.blit(child_render, (self.x, self.y))

            renpy.redraw(self, 0)
            return rv

    class doll_player:
        def __init__(self, name, image, doll, doll_butt, indicator):
            self.name = name
            self.image = image
            self.doll = doll
            self.doll_butt = doll_butt
            self.indicator = indicator
            self.target = 0
            self.history = []
            self.current = []
            self.playing = True
            self.holding = None

        def pick(self, doll):
            if not self.playing:
                return
            if self.holding:
                return
            play_one("minigames/doll/take.ogg")
            self.holding = doll
            self.doll.remove(doll)

        def take(self, doll):
            if self.playing:
                return
            play_one("minigames/doll/take.ogg")
            self.doll.append(doll)
            Hide(doll)()

    class doll_class:
        def __init__(self, target, players):
            self.target = 301
            self.players = players
            self.bottom_arrow = doll_bar("doll_bottom_arrow")
            self.side_arrow = doll_bar("doll_side_arrow")
            self.bottom_arrow.y = 450
            self.side_arrow.x = -450
            self.current_player = None
            self.winner = None
            self.stat = "waiting"
            self.tries = 0

        def next(self):
            if len(self.current_player.doll) < 3:
                renpy.notify("Pick up your doll, will ya?")
                return
            self.players.append(self.current_player)
            self.current_player = self.players.pop(0)
            self.current_player.playing = True

        def throw(self):
            x = self.bottom_arrow.x
            y = self.side_arrow.y
            pixel = get_pixel("images/minigames/dolls/doll_zones.png", x+960, y+540)
            base = pixel[0]//10
            multiplier = (pixel[1]//100) + 1
            score = base*multiplier
            if base == 21:
                score = 25
            elif base == 22:
                score = 50
            elif base == 25:
                score = 0
            self.current_player.current.append(score)
            if base == 25:
                play_one("minigames/doll/doll_1.ogg")
                self.stick(x, y, True)
            else:
                play_one("minigames/doll/doll_2.ogg", "minigames/doll/doll_3.ogg", "minigames/doll/doll_4.ogg")
                self.stick(x, y)

        def stick(self, x, y, bounce = False):
            r = random.randint(0,180)
            tag = self.current_player.holding
            if bounce:
                Show("doll_doll_screen", x = x, y = y, r = r, tag = tag, g = self, _tag = tag, bounce = self.current_player.holding)()
            else:
                Show("doll_doll_screen", x = x, y = y, r = r, tag = tag, g = self, _tag = tag)()

            self.current_player.holding = None
            if len(self.current_player.doll) < 1:
                self.current_player.playing = False
                Show("doll_checker", g = self)()

        def check_for_win(self):
            self.current_player.target -= sum(self.current_player.current)
            if self.current_player.target < 0:
                self.winner = self.current_player
            else:
                self.current_player.current = []

        def test(self):
            x,y = renpy.get_mouse_pos()
            pixel = get_pixel("images/minigames/dolls/doll_zones.png", x, y)
            base = pixel[0]//10
            renpy.notify(base)

        def clicked(self):
            if not self.current_player.holding:
                return
            if self.bottom_arrow.x_moving:
                self.bottom_arrow.x_moving = False
                self.side_arrow.y_moving = True
            elif self.side_arrow.y_moving:
                self.side_arrow.y_moving = False
                self.throw()
            else:
                self.bottom_arrow.x_moving = True

        def start(self):
            for i in self.players:
                i.target = self.target
                i.history = []
                i.current = []
                i.playing = True
                i.holding = None
            self.current_player = self.players.pop(0)
            self.winner = None
            self.stat = "playing"

init:
    image orange_doll_1 = "orange_doll"
    image orange_doll_2 = "orange_doll"
    image orange_doll_3 = "orange_doll"

    image green_doll_1 = "green_doll"
    image green_doll_2 = "green_doll"
    image green_doll_3 = "green_doll"

transform doll_doll_animation(x,y,r):
    xoffset random.randint(0,100)
    yoffset random.randint(400,500)
    rotate 0
    zoom 3
    parallel:
        ease_circ .2 xoffset x yoffset y zoom 1
    parallel:
        linear .2 rotate r

transform doll_bounce_animation(x,y):
    alpha 0
    pause .2
    alpha 1
    xoffset 0 yoffset 0
    ease .2 xoffset random.randint(-100,100) yoffset 1200 rotate random.randint(300,500)

screen doll_checker(g):
    timer 3 action Function(g.check_for_win), Hide("doll_checker")

screen doll_indicator_screen(x, tag, g, img):
    button:
        align .5,1.0 xoffset x
        add g.current_player.indicator
        action Function(g.current_player.take, tag)

screen bounced_doll_screen(x, y, tag, g, img):
    timer .4 action Show("doll_indicator_screen", x = x, tag = tag, g = g, img = img, _tag = tag)
    button:
        align .5,.5 offset x,y at doll_bounce_animation(x, y)
        add tag
        action Function(g.current_player.take, tag)
    text tag yoffset 100

screen doll_doll_screen(x, y, r, tag, g, bounce = None):
    if bounce:
        timer .2 action Show("bounced_doll_screen", x = x, y = y, tag = tag, g = g, img = bounce, _tag = tag)

    button:
        align .5,.5 at doll_doll_animation(x, y, r)
        add g.current_player.doll_butt
        action Function(g.current_player.take, tag)

screen doll_screen():
    modal True
    default g = doll_class(
            301,
            [
                doll_player(
                    "June",
                    "doll_june",
                    ["orange_doll_1", "orange_doll_2", "orange_doll_3"],
                    "orange_doll_butt",
                    "orange_doll_indicator"
                ),
                doll_player(
                    "Debbie",
                    "doll_debbie",
                    ["green_doll_1", "green_doll_2", "green_doll_3"],
                    "green_doll_butt",
                    "green_doll_indicator"
                )
            ]
        )

    add g.bottom_arrow align .5,.5
    add g.side_arrow align .5,.5

    button:
        action Function(g.clicked)
    fixed:
        xysize 430,73 align 1.0,1.0 offset -40,-100
        hbox:
            align .5,.5 spacing 20 yoffset -40
            if g.current_player:
                for i in g.current_player.doll:
                    button:
                        add i
                        action Function(g.current_player.pick, i)
        add "doll_holder":
            align .5,.5
        if g.current_player:
            if not g.current_player.playing:
                button:
                    align .5,.5
                    text "Next"
                    action Function(g.next)
    if g.current_player:
        vbox:
            offset 40,40
            add g.current_player.image
            text g.current_player.name
            text "[g.current_player.target]"
            hbox:
                text "[g.current_player.current]"

    if g.stat == "waiting":
        frame:
            align .5,.5 background "#000d" padding 40,40
            vbox:
                text "Are you ready?"
                button:
                    align .5,.5 background "#000d" padding 20,20
                    text "Start"
                    action Function(g.start)

    if g.winner:
        frame:
            align .5,.5 background "#000d" padding 40,40
            vbox:
                text "Great job!"
                button:
                    align .5,.5 background "#000d" padding 20,20
                    text "Next"
                    action Return(g.winner)

label doll_game_center:
    scene black
    show doll_board with dissolve
    call screen doll_screen
