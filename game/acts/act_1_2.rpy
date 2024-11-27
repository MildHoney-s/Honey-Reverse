label act1_2_shot_1:
    scene bg7day with eye_open
    play music morning_bgm loop fadein 1.0
    pov "(เช้าวันรุ่งขึ้น หลังจากที่ฉันหนีไปนอนเพราะเสียงประหลาดในช่วงกลางคืน)"
    pov "(ก็ไม่ค่อยแน่ใจว่ามันคือเสียงอะไรกันแน่ ถึงจะถามเจ้าของบ้านคนก่อน เขาว่า“มันก็ไม่มีอะไร”นี่สิ)"
    pov "(เห้อ เอาเถอะ ยังไงซะต่อให้ฉันรู้ว่ามี หรือไม่มีอะไรเกิดขึ้น ฉันก็ทำอะไรไม่ได้อยู่แล้ว เตรียมตัวออกไปซื้อของเข้าร้านก่อนดีกว่า)"
    pov "เอาล่ะ วันนี้ก็ สู้!"
    scene black with dissolve
    centered "{=centered_text} 1 ชั่วโมงผ่านไปหลังจากที่ฉันซื้อของเสร็จกลับมาที่ร้าน{/centered_text}"
    scene bg2day with fade
    play sound door_sfx fadein 0.25 volume 0.55
    show mild maid_smile6 at leftposmild
    with easeinleft
    pause 0.5
    pov "อ่ะ อรุณสวัสดิ์ มายด์"
    show mild maid_wave at middleposmild
    with easeinleft
    mild "สวัสดีตอนเช้าค่ะ [povname]"
    pov "ทานอะไรมั้ย เดี๋ยวฉันทำอะไรให้กิน"
    show mild maid_flustered at middleposmild
    with dissolve
    mild "ค-คะ!?"
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_grumpy at mild_close,bounce
    with dissolve
    mild "รอบนี้จะแกล้งให้ฉันต้องจ่ายค่าอาหารให้คุณอีกมั้ยคะเนี่ย"
    pov "กะ ก็ต้องไม่ใช่น่ะซิ! เป็นสวัสดิการให้พนักงานน่ะ!"
    pov "(นี่เธอยังระแวงเรื่องเมื่อตอนนั้นอยู่อีกหรอเนี่ย..)"
    pov "แล้วเธออยากทานอะไรล่ะ มีอะไรอยากกินเป็นพิเศษรึเปล่า"
    show mild maid_doubt at mild_close
    with dissolve
    mild "อื้ม.... พอดีฉันไม่ค่อยมีเมนูในใจเลยค่ะ ที่ทานแล้วอร่อยคงเป็น ชานม ที่[povname] เคยเอามาให้"
    pov "งั้น เอาเป็นเมนูของที่ร้านแล้วกันเนอะ"
    show mild maid_smile1 at mild_close
    with dissolve
    pov "เอาล่ะ! ได้เวลาโชว์ฝีมือแล้วสินะ!"
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_blush2 at mild_close
    with fade
    mild "(ถึงจะรู้อยู่แล้วว่า [povname] ทำอาหารเก่งก็เถอะนะ แต่พอได้ดูใกล้ๆ แบบนี้..)"
    pov "เสร็จแล้ว!"
    show mild maid_smile3 at mild_close
    with dissolve
    pov "เชิญทานเลย ออมไรส์สูตรพิเศษจากฉันเอง!"
    mild "งั้นขออนุญาต..ทานนะคะ"
    show mild maid_smile9 at mild_close
    with dissolve
    mild "อร่อยมากเลยค่ะ!"
    pov "แน่นอนอยู่แล้ว~ ถ้าเธอทานไม่หมดฉันจะเสียใจเอาน้าา"
    mild "แน่นอนค่ะ!"
    show mild maid_smile6 at mild_close
    show rice at rice
    with fade
    mild "ฮ่าส์ ขอบคุณสำหรับอาหารค่ะ!"
    pov "อื้มมม อันนี้ชานม เติมพลังแล้วก็ยิ้มไว้เยอะๆ นะโอเคมั้ย"
    show mild maid_smile3 at mild_close
    with dissolve
    mild "ขอบคุณนะคะ"

    jump act1_2_shot_2

