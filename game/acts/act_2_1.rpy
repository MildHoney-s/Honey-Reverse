label act2_1_shot_1:
    scene bg2day
    with fade
    stop music fadeout 1.5
    "ไม่รู้ทำไมเหมือนกันแต่เวลาที่ได้อยู่ด้วยกันกับมายด์ ผ่านไปเร็วมากเลยล่ะ รู้ตัวอีกทีก็ผ่านไป 1 เดือนซะแล้ว"
    scene bg2day
    show curtain:
        alpha 0.25
    show mild maid_smile10 at middleposmild
    with fade
    pov "นะ นั่นมายด์หรอ"
    show mild maid_smile10 at farmild
    with dissolve
    show del normal_police at rightposdel
    show tsuru normal_grumpy1 at leftpostsuru
    with zoomin
    play music nightmare_bgm loop fadein 0.5 fadeout 1.0
    debirun "เอาเงินมาให้เราซะดีๆ ผู้จัดการรร หึหึ"
    show mild maid_smile10 at farfarmild
    with dissolve
    show del normal_police at closerightposdel
    show tsuru normal_grumpy2 at closeleftpostsuru
    with zoomin
    pov "เอิ่ม... พวกเธอมาจากไหนกัน?"
    tsuru "ไม่ลืมเงินของพวกเราใช่ไหม คุณผู้จัดการ"
    pov "ด-เดี๋ยวสิ!? อ๊ากก!"
    scene black with eye_shut

    jump act2_1_shot_2

label act2_1_shot_2:
    stop music fadeout 1.0
    play sound nightmare_sfx
    pov "เฮือกกกกก-!!"
    scene bg7day with eye_open
    "หลังจากที่ตื่นจากฝันอันแปลกประหลาด เราได้พบว่าตัวเองอยู่ที่พื้นข้างๆ เตียง"
    play music morning_bgm loop fadein 0.5 fadeout 1.0 volume 0.5
    pov "ฝันร้ายอะไรกันนี่..."
    pov "ทำไม... ฉันต้องฝันว่าเจอสองคนนั้นไถเงินด้วยล่ะเนี่ย อุส่าได้เจอมายด์ในฝันแท้ ๆ เชียว"
    pov "แปปนะไถเงินหรอ วันนี้วันเสาร์... วันที่ต้องจ่ายเงินเดือนนี่น่า"
    pov "เจองี้ไปนอนไม่หลับแล้ว เดี๋ยวจะต้องไปอ่านกล่องรับความคิดเห็นอีก แถมทั้งซึรุกับเดลก็จะมารับเงินเดือนด้วย"
    pov "ว่าแต่ตอนนี้มายด์ตื่นหรือยังนะ..."

    jump act2_1_shot_3

label act2_1_shot_3:
    scene bg5day with wiperight
    "หลังจาก [pov] ได้ลุกขึ้นมาจากข้างเตียงของเขา ก็ได้ไปยังห้องนอนของมายด์เพื่อที่จะปลุกมายด์"
    play sound walking_sfx
    pov "(มายด์เขามักจะตื่นสายเสมอเลยถ้าไม่มีใครไปปลุก)"
    pov "(ปกติเดลหรือซึรุจะเป็นคนมาปลุกมายด์ แต่วันนี้ฉันน่าจะเป็นคนไปปลุกแทนเพราะสะดุ้งตื่นจากสองคนนั้นเนี่ย)"
    pov "(แปลกจังเลยนะปกติวันหยุด เดลกับซึรุจะมาเล่นกับมายด์หนิ ทำไมยังไม่มากันอีก)"
    show bg22:
        zoom 1.5
        xalign 0.5
        yalign 0.6
    with dissolve
    pov "(วันนี้สงสัยทั้งคู่ติดธุระกันอยู่)"
    play sound knock_sfx fadein 0.25
    pov "มายด์ตื่นหรือยัง"
    play sound opendoor_sfx fadein 0.25
    scene bg6day
    show mild pajamas_sleep at mild_zoom
    with dissolve
    "หลังจากผ่านไปสักครู่ ประตูก็ได้เปิดออกมา"
    show mild pajamas_flustered1 at mild_zoom,bounce
    mild "*กรี้ด* อ๊าา-!! เดี๋ยว-!!"
    play sound doorclose_sfx fadein 0.25
    show bg5day with hpunch
    pov "อะ ขอโทษนะมายด์-! เอิ่ม... มาปลุกให้ไปกินข้าวน่ะ "
    play sound walking_sfx
    pov "เดี๋ยวฉันลงไปทำข้าวเช้ารอนะ ถ้าแต่งตัวเสร็จแล้วลงมาทานด้วยนะ"
    stop sound

    jump act2_1_shot_4

