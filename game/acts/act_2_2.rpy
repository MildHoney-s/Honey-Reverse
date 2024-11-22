label act2_2_shot_1:
    $ quick_menu = False
    play music minigame1_bgm loop fadein 1.0
    call screen minigame_1(minigame1_act2_2)
    $ renpy.block_rollback()
    $ quick_menu = True
    play sound door_sfx fadein 0.25 volume 0.45
    scene bg2day
    play music pixfia_bgm loop fadein 1.5
    show mild maid_idle3 at leftposmild
    mild "ยินดีต้อนรับค่าาา"
    show pixchan at shadowright
    show zoulfia at shadowmid
    with easeinright
    pixchan "สวัสดีค่า สองที่ค่ะคุณเมด"
    show mild maid_smile3 at leftposmild
    mild "สองคนสินะคะ เชิญนั่งได้เลยค่ะ เดี๋ยวฉันไปรับเมนูนะคะ"
    hide mild maid_smile3
    with easeoutleft
    pause 1.0
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show pixchan at shadowcloser
    show zoulfia at shadowclosel
    show pixchan at bounce,shadowcloser
    pixchan "เธ๊อออ เมดคนเมื่อกี้น่ารักเนอะะ"
    show zoulfia at bounce,shadowclosel
    zoulfia "เธอว่าไงนะ…!"
    show pixchan at bounce,shadowcloser
    pixchan "อ้ยย ต่อให้ฉันจะชมใคร เธอก็น่ารักที่สุดอยู่แล้วนะคะ คุณแฟนที่น่ารัก"
    show zoulfia at bounce,shadowclosel
    zoulfia "เธอเนี่ย คนเยอะแยะ อ๊ากกกกกกกกกก! คนบว้าๆๆๆๆๆ"
    show pixchan at bounce,shadowcloser
    pixchan "ฮิฮิ น่ารักจังเลยน้าา"
    show pixchan at bounce,shadowcloser
    pixchan "ป่ะๆ ไปนั่งกันได้แล้วล่ะนะ"
    show zoulfia at bounce,shadowclosel
    zoulfia "อื้อ"
    scene bg2day
    with fade
    show mild maid_idle4 at mild_close
    with dissolve
    mild "รับอะไรดีคะ"
    pixchan "มีอะไรแนะนำบ้างมั้ยคะ"
    show mild maid_smile3 at mild_close
    with dissolve
    mild "ถ้าในร้านของเราตอนนี้ เมนูแนะนำคือ ฮันนี่บราวชูก้า ค่ะ"
    show mild maid_smile5 at mild_close
    with dissolve
    mild "และพิเศษ ถ้าลูกค้าสั่งเซ็ตฮันนี่สเปเชียล จะได้รับอาหาร 1 จาน ทาโกะยากิ 1 จาน เครื่องดื่ม 1 แก้ว และสามารถเลือกน้องเมดแสดงบนสเตจได้ค่ะ"
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show pixchan at shadowcloser
    show zoulfia at bounce,shadowclosel
    zoulfia "มีการแสดงด้วยหรอคะะะะ"
    show zoulfia at bounce,shadowclosel
    zoulfia "เธ๊ออ ชั้นอยากดูจังเลยยย"
    show pixchan at bounce,shadowcloser
    pixchan "เธออยากดูหรอ ฉันก็สนใจอยู่เหมือนกันล่ะนะ"
    show pixchan at bounce,shadowcloser
    pixchan "ถ้างั้นชั้นขอสั่งเซ็ตนี้เลยค่ะ"
    scene bg2day
    show mild maid_smile6 at mild_close
    with dissolve
    mild "รับทราบค่าาา น้องเมดคนไหนดีคะ"
    mild "มีซึรุรุ เดบีรุ-"
    zoulfia "ขอเป็นคุณเมดเลยค่ะ!"
    show mild maid_flustered at mild_close
    with dissolve
    mild "ค-คะะะ!?"
    zoulfia "คุณเมดนั่นแหละค่าาา"
    show mild maid_blush2 at mild_close
    with dissolve
    mild "ดะ ได้ค่า อยากให้แสดงแบบไหนดีคะ"
    zoulfia "เอาแบบที่คุณเมดอยากแสดงเลยค่า"
    pixchan "แบบที่คุณเมดถนัดได้เลยนะคะ"
    show mild maid_blush1 at mild_close
    with dissolve
    mild "ค-ค่า"
    hide mild maid_blush1 with easeoutleft
    pause 1.0
    scene bg8day
    play music before_bgm loop fadein 0.5 fadeout 1.0
    with fade
    show tsuru maid_wow at rightpostsuru
    with None
    show mild maid_sorry at leftposmild
    show emotion_worried at emotepairpos1
    with easeinleft
    tsuru "เป็นอะไรหรอมายด์ ทำไมทำหน้าแบบนั้นล่ะ"
    show mild maid_blush1 at leftposmild
    hide emotion_worried
    show emotion_stressed at emotepairpos1
    with dissolve
    mild "ซึรุ ฉันต้องไปแสดงบนสเตจ"
    show tsuru maid_smile2 at rightpostsuru
    with dissolve
    tsuru "จริงหรออ ก็ดีแล้วนี่นาาา"
    hide emotion_stressed
    show mild maid_grumpy at leftposmild
    with dissolve
    mild "ตะ… แต่ฉันไม่มั่นใจเลย"
    show tsuru maid_smile4 at rightpostsuru
    tsuru "ไม่ต้องห่วงนะ ฉันเป็นกำลังใจให้ และฉันมีเพลงเตรียมไว้ให้แกด้วยนะ"
    show mild maid_doubt at leftposmild
    with dissolve
    mild "เพลงอะไรอ่ะ"
    scene black
    with fade
    stop music
    centered "ก่อนจะเข้าสู่สเตจ ขอเชิญ Mild-R ที่กลางจอ เพื่อเข้าสู่การแสดงในลำดับต่อไป ขอบพระคุณ"
    $ _game_menu_screen = None
    play movie "Bang Pho.webm"
    $ _game_menu_screen = "save"
    $ renpy.pause(26, hard=True)
    scene black
    with fade
    $ renpy.pause(1, modal = True)
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    with fade
    show pixchan at shadowcloser
    show zoulfia at bounce,shadowclosel
    play music maid_bgm loop fadeout 0.5
    zoulfia "สนุกมากเลยค่าาาาาาาาาาาา *แฮ๊กๆ*"
    show pixchan at bounce,shadowcloser
    pixchan "สนุกใหญ่เลยนะเธอ"
    show zoulfia at bounce,shadowclosel
    zoulfia "ก็คุณเมดโยกมันส์มากเลยอ่ะเธ๊ออออออ"
    show pixchan at bounce,shadowcloser
    pixchan "จ้าาาา ป่ะๆ ไปนั่งพักนะ เดี๋ยวฉันมา"
    hide pixchan
    with easeoutright
    scene bg2day
    show mild maid_smile3 at leftposmild
    with dissolve
    show pixchan at shadowcloser
    with easeinright
    pixchan "สเตจสนุกมากเลยค่า ขอบคุณที่เหนื่อยนะคะ"
    show mild maid_smile11 at leftposmild
    with dissolve
    mild "ยะ ยินดีที่ชอบนะคะ"
    show mild maid_smile8 at leftposmild
    with dissolve
    pixchan "แล้วก็ ฉันอยากมาให้กำลังใจ คุณเมดค่ะ"
    pixchan "ถึงคุณเมดดูจะเป็นกังวล ระแวงและกลัวคนรอบข้างอยู่ตลอดเลย ลองผ่อนคลายลงสักหน่อยก็ได้นะคะ?"
    pixchan "ฉันเองก็เป็นมิวแทนท์ เหมือนกับคุณนั่นแหละค่ะ ถึงจะต่างออกไปนิดหน่อยก็เถอะ"
    show mild maid_doubt at leftposmild
    with dissolve
    mild "มะ หมายความว่ายังไงหรอคะ"
    mild "ระ หรือว่าหูยาวๆ นั่น …."
    pixchan "ใช่แล้วค่ะ หูนี่น่ะ ไม่ใช่ที่คาดผม แต่เป็นหูจริงๆ ของฉันค่ะ"
    show mild maid_sorry at leftposmild
    with dissolve
    mild "ยะ อย่างนี้นี่เอง คุณเองก็เป็นมิวแทนท์เหมือนกันหรอคะ…"
    pixchan "อย่าทำหน้าแบบนั้นสิคะ ไม่ต้องคิดมากหรอกนะ"
    pixchan "ไม่มีใครจะทำร้ายเธอทั้งนั้นแหละ อีกอย่างเธอต้องเจอกับคนคนนั้นแน่นอน"
    show mild maid_doubt at leftposmild
    with dissolve
    mild "คนคนนั้น?"
    pixchan "คนที่พร้อมจะช่วยเหลือ ดูแล เอาใจใส่ แล้วก็ปกป้องเธอด้วยชีวิต"
    show mild maid_blush1 at leftposmild
    with dissolve
    pixchan "เธออาจจะยังไม่รู้ตัวหรอก แต่ว่าเรื่องนั้นก็ส่วนเรื่องนั้นล่ะนะ"
    pixchan "หวังว่าจากนี้เธอจะใช้ชีวิตได้อย่างเต็มที่ มีความสุขในทุกๆ วันนะคะ"
    zoulfia "เธ๊อออ มากินเร็วๆ มาป้อนฉันนนนน"
    pixchan "อ่ะ ฉันไปก่อนนะคะ เพราะคนคนนั้นของฉันเรียกแล้วค่ะ"
    hide pixchan
    with easeoutright
    show mild maid_smile4 at leftposmild
    with dissolve
    mild "ขอบคุณสำหรับคำแนะนำนะคะะะะะะะ!"
    stop music fadeout 1.5
    scene black
    with fade
    scene bg29
    with dissolve
    play music cafe_bgm loop fadein 1.5
    pov "(หลังจากที่ไปแสดงสเตจวันนั้น มายด์ก็ดูมีชีวิตชีวามากขึ้นนะ รวมทั้งยอมขึ้นสเตจตามปกติแล้วด้วย)"
    pov "(และแล้วก็มาถึงอีเว้นท์ของเดือนกันยายนจนได้ นั่นก็คือ วันเกิดซึรุรุ!)"
    pov "(ธีมที่ซึรุขอมาก็คือ กบ)"
    pov "(กบ อ๊บๆ นั่นแหละ เหมือนเจ้าตัวจะชอบเล่นเป็นกบมากเลยนะ คงเป็นอีเว้นท์อีกวันที่สนุกแน่ๆ เลย)"
    show tsuru maid_frog1 at middlepostsuru
    with dissolve
    tsuru "สวัสดีค่าาาาา อะฮุฮิฮุฮิ คุโมกุ ซึรุรุ อ๊บตัวน้อยที่โดดสูงที่สุดจากร้านฮันนี่ รีเวิร์ส มาต้อบรับพี่ๆ ทุกคนแล้วค่าาาาา อ๊บอ๊บบบ"
    show tsuru maid_frog2 at tsuru_close
    with dissolve
    tsuru "ขอบคุณทุกคนที่มาอีเว้นท์วันเกิดของซึรุนะค๊าาาาา"
    show tsuru maid_frog3 at tsuru_close
    with dissolve
    tsuru "วันนี้ซึรุ มีของขวัญสุดพิเศษ มาฝากพี่ๆ ทุกคนล่ะอ๊บ ช่วยรับฟังด้วยนะ อ๊บอ๊บ"
    play music idol_bgm fadein 0.5
    $ _game_menu_screen = None
    play movie "Tsuru Dance.webm"
    $ _game_menu_screen = "save"
    $ renpy.block_rollback()
    $ renpy.pause(27, hard=True)
    scene black
    with fade
    stop music fadeout 1.5
    $ renpy.pause(1, modal = True)
    play sound clap_sfx fadein 0.5
    scene bg29
    show tsuru maid_frog4 at tsuru_close
    with dissolve
    tsuru "ขอบคุณค่าาาาาาาาา"
    play music bright_bgm loop fadein 0.5
    show edamame at truecenter:
        zoom 0.7
    stop sound fadeout 0.5
    tsuru "แล้วอย่าลืมสั่งเมนูพิเศษ ถั่วแระญี่ปุ่น ของโปรดซึรุด้วยนะค๊าาาา" # //Asset ถั่วแระญี่ปุ่น
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_smile1 at llposmild
    show del maid_smile4 at llposdel
    with fade
    show tsuru maid_frog2 at rightpostsuru
    with easeinright
    mild "ซึรุ๊ววววว เก่งมากเลยยยยยยย"
    show mild maid_smile2 at llposmild
    with dissolve
    mild "สเตจก็ดีมากเลย"
    show tsuru maid_frog3 at rightpostsuru
    with dissolve
    tsuru "ขอบคุณนะแก ฉันดีใจมากเลย"
    show del maid_smile2 at llposdel
    with dissolve
    debirun "พี่ซึรุ ร้องเพลงเพราะมากเลยค่ะ แล้วก็เต้นเก่งด้วย"
    show tsuru maid_frog1 at rightpostsuru
    with dissolve
    tsuru "ขอบใจนะเดล ฉันขอไปพักในห้องพนักงานก่อนนะ"
    show mild maid_smile3 at llposmild
    show del maid_smile1 at llposdel
    with dissolve
    hide tsuru maid_frog1
    with easeoutleft
    mild_debirun "ได้เลยจ้าา"
    stop music fadeout 1.5
    scene black
    centered "{=centered_text}แล้วเวลาก็ผ่านไปจนถึงเวลาร้านปิด{/centered_text}"
    scene bg2night
    play music night_bgm loop fadein 0.5
    with fade
    show del maid_idle2 at leftposdel
    show tsuru maid_smile1 at rightpostsuru
    show mild maid_smile11 at middleposmild
    with dissolve
    pov "เหนื่อยหน่อยน้าาาา ทุกคนนนนนน"
    mild_tsuru_debirun "เหนื่อยหน่อยนะคะะ"
    pov "วันนี้ฉันขอตัวไปนอนเร็วหน่อยนะ ฝากปิดร้านด้วยนะทุกคน"
    show del maid_smile4 at leftposdel
    show tsuru maid_smile3 at rightpostsuru
    show mild maid_smile6 at middleposmild
    with dissolve
    mild_tsuru_debirun "ค่าาาาา"
    scene bg2night:
        crop (100,200,1480,720)
        size (1920, 1080)
    show del maid_smile6 at del_close
    with dissolve
    debirun "สุขสันต์วันเกิดนะคะพี่ซึรุ อยู่กับหนูไปนานๆเลยน้า"
    scene bg2night:
        crop (400,200,1780,720)
        size (1920, 1080)
    show mild maid_smile1 at mild_close
    with dissolve
    mild "แฮปปี้เบิร์ดเดย์นะแก"
    scene bg2night:
        crop (600,200,1980,720)
        size (1920, 1080)
    show tsuru maid_smile5 at tsuru_close
    with dissolve
    tsuru "ขอบใจมากเลยนะ นี่ๆ เราไปเดินเล่นกันมั้ย"
    show del maid_doubt at leftposdel
    show tsuru maid_smile5 at rightpostsuru
    show mild maid_doubt at middleposmild
    with dissolve
    debirun "เดินเล่นหรอ"
    mild "ไปทำอะไรอ่ะ"
    show tsuru maid_smile6 at rightpostsuru
    with dissolve
    tsuru "ก็เดินเล่นเฉยๆ อ่าาาา ไปกับฉันหน่อยน้าา"
    show del maid_smile5 at leftposdel
    show mild maid_smile4 at middleposmild
    with dissolve
    debirun "ไปๆ เดลไปปป"
    mild "อื้มๆ ไปกัน"
    scene black
    with fade
    play music roman_bgm loop fadein 0.5 fadeout 0.5
    scene bg14night
    with walkingVertical
    show tsuru normal_smile1 at bounce,leftpostsuru
    with easeinleft
    tsuru "มายด์เป็นยังไงบ้าง ทำงานมาได้พักนึงแล้ว"
    mild "ก็สนุกดีนะ เริ่มชินกับงานมากขึ้น แล้วก็ได้ขึ้นสเตจแรกแล้วด้วย"
    show del normal_smile1 at bounce,rightposdel
    with easeinright
    debirun "พี่โยกมันส์มากเลยนะ"
    show tsuru normal_smile4 at leftpostsuru
    tsuru "แกทำได้ดีกับสเตจแรกเลยนะ เป็นสเตจที่สนุกมากคับ"
    mild "ขอบคุณพวกเธอนะ ฉันเลยมีความกล้ามากขึ้นแล้วล่ะ"
    show tsuru normal_smile5 at leftpostsuru
    tsuru "ดีใจที่ช่วยแกได้นะ ฮี่ฮี่"
    show del normal_smile3 at bounce,rightposdel
    debirun "นี่ๆ พี่ๆ ตรงนั้นมีตู้ถ่ายรูปสติ๊กเกอร์ด้วยแหละะะ"
    show tsuru normal_smile3 at leftpostsuru
    with dissolve
    tsuru "เห้ยย ความคิดดีนี่น้องเดลล"
    show tsuru normal_smile6 at bounce,leftpostsuru
    with dissolve
    tsuru "ป่ะแก ไปถ่ายรูปกันน"
    mild "ถะ ถ่ายรูป???"
    scene black
    with wipeleft
    play sound camera_sfx fadein 0.125
    scene bg28 with eye_open
    show photo_sd at truecenter:
        zoom 0.55
    debirun "หนูหน้าแปลกอ่าาา พี่ซึรู๊ววว"
    tsuru "ไม่หรอกเดลก็สมกับเป็นเดลแล้วนี่นาา"
    debirun "ฮิฮิ ก็จริงของพี่นะ"
    tsuru "อ่ะนี่ อันนี้ของมายด์นะ"
    mild "ขอบใจนะรักพวกแกที่สุดเลยยย"
    tsuru "จ้าาาา"
    debirun "ค้าบบบ พี่สาวสุดสวยย"
    scene black
    with fade
    centered "หลังจากนั้นทั้งสามสาวก็ใช้เวลาเดินเที่ยวเล่นอย่างเพลิดเพลิน ในยามค่ำคืน"
    stop music fadeout 1.5

    jump act2_3_shot_1
