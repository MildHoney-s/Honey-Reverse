default confirm_skip_text = "ต้องการกดข้ามจริงๆหรอ?"
default show_initial_buttons = True  # To toggle between the initial buttons and the new button.

screen confirm_skip():
    add "gui/overlay/confirm.png"
    add "gui/overlay/popup_box.png" align(0.5, 0.5)
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        ysize 200
        vbox:
            # Dynamically display the text from the variable
            text confirm_skip_text xalign 0.5 yalign 0.4 ypos 75
            # Conditional button logic
            if show_initial_buttons:
                # Initial buttons: "ไม่" and "ใช่"
                hbox:
                    spacing 200  # Space between buttons
                    xalign 0.5
                    ypos 70
                    textbutton "ใช่":
                        if enable_skip:
                            action [Skip(), Return()]
                        else:
                            action [SetVariable("confirm_skip_text", "Skip is disabled")]
                    textbutton "ไม่" action Return()
            else:
                # Centered button when "ใช่" is clicked
                textbutton "แฮร่~" action Return() xalign 0.5 ypos 70

label confirm_pause():
    # Reset the confirmation text and buttons
    $ confirm_skip_text = "ต้องการกดข้ามจริงๆหรอ?"
    $ show_initial_buttons = True
    # Pause the game flow and show the screen
    call screen confirm_skip
    return
