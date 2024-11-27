## Basic Settings #########################################################

## Human-readable game name.
define config.name = _("HONEY REVERSE")

## Game version for display and debugging purposes.
define config.version = "1.00"

## Short name used in builds (no spaces or special characters).
define build.name = "HoneyReverse"

## The directory for game save files.
define config.save_directory = "HoneyReverse"

## Enable or disable sound, music, and voice support.
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False

## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Between screens of the game menu.

define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.

define config.after_load_transition = None

## Used when entering the main menu after the game has ended.

define config.end_game_transition = None

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.

## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"

## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/honey_revense_logo.png"

## Main Menu ###################################################################

define config.main_menu_music = "audio/start_game.mp3"

## Mouse #######################################################################

define config.mouse = {}
define config.mouse['shooter'] = [(im.Scale("images/minigames/shooting/shooting_pointer.png", 80, 80), 0, 0)]

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Exclude temporary and backup files from the build process.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("**/__pycache__", None)
    build.classify("**/__pycache__/**", None)

    ## Exclude unnecessary development resources like layered image files.
    build.classify('**.psd', None)        # Photoshop files.
    build.classify('**.xcf', None)        # GIMP files.

    ## Exclude source control folders (e.g., `.git`, `.svn`).
    build.classify('**/.git/**', None)
    build.classify('**/.svn/**', None)

    ## Exclude documentation files from the build (optional).
    build.classify('**/*.md', None)       # Markdown files (e.g., README.md)
    build.classify('**/*.txt', None)      # Text files (e.g., notes.txt)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."

## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
