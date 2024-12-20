﻿################################################################################
## Initialization
################################################################################

init offset = -1
default money = 0
default honey_score = 0
default tokens = 1
default persistent.gameclear = False
default persistent.secret_cg = False
default persistent.current_page = 1
default persistent.current_page_gallery = 1
default is_video_render = False
default load_from_main = True
default config_from_main = True
default show_skip_btn = True
default history_name_checker = ""
default nvl_name_checker = ""

init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # The first unlocked image (main_menu.png)
    g.button("main_menu")   # Button for the first unlocked image
    g.image("gui/main_menu.png")
    g.condition("persistent.gameclear")

    # Locked images
    g.button("CG1")
    g.image(im.Scale("images/cg/cg2.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("CG2")
    g.image(im.Scale("images/cg/cg3.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("CG3")
    g.image(im.Scale("images/cg/cg4.jpg",1920,1080))
    g.condition("persistent.gameclear")

    g.button("CG4")
    g.image(im.Scale("images/cg/cg5.png",1920,1080))
    g.condition("persistent.gameclear and persistent.secret_cg")

    g.button("SD1")
    g.image(im.Scale("images/sd/ashy_sd_1.png",1920,1080))
    g.image(im.Scale("images/sd/ashy_sd_2.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD2")
    g.image(im.Scale("images/sd/ami_sd_1.png",1920,1080))
    g.image(im.Scale("images/sd/ami_sd_2.png",1920,1080))
    g.image(im.Scale("images/sd/ami_sd_3.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD3")
    g.image(im.Scale("images/sd/sd_wanted.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD4")
    g.image(im.Scale("images/sd/mildru_sd_1.png",1920,1080))
    g.image(im.Scale("images/sd/mildru_sd_2.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD5")
    g.image(im.Scale("images/sd/delbyou.jpg",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD6")
    g.image(im.Scale("images/sd/milddel.jpg",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD7")
    g.image(im.Scale("images/sd/dual_sd.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD8")
    g.image(im.Scale("images/sd/mild_please_sd.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD9")
    g.image(im.Scale("images/sd/photo_sd.png",1620,1080))
    g.condition("persistent.gameclear")

    g.button("SD10")
    g.image(im.Scale("images/sd/ppan_sd.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("SD11")
    g.image(im.Scale("images/sd/garapon_sd.jpg",1920,1080))
    g.image(im.Scale("images/sd/garapon_win_sd.jpg",1920,1080))
    g.condition("persistent.gameclear")

    g.button("CB1")
    g.image(im.Scale("images/sd/chibi_1.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("CB2")
    g.image(im.Scale("images/sd/chibi_2.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("CB3")
    g.image(im.Scale("images/sd/som.png",1920,1080))
    g.condition("persistent.gameclear")

    g.button("CB4")
    g.image(im.Scale("images/sd/rabbit.png",1512,1080))
    g.condition("persistent.gameclear")

    g.button("CB5")
    g.image(im.Scale("images/sd/capybara.png",1512,1080))
    g.condition("persistent.gameclear")

    g.button("CB6")
    g.image(im.Scale("images/sd/hornbill.png",1512,1080))
    g.condition("persistent.gameclear")

    g.button("CB7")
    g.image(im.Scale("images/sd/panda.png",1512,1080))
    g.condition("persistent.gameclear")

    g.button("CB8")
    g.image(im.Scale("images/sd/del_lili.png",1512,1080))
    g.condition("persistent.gameclear")

    g.button("AS1")
    g.image(im.Scale("images/assets/cucumbag.png",1000,1080))
    g.condition("persistent.gameclear")

    g.button("AS2")
    g.image(im.Scale("images/assets/cucumburg.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS3")
    g.image(im.Scale("images/assets/milktea.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS4")
    g.image(im.Scale("images/assets/omurice.png",1000,1000))
    g.image(im.Scale("images/assets/omurice_red.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS5")
    g.image(im.Scale("images/assets/diary.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS6")
    g.image(im.Scale("images/assets/caring.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS7")
    g.image(im.Scale("images/assets/siralfred.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS8")
    g.image(im.Scale("images/assets/spa.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS9")
    g.image(im.Scale("images/assets/edamame.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS10")
    g.image(im.Scale("images/assets/cake.png",1000,1000))
    g.image(im.Scale("images/assets/cake2.png",1000,1000))
    g.condition("persistent.gameclear")

    g.button("AS11")
    g.image(im.Scale("images/assets/locket_close.png",1000,1000))
    g.image(im.Scale("images/assets/locket_open.png",1000,1000))
    g.condition("persistent.gameclear")

    # The transition used when switching images.
    g.transition = dissolve


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                if "&" in who:
                    text who id "who" size 30
                else:
                    text who id "who"

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

    line_spacing 10

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 480
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if not is_video_render:
        key "K_ESCAPE" action ShowMenu("preferences")
        key "mouseup_3" action ShowMenu("preferences")

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.978

            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            if show_skip_btn:
                textbutton _("Skip") action Call("confirm_pause")
            else:
                textbutton _("Skip") action Return() sensitive False
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Setting") action ShowMenu("preferences")
            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.
image blackimage = Solid("#000000")
default lastsave = renpy.newest_slot(r"\d+")
screen black_screen():
    add (blackimage)

screen navigation():

    add im.Scale("gui/game_logo.png",480,280):
        align(0.05,0.025)

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:

            # Start Button (Image)
            imagebutton auto "images/main_menu/start_%s.png":
                focus_mask True
                action [SetVariable("load_from_main", False), SetVariable("config_from_main", False), Start()]

            # Load Button (Image)
            imagebutton auto "images/main_menu/load_%s.png":
                focus_mask True
                action [SetVariable("load_from_main", True), ShowMenu("load")]

            # Preferences Button (Image)
            imagebutton auto "images/main_menu/settings_%s.png":
                focus_mask True
                action [SetVariable("config_from_main", True), ShowMenu("preferences")]

            imagebutton auto "images/main_menu/gallery_%s.png":
                focus_mask True
                action [SetVariable("config_from_main", True),ShowMenu("gallery_"+str(persistent.current_page_gallery))]

        else:

            # History Button (Image)R
            imagebutton auto "images/main_menu/history_%s.png":
                focus_mask True
                action ShowMenu("history")

            # Save Button (Image)
            imagebutton auto "images/main_menu/save_%s.png":
                focus_mask True
                action ShowMenu("save")

            # Load Button (Image)
            imagebutton auto "images/main_menu/load_%s.png":
                focus_mask True
                action ShowMenu("load")

            # Preferences Button (Image)
            imagebutton auto "images/main_menu/settings_%s.png":
                focus_mask True
                action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            imagebutton auto "images/main_menu/exit_%s.png":
                focus_mask True
                action Quit(main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    #add "gui/main_menubar.png"

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 300

style game_menu_navigation_frame:
    xsize 230
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    add gui.game_menu_background
    imagebutton auto "gui/button/window_%s.png" action Return() align(0.91,0.1)
    text ("Save") align(0.095,0.1):
        style "pref_label_text"
    hbox:

        xalign 0.14
        yalign 0.145
        spacing 5

        textbutton _("Home") action MainMenu()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')
        textbutton _("Setting") action ShowMenu("preferences")

    use file_slots(_("Save"))

screen load():

    tag menu
    key "K_ESCAPE" action Return()
    if load_from_main == False:
        add gui.game_menu_background
        imagebutton auto "gui/button/window_%s.png" action Return() align(0.91,0.1)
        text ("Load") align(0.095,0.1):
            style "pref_label_text"
        hbox:

            xalign 0.14
            yalign 0.145
            spacing 5

            textbutton _("Home") action MainMenu()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Setting") action ShowMenu("preferences")
    else:
        add gui.main_menu_background
        add "images/save_load/menu_load.png"
        imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.935

    use file_slots(_("Load"))

screen file_slots(title):

    vbox:
        if load_from_main == False:
            xpos 176
            ypos 236
        else:
            xpos 119
            ypos 168
        grid 3 2:
            if load_from_main == False:
                spacing 13
            else:
                spacing 60
            for i in range(6):
                $ slot = i + 1
                frame:
                    xsize 512
                    ysize 288

                    imagebutton auto "images/save_load/bg_frame_%s.png" action FileAction(slot)

                    image FileScreenshot(slot) align((0,0)) xsize 512 ysize 288

                    image "images/save_load/Slot_number.png" align((0.01,0.048))
                    text "#[slot]":
                            style "slot_number_text" align((0.05,0))

    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            style_prefix "page"
            grid 10 1:
                spacing 15
                for page in range(1,11):
                    frame:
                        xsize 68
                        ysize 68
                        if page == persistent.current_page:
                            image "images/save_load/page_hover.png"
                            text "[page]":
                                style "slot_time_text" align((0.65,0.65))
                        else:
                            imagebutton auto "images/save_load/page_%s.png" action [SetVariable("persistent.current_page",page),FilePage(page)]
                            text "[page]":
                                style "slot_time_text" align((0.65,0.65))

style slot_number_text is gui_label_text

style slot_button_text is gui_button_text

style slot_time_text:
    font "fonts/Mali-SemiBold.ttf"
    size 40
    color '#320000'

style slot_number_text:
    font "fonts/Mali-SemiBold.ttf"
    size 37
    spacing 2
    color '#750000'

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    if config_from_main == False:
        add gui.game_menu_background
        imagebutton auto "gui/button/window_%s.png" action Return() align(0.91,0.1)
        text ("Setting") align(0.095,0.1):
            style "pref_label_text"
        hbox:

            xalign 0.14
            yalign 0.145
            spacing 5

            textbutton _("Home") action MainMenu()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Setting") action ShowMenu("preferences")
    else:
        add gui.main_menu_background
        add "images/config/settings.png" align((0.5, 0.5))
        imagebutton auto "gui/button/return_%s.png" action Return() xalign 0.5 yalign 0.825

    image "images/config/setting_message.png" xpos 516 ypos 416
    image "images/config/setting_skip.png" xpos 949 ypos 273
    image "images/config/setting_sound.png" xpos 516 ypos 589
    image "images/config/setting_window.png" xpos 516 ypos 273
    use game_menu(_("Preferences"), scroll="viewport"):
        hbox:
            hbox:
                xpos 245
                ypos 15
                spacing 6
                if preferences.fullscreen == False:
                    imagebutton:
                        focus_mask True
                        idle "images/config/settings_checked.png"
                    text ("Window"):
                        style "setting_text"
                    imagebutton auto "images/config/settings_%s.png":
                        focus_mask True
                        action Preference("display", "fullscreen")

                    text ("Full Screen"):
                        style "setting_text"
                else:
                    imagebutton auto "images/config/settings_%s.png":
                        focus_mask True
                        action Preference("display", "any window")

                    text ("Window"):
                        style "setting_text"
                    imagebutton:
                        focus_mask True
                        idle "images/config/settings_checked.png"

                    text ("Full Screen"):
                        style "setting_text"
            hbox:

                xpos 360
                ypos 15

                spacing 6

                if preferences.skip_unseen == False:
                    imagebutton:
                        focus_mask True
                        idle "images/config/settings_checked.png"
                    text ("Only Seen Text "):
                        style "setting_text"
                    imagebutton auto "images/config/settings_%s.png":
                        focus_mask True
                        action Preference("skip", "toggle")
                    text ("All Text"):
                        style "setting_text"
                else:
                    imagebutton auto "images/config/settings_%s.png":
                        focus_mask True
                        action Preference("skip", "toggle")
                    text ("Only Seen Text"):
                        style "setting_text"
                    imagebutton:
                        focus_mask True
                        idle "images/config/settings_checked.png"
                    text ("All Text"):
                        style "setting_text"

    hbox:
        style_prefix "slider"
        box_wrap True
        vbox:
            text ("Music"):
                style "setting_text"
            bar :
                value Preference("music volume")
                xsize 819
                ysize 24
            xpos 532
            ypos 640

    hbox:
        style_prefix "slider"
        box_wrap True
        vbox:
            text ("SFX"):
                style "setting_text"
            bar :
                value Preference("sound volume")
                xsize 819
                ysize 24
                xalign 0.5
            xpos 532
            ypos 700

    hbox:
        style_prefix "slider"
        box_wrap True
        vbox:
            text ("Text Speed"):
                style "setting_text"
            bar :
                value Preference("Text Speed")
                xsize 819
                ysize 24
            xpos 532
            ypos 470
    hbox:

        xpos 1248
        ypos 762
        spacing 6
        imagebutton :
            selected_idle "images/config/settings_checked.png"
            selected_hover "images/config/settings_checked.png"
            idle "images/config/settings_idle.png"
            hover "images/config/settings_idle.png"
            action Preference("all mute", "toggle")

        text ("Mute All"):
            style "setting_text"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style setting_text:
    font "fonts/Mali-Bold.ttf"
    size 25
    spacing 2
    color '#000000'

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    add gui.game_menu_background
    imagebutton auto "gui/button/window_%s.png" action Return() align(0.91,0.1)
    text ("History") align(0.095,0.1):
        style "pref_label_text"
    hbox:

        xalign 0.14
        yalign 0.145
        spacing 5

        textbutton _("Home") action MainMenu()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')
        textbutton _("Setting") action ShowMenu("preferences")

    predict False
    frame:

        style_prefix "history"

        xmargin 180
        ymargin 50
        xpadding 50
        ypadding 160

        vpgrid:

            cols 1.0
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:

                for h in _history_list:

                    window:
                        if (h.who != None) and (str(h.who) is not history_name_checker):
                            background Image("gui/historynamebox_lg.png", xalign=0, yalign=0)
                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True
                        if (h.who != None):
                            if str(h.who) is not history_name_checker:
                                label h.who:
                                    if "&" in h.who:
                                        style "history_manyname_text"
                                    else:
                                        style "history_name_text"
                                    substitute False

                                    ## Take the color of the who text from the Character, if
                                    ## set.
                                    if "color" in h.who_args:
                                        text_color h.who_args["color"]

                                $ history_name_checker = h.who
                        else:
                            $ history_name_checker = ""

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            if h.who == None:
                                xalign 0.8
                                line_spacing 5
                                substitute False
                                size 40
                            else:
                                xalign 1.15
                                line_spacing 5
                                substitute False
                                size 45
                    ## This puts some space between entries so it's easier to read
                    null height 20

                if not _history_list:

                    text "The text log is empty." line_spacing 10
                    ## Adding line_spacing prevents the bottom of the text
                    ## from getting cut off. Adjust when replacing the
                    ## default fonts.

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    font gui.name_text_font

style history_name_text:
    xpos 0
    ypos .05
    yanchor 1
    size 20
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_manyname_text:
    xpos 0
    ypos .05
    yanchor 1
    size 10
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    kerning 1.5
    font "TCS4GiveKhemThit.ttf"
    color gui.interface_text_color

style history_label:
    xfill True
    top_margin -100

style history_label_text:
    xalign 0.5
    ## Note: When altering the size of the label, you may need to increase the
    ## ypadding of the Frame, or separate it again into top_padding and bottom_padding

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    if "overwrite" in message:
        $ show_text = "Overwrite Save"
        $ show_message = "Do you want to overwrite a save? "
    elif "Loading" in message:
        $ show_text = "Load"
        $ show_message = "Loading will lose unsaved progress"
    elif message == "Are you sure you want to quit?":
        $ show_text = "Exit"
        $ show_message = message
    elif "main menu" in message:
        $ show_text = "Back to Title"
        $ show_message = "Return to main menu?"

    add "gui/overlay/confirm.png"
    add "gui/overlay/popup_box.png" align(0.5,0.5)

    frame:
        vbox:
            xalign 0.5
            spacing 45
            label _(show_text):
                style "confirm_prompt_text"
                xalign 0.5
            label _(show_message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 35

                imagebutton auto "gui/confirm/yes_%s.png" action yes_action
                imagebutton auto "gui/confirm/no_%s.png" action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_prompt:
    font "fonts/Mali-SemiBold.ttf"
    size 32
    bold True
    color '#320000'

style confirm_prompt_text:
    font "fonts/Mali-SemiBold.ttf"
    size 32
    spacing 2
    color '#750000'

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .475

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    if str(d.who) is not nvl_name_checker:
                        text d.who:
                            id d.who_id
                        $ nvl_name_checker = str(d.who)

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

screen tutorial(tutorial="cafe"):
    add "images/tutorial/[tutorial]_tutorial.png"
    imagebutton auto "images/tutorial/close_%s.png":
        focus_mask True
        action Return()

screen tutorial_popup(tutorial="cafe"):
    add "images/tutorial/[tutorial]_tutorial.png"
    imagebutton auto "images/tutorial/close_%s.png":
        focus_mask True
        action [Hide("tutorial_popup")]
