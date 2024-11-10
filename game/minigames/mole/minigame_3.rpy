init python:
    class mole:
        def __init__(self, x, y):
            self.name = None
            self.image = "mole_molly"
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
                m.yo = 0
                renpy.play("minigames/mole/popup.ogg", "sound")
                self.popped += 1
            self.last = m

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
                            add i.image
                            if i.yo > 499:
                                add "mole_bands"
                        action Function(g.whack, i)
        frame:
            align .569,.04 xysize 120,50 background None
            text "{} / {}".format(g.whacked, g.popped) align .5,.5 size 20 color "#0f0"
        vbox:
            align .772,.0 yoffset 246 spacing 20
            frame:
                xysize 120,50 background None
                if g.body:
                    text str(g.body) align .5,.5 color "#0f0"
                else:
                    timer 1 repeat True action ToggleScreenVariable("insert", "insert", "coin")
                    text insert align .5,.5 color "#0f0" size 20
            button:
                align .5,.5 xysize 40,70 background None
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
        ["mole_whack cover small", 345],
        ["mole_whack_top", 0],
        mole(-190, -140), mole(190, -140),
        ["mole_whack cover big", 499],
        ["mole_whack_up", 410],
        mole(-382, 0), mole(0, 0), mole(382, 0),
        ["mole_whack cover small", 643],
        ["mole_whack_down", 562],
        mole(-190, 140), mole(190, 140),
        ["mole_whack_bottom", 711],
    ],
    ["mole_molly", "mole_eddmo", "mole_mall", "mole_melle", "mole_mill", "mole_mole doc", "mole_mollo"]
)

label whack_a_mole_game_center:
    call screen whack_a_mole(whack_1)