label act1_2_shot_2:
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_smile10 at mild_close
    show rice at rice
    with dissolve
    pov "อ่ะ! อยู่เฉยๆ แปปนึงนะมายด์"
    menu:
        "เอามือไปลูบแก้ม เอาเม็ดข้าวที่ติดออกและนำเข้าปากตัวเอง":
            $ honey_score -= 1

        "เอากระดาษทิชชู่ไปลูบแก้มเพื่อเอาข้าวที่ติดออก":
            $ honey_score += 1
    show mild maid_flustered at mild_close
    hide rice
    with sshake
    mild "ค-ค-ค-คะ!!?"
    pov "ฮิฮิ"
    stop music fadeout 1.0
    play sound door_sfx fadein 0.25 volume 0.55
    unknow_debirun "เอ่อคือ..."
    scene bg2day
    show mild maid_blush1 at leftposmild
    with dissolve
    play music cafe_bgm loop fadein 1.0 fadeout 1.0
    unknow_debirun "สวัสดีค่ะ ผู้จัดการ.."
    show del normal_smile2 at rightposdel
    with easeinright
    pov "อ่ะ ว่าไงสวัสดียามเช้านะ เดลจัง มาเช้าจังเลยนะ"
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show del normal_idle1 at del_close
    with dissolve
    debirun "ก็มันว่างนี่คะ..."
    hide del normal_idle1
    show del normal_smile1 at del_close
    with dissolve
    debirun "แล้วนี่หนูมาขัดจังหวะผู้จัดการกับแฟนรึเปล่าคะเนี่ย..."
    scene bg2day
    show mild maid_flustered at leftposmild
    show del normal_smile7 at rightposdel
    with dissolve
    pov "ฟะ แฟนอะไรละ มะ ไม่ใช่สักหน่อย เนอะมายด์-"
    pov "(ระหว่างที่ฉันแก้ตัวพอได้หันไปมองที่มายด์ กลับเห็นสีหน้าของเธอที่แดงผ่าวราวกับมะเขือเทศ\nนะ นี่เธอเขินอยู่อย่างงั้นหรอ!)"
    show del normal_smile8 at rightposdel
    show mild maid_blush2 at leftposmild
    with dissolve
    debirun "เอาน่าาาา หนูก็แค่แซววววววว ฮิฮิ"
    pov "หนอยยยย ยัยเด็กนี่!"
    pov "ฟู่วว เอาเป็นว่า เธอคนนี้คือพนักงานใหม่ของร้านเรา ชื่อ มายด์อาร์"
    show del normal_idle2 at rightposdel
    show mild maid_idle1 at leftposmild
    with dissolve
    mild "มายด์อาร์ค่ะ เรียก มายด์เฉยๆ ก็ได้นะคะ"
    pov "มายด์ส่วนนี่ เดบิรุน"
    show del normal_smile1 at rightposdel
    with dissolve
    debirun "สวัสดีค่ะ เดบิรุน เรียกเดลก็ได้นะคะ"
    debirun "จะว่าไป คุณมายด์ อายุเท่าไหร่หรอคะ"
    pov "(จริงด้วยสิ ฉันเองก็ยังไม่เคยรู้เลยแฮะ)"
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_doubt at mild_close
    show emotion_question at emoteclose
    with dissolve
    mild "มายด์หรอ อืม.."
    mild "คิดว่าน่าจะประมาณ 20 กว่าๆ แล้วนะคะ"
    scene bg2day
    show mild maid_idle1 at leftposmild
    show del normal_smile5 at rightposdel
    with dissolve
    debirun "อ่ะ งั้นก็เป็นพี่ของเดลสินะ ฝากตัวด้วยนะพี่มายด์"

    jump act1_2_shot_3