label act2_1_shot_4:
    scene bg8day
    with fade
    play music rest_bgm loop fadein 0.75 fadeout 1.0
    "หลังจากผ่านไปสักพักหนึ่ง มายด์ก็ได้เดินตามมาที่ครัว"
    show mild pajamas_idle2 at leftposmild
    with easeinleft
    pov "มายด์มาแล้วหรอ จะว่าไปเมื่อกี้ยังไม่ได้ถามเลยว่าจะกินอะไร"
    menu:
        "ออมไรซ์":
            pass

        "ข้าวกะเพราไก่ไข่ดาว":
            pass

        "สปาเก็ตตี้หมูกรอบซอสครีมชีส":
            pass

        "หรือว่า [povname] ดีล่ะ":
            $ honey_score -= 1

    show mild pajamas_smile6 at leftposmild
    with dissolve
    mild "ชานม-!!"
    pov "ไม่ได้สิมายด์ ตอนเช้ามันต้องกินข้าวสิ"
    show mild pajamas_grumpy at leftposmild
    show emotion_worried at emotepairpos1
    with dissolve
    mild "ม่ายอาววว จะกินชานม จะกินชานม ชานม ชานม-!"
    pov "ถ้าจะกินชานมก็หลังจากกินข้าวก่อนนะ ฉันจะให้กิน 1 แก้ว"
    pov "แต่ถ้ามายด์ยังตื่นสายบ่อยๆ แบบนี้ คงต้องอดชานมสักวันแล้วล่ะ..."
    hide emotion_worried
    show mild pajamas_sorry at paja
    with dissolve
    mild "การที่ไม่ให้ชานม ก็เหมือนกับบอกว่าไม่รักมายด์นั่นแหละ"
    pov "ได้ๆ ฉันจะไม่ห้ามเธอกินชานมแล้ว"
    pov "(อ่า... งั้นเปลี่ยนเป็นให้ชานมแค่ครึ่งแก้วแล้วกัน)"

    jump act2_1_shot_5

label act2_1_shot_5:
    scene bg8day
    "และหลังจากนั้น ฉันก็ได้ทำมื้อเช้าให้ทั้งตัวเองและก็มายด์"
    show spa at truecenter:
        zoom 0.7
    "ซึ่งมายด์บอกว่าอยากจะกินสปาเก็ตตี้หมูกรอบซอสครีมชีส"
    show spa at rightposmild
    show mild pajamas_idle3 at leftposmild
    with dissolve
    mild "หอมจังเลยค่ะ"
    pov "แน่นอนอยู่แล้ว~ ถ้าทำให้เธอทานฉันก็ตั้งใจทำด้วยความรักทุกจานอยู่แล้ว"
    hide spa
    show mild pajamas_flustered1 at paja
    with dissolve
    mild "คะ คะ?"
    window hide
    show mild pajamas_flustered1 at bounce,mild_zoom
    pause 1.5
    scene black with fade
    pause 0.5
    stop music fadeout 2.5
    centered "{=centered_text}และทั้งคู่ก็กินข้าวอย่างเป็นสุขชั่วนิรันดร์{/centered_text}"
    centered "{=centered_text}อวสาน{/centered_text}"
    centered "{=centered_text}thank you for plaping{/centered_text}"
    stop music
    stop sound
    $ quick_menu = False
    $ is_video_render = True
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    play movie "meme.webm"
    $ renpy.pause(25, hard=True)
    $ is_video_render = False
    $ quick_menu = True
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"

    jump act2_1_shot_6

