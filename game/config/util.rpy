default confirm_skip_text = "จะข้ามจริงๆหรอ?"
default show_initial_buttons = "text_1"  # To toggle between the initial buttons and the new button.

style confirm_prompt_thai:
    font "fonts/Mali-SemiBold.ttf"
    size 32
    color '#750000'

screen confirm_skip():
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    add "gui/overlay/popup_box.png" align(0.5, 0.5)

    frame:
        vbox:
            xalign 0.5
            spacing 45
            # Dynamically display the text from the variable
            label "Skip":
                style "confirm_prompt_text"
                xalign 0.5
            text confirm_skip_text:
                style "confirm_prompt_thai"
                xalign 0.5
            # Conditional button logic
            hbox:
                xalign 0.5
                spacing 35
                if show_initial_buttons == "text_1":
                    # Initial buttons: "ไม่" and "ใช่"
                    imagebutton auto "gui/confirm/thai_yes_%s.png":
                        if enable_skip:
                            action [Skip(), Return()]
                        else:
                            action [SetVariable("confirm_skip_text", "แต่งกันมาตั้งนานเลยนะ จะข้ามจริงหรอ?"), SetVariable("show_initial_buttons", "text_2")]
                    imagebutton auto "gui/confirm/thai_no_%s.png" action Return()
                elif show_initial_buttons == "text_2":
                    imagebutton auto "gui/confirm/thai_yes_%s.png":
                        if enable_skip:
                            action [Skip(), Return()]
                        else:
                            action [SetVariable("confirm_skip_text", "คนวาดก็ตัวจะแตกเลยนะ ไม่ดูหน่อยหรอ?"), SetVariable("show_initial_buttons", "text_3")]
                    imagebutton auto "gui/confirm/thai_no_%s.png" action Return()
                elif show_initial_buttons == "text_3":
                    imagebutton auto "gui/confirm/thai_yes_%s.png":
                        if enable_skip:
                            action [Skip(), Return()]
                        else:
                            action [SetVariable("confirm_skip_text", "คนทำเกมก็อดนอน จะไม่ดูอีกหรอ TT"), SetVariable("show_initial_buttons", "text_4")]
                    imagebutton auto "gui/confirm/thai_no_%s.png" action Return()
                elif show_initial_buttons == "text_4":
                    imagebutton auto "gui/confirm/thai_yes_%s.png":
                        if enable_skip:
                            action [Skip(), Return()]
                        else:
                            action [SetVariable("confirm_skip_text", "แค่ถามไปงั้นแหละ ไม่ให้หรอก! -3-"), SetVariable("show_initial_buttons", "text_5")]
                    imagebutton auto "gui/confirm/thai_no_%s.png" action Return()
                else:
                    imagebutton auto "gui/confirm/thai_hae_%s.png" action [SetVariable("show_skip_btn", False), Return()]

label confirm_pause():
    # Reset the confirmation text and buttons
    $ confirm_skip_text = "จะข้ามจริงๆหรอ?"
    $ show_initial_buttons = "text_1"
    # Pause the game flow and show the screen
    call screen confirm_skip
    return
