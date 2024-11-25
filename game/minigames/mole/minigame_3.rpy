default persistent.mole_highscore = 120
default limit_coin_mole = False
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
            self.last = []
            self.popped = 0
            self.whacked = 0
            self.coin = 3 # Number of coins inserted
            self.body = 0
            self.time_remaining = 60  # Timer starts at 60 seconds
            self.speed = 1.2  # Initial mole pop-up interval
            self.running = False  # Whether the game is running
            self.score = 0  # Current score
            # self.highest_score = persistent.mole_highscore # Highest score

        def whack(self, mole):
            if self.running:
                mole.yo = 500
                self.whacked += 1
                self.score += 10  # Increase score by 10 for each successful whack
                if self.score > persistent.mole_highscore:
                    persistent.mole_highscore = self.score
                renpy.play("minigames/mole/whack.ogg", "sound")

        def insert_coin(self):
            if not self.running and self.coin < 3 :
                self.coin += 1  # Add one coin
                renpy.play("minigames/mole/coin.ogg", "sound")

        def click_to_play(self):
            if self.coin >= 3 and not self.running:
                self.started = True  # Enable game start
                self.coin -= 3  # Deduct 3 coins
                renpy.play("minigames/mole/start.mp3", "sound")
                self.reset_game()

        def reset_game(self):
            self.popped = 0
            self.whacked = 0
            self.score = 0
            self.time_remaining = 60
            self.speed = 1.2
            self.running = True

        def tick(self):
            if not self.running:
                return

            # Decrease the timer
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.time_remaining = 0
                for i in self.layers:
                    if isinstance(i, mole) and i.yo != 500:
                        i.yo = 500
                self.running = False  # Stop the game
                renpy.play("minigames/mole/timeout.mp3", "sound")
                return

            # Handle multiple mole popping
            for i in self.layers:
                if isinstance(i, mole) and i.yo == 0:
                    i.yo = 490
                    renpy.play("minigames/mole/godown.ogg", "sound")

            for _ in range(3):  # Show two moles at a time
                m = renpy.random.choice(self.layers)

                if isinstance(m, mole) and m.yo and m not in self.last:
                    m.image = renpy.random.choice(self.moles)
                    m.injured_image = f'{m.image}_injured'
                    m.yo = 0
                    renpy.play("minigames/mole/popup.ogg", "sound")
                    self.popped += 1
                    self.last.append(m)

            # Limit the number of active moles
            if len(self.last) > 3:
                self.last.pop(0)

            # Increase speed as the game progresses
            if self.time_remaining <= 40:
                self.speed = 0.8
            if self.time_remaining <= 20:
                self.speed = 0.6

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

screen whack_a_mole(g):
    frame:
        padding 0, 0 background None
        if g.shaking:
            at whack_shaking

        # Show moles
        for i in g.layers:
            if isinstance(i, list):
                button:
                    xalign .5 padding 0, 0 focus_mask True background None yoffset i[1]
                    add i[0]
                    action Function(g.body_shot)
            else:
                frame:
                    align .5, .61 offset i.x, i.y background None padding 0, 0
                    button:
                        focus_mask True
                        at mole_pos(i.yo)

                        fixed:
                            fit_first True
                            add i.image size(300, 500)
                            if i.yo > 499:
                                add i.injured_image size(300, 500)
                        action Function(g.whack, i)

        # Timer display
        frame:
            align .5, .08 xysize 240, 80 background None
            if g.time_remaining >= 10:
                text "TIME \n 0{}".format(g.time_remaining) align .5, .5 size 30 color "#f00"
            else:
                text "TIME \n 00{}".format(g.time_remaining) align .5, .5 size 30 color "#f00"
        # Score display
        frame:
            align .4, .15 xysize 240, 80 background None
            if g.score < 10:
                text "SCORE \n  00{}".format(g.score) align .5, .5 size 30 color "#0f0"
            elif g.score < 100:
                text "SCORE \n  0{}".format(g.score) align .5, .5 size 30 color "#0f0"
            else:
                text "SCORE \n  {}".format(g.score) align .5, .5 size 30 color "#0f0"
        # Highest score display
        frame:
            align .61, .15 xysize 240, 80 background None
            text "HIGH SCORE \n      {}".format(persistent.mole_highscore) align .5, .5 size 30 color "#ff0"

        # Show "Click to Play" or Insert Coin
        if not g.running:
            frame:
                align .5, .24 background None
                if g.coin < 3:
                    text "Insert {} More Coins".format(3 - g.coin) style "blink_text" at blink
                else:
                    textbutton "CLICK HERE TO START":
                        text_style "tx_button"
                        action Function(g.click_to_play)

        button:
            align .736, .17 xysize 93, 29 background "images/minigames/mole/mole_coin_acceptor.png"
            if tokens-3 >= 6 and g.coin < 3:
                action [Function(g.insert_coin),SetVariable("tokens",tokens-1)]
            elif tokens >= 8 and g.coin >= 1 and g.coin < 3:
                action [Function(g.insert_coin),SetVariable("tokens",tokens-1)]
            elif tokens >= 7 and g.coin >= 2 and g.coin < 3:
                action [Function(g.insert_coin),SetVariable("tokens",tokens-1)]
            elif g.coin != 3:
                action SetVariable("limit_coin_mole",True)
    if limit_coin_mole:
        text "NOT ENOUGH COIN LEFT FOR THIS GAME" align(0.5, 0.5) color "#ff0000ff" outlines [ (2, "#ffffff", 0, 0) ]
    if g.coin == 0 and not g.running:
        textbutton "Exit":
            text_style "exit_tx_button"
            align (1.0, 1.0)
            action Return()
    if not g.running:
        imagebutton auto "images/tutorial/howtoplay_button_%s.png":
            focus_mask True
            action Show("tutorial_popup",tutorial="mole")
    hbox:
        spacing 25
        align (0.975,0.025)
        add "doll_coin" size (100,100)
        text "{}".format(tokens) size 100 offset (0, -20) color "#abaeaeff"


    if g.running:
        timer g.speed repeat True action Function(g.tick)
    if g.shaking:
        timer .4 repeat True action Function(g.stop_shaking)

transform blink:
    alpha 1.0
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.0
        repeat

# Define the style for blinking text
style blink_text:
    size 35
    color "#be58b2"  # White text color
    outlines [(2, "#000000", 0, 0)]  # Black outline for better visibility

style tx_button:
    color "#be58b2"
    size 35

style exit_tx_button:
    color "#84efe8"
    size 80

transform mole_pos(yo):
    ease .4 yoffset yo

transform whack_shaking:
    ease .1 xoffset -20
    ease .1 xoffset 20
    repeat

default whack_1 = whack_a_mole_game(
    [
        ["mole_4", 0],
        ["mole_3", 365],
        mole(-350, -200), mole(0, -200), mole(350, -200),
        ["mole_2", 550],
        mole(-420, 25), mole(10, 25), mole(420, 25),
        ["mole_1", 789],
    ],
    ["mole_honey", "mole_cubie", "mole_huangyang", "mole_bluebell", "mole_dustirion", "mole_manta"]
)

label whack_a_mole_game_center:
    $ quick_menu = False
    call screen whack_a_mole(whack_1)
    $ quick_menu = True
    jump act2_3_shot_2