label act2_1_shot_6:
    scene black
    centered "{=centered_text}และซึรุกับเดลก็เดินเข้าร้านมา{/centered_text}"
    with dissolve
    pause 1.0
    play sound door_sfx volume 0.5
    scene bg2day
    play music bright_bgm loop fadein 0.5 fadeout 1.0
    show mild pajamas_flustered1 at lsposmild
    with dissolve
    show tsuru normal_smug at middlepostsuru
    show del normal_idle2 at rightposdel
    with easeinright
    tsuru "สวัสดีค่ะผู้จัดการ อ่ะ ทั้งคู่ทำอะไรกันน่ะ ทำไมมายด์หน้าแดงล่ะ"
    show del normal_police at rightposdel
    with dissolve
    debirun "สวัสดีค่ะคุณผู้จัดการ ทำอะไรกับพี่มายด์น่ะ-!! ปี้ป่อปี้ป่อ-!!"
    pov "อะไรกันนี่ทั้งคู่เลย เราพึ่งกินข้าวเช้ากันเนี่ย"
    pov "จะว่าไป ปกติพวกเธอมาเช้ากว่านี้นะ ทำไมวันนี้มาช้าจัง"
    scene bg2day:
        crop (800,200,1980,720)
        size (1920, 1080)
    show del normal_sorry at del_close
    with dissolve
    debirun "รถเสียค่ะผู้จัดการ แล้วกว่าจะลากไปถึงอู่ซ่อมได้ใช้เวลานานมากเลย"
    pov "เดี๋ยวนะเดล รถเป็นอะไรมากมั้ยน่ะ"
    show del normal_crying1 at del_close
    with dissolve
    debirun "รถสตาร์ทไม่ติด-"
    pov "เนี่ยไม่ใช้น้ำมันได*** ใช้แล้วเครื่องฟิตสตาร์ทติดง่าย-"
    show del normal_abuse2 at del_close
    show emotion_question at emoteclose
    debirun "เอิ่ม... ก็แบบว่า หนูรู้จักแต่โตเกียวนะ อร่อยด้วย ได*** คืออะไรหรอ..."
    pov "..."
    scene bg2day:
        crop (400,200,1780,720)
        size (1920, 1080)
    show tsuru normal_stunned at tsuru_close
    with dissolve
    show loading at loading
    pov "งั้นซึรุล่ะ"
    tsuru "อ๋อ..."
    pov "ซึรุ... ซึรุ-!!"
    hide loading
    show tsuru normal_idle2_2 at bounce,tsuru_close
    tsuru "อ๋อ-!! หนูตื่นสายค่ะ..."
    pov "(โอเคพอจะเดาออกแล้วล่ะ...)"

    jump act2_1_shot_7

label act2_1_shot_7:
    scene bg2day
    show mild pajamas_idle1 at lsposmild
    show tsuru normal_idle1_1 at middlepostsuru
    show del normal_idle1 at rightposdel
    with dissolve
    pov "โอเค ในเมื่อมากันครบแล้วมาคุยกันเรื่องจ่ายเงินเดือนกันไหม"
    "จากนั้น [pov] ได้ยื่นซองให้กับแต่ละคน"
    pov "นี่เงินเดือนของแต่ละคนในเดือนนี้ สำหรับมายด์เป็นเงินเดือนแรกด้วย ใช้จ่ายให้เหมาะสมล่ะ"
    show del normal_idle2 at rightposdel
    with dissolve
    debirun "ผู้จัดการยังให้เงินเดือนแบบนี้อยู่อีกหรอ สมัยนี้เขาเปลี่ยนไปใช้ระบบโมบายแบงค์กิ้งในแอพมือถือกันหมดแล้วนะ"
    pov "หรือเธอจะไม่เอา..."
    show del normal_stunned2 at rightposdel
    with dissolve
    debirun "ไม่ได้นะผู้จัดการ-!! เอาค่ะๆ นี่มันเงินจากการทำงานของหนูเชียวนะ"

    jump act2_1_shot_8

