################################################################################
## Initialization
################################################################################

# The init offset statement ensures that initialization in this file
# runs before the init statements in any other file.
init offset = -2

# Reset GUI styles to default and set the game resolution to 1920x1080.
init python:
    gui.init(1920, 1080)

################################################################################
## GUI Configuration Variables
################################################################################

## Colors ######################################################################
# Defines the color scheme for the user interface (UI) elements.

define gui.accent_color = '#201c1e'         # Accent color used for highlights.
define gui.idle_color = '#7a7676'           # Color for idle (not hovered) text buttons.
define gui.idle_small_color = '#623e08'     # Brighter color for smaller text.
define gui.hover_color = '#403737'          # Color for hovered buttons.
define gui.selected_color = '#000000'       # Color for selected text buttons.
define gui.insensitive_color = '#aaaaaa7f'  # Color for disabled buttons.

# Muted colors for bars and their hover states.
define gui.muted_color = '#e066a3'
define gui.hover_muted_color = '#ea99c1'

# Text colors used for dialogue and UI text.
define gui.text_color = '#0e0d0d'
define gui.interface_text_color = '#cab9bc'

## Fonts and Font Sizes ########################################################
# Font settings for different UI components.

define gui.name_text_outlines = [(2, "#000000", 0, 0)]      # Outline for name text.
define gui.text_font = "fonts/Mali-Bold.ttf"                  # In-game text font.
define gui.name_text_font = "fonts/Mali-SemiBold.ttf"         # Character name font.
define gui.interface_text_font = "fonts/Mali-SemiBold.ttf"    # UI font.

# Text sizes for dialogue, UI, and titles.
define gui.text_size = 30
define gui.name_text_size = 45
define gui.interface_text_size = 33
define gui.label_text_size = 36
define gui.notify_text_size = 24
define gui.title_text_size = 75

## Main and Game Menus #########################################################
# Images used for the main and game menus.

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## Dialogue ####################################################################
# Variables controlling the dialogue box's appearance and positioning.

define gui.textbox_height = 280             # Height of the textbox.
define gui.textbox_yalign = 0.98            # Vertical alignment of the textbox.

# Placement and alignment of the speaking character's name.
define gui.name_xpos = 520
define gui.name_ypos = 0
define gui.name_xalign = 0.5

# Size and borders of the name box.
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(0, 0, 0, 0)

define gui.namebox_tile = False             # Whether the namebox background is tiled.

# Placement and alignment of dialogue text inside the textbox.
define gui.dialogue_xpos = 300
define gui.dialogue_ypos = 90
define gui.dialogue_width = 1360
define gui.dialogue_text_xalign = 0.0

## Buttons #####################################################################
# Settings for button dimensions, borders, fonts, and colors.

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font  # Button font.
define gui.button_text_size = gui.interface_text_size  # Button text size.

# Button text colors for different states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# Text alignment within the button.
define gui.button_text_xalign = 0.0

# Custom borders for radio and check buttons.
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)

# Custom settings for the confirm button and page navigation buttons.
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)

# Quick buttons customization.
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Choice Buttons ##############################################################
# Settings for in-game choice buttons.

define gui.choice_button_width = 1200
define gui.choice_button_height = 96
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = 32
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_yalign = 0.5
define gui.choice_button_text_idle_color = "#5c5959"
define gui.choice_button_text_hover_color = "#1a1919"
define gui.choice_button_text_insensitive_color = "#444444"

## File Slot Buttons ###########################################################
# Settings for save/load file slot buttons.

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

# Thumbnail dimensions for save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

# Number of file slots in the grid.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Positioning and Spacing #####################################################
# Position and spacing for various UI elements.

define gui.navigation_xpos = 60             # Position of navigation buttons.
define gui.skip_ypos = 15                   # Vertical position of the skip indicator.
define gui.notify_ypos = 68                 # Vertical position of the notify screen.

define gui.choice_spacing = 33              # Spacing between menu choices.
define gui.navigation_spacing = 6           # Spacing between navigation buttons.

# Spacing for preference buttons.
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0

define gui.page_spacing = 0                 # Spacing between file page buttons.
define gui.slot_spacing = 15                # Spacing between file slots.

# Main menu text alignment.
define gui.main_menu_text_xalign = 1.0

## Frames ######################################################################
# Borders for frames used in the UI.

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False

# Whether frame backgrounds should be tiled.
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders ###############################################
# Control sizes and borders for bars, scrollbars, and sliders.

define gui.bar_size = 38                    # Height/width of bars.
define gui.scrollbar_size = 18              # Size of scrollbars.
define gui.slider_size = 38                 # Size of sliders.

define gui.bar_tile = False                 # Should bar images be tiled?
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)  # Horizontal borders for bars.
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

define gui.vbar_borders = Borders(6, 6, 6, 6)  # Vertical borders for bars.
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"

## History #####################################################################
# Settings for the dialogue history screen.

define config.history_length = 250          # Number of history blocks to keep.
define gui.history_height = 210             # Height of a history entry.
define gui.history_name_xpos = 233          # Position and alignment of character names.
define gui.history_name_ypos = 0
define gui.history_name_width = 180
define gui.history_name_xalign = 0

define gui.history_text_xpos = 255          # Position and alignment of dialogue text.
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

## NVL-Mode ####################################################################
# Settings for NVL-mode (visual novel format) dialogue.

define gui.nvl_borders = Borders(0, 240, 0, 0)
define gui.nvl_list_length = 12             # Max number of NVL-mode entries.
define gui.nvl_height = None                # Height of NVL-mode entry.
define gui.nvl_spacing = 15                 # Spacing between NVL-mode entries.

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"

################################################################################
## Mobile devices
################################################################################

init python:
    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():
        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51
        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650
        ## Change the size and spacing of various things.
        gui.slider_size = 54
        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        gui.history_height = 285
        gui.history_text_width = 1035
        gui.quick_button_text_size = 30
        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        ## NVL-mode.
        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