label act1_2_shot_3:
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show del normal_doubt1 at del_close
    show emotion_question at emoteclose
    with fade
    debirun "เห็นว่าเป็นพนักงานใหม่แล้วพี่มายด์เล่นบทอะไรหรอผู้จัดการ"
    pov "ฮื้ม.. จริงๆ ฉันก็คิดไว้สักพักแล้วแหละ ว่าคาแรคเตอร์แบบมายด์ที่ฉันเห็นควรจะเป็น..."
    menu:
        "เมดพยาบาล แบบไอดอลสาวไปเลย":
            $ honey_score += 1
            scene bg2day:
                crop (100,200,1480,720)
                size (1920, 1080)
            show mild maid_doubt at mild_close
            mild "ไอ..ดอล?"
            pov "มะ ไม่มีอะไรก็หมายถึงเมดพยาบาลนั่นแหละ"

        "แฟนฉัน":
            $ honey_score -= 1
            scene bg2day:
                crop (100,200,1480,720)
                size (1920, 1080)
            show mild maid_flustered at mild_close
            mild "ฟะ แฟน..?"
            pov "หมายถึงเมดพยาบาล แบบไอดอลสาวนะ"
    show mild maid_smile3 at mild_close
    with dissolve
    mild "คะ ค่า แล้ว ไอดอล..."
    show mild maid_doubt at mild_close
    show emotion_question at emoteclose
    with dissolve
    mild "คืออะไรหรอคะ"
    pov "ไอดอลน่ะ เป็นเหมือนผู้ที่คอยมอบรอยยิ้ม ความสดใส ที่จะช่วย รักษาหัวใจ ให้กับผู้คนยังไงล่ะ"
    show mild maid_blush2 at mild_close
    hide emotion_question
    with dissolve
    mild "ฉันเป็นแบบนั้นหรอคะ.."
    pov "อื้มม ใช่สิ ออร่าที่มาจากตัวเธอน่ะ สุดยอดมากเลยนะ"
    scene bg2day
    show mild maid_blush1 at leftposmild
    show del normal_smile7 at rightposdel
    with dissolve
    debirun "ผู้จัดการยังชมขนาดนั้น พี่มายด์เชื่อมั่นในตัวเองไว้นะ"
    show del normal_doubt1 at rightposdel
    with dissolve
    debirun "จะว่าไป นี่ก็ใกล้เวลาเปิดร้านแล้วนะ ทำไมพี่ซึรูรุยังไม่มาอีก"
    pov "เอาเถอะไม่เป็นไรหรอก พวกเธอไปเตรียมตัวกันได้เลยนะ"
    show mild maid_smile3 at leftposmild
    show del normal_smile1 at rightposdel
    with dissolve
    mild_debirun "ค่าาาาาาาาา !"
    scene black with eye_shut
    pause 0.5
    scene bg2day with fade
    show del maid_idle1 at middleposdel
    debirun "เอาล่ะ *ได้เวลางานแล้วๆๆๆ*"
    show del maid_idle1 at rightposdel
    show mild maid_doubt at leftposmild
    with easeinleft
    mild "เป็นอะไรไปหรอเดลจัง"
    scene bg2day
    play sound "<from 0.5 to 2.5>SFX/slap_sfx.mp3" fadein 0.25
    show delbyou at truecenter:
        zoom 1.1
    with fade
    debirun "ย๊า ด้วยนามของผู้อยู่เหนือกาลเวลา พวกเจ้าจงฟัง! นามของข้าคือเดบิรุน! \nก้มหัวสะสิ 5 5 5  5 5 5 5 5 5 55 5 5 5 5 5 5 55 !"
    mild "ดะ..เดล.. จัง.... เปี่ยน.. ไป๊"
    debirun "เอาล่ะ! ได้เวลาไปต้อนรับเจ้าพวกมนุษย์แล้วสินะ ฮ่าฮาฮ่า!"
    mild "...."

    $ quick_menu = False
    play music minigame2_bgm loop fadein 1.0 fadeout 0.5
    call screen minigame_1(minigame1_act1_2_shot_3)
    $ renpy.block_rollback()
    $ quick_menu = True

    jump act1_2_shot_4