label act2_1_shot_8:
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild pajamas_smile2 at paja
    with dissolve
    mild "//เปิดซองดู แล้วเห็นเงินธนบัตรอยู่ภายใน"
    show mild pajamas_doubt at paja
    with dissolve
    mild "เอ๋ นี่คืออะไรหรอค่ะ [povname]"
    pov "สิ่งนี้เรียกว่าเงินนะมายด์"
    pov "(การจ่ายเงินค่าอาหาร น้ำ และการบริการของร้านคาเฟ่นี้จะให้จ่ายผ่านทางเคาน์เตอร์อย่างเดียว)"
    pov "(เงินจึงไม่ได้ผ่านมือของสาวๆ โดยตรงเท่าไหร่นอกจากช่วงที่จ่ายเงินเดือน)"
    pov "(นี่เป็นครั้งแรกที่มายด์ได้เห็นและรู้จักสิ่งที่เรียกว่า “เงินตรา” เป็นครั้งแรก)"
    scene bg2day
    show mild pajamas_idle2 at lsposmild
    show tsuru normal_idle2_1 at middlepostsuru
    show del normal_gloomy1 at rightposdel
    with dissolve
    debirun "//ทำหน้าจ๋อย"
    show tsuru normal_doubt at middlepostsuru
    with dissolve
    tsuru "เดลเป็นอะไรไปน่ะ"
    show del normal_crying2 at rightposdel
    with dissolve
    debirun "คือ งบเติมกาชาหนูหมดไปแล้วกับค่าซ่อมรถน่ะค่ะ... แล้ว แล้ว... กาชาที่หนูว่าจะเปิดมันจะหมดแล้ว แง"
    mild "//ยื่นซองให้เดล"
    show mild pajamas_smile4 at lsposmild
    with dissolve
    mild "อ่ะเดลอันนี้ฉันให้"
    show del normal_smile5 at rightposdel
    with dissolve
    pov "มายด์ อันนี้เงินส่วนของมายด์นะจะดีหรอ"
    show mild pajamas_smile8 at lsposmild
    with dissolve
    mild "ไม่เป็นไรค่ะ ยังไงฉันก็ไม่ได้ใช้อะไรอยู่แล้ว เป็นคำขอบคุณด้วยตลอดเวลาที่ผ่านมา"
    show del normal_smile3 at rightposdel
    with dissolve
    debirun "ขะ ขอบคุณนะ พี่มายด์"
    show tsuru normal_grumpy2 at middlepostsuru
    tsuru_pov "แย่ล่ะ-"
    show del normal_smile3 at leftposdel
    with easeinright
    pause 0.1
    hide del normal_smile3
    with moveoutright
    show mild pajamas_stunned at lsposmild
    with dissolve
    play sound door_sfx volume 0.5
    "แล้วเดลก็หยิบซองน้ำตาลของมายด์ด้วยความเร็วสูง แล้ววิ่งออกจากร้านไป"
    show tsuru normal_sorry at middlepostsuru
    with dissolve
    tsuru_pov "อ่า ไม่ทันแล้ว"
    mild "อ่ะ เดล... เดลหายไปแล้ว"
    play sound door_sfx volume 0.5
    show del normal_smile6 at rightposdel
    with easeinright
    debirun "เย่ๆ-!! ได้เปิดกาชาแล้ว-!! กดเลย-!!"
    scene black
    centered "{=centered_text}เดลได้กดกาชาที่ตัวเองอยากได้หลังจากนั้น...{/centered_text}"
    centered "{=centered_text}เดลได้ถอนหายใจออกมายาวๆ พร้อมกับส่ายหัวไปชุดนึง{/centered_text}"
    scene bg2day
    pov "เฮ่อ... (สม...)"
    show mild pajamas_idle1 at lsposmild
    show tsuru normal_idle1_2 at middlepostsuru
    show del normal_crying1 at rightposdel
    with dissolve
    tsuru "มายด์... ลองกดดูสิ ถ้ากดแล้วออกหน้าตู้มา เดลอาจจะกลับมาเป็นเหมือนเดิมก็ได้นะ"
    mild "ค่ะ..."
    scene bg2day
    window hide
    $ _game_menu_screen = None
    $ is_video_render = True
    show gacha_movie
    stop music fadeout 0.5
    show phone at truecenter:
        zoom 3.2
    $ quick_menu = False
    $ renpy.pause(39, hard=True)
    $ is_video_render = False
    $ _game_menu_screen = "save"
    $ quick_menu = True
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    play music bright_bgm loop fadein 0.5 fadeout 1.0
    show tsuru normal_smile3 at tsuru_close
    with dissolve
    tsuru "เดลดูนี่สิ ดูนี่สิ ได้หน้าตู้ล่ะ"
    hide tsuru normal_smile3
    show del normal_crying1 at del_close
    with fade
    pause 1.5
    show del normal_idle1 at del_close
    with dissolve
    pause 1.5
    show del normal_smile6 at bounce,del_close
    with dissolve
    pause 1.5
    scene bg2day:
        crop (400,200,1780,720)
        size (1920, 1080)
    show mild pajamas_smile5 at paja
    with dissolve
    pov "มายด์ เราเอาเงินตรงนั้นมาซื้อชานมได้นะ..."
    show mild pajamas_flustered1 at paja
    mild "อ่ะ จริงด้วยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยย-!!"
    "และนี่ก็เป็นครั้งแรกที่มายด์ได้รับบทเรียนเกี่ยวกับการใช้เงิน"

    jump act2_1_shot_9

