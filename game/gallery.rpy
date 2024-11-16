screen gallery_1():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("main_menu", im.Scale("gui/main_menu.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("CG1", im.Scale("images/cg/cg2.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("CG2", im.Scale("images/cg/cg3.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CG3", im.Scale("images/cg/cg4.jpg" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CG4", im.Scale("images/cg/cg5.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image extra condition

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_2():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("SD1", im.Scale("images/sd/ashy_sd_1.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD2", im.Scale("images/sd/ami_sd_2.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD3", im.Scale("images/sd/sd_wanted.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("SD4", im.Scale("images/sd/mildru_sd_1.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("SD5", im.Scale("images/sd/delbyou.jpg" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5) # Locked image
        add g.make_button("SD6", im.Scale("images/sd/milddel.jpg" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_3():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("SD7", im.Scale("images/sd/dual_sd.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD8", im.Scale("images/sd/mild_please_sd.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD9", im.Scale("images/sd/photo_sd.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("SD10", im.Scale("images/sd/ppan_sd.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("SD11", im.Scale("images/sd/garapon_sd.jpg" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5) # Locked image

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_4():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("CB1", im.Scale("images/sd/chibi_1.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image  # Unlocked first image
        add g.make_button("CB2", im.Scale("images/sd/chibi_2.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB3", im.Scale("images/sd/rabbit.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("CB4", im.Scale("images/sd/capybara.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB5", im.Scale("images/sd/hornbill.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB6", im.Scale("images/sd/panda.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_5():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("CB7", im.Scale("images/sd/del_lili.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_6():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("AS1", im.Scale("images/assets/cucumbag.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("AS2", im.Scale("images/assets/cucumburg.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS3", im.Scale("images/assets/milktea.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS4", im.Scale("images/assets/omurice.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS5", im.Scale("images/assets/diary.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS6", im.Scale("images/assets/caring.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935


screen gallery_7():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add gui.main_menu_background
    add "images/save_load/menu_gallery.png"

    # A grid of buttons.
    # Create a grid layout with 2 rows and 3 columns.
    grid 3 2:

        xpos 119
        ypos 168
        spacing 13

        # Call make_button to display the gallery images or locked placeholders.
        add g.make_button("AS7", im.Scale("images/assets/siralfred.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("AS8", im.Scale("images/assets/spa.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS9", im.Scale("images/assets/edamame.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS10", im.Scale("images/assets/cake.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS11", im.Scale("images/assets/locket_close.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 7 1:
                spacing 15
                for g_page in range(1,8):
                    frame:
                        xsize 68
                        ysize 68
                        if g_page == persistent.current_page_gallery:
                            image "images/save_load/page_hover.png"
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page_gallery",g_page),ShowMenu("gallery_"+str(g_page))]
                            text "[g_page]":
                                style "slot_time_text" align((0.65,0.65))

    imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935