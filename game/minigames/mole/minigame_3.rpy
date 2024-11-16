init python:
    import renpy.store as store

    class mole:
        def __init__(self, x, y):
            self.name = None
            self.image = "mole_honey"
            self.injured_image = f'{self.image}_injured'
            self.x = x
            self.y = y
            self.yo = 500

    class whack_a_mole_game:
        def __init__(self, layers, moles):
            self.layers = layers
            self.moles = moles

            self.shaking = False
            self.last = None
            self.popped = 0
            self.whacked = 0
            self.body = 0

        def whack(self, mole):
            mole.yo = 500
            self.whacked += 1
            renpy.play("minigames/mole/whack.ogg", "sound")

        def insert_coin(self):
            if self.body < 1:
                self.popped = 0
                self.whacked = 0
            self.body += 1
            # handle global money in game
            if store.money >= 0:
                store.money -= 10
            else:
                store.money += 10
            renpy.play("minigames/mole/coin.ogg", "sound")

        def body_shot(self):
            self.body -= 1
            if self.body < 0:
                self.body = 0
            renpy.play("minigames/mole/body.ogg", "sound")
            self.shaking = True
            for i in self.layers:
                if isinstance(i, mole):
                    i.yo = 490

        def stop_shaking(self):
            self.shaking = False

        def tick(self):
            for i in self.layers:
                if isinstance(i, mole) and i.yo == 0:
                    i.yo = 490
                    renpy.play("minigames/mole/godown.ogg", "sound")

            m = renpy.random.choice(self.layers)

            if isinstance(m, mole) and m.yo and m != self.last:
                m.image = renpy.random.choice(self.moles)
                m.injured_image = f'{m.image}_injured'
                m.yo = 0
                renpy.play("minigames/mole/popup.ogg", "sound")
                self.popped += 1
            self.last = m

image resize_mole_coin_acceptor = im.Scale("images/minigames/mole/mole_coin_acceptor.png", 20, 60)

screen whack_a_mole(g):
    default insert = "insert"
    frame:
        padding 0,0 background None
        if g.shaking:
            at whack_shaking
        for i in g.layers:
            if isinstance(i, list):
                button:
                    xalign .5 padding 0,0 focus_mask True background None yoffset i[1]
                    add i[0]
                    action Function(g.body_shot)
            else:
                frame:
                    align .5,.61 offset i.x,i.y background None padding 0,0
                    button:
                        focus_mask True
                        at mole_pos(i.yo)

                        fixed:
                            fit_first True
                            add i.image size(300,500)
                            if i.yo > 499:
                                add i.injured_image size(300,500)
                        action Function(g.whack, i)
        frame:
            align .569,.2 xysize 120,50 background None
            text "{} / {}".format(g.whacked, g.popped) align .5,.5 size 20 color "#0f0"
        vbox:
            align .74,-.12 yoffset 246 spacing 20
            frame:
                xysize 500,20 background None
                if g.body:
                    text str(g.body) align .7,.1 color "#0f0"
                else:
                    # timer 1 repeat True action ToggleScreenVariable("insert", "insert", "coin")
                    text "insert coin" align .75,-.05 color "#0f0" size 20
            button:
                align .725,.5 xysize 40,70 background "resize_mole_coin_acceptor"
                action Function(g.insert_coin)
    if g.body:
        timer 1.2 repeat True action Function(g.tick)
    if g.shaking:
        timer .4 repeat True action Function(g.stop_shaking)

transform mole_pos(yo):
    ease .4 yoffset yo

transform whack_shaking:
    ease .1 xoffset -20
    ease .1 xoffset 20
    repeat

default whack_1 = whack_a_mole_game(
    [
        # ["mole_whack cover small", 345],
        ["mole_4", 0],
        # ["mole_whack cover big", 499],
        ["mole_3", 364],
        mole(-350, -200), mole(0, -200), mole(350, -200),
        # ["mole_whack cover small", 643],
        ["mole_2", 559],
        mole(-420, 25), mole(10, 25), mole(420, 25),
        ["mole_1", 804],
    ],
    ["mole_honey", "mole_cubie", "mole_huangyang", "mole_bluebell", "mole_dustirion", "mole_manta"]
)

label whack_a_mole_game_center:
    call screen whack_a_mole(whack_1)