label act2_1_shot_9:
    scene black with eye_shut
    play music maid_bgm loop fadein 0.75 fadeout 1.0
    centered "{=centered_text}หลังจากเรื่องวุ่น ๆ จบลง เราก็นำกล่องความคิดเห็นมาเปิดอ่าน{/centered_text}"
    scene bg2day
    pov "แต่ละคนได้รับความเห็นเป็นยังไงบ้างนะ"
    show tsuru normal_idle2_1 at tsuru_close
    tsuru "งั้นเริ่มที่หนูนะ ...เอ๊ะ ?"
    show tsuru normal_smile1 at tsuru_close
    with dissolve
    tsuru "มีแต่คนชมหนูทั้งนั้นเลยหนิน่า ผู้จัดการ"
    pov "ชมว่ายังไงบ้างหรอ ไหนๆ"
    show tsuru normal_smile2 at tsuru_close
    with dissolve
    tsuru "“ระหว่างอยู่ในร้าน ซึรุหลับในเวลาตอนที่มารับเมนูบ้าง ตอนที่นั่งพักอยู่บ้าง แม้แต่ตอนที่ยืนรออาหารเพื่อมาเสิร์ฟอยู่”"
    tsuru "และนี่อีกคำชมนึง"
    show tsuru normal_smile3 at bounce,tsuru_close
    tsuru "“ฉันกำลังจะออกจากร้าน ฉันเห็นซึรุคุยกับกบด้วยเสียงแบบกบ อย่างเหมือนเลย”"
    show tsuru normal_smile6 at tsuru_close
    pov "นั่นไม่น่าใช่คำชมนะซึรุ..."
    pov "งั้นทางฝั่งเดล ได้คำติชมยังไงบ้างหรอ"
    scene bg2day
    show del normal_smile2 at del_close
    with dissolve
    debirun "ส่วนฝั่งหนูก็ “คุยเรื่องเกมกับอนิเมะได้สนุกมาก โดยเฉพาะเกมกาชา”"
    pov "เดี๋ยวนะ..."
    show del normal_smile9 at del_close
    with dissolve
    debirun "ยังมีอีกนะผู้จัดการ “ท่านผบ.ช่างปรีชาสามารถแสดงกิริยาอาการแสน... บลา บลา บลา”"
    show del normal_smile3 at del_close
    with dissolve
    pov "(เราไม่เข้าใจเลยว่าเดลกำลังพูดถึงอะไรอยู่ เหมือนดูอนิเมะมากเกินไป เดี๋ยวนะ เมื่อกี้ได้ยินคำว่า “ข้านั้นเก่งที่สุดในจักรวาล ฮะฮาฮ่า-!” ใช่มั้ยนะ ?)"
    pov "อะ โอเค...ดีมากเลยเดล (สมกับเป็นเดลจริงๆ ...) // กุมขมับ"

    jump act2_1_shot_10

label act2_1_shot_10:
    scene bg2day
    show  mild pajamas_idle2 at paja
    with dissolve
    pov "ถ้างั้นมายด์ล่ะ มีคำติชมพูดถึงมายด์ว่ายังไงบ้าง"
    show  mild pajamas_idle3 at paja
    with dissolve
    mild "คะ ค่ะ ฉันได้มาเป็น “มายด์น่ารัก น่ารักมาก น่ารักที่สุด” ค่ะ [povname]"
    pov "(ดะ เดี๋ยว... นั่นที่ฉันเขียนเล่นๆ หนิ นึกว่าทิ้งไปแล้วซะอีก ใครเอาไปใส่ในนั้นล่ะเนี่ย)"
    show  mild pajamas_smile5 at paja
    with dissolve
    pov "ละ แล้วมีคำติชมอื่นอีกหรือเปล่านะ"
    show mild pajamas_doubt at paja
    with dissolve
    mild "มีค่ะ มีค่ะ เขาว่า “ตอนนี้ยังดูเขินๆ อยู่เลย อยากให้มายด์แสดงให้สมบทบาทมากขึ้นกว่านี้จัง มันไม่เข้ากับบทบาทเลย”"
    pov "..."
    show mild pajamas_sorry at paja
    with dissolve
    pov "...จะว่าไป มายด์ก็ยังไม่มีบทบาทประจำตัวเลยนะ"
    scene bg2day
    with dissolve
    show tsuru normal_smile2 at leftpostsuru
    with easeinleft
    tsuru "งั้นตอนนี้แหละผู้จัดการ เราหาบทให้มายด์เลยสิ"
    pov "ความคิดดีนะซึรุ"
    show del normal_smile2 at rightposdel
    with easeinright
    debirun "อื้มๆ ใช่-!!"

    jump act2_1_shot_11

