# a simple function that puts a string into the clipboard
init python:
    import pygame.scrap
    def clip_put(m):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, m.encode("utf-8"))
    def find_my_mouse():
        m = renpy.get_mouse_pos()
        pos = str(m[0]) + "," + str(m[1])
        clip_put(pos)
    config.underlay.append(
        renpy.Keymap(
            K_BACKQUOTE=lambda: find_my_mouse()
        )
    )