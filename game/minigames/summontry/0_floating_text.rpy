init python:
    def floating_text(m, x = 0, y = 0):
        t = "fight_notif{}".format(random.randint(1, 10000))
        renpy.show_screen("floating_text_screen", msg = m, x = x, y = y, tag = t, _tag = t)

transform floating_text_animation(o):
    parallel:
        ease 2 yoffset o
    parallel:
        pause .2
        ease 1.8 alpha 0

screen floating_text_screen(msg, x, y, tag):
    zorder 2000
    timer 1.3 action Hide(tag)
    if int(msg) < 0:
        text f"{msg}" at floating_text_animation(200):
            align .5,.5 size 30 color "#900" outlines [ (4, "#000", 0, 0) ]
            offset (x,y)
    else:
        text f"{msg}" at floating_text_animation(-200):
            align .5,.5 size 30 color "#4f0" outlines [ (4, "#000", 0, 0) ]
            offset (x,y)