label act2_1_shot_11:
    style cafe_text:
        color "#814412"
    style down_text:
        color "#d04f40"
    scene bg2day
    play music role_bgm loop fadein 0.75 fadeout 1.0
    show  mild pajamas_smile8 at paja
    with dissolve
    mild "งะ งั้นเริ่มเลยนะ"
    hide mild pajamas_smile8
    with fade
    centered "{=cafe_text}- บทบาทซึนเดเระ -{/cafe_text}"
    show mild pajamas_tsundere at paja
    mild "ยะ อยู่รึเปล่า ชั้นมาหาแล้วนะ ขอบใจชั้นด้วยล่ะ หึ! ฉันมะ ไม่ได้ตั้งใจทําให้นายหรอกนะ! เชอะ!!!"
    pov "เหมือนมายด์กำลังโมโหอยู่เลย..."
    show del normal_idle1 at leftclosedel
    show tsuru normal_idle1 at rightclosetsuru
    tsuru "แหะๆ นั่นสินะคะ"
    debirun "ใช่เลยผู้จัดการ"
    scene bg2day
    with fade
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}- บทบาทยันเดเระ -{/cafe_text}"
    show mild pajamas_angry1 at paja
    mild "ถ้าคิดจะไปกินของคนอื่นล่ะก็.... จะไม่มีเค้ากับเธอ... มีแต่ฉันกับแก..."
    show mild pajamas_angry2 at paja
    with dissolve
    mild "เดี๋ยวนะ... กลิ่นนี้ไม่คุ้นเลย แกไปหาคนอื่นมาใช่ไหม-!!"
    show del normal_idle2 at leftclosedel
    show tsuru normal_idle1_1 at rightclosetsuru
    pov_tsuru_debirun "คะ ครับ / ค-ค่ะ"
    scene bg2day
    with fade
    centered "{=down_text}บทนี้น่ากลัวเกิน{/down_text} "
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}- บทบาทคูลเดเระ -{/cafe_text}"
    show mild pajamas_cooldere at paja
    mild "อาหารของคุณที่สั่ง กินให้อร่อยนะ..."
    play sound "<from 0.2 to 10.5>SFX/silentwind_sfx.mp3" fadein 0.5
    pov_tsuru_debirun "..."
    scene bg2day
    with fade
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}- บทบาทพี่มินอาร์ -{/cafe_text}"
    show mild pajamas_smile2 at paja
    mild "แหมมม อยากให้คนอื่นมารับเมนูอย่างงั้นหรอ... ทำไมต้องอยากได้คนอื่นล่ะ ในเมื่อมีฉันอยู่ทั้งคนแล้วหนิ"
    show mild pajamas_smile1 at paja:
        xpos 450
        zoom 1.35
    with zoomout
    play sound ear_sfx fadein 0.25
    mild "ฟู่วว.."
    show mild pajamas_smile5 at paja:
        xpos 450
        zoom 1.35
    with dissolve
    pov "*เฮือก-!!*"
    pov "ซึรุกับเดลเป็นอะไรไปหรอ?"
    show del normal_crying1 at leftclosedel
    show tsuru normal_crying at rightclosetsuru
    hide mild pajamas_smile5
    with dissolve
    tsuru_debirun "เอาพี่มายด์ของหนูคืนมา-!!"
    scene bg2day
    with fade
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}- บทบาทพี่สมหมาย -{/cafe_text}"
    show som at truecenter
    mild "คุณลูกค้าอยากจะรับอะไรดี หรือว่า จะรับตัวผมสักคำไหมครับ"
    pov "บทนี้เข้มดีนะ"
    show del normal_doubt1 at leftclosedel
    show tsuru normal_doubt at rightclosetsuru
    tsuru "อื้ม"
    debirun "อื้ม"
    scene bg2day
    with fade
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}- บทบาทมายบิรุน -{/cafe_text}"
    show mild pajamas_biao at paja
    with eye_open
    pause 1.0
    nvl clear
    show white_transparent
    play music byou_bgm fadein 0.25 loop
    mild_nvl "ผู้บัญชาการสูงสุดแห่งกองทัพลับฮันนี่โอลอย"
    mild_nvl "มายด์บิลอสอาลาเชียไดโนเสาร์พารามิเตอร์"
    mild_nvl "ผู้ถือครองวัตถุโบราณสตาร์ดัสไลค์แอนด์ดาร์คเนสออฟเดอะโพคาลิป"
    mild_nvl "ผู้นำทางชานมไร้ที่สิ้นสุดรัชทายาทแห่งจักรวรรดิบางโพธิ์ที่ล่มสลาย"
    mild_nvl "อควาเรี่ยมผู้ถูกเลือกจากบุตรแห่งดวงตาทมิฬโลหิตมะงื้อ"
    mild_nvl "ผู้นำทางหายนะอันยิ่งใหญ่จากจักรวาลมาสู่โลกาและมวลมนุษยชาติ"
    mild_nvl "มายด์-บิ-รุน รุน รุน รุน-!!"
    hide white_transparent
    tsuru_pov "..."
    scene bg2day
    show del normal_smile3 at del_close
    with dissolve
    debirun "ว้าววว สุดยอดเลยยย-!! ไม่น่าเชื่อเลยว่าพี่มายด์จะสามารถแสดงบทบาทได้เหมือนหนูขนาดนี้"
    debirun "แต่น่าเสียดายนะ ในที่แห่งนี้ มีผู้บัญชาการสูงสุดได้เพียงแค่คนเดียว-!!"
    show del normal_smile9 at del_close
    with dissolve
    debirun "งั้นมาดวลกัน"
    nvl clear
    show blue_transparent
    del_nvl "ข้าในนามผู้บัญชาการสูงสุดกองทัพลับเมเทโอรอยด์"
    del_nvl "เดบีรอส อลาเซีย ไดซีนิส เดอ โพลาดิโน่"
    del_nvl "ผู้ถือครองเอสเมอรันสตาร์ดัส"
    del_nvl "ไลท์ แอนด์ ดาร์กเนส ออฟ อโพคาลิป"
    del_nvl "ผู้นำทางดวงดาวอันไร้ที่สิ้นสุด"
    del_nvl "ทายาทแห่งจักวรรดิสงครามที่ล่มสลายคาริทัส"
    del_nvl "ผู้ถูกเลือกจากบุตรแห่งมังกรทมิลฬโลหิตเฮเดลอส"
    del_nvl "ผู้นำพาหายนะอันแสนยิ่งใหญ่จากจักรวาลมาสู่โลกาและมวลมนุษยชาติ"
    del_nvl "เด-บิ-รุน-!!"
    show dual_sd at truecenter:
        zoom 0.4
    mild_debirun "ดูเอล-!!"
    tsuru_pov "หยุด-!!"
    scene bg2day
    with fade
    stop music fadeout 1.5
    centered "{=down_text}XXX ปัดตก XXX{/down_text} "
    centered "{=cafe_text}และทุกคนก็ลงความคิดเห็นได้ว่า... มายด์เป็นเหมือนเดิมแหละดีแล้ว{/cafe_text}"

    jump act2_1_shot_12

