label end_credit:
    stop music
    stop sound
    $ quick_menu = False
    $ is_video_render = True
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    play movie "end_credit.webm"
    $ renpy.pause(132, hard=True)
    $ is_video_render = False
    $ quick_menu = True
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"

    $ persistent.gameclear = True
