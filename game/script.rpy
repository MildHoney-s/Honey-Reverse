### Auto-save activation:
init -1 python hide:
    config.has_autosave = True

# The script of the game goes in this file.
init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("transition/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("transition/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
    Solid("#000")
image white:
    Solid("#FFF")


init:
    python:
        import math

        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()

                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

        Shake = renpy.curry(_Shake)

init:
    $ sshake = Shake((0, 0, 0, 0), 0.25, dist=5)
    $ lshake = Shake((0, 0, 0, 0), 0.5, dist=5)
    $ ashyShake = Shake((0, 0, 0, 0), 1, dist=10)
    define walkingVertical = Move((0, 5), (0, -5), 0.75, bounce=True, repeat=True, delay=2)
    define runningVertical = Move((2, 10), (2, -10), 0.25, bounce=True, repeat=True, delay=1.75)
    define dottransition = ImageDissolve("images/transition/dots.png", 1.0, time_warp=_warper.easeout)
    define transition_4 = ImageDissolve("images/transition/4.jpg", 1.0, time_warp=_warper.easeout)
    define tv_transition = ImageDissolve("images/transition/tv.png", 1.0, time_warp=_warper.easeout)
    define curtain = ImageDissolve("images/transition/curtain.jpeg", 1.0, time_warp=_warper.easeout)


# The game starts here.
label start:
    #$ povname = "Test"
    #$ _skipping = False
    #$ config.rollback_enabled = False
    # $ persistent.gameclear = True
    #jump doll_game_center
    jump act1_1_shot_1
    # $ money = 100
    # jump act2_3_shot_1
    # jump whack_a_mole_game_center
    # jump shooting_game_center