label act2_1_shot_12:
    play music cafe_bgm loop fadein 1.5
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    with fade
    show mild pajamas_idle1 at lsposmild
    show tsuru normal_idle1_2 at middlepostsuru
    show del normal_smile1 at rightposdel
    pov "จะว่าไปแล้ว"
    pov "มายด์... ลองขึ้นสเตจดูมั้ย"
    show mild pajamas_shock at lsposmild
    with sshake
    show tsuru normal_doubt at middlepostsuru
    show del normal_idle2 at rightposdel
    with dissolve
    tsuru "พี่ผู้จัดการ จะให้มาย เขาลองขึ้นสเตจหรอ"
    show emotion_shock at emotepairpos2
    debirun "ผะ ผู้จัดการ ดูพี่มายด์สิ ตอนนี้ยืนตัวแข็งไปแล้ว-!!"
    show del normal_idle2 at middleposdel
    show tsuru normal_doubt at rightpostsuru
    hide emotion_shock
    with easeinleft
    debirun "พี่มายด์ ทำใจดีๆ ไว้ พี่มายด์-!! พี่ซึรุทำอะไรสักอย่างทีสิ"
    show tsuru normal_dark at rightpostsuru
    with dissolve
    tsuru "มายด์ขึ้นสเตจหรอ... อะฮุฮิฮุฮิ น่าสนใจดีหนิน่า พี่มายด์ขึ้นสเตจ"
    scene bg2day
    show mild_please_sd at truecenter:
        zoom 0.7
    mild "ฉะ ฉันขอดูอีกสักพักได้ไหมคะ [povname]"
    mild "ฉันไม่แน่ใจว่าจะทำได้น่ะค่ะ..."
    mild "น้าาาาาาาาาาา"
    hide mild_please_sd
    with fade
    show tsuru normal_doubt at middlepostsuru
    tsuru "มายด์... พี่ผู้จัดการ ลองพูดอะไรหน่อยสิ"
    pov "ดะ เดี๋ยว ทำไมเป็นฉันล่ะ"
    show tsuru normal_smile4 at middlepostsuru
    with dissolve
    tsuru "เพราะ พี่เป็นผู้จัดการไง หนูเชื่อว่าพี่ต้องทำอะไรได้แน่นอน"
    pov "(ยัยนี่นี่นะ... เอาโรลในร้านมาใช้เลยหรอ...)"
    show mild pajamas_grumpy at paja
    with dissolve
    pov "อะแฮ่ม... (ไม่ลองก็ไม่รู้ล่ะนะ)"
    menu:
        "ลองพูดถึงซึรุและเดล":
            pov "มายด์ คือว่า ซึรุกับเดลเขาได้ขึ้นสเตจแล้วนะ มายด์ไม่สนใจขึ้นบ้างสักหน่อยหรอ"
            window hide
            show mild_please_sd
            pause 2.0
            menu:
                "อาวุธลับ":
                    jump act2_1_shot_13

        "อาวุธลับ":
            jump act2_1_shot_13

