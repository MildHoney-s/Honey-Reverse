init python:
    def spawn_stamina(x, y, stamina, g):
        tag = f"spawn_{random.randint(0,10000)}"
        Show("spawn_stamina_screen", x = x, y = y, stamina = stamina, g= g, tag = tag, _tag = tag)()

screen spawn_stamina_screen(x,y,stamina,g,tag):
    add "cafe_coin" align (0.5, 0.5) size (48, 48) at stamina_get_animation(x, y)
    timer .6 repeat True action Function(g.gain_stamina, stamina)
    timer 1 repeat True action Hide(tag)

transform stamina_get_animation(x, y):
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
