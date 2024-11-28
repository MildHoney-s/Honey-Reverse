screen gallery_1():

    # Ensure this replaces the main menu.
    tag menu
    key "K_ESCAPE" action Return()

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
        add g.make_button("main_menu", im.Scale("images/gallery/gallery_1.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("CG1", im.Scale("images/gallery/gallery_2.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("CG2", im.Scale("images/gallery/gallery_3.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CG3", im.Scale("images/gallery/gallery_4.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CG4", im.Scale("images/gallery/gallery_5.png" if persistent.gameclear and persistent.secret_cg else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image extra condition

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("SD1", im.Scale("images/gallery/gallery_6.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD2", im.Scale("images/gallery/gallery_7.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD3", im.Scale("images/gallery/gallery_8.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("SD4", im.Scale("images/gallery/gallery_9.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("SD5", im.Scale("images/gallery/gallery_10.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5) # Locked image
        add g.make_button("SD6", im.Scale("images/gallery/gallery_11.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("SD7", im.Scale("images/gallery/gallery_12.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD8", im.Scale("images/gallery/gallery_13.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("SD9", im.Scale("images/gallery/gallery_14.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("SD10", im.Scale("images/gallery/gallery_15.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("SD11", im.Scale("images/gallery/gallery_16.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5) # Locked image

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("CB1", im.Scale("images/gallery/gallery_17.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image  # Unlocked first image
        add g.make_button("CB2", im.Scale("images/gallery/gallery_18.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB3", im.Scale("images/gallery/gallery_19.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("CB4", im.Scale("images/gallery/gallery_20.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB5", im.Scale("images/gallery/gallery_21.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("CB6", im.Scale("images/gallery/gallery_22.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("CB7", im.Scale("images/gallery/gallery_23.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("CB8", im.Scale("images/gallery/gallery_24.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("AS1", im.Scale("images/gallery/gallery_25.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("AS2", im.Scale("images/gallery/gallery_26.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS3", im.Scale("images/gallery/gallery_27.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS4", im.Scale("images/gallery/gallery_28.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS5", im.Scale("images/gallery/gallery_29.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS6", im.Scale("images/gallery/gallery_30.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)

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
    key "K_ESCAPE" action Return()

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
        add g.make_button("AS7", im.Scale("images/gallery/gallery_31.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Unlocked first image
        add g.make_button("AS8", im.Scale("images/gallery/gallery_32.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS9", im.Scale("images/gallery/gallery_33.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)
        add g.make_button("AS10", im.Scale("images/gallery/gallery_34.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image
        add g.make_button("AS11", im.Scale("images/gallery/gallery_35.png" if persistent.gameclear else "images/save_load/locked.png", 552, 314), xalign=0.5, yalign=0.5)  # Locked image

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