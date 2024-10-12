


init python:
    def spawn_mana(x, y, mana, g):
        tag = f"spawn_{random.randint(0,10000)}"
        Show("spawn_mana_screen", x = x, y = y, mana = mana, g= g, tag = tag, _tag = tag)()



screen spawn_mana_screen(x,y,mana,g,tag):
    add "mana_drop" align (0.5, 0.5) at mana_get_animation(x, y)
    timer .6 repeat True action Function(g.gain_mana, mana)
    timer 1 repeat True action Hide(tag)


transform mana_get_animation(x, y):
    xoffset x yoffset y
    ease .2 yoffset y-60
    parallel:
        ease .5 xoffset -900
    parallel:
        pause .4
        ease .1 alpha 0
    parallel:
        ease .6 yoffset -540


# self.parent.spawn_explosion(self.x, self.y)
