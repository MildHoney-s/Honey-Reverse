init python:
    renpy.music.register_channel("sfx1", "sfx", False)

    def play_one(*args):
        chosen = random.choice(args)
        renpy.play(chosen, "sfx1")