label act1_2_shot_4:
    scene bg2day
    play music cafe_bgm loop fadein 1.0 fadeout 1.0
    show del maid_doubt at rightposdel
    show mild maid_smile10 at leftposmild
    with fade
    debirun "นี่ก็ผ่านมาสักพักแล้วนะผู้จัดการ พี่ซึรุเขายังไม่มาเลย"
    pov "นั่นสิเป็นอะไรรึเปล่านะ.."
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show mild maid_doubt at mild_close
    mild "(ตอนคุยกับพวกเรายังเป็นเดลจังตอนปกติสินะ..)"
    scene bg2day
    show del maid_doubt at rightposdel
    show mild maid_doubt at leftposmild
    with fade
    pause 0.5
    play sound "<from 0.5 to 2.5>SFX/running_sfx.mp3" fadein 0.25
    queue sound door_sfx fadein 0.25
    pause 4
    show mild maid_doubt at llposmild
    show del maid_doubt at llposdel
    show tsuru normal_smug at rightpostsuru
    with easeinright
    tsuru "มาแล้วค่าาาาาาาา!"
    show mild maid_idle1 at llposmild
    show del maid_idle2 at llposdel
    with dissolve
    debirun "พี่ซึรุ"
    show mild maid_idle2 at llposmild
    with dissolve
    mild "ซึรุทำไมมาช้าจัง"
    pov "หวังว่ารอบนี้จะมีข้อแก้ตัวดี ๆ นะซึรุ.."
    show del maid_idle1 at llposdel
    show tsuru normal_smile5 at rightpostsuru
    show emotion_tear at emotepairpos2
    with dissolve
    tsuru "อ่า..เอ่อ..นะ หนู นอนเพลิน แหะๆ"
    show mild maid_idle1 at llposmild
    with dissolve
    mild "โถ้ว นึกว่าเป็นอะไรซะอีกนะ"
    hide emotion_tear
    with dissolve
    pov "ก็ยังดีว่าเป็นอะไรไปละนะ เอาล่ะ ไปเตรียมตัวเข้างานได้แล้ว ชดเชยในส่วนที่มาสายด้วยล่ะ"
    show tsuru normal_smile4 at rightpostsuru
    with dissolve
    tsuru "ค้าบบบบบบบ"
    stop music fadeout 1.0
    show black
    with fade


    $ quick_menu = False
    play music minigame2_bgm loop fadein 1.0 fadeout 0.5
    call screen minigame_1(minigame1_act1_2_shot_4)
    $ renpy.block_rollback()
    $ quick_menu = True

    jump act1_2_shot_5

label act1_2_shot_5:
    scene bg2night
    play music night_bgm loop fadein 1.5 fadeout 0.5
    pov "(หลังจากที่ร้านปิด ฉันเดินออกมาจากห้องพักพนักงานเพื่อที่จะเริ่มเก็บกวาดครัว ส่วนสาวๆ ก็กำลังเม้าท์ไปเก็บกวาดร้านไปด้วย)"
    show caring at truecenter:
        zoom 0.3
    pov "เอ๊ะ! อันนี้น่ะลูกค้าทำตกไว้รึเปล่า?"
    show caring at emoteclose:
        zoom 0.3
    show tsuru maid_wow at rightpostsuru
    show emotion_shock at emotepairpos2
    with easeinright
    tsuru "อ่ะ! ของหนูๆ"
    tsuru "พวงกุญแจของหนูมันชอบตกตลอดเลย ดีนะที่ยังตกอยู่ในร้าน"
    show del maid_stunned at llposmild
    with easeinleft
    hide emotion_shock
    debirun "ตัวห่วงคล้องมันหลุดไปแล้วหนิพี่ซึรุ"
    show tsuru maid_idle2 at rightpostsuru
    with dissolve
    tsuru "เอ๊ะ! จริงด้วย เดี๋ยวกลับไปซ่อมให้นะน้องห่วงใย"
    scene bg2night:
        crop (400,240,1280,720)
        size (1920, 1080)
    show tsuru maid_smile3 at tsuru_close
    with dissolve
    tsuru "ขอบคุณนะคะผู้จัดการ"
    scene bg2night
    show tsuru maid_idle2 at rightpostsuru
    show del maid_gloomy1 at leftposdel
    with dissolve
    debirun "แบบนี้คงจะไม่มีน้องติดตัวไปสักพักสินะพี่ซึรุ"
    show tsuru maid_smile2 at rightpostsuru
    with dissolve
    tsuru "อ๋อ ไม่เป็นไร ยังมีตัวจริงให้กอดอยู่ที่ห้องน่ะ"
    show del maid_gloomy2 at leftposdel
    with dissolve
    tsuru "แต่ก็คงจะคิดถึงตอนออกมาทำงานแน่เลย"
    scene bg2night:
        crop (400,240,1280,720)
        size (1920, 1080)
    show siralfred at truecenter:
        zoom 0.5
    with fade
    debirun "จริงหรอพี่! หนูก็มีตุ๊กตาเหมือนกัน ชื่อว่า ท่านเซอร์อัลเฟรด ล่ะ"
    scene bg2night
    show siralfred at emoteclose:
        zoom 0.3
    show tsuru maid_smile at rightpostsuru
    show del maid_smile2 at leftposdel
    with dissolve
    tsuru "แน่ละสิ ก็เดลชอบกอดนี่นา ตอนมานอนกับพี่ทีไรยังขอกอดพี่อยู่บ่อยๆ เลย"
    show del maid_crying at leftposdel
    with dissolve
    debirun "อ๊ากกก อย่าพูดน้าาา"
    hide siralfred
    show del maid_doubt at middleposdel
    show tsuru maid_smile2 at rightpostsuru
    show mild maid_smile3 at llposmild
    with easeinleft
    debirun "แล้วพี่มายด์ล่ะ มีตุ๊กตาบ้างมั้ย"
    show mild maid_doubt at llposmild
    with dissolve
    mild "ตุ๊กตาหรอคะ..."
    show emotion_question at emotepairpos1
    mild "ที่เป็นตัวนุ่มๆ น่ารักๆ เอาไว้กอดหรอคะ.."
    hide emotion_question
    show del maid_smile4 at middleposdel
    show tsuru maid_smile1 at rightpostsuru
    with dissolve
    debirun "ช่ายๆ ประมาณนั้นแหละ มีบ้างมั้ย"
    show mild maid_idle1 at llposmild
    with dissolve
    mild "ถ้าฟังจากที่คุยๆ กัน อื้ม... ไม่มีเลยค่ะ"

    jump act1_2_shot_6