label act2_1_shot_13:
    pov "(ช่วยไม่ได้ คงต้องใช้วิธีนั้นแล้วสินะ)"
    pov "มายด์... ถ้ามายด์ได้ขึ้นสเตจ จะให้ชานมเพิ่มขึ้นอีกวันละแก้วเลยนะ"
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild pajamas_doubt at paja
    mild "..."
    mild "{size=*0.5}เดือนนึง... //พูดด้วยเสียงเบาๆ{/size}"
    pov "อะ อะไรนะมายด์"
    show mild pajamas_grumpy at bounce,paja
    with dissolve
    mild "ฉันขอชานมเพิ่มขึ้นเดือนนึงเต็มๆ เลยยยยย-!!"
    pov "ดะ เดี๋ยว... ไม่ได้ ฉันให้ได้แค่สัปดาห์เดียวเท่านั้น มากกว่านั้นมันจ-"
    show mild pajamas_sorry at leftposmild
    with zoomout
    pause 1.5
    pov "งะ งั้น 2 สัปดาห์"
    show mild pajamas_sorry at left:
        zoom 0.3
    with zoomout
    pause 1.5
    show del normal_gloomy2 at rightposdel
    with easeinright
    debirun "ดูแล้ว... ผู้จัดการต้องยอมแล้วแหละ"
    pov "เห้อ... โอเค มายด์ งั้นถ้ามายด์ขึ้นสเตจ จะให้ชานมเพิ่มขึ้นวันละแก้วเดือนนึงเลย"
    hide del normal_gloomy2
    with None
    show mild pajamas_smile6 at bounce,paja
    with zoomin
    mild "เย้-!!"
    stop music fadeout 1.5
    pov "(ฉันคงใช้วิธีนี้บ่อยๆ ไม่ได้ ไม่งั้นรายได้ฉันหายแน่นอน)"
    scene bg7light
    play music diary_bgm loop fadein 1.5
    with fade
    show diary
    show brown_transparent
    nvl clear
    diary "ถึงไดอารี่ ในวันนี้เป็นวันเงินเดือนออกของพนักงานก็จริง แต่ไม่วายจะให้เกิดเรื่องวุ่นวายจนได้"
    diary "ทั้งเงินเดือนของมายด์ที่ได้กลายเป็นค่ากาชาของเดลไป"
    diary "มายด์น่าจะเข้าใจถึงเรื่องเงินไปอีกนานเลยล่ะ"
    diary "ทั้งเรื่องในกล่องความคิดเห็นอีก ใครกันนะ ที่มาว่ามายด์แสดงได้ไม่ดีพอ"
    diary "แต่เพราะอย่างนั้น เราก็เลยได้เห็นมายด์ในหลายๆ ลุคเลย"
    diary "รวมไปถึงเราจะได้เห็นมายด์ขึ้นสเตจแล้ว ฉันดีใจมากเลย"
    diary "ถึงแม้ว่า... ฉันจะต้องสังเวยชานมสำหรับหนึ่งเดือนไป"
    diary "มันต้องคุ้มแน่ๆ กับการที่มายด์-"
    play sound falling_sfx fadein 0.15
    nvl clear
    hide diary
    hide brown_transparent
    pov "อ่า วันนี้ก็ยังมีเสียงดังเหมือนเดิมเลยแหะ แต่นี่ผ่านมาเดือนนึงแล้วนะ ยังไม่หายไปเลย คงต้องจัดการสักหน่อยแล้ว"
    play sound cry_sfx fadein 0.25 fadeout 1.5 volume 0.35
    scene bg7night
    with dissolve
    pov "วะ วันนี้คงต้องนอนแล้วล่ะ คะ คุณสุรชัยมาทักแล้ว"
    pov "(แต่ฉันก็สงสัยอยู่ดีว่า สรุปแล้วเป็นเสียงจากอะไรกันแน่)"
    pov "(เอาเป็นว่า วันนี้นอนก่อนดีกว่า)"
    stop music fadeout 2.0
    stop sound fadeout 0.5
    scene black with eye_shut
    pause 1.0

    jump act2_2_shot_1