label act1_2_shot_6:
    show tsuru maid_idle1 at rightpostsuru
    with dissolve
    tsuru "มายด์เขาพึ่งหลุดออกมาจากห้องทดลองน่ะ ก็เลยไม่ค่อยรู้เกี่ยวกับโลกภายนอกเท่าไหร่"
    show del maid_doubt at middleposdel
    with dissolve
    debirun "เอ๊ะ! หลุดมาจากห้องทดลอง!?"
    show tsuru maid_smile2 at rightpostsuru
    with dissolve
    tsuru "ผู้จัดการยังไม่เล่าให้ฟังหรอ"
    debirun "ยังนะพี่...."
    pov "//กระแอม"
    show tsuru maid_smile3 at rightpostsuru
    with dissolve
    tsuru "เรื่องมีอยู่ว่า..."
    scene black with dissolve
    stop music fadeout 1.0
    centered "{=centered_text} ซึรุได้เล่าเรื่องราวทั้งหมดให้เดลฟัง{/centered_text}"
    scene bg2night with fade
    play music roman_bgm loop fadein 1.5 fadeout 0.5
    show milddel at truecenter:
        zoom 1.05
    debirun "โถ่ววว พี่สาวคนสวยของหนู หนูอยู่นี่น้า "
    debirun "หนูไม่รู้เลยว่าพี่จะเจอเรื่องแบบนี้ อ่ะกอดๆ นะค้าบบ"
    mild "พี่ไม่เป็นไรแล้วเดลจัง โอ๋ๆ"
    debirun "อื้อ.. //เดลถอยตัวออกจากมายด์มา"
    show mildru_sd_1 at truecenter:
        zoom 0.7
    with dissolve
    mild "ซะ ซึรุ"
    show mildru_sd_2 at truecenter:
        zoom 0.7
    with dissolve
    tsuru "โอ๋ๆ ไม่เป็นไรนะ ฉันจะอยู่ข้างเธอเอง"
    pause 1.5
    jump act1_2_shot_7

label act1_2_shot_7:
    scene bg2night
    with fade
    show mild maid_smile11 at middleposmild
    show del maid_smile2 at leftposdel
    show tsuru maid_smile2 at rightpostsuru
    tsuru "แล้วมายด์เคยเห็นสัตว์บนโลกบ้างรึยังล่ะ"
    show mild maid_sorry at middleposmild
    mild "เคยเห็นแต่แมวแถวๆ หน้าร้านน่ะ"
    show del maid_smile6 at leftposdel
    debirun "งั้นพี่มายด์ ดูนี่ๆ"
    scene black with dissolve
    stop music
    $ _game_menu_screen = None
    $ quick_menu = False
    $ renpy.block_rollback()
    play movie "frog.webm"
    $ renpy.block_rollback()
    $ renpy.pause(42, hard=True)
    scene white with tv_transition
    stop music
    play movie "animal.webm"
    $ renpy.pause(36, hard=True)
    $ quick_menu = True
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"
    stop music
    scene bg2night with fade
    play music night_bgm loop fadein 0.5 fadeout 1.0
    show mild maid_blush1 at rightposmild
    mild "น่ารักจัง ตัวกลมๆ ขาวๆ หน้ามีรอยดำๆ น่ากอดจัง.."
    show tsuru maid_idle2 at leftpostsuru
    with moveinleft
    tsuru "ตัวนี้เรียกว่าแพนด้าน่ะ"
    show mild maid_doubt at rightposmild
    with dissolve
    mild "แพน... อะไรนะคะ?"
    show tsuru maid_smile4 at leftpostsuru
    with dissolve
    tsuru "แพนนนนนนนน ด้าาา"
    show mild maid_stunned at rightposmild
    with dissolve
    mild "พะ แพน...."
    mild "ออกเสียงยากจัง"
    show mild maid_stunned at middleposmild
    show del maid_smile4 at rightposdel
    with easeinright
    debirun "งั้นก็เรียกพี่แพน เลยก็ได้นี่"
    show mild maid_smile11 at middleposmild
    mild "พี่แพน.. งื้อออออ น่ารักจังงง"
    show tsuru maid_smile2 at leftpostsuru
    with dissolve
    tsuru "ไว้มีโอกาสฉันจะหาพี่แพนมาให้นะ ถึงจะเป็นพวงกุญแจก็เถอะ ไว้สักวันเราไปหาซื้อพี่แพนด้วยกันนะ"
    mild "อื้ออ!"
    pov "(มายด์ยังต้องเรียนรู้โลกภายนอกอีกเยอะเลยสินะ ไว้ถ้ามีโอกาสฉันคงต้องพาออกไปข้างนอกสักหน่อยแล้วล่ะ แต่แบบนี้ก็คือ ดะ เดท..สินะ...)"
    pov "เอาล่ะพวกเธอ ถ้าเก็บร้านเสร็จแล้วก็กลับบ้านได้เลยนะ เดินทางปลอดภัยล่ะ วันนี้ก็ขอบคุณมาก"
    show mild maid_smile3 at middleposmild
    show del maid_smile1 at rightposdel
    show tsuru maid_smile4 at leftpostsuru
    with dissolve
    mild_tsuru_debirun "ขอบคุณที่เหนื่อยค่าาาาาาาาาาา"
    stop music fadeout 1.0
    jump act1_2_shot_8

label act1_2_shot_8:
    scene bg7light
    with fade
    play music diary_bgm loop fadein 0.5 fadeout 1.0
    pov "(เอาล่ะวันนี้ผ่านไปอีกวัน ทีนี้ก็มาเขียนสรุปไดอารี่ดีกว่า)"
    show diary
    show brown_transparent
    nvl clear
    diary "วันนี้ซึรุก็มาสายอีกแล้ว แถมยังตื่นสายเหมือนเดิมเลยด้วย ทำเอาฉันตกใจได้ทุกครั้งเลยนะ"
    diary "อ๋อเป็นวันแรกที่เดลกับมายด์ได้เจอกันด้วย สนิทกันไวดีจริงๆ นะ เข้ากันเป็นปี่เป็นขลุ่ยเลย เห็นแบบนี้ก็ชื่นใจสุดๆ ที่สาวๆ เข้ากันได้ดี"
    diary "ถึงมายด์จะตกใจตอนที่เดลเข้าโหมดทำงานก็เถอะ ฮ่าฮ่าฮ่า...)"
    diary "วันนี้ได้รู้อะไรเกี่ยวกับมายด์เพิ่มขึ้นด้วย จากที่สาวๆ คุยกันเหมือนมายด์จะชอบแพนด้า มาก ๆ เลยนะ ถึงแม้วิธีเรียกจะแปลกๆ ..."
    diary "พี่แพนงั้นหรอ... น่ารักดีแฮะ... บ้าจริงแค่นึกถึงฉันก็หุบยิ้มไม่ได้แล้วเนี่ย น่ารักจนใจแทบวายเลย! "
    hide diary
    hide brown_transparent
    with dissolve
    pov "วันนี้ก็คงประมาณนี้แหละ หวังว่าหลังจากนี้จะราบรื่นเหมือนกันทุกวันนะ~"
    scene bg7night
    with dissolve
    play sound body_sfx volume 0.75
    pov "นอนดีกว่า~ "
    pov "อีกแล้วหรอ แหะๆ ห้ามทักนี่นา.. รีบหนีไปนอนดีกว่า.."
    stop sound
    scene black with eye_shut
    pause 1.0

    jump act2_1_shot_1
