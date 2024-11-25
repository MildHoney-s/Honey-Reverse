label act1_1_shot_1:
    #Start scene Story Board Shot 1
    scene bg1 with dissolve
    play music walking_bgm loop

    manager "ตอนนี้ฉันเป็นเชฟมือใหม่ ที่พึ่งจบจากโรงเรียนยอดเชฟจากต่างประเทศ"
    manager "ครอบครัวของฉันเป็นเชฟกันหมด แถมยังมีร้านอาหารเป็นของตัวเองกันทุกคน แต่ละคนก็มีสไตล์อาหารของตัวเองแตกต่างกันไป"
    manager "ส่วนตัวฉันในตอนนี้ก็ได้เปิดร้านอาหารเล็กๆเหมือนคาเฟ่"
    manager "ถึงช่วงแรกจะโดนพวกพี่ๆ กับ ญาติๆบอกให้ไปช่วยงานที่ร้านของเขาก่อนก็เถอะ แต่ฉันมันดื้อ เลยมาเปิดร้านของตัวเองซะก่อน"
    manager "แรกๆ ก็มีคุณน้ามาช่วยอยู่ 2 - 3 เดือน แต่ตอนนี้เธอก็กลับไปดูแลร้านของตัวเองแล้วล่ะ"
    manager "ตัดกลับมาที่ร้านของฉัน"

    play sound walking_sfx loop
    window hide
    $ renpy.pause(1.5,modal=True)
    scene bg1:
        crop (0,0,1920,1080)
        size (1920, 1080)
        linear 2.0 crop (300, 200, 1280, 720)
    with walkingVertical
    $ renpy.pause(1,modal=True)

    window show
    manager "ตอนนี้ร้านของเราลูกค้าก็เยอะขึ้นแล้ว สองคนนั้นจะไหวไหมเนี่ย คนนึงก็เด็กซุ่มซ่าม ส่วนอีกคนก็……"
    manager "ยิ่งเสียงตอนเรียกหาฉันเวลามีปัญหา…"
    manager "เห้ออ…"
    manager "แล้วฉันก็ทำงานในครัวคนเดียวซะด้วยสิ หรือว่า- จะหาสาวสวยๆมาช่วยทำครัวเพิ่มดีน้าา อะแหะๆ.."
    stop sound
    manager "ถึงจะเคยประกาศรับสมัครไปแล้วก็เถอะ แต่ผลลัพธ์ที่ได้ก็……"
    stop music fadeout 0.5
    window hide dissolve

    jump act1_1_shot_2 #go to shot 2

#Interview scene with Ashy/Ami  Shot 2
label act1_1_shot_2:
    #Ashy scene
    scene black
    centered "{=centered_text}บุคคลปริศนา มีผมสีส้มยาวสลวย พร้อมกิ๊ปที่มีรูปภูเขาไฟ มีท่าทางดูสดใส และ มั่นใจในตัวเอง{/centered_text}"

    scene bg2day with eye_open

    style centered_text:
        color "#b5b5e9"  # Blue text color

    show sd_ashy_1_black at truecenter:
        zoom 0.6

    window show dissolve

    manager "ยินดีต้อนรับ ไม่ทราบว่าตอนนี้อายุเท่าไหร่แล้ว?"
    hide sd_ashy_1_black
    show ashy_sd_1 at truecenter:
        zoom 0.6
    with dissolve
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    play movie "ASH rap.webm"
    $ renpy.pause(15, hard=True)
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"
    hide ashy_sd_1
    show ashy_sd_2 at truecenter:
        zoom 0.6
    manager "(เดี๋ยวนะ ใครมันไปเอานักพากย์แข่งเรือแจวมาเนี่ย)"
    play music cafe_bgm loop volume 0.8
    manager "อ่า ใจเย็นๆก่อนนะ ขอโทษด้วยที่ถามเรื่องอายุ แล้วไม่ทราบว่า มีเมนูที่อยากแนะนำลูกค้ามั้ย"
    hide ashy_sd_2
    show ashy_sd_1 at truecenter:
        zoom 0.6
    with dissolve
    ashy "คุณผู้จัดการจ๋าาา ถ้าไม่รังเกียจละก็… หนูเอาแตงกวาจากสวนที่บ้านมาฝากด้วยล่ะ!!"

    show ashy_sd_1 at truecenter:
        crop (0,0,1920,1080)
        size (1920,1080)
        linear 2.0 crop (300, 200, 1920, 1080)
    with None
    pause 1.5
    show cucumbag at cucumber
    with dissolve
    manager "(เมื่อมองผ่านด้านหลังของผู้สมัครคนนี้ ก็พบว่ามีกระสอบขนาดใหญ่วางอยู่ด้านหลัง)"
    hide ashy_sd_1
    hide cucumbag
    show ashy_sd_1 at truecenter:
        zoom 0.6
    with dissolve

    ashy "หนูอยากทำทุกเมนูให้มีแตงกวาอยู่เยอะ ๆ เลยค่ะ!"
    manager "อ๋าา… แบบนี้เอง ไหนลองทำอาหารที่ครัวมาเมนูนึงได้มั้ย"
    ashy "ได้ค่าาา"

    scene black
    centered "{=centered_text}-เวลาผ่านไป-{/centered_text}"

    scene bg2day

    show ashy_sd_1 at truecenter:
        zoom 0.667
    with dissolve
    ashy "มาแล้วค่า~ นายท่าน เบอร์เกอร์สูตรพิเศษจากหนูเอง!"
    manager "ดูดีนี่ ไหนลองซิ…"
    manager "**ลองชิม**"
    show cucumburg at truecenter
    with dissolve
    stop music fadeout 1.0
    manager "แค่กๆ อะไรกันเนี่ยทำไมไส้ในถึงได้มีแต่แตงกวาล่ะ!" with sshake
    play music nightmare_bgm loop  fadein 1.25
    hide cucumburg
    ashy "เธอจ๋าาา จะไม่เอาแตงกวาจริงหรอจ๊ะ นี่น่ะของดีประจำอำเภ…"
    manager "เดี๋ยวลูกค้าก็ได้กินแตงกวาทุกเมนูพอดี ไม่ได้ๆ แบบนี้คงต้องให้ไม่ผ่าน!"
    manager "ไม่ผ่าน!!!" with ashyShake
    hide ashy_sd_1 with dissolve
    window hide

    #Ami scene
    scene black with dissolve
    stop music
    centered "{=centered_text}หลังจากผ่านไป 3 วัน บุคคลปริศนา2 ที่มาสมัครงาน มีผมสีขาว ลักษณะเป็นทวินเทล \nมีบางอย่างที่คล้ายๆที่ไขลานอยู่ด้านบน มีท่าทางเขินอาย ดูน่ารักน่าทะนุถนอม{/centered_text}"

    $ renpy.pause(1,modal=True)
    scene bg2day with eye_open
    show ami_sd_1 at truecenter
    #play music ami_bgm loop
    play music ami_bgm loop fadein 0.25
    window show
    ami "(อื้อออ...เราทำได้..ทำได้..ใช่ทำได้)"
    ami "สวัสดีค่าา หัวใจที่บอบช้ำของคุณ ขอเค้าดูแลเถอะนะคะ ><"
    ami "ตะ….. ตื่นเต้นจังเลยค่ะ"

    manager "ไม่เป็นไรนะ สบายๆนะ"
    manager "ถ้างั้นช่วยแจกใบปลิวสัก 15 ใบได้มั้ย"
    show ami_sd_1 at bounce,truecenter
    with dissolve
    ami "ได้ค่ะ! เค้าจะพยายามนะคะ!"
    scene bg4
    hide ami_sd_1
    show ami_sd_2 at truecenter:
        zoom 0.667
    with dissolve
    stop music
    play sound crowded_sfx loop volume 0.75 fadein 1.25
    ami "“สวัสดีค่า~! ขอฝากใบปลิวของร้านไว้หน่อยนะคะ~"
    "หลังจากนั้นก็มีกลุ่มผู้คนเข้ามารุมล้อม จนบังตัวผู้สัมภาษณ์คนนี้จนหมด"
    ami "อะ เอ่อ… ใบปลิวหมดแล้วค่าาา.. งื้อออ…. ค-คุณผู้จัดการคะะ..ช่วยด้วยค่าา…"
    manager "เดี๋ยวก่อน เผลอแปปเดียว ทำไมคนมาเยอะขนาดนั้นล่ะ!"
    manager "หยุดก่อน หยุดก่อนนนนนน"
    manager "(ถึงแม้ตัวฉันจะพยายามห้ามผู้คนที่มารุมล้อมเท่าไหร่ ก็ไม่สามารถเข้าไปช่วยเหลือได้)"
    stop sound
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    play movie "Ami crowded.webm"
    $ renpy.pause(18, hard=True)
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"
    hide ami_sd_2
    show ami_sd_3 at truecenter:
        crop (0,0,1920,1080)
        size (1920,1080)
        linear 1.0 crop (350, 200, 1280, 720)
    ami "พวกเตงอย่ามาชมกันแบบนี้สิคะะะ~~~"
    stop sound fadeout 1.0
    scene black with dissolve
    centered "{=centered_text}มีมือประหลาด 2 ข้าง พุ่งออกมาทำให้ผู้คนที่รุมล้อมและตัวฉันกระจายออกไป{/centered_text}"
    scene bg2day
    show ami_sd_3 at truecenter:
        zoom 0.667
    play sound mecha_sfx volume 0.8
    ami "ชะ- ช่วยด้วยค่าาาาาา ToT"
    manager "(จากนั้นหัวของเธอ ก็ได้หมุนไปเรื่อยๆ ไม่หยุด ทำให้ได้รู้ว่าหากเด็กคนนี้เขิน ร่างกายในส่วนหัวของเธอจะหมุนไม่หยุด . . . แม้กระทั่งเธอได้เดินออกจากร้านไป และการสัมภาษณ์ก็ได้จบลง...)"

    jump act1_1_shot_3 #go to shot 3

#Met Mild-R shot3
label act1_1_shot_3:
    # Back to the street scene
    scene  bg1 with transition_4
    play music walking_bgm loop fadein 1.0
    manager "นี่ก็ประกาศมา 2 สัปดาห์แล้วนะ ทำไมถึงไม่เจอสักที พนักงานดีๆน่ะ!"
    manager "ขอล่ะ ช่วยส่งพนักงานที่ใช้ได้มาให้ฉันที!!~" with vpunch
    play sound wind_sfx volume 1.25
    window hide dissolve
    show sd_wanted at truecenter:
        zoom 1.1
    stop music
    manager "เอ๊ะ กระดาษอะไรปลิวมาใส่หน้ากันล่ะเนี่ย.."
    play sound "<from 10.5 to 13>SFX/paper_sfx.mp3"
    play music poster_bgm loop fadein 0.5 volume 0.5
    show white_transparent
    diary "{=down_text}ในโลกที่มีการวิจัยดัดแปลงสิ่งมีชีวิตหรือที่เรียกกันว่ามิวแทนต์{/down_text}"
    diary "{=down_text}ได้ถูกสร้างและดัดแปลงโดยเหล่านักวิทยาศาสตร์{/down_text}"
    diary "{=down_text}แต่ด้วยความอยากรู้อยากเห็นพวกเขาได้ทำการทดลองกับร่างกายมนุษย์จริงๆ{/down_text}"
    diary "{=down_text}จนกระทั่งถูกรัฐบาลจับได้ว่าทำการทดลองกับมนุษย์{/down_text}"
    diary "{=down_text}จึงมีการบุกจับกุมยังห้องทดลอง{/down_text}"
    diary "{=down_text}ทว่า กลับไม่พบร่องรอยเหลืออยู่เลย เหลือเพียงความว่างเปล่า{/down_text}"
    diary "{=down_text}อีกทั้งยังไม่พบกับร่างของมนุษย์ผู้ที่ถูกดัดแปลงอีกด้วย{/down_text}"
    diary "{=down_text}ฝากแก่ทุกท่าน มิวแทนต์⬜⬜⬜เป็นอันตราย{/down_text}"
    diary "{=down_text}กรุณาจัดการ⬜⬜⬜มิวแทนต์ ถ้าเป็นไปได้{/down_text}"
    nvl clear
    play sound "<from 13 to 15>SFX/paper_sfx.mp3"
    hide white_transparent

    hide sd_wanted
    manager "นักวิทยาศาสตร์ชอบทดลองอะไรประหลาดๆ อยู่เรื่อย"
    manager "เห้ออ… นั่นคนเลยนะ เป็นมนุษย์เหมือนกันแท้ๆ"
    manager "แล้วข้อความสุดท้ายนั่นก็คือ… ให้ระวังมิวแทนต์ไว้เพราะเป็นอันตรายงั้นหรอ…… เอาเถอะคงไม่เกี่ยวกับฉันล่ะมั้ง…"
    window hide
    stop music fadeout 1.25
    play sound walking_sfx loop fadein 0.5
    scene bg4 with wipeleft
    scene bg4
    show chibi_1 at mildchibi
    with walkingVertical
    play music found_bgm loop fadein 2.0
    $ renpy.pause(2,modal=True)
    manager "เอ๊ะ? นั่นใครน่ะ???"
    play sound running_sfx loop fadein 0.25
    scene bg4 :
        crop (0,0,1920,1080)
        size (1920, 1080)
        linear 2.0 crop (550, 300, 1600, 1200)
    show chibi_1 at mildchibi:
        parallel:
            ypos 620
            xpos 980
            linear 2.0 align((0.5, 0.75))
        parallel:
            linear 2.0 zoom(1.2)

    with runningVertical
    $ renpy.pause(1.0,modal=True)
    stop sound
    scene black with dissolve
    scene bg4 :
        size (1920, 1080)
        crop (550, 300, 1600, 1200)
    show chibi_1 at truecenter:
        zoom 0.4
    with eye_open

    manager "เดี๋ยวสิ!!!"
    manager "คุณๆ เป็นอะไรรึป่าว?"

    hide chibi_1 with fade
    window show
    show chibi_2 at truecenter:
        zoom 0.6
    with dissolve

    manager "(เรียกแล้วไม่ตื่น จึงอุ้มขึ้นมา แอบเห็นแขนที่ลักษณะเป็นหลอดๆ มีน้ำชมพูๆอยู่ภายใน)"
    manager "ดะ เดี๋ยวก่อนนะ… นะ นี่คนคนนี้… หรือว่าจะเป็น มิวแทนต์ในข่าวนั้น… เอาไงดีถ้าพาไปโรงพยาบาลคนนี้จะเป็นอันตรายมั้ยนะ"
    manager "(ระหว่างที่อุ้ม ก็ยืนนิ่งคิดอยู่สักพัก)"
    manager "อ่ะ! จริงสิ พาไปที่ร้านของเราก่อนแล้วกันนะ ถ้าตื่นแล้วลองคุยดูก่อนละกัน" with sshake
    window hide
    play sound walking_sfx
    scene bg4:
        crop (0,0,1920,1080)
        size (1920, 1080)
        linear 2.0 crop (0, 250, 1280, 720)
    show chibi_2 at truecenter:
        align (0.5,-1.1)
        zoom 0.6
    with walkingVertical
    jump act1_1_shot_4

#Introduce Mild and Tsuru shot 4-5
label act1_1_shot_4:
    # Scene transition to the cafe
    play sound door_sfx fadein 0.25 volume 0.55
    scene bg2day
    play music cafe_bgm loop fadein 0.5
    show tsuru maid_idle2 at middlepostsuru
    show emotion_question at emotepos
    with fade
    tsuru "เอ้านั่นคุณผู้จัดการ ไปอุ้มใครมาคะเนี่ย"
    hide tsuru maid_idle2
    hide emotion_question
    show tsuru maid_dark_smile at middlepostsuru

    with dissolve
    "ซึรุได้หยิบมือถือขึ้นมาจากกระเป๋า"
    tsuru "เบอร์คุณตำรวจเบอร์อะไรน้า~"
    manager "ไม่ใช่ๆ"
    manager "หยุดเลยนะซึรุ ฉันไปเจอเขานอนสลบอยู่ข้างทางก่อนถึงร้านน่ะ"
    hide tsuru maid_dark_smile
    show tsuru maid_smile at middlepostsuru
    with dissolve
    manager "เอ้อ นี่ซึรุ เหมือนเขาจะเป็นมิวแทนต์นะ"
    show emotion_sparkle at emotepos
    hide tsuru maid_smile
    show tsuru maid_wow at middlepostsuru
    with dissolve
    tsuru "คะ"
    tsuru "ค๊าา!!! ตัวจริงหรอๆ หนูอยากเห็นจังเลยยย" with sshake
    manager "เดี๋ยวสิซึรุ บะ แบบว่าเห็นข่าวในใบปลิว บอกว่าอาจจะอันตราย เราควรระวังไว้ดีกว่ามั้ย"
    hide emotion_sparkle
    hide tsuru maid_wow
    show tsuru maid_idle2 at middlepostsuru
    show emotion_worried at emotepos
    with dissolve
    tsuru "คุณผู้จัดการไปได้ยินจากไหนคะ เขาก็มนุษย์คนนึงนะ อีกอย่างถ้าอันตรายขนาดนั้น\nก็คงจะมีตำรวจเดินไปเดินมาท๊างงง~วันแล้วสิ
    ดังนั้นอย่าพึ่งคิดอะไรไปก่อนเลยนะคะ เรามาหาวิธีช่วยก่อนดีกว่าค่ะ"
    hide emotion_worried
    with None
    show tsuru maid_idle2 at leftpostsuru
    with moveoutleft
    show mild hood_idle2 at mildhood
    show emotion_spiral at emotepairpos2
    with dissolve

    hooded_figure "งืม งั่ม น .§€÷สกsdากวkjบ"
    hide mild hood_idle2
    show mild hood_idle1 at mildhood
    show tsuru maid_wow at leftpostsuru
    with dissolve

    tsuru "คุณผู้จัดการ เขาพูดอะไรด้วยยย"
    hide mild hood_idle1
    show mild hood_scared at mildhood
    with dissolve
    hooded_figure "นะ น้ำ… ขะ ขอ… น้ำาา.."
    hide mild hood_scared
    show mild hood_idle1 at mildhood
    with dissolve
    show tsuru maid_angry at leftpostsuru
    hide emotion_spiral
    tsuru "คุณผู้จัดการ!" with sshake
    show emotion_angry at emotepairpos1
    tsuru "น้ำ!" with sshake
    hide emotion_angry
    show emotion_anger at emotepairpos1
    tsuru "ไปเอาน้ำมาสิค๊า!" with ashyShake
    manager "อะ โอเค!"
    manager "(ทำไมฉันเหมือนเป็นเด็กเสิร์ฟซะเองล่ะเนี่ย)"

    scene blackimage with fade
    pause 1.0
    $ renpy.pause(1,modal=True)

    scene bg2day
    with fade
    manager "อะนี่เอามาแล้ว"
    show milktea at truecenter
    "กลับมาพร้อมน้ำ 1 แก้ว ที่มีสีน้ำตาลอมแดงและมีกลิ่นหอมเฉพาะตัว "
    hide milktea
    show tsuru maid_idle1 at leftpostsuru
    show mild hood_idle1 at mildhood
    with dissolve
    show emotion_question at emotepairpos1
    tsuru "เอ๊~ อะเรรรรรรรร๊?…คุณผู้จัดการ.. ไม่มีน้ำเปล่าหรอคะ"
    manager "พอดีร้านน้ำที่สั่งไป เขายังไม่มาส่งน่ะ แต่อาการแบบนี้ฉันว่าให้ดื่มอะไรที่มีน้ำตาลน่าจะช่วยได้มากกว่านะ"
    hide emotion_question
    show tsuru maid_idle2 at leftpostsuru
    with dissolve
    manager "(เอาแก้วให้ดื่ม)"
    manager "อ่ะดื่มนี่สิ ดื่มอะไรหวานๆ น่าจะทำให้สดชื่นขึ้นนะ"
    hooded_figure "//ค่อยๆดื่มเข้าไป"
    show emotion_anger at emotepairpos2
    with lshake
    hooded_figure "//สะดุ้ง ฮู้ดที่คลุมเปิดออก"
    play sound glitter_sfx fadein 0.25
    queue sound heartbeat_sfx fadein 0.25 volume 0.5
    play music bright_bgm loop
    scene cg2:
        size(1920,1080)
    with Dissolve(2.0)
    $ renpy.pause(1.5, hard=True)
    with dissolve
    mild_nohood "อะ อร่อยยยยยย อะไรกันนี่น่ะะะ ความหวานมัน กลมกล่อม แล้วยังมีกลิ่นหอมเฉพาะ นี่คุณ! นี่น่ะมันเรียกกว่าอะไรหรอ!!!"
    manager "เป็นเมนูชานมสูตรพิเศษประจำร้าน มีชื่อว่า “ฮันนี่บราวน์ชูก้า!”"
    mild_nohood "ฉะ ฉัน อยากดื่มชานมทุกวันเลยค่ะ!"
    mild_nohood "//ดูดจนหมด"
    mild_nohood "อื้มมม ขอบคุณที่ช่วยฉันไว้นะคะ ชานมอร่อยมากเลยค่ะ"
    scene bg2day
    show tsuru maid_idle2 at leftpostsuru
    show emotion_worried at emotepairpos1
    show mild unhood_smile at mildhood
    with dissolve
    tsuru "ก็ดีแล้วที่เธอไม่เป็นอะไรนะ"
    hide emotion_worried
    show tsuru maid_idle1 at leftpostsuru
    with dissolve
    tsuru "//หันไปมองฮันนี่"
    show tsuru maid_smile at leftpostsuru
    with dissolve
    tsuru "คุณผู้จัดการทำไมทำหน้าตาแบบนั้นล่ะ"
    manager "ป ป่าว มะ ไม่มีอะไรหรอก" with sshake
    manager "(บ้าจริงน่ารักมากกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกก)"
    show emotion_celebrate at emotepairpos1
    tsuru "เอ๊~ ถ้าไม่มีอะไรทำไมหน้าแดงล่ะ"
    tsuru "//จ้องฮันนี่"
    manager "อ อ อ่ อ่ะ เอาเป็นว่า เธอไม่ได้กินอะไรเลยหรอ ถึงได้หมดสติอยู่แถวนี้น่ะ"
    stop music fadeout 2.0
    show mild unhood_idle1 at mildhood
    hide emotion_celebrate
    show tsuru maid_idle2 at leftpostsuru
    with dissolve
    mild_nohood "คือฉัน………"
    manager "อ่ะ ไม่ต้องห่วงนะ ที่นี่ไม่มีใครทำร้ายเธอหรอกนะ"
    mild_nohood "//พยักหน้า"
    scene black with dissolve
    centered "{=centered_text}ผ่านไปสักพัก ก็ยอมเล่าเหตุการณ์ที่เกิดขึ้น{/centered_text}"
    scene bg2day
    play music dark_bgm loop fadein 0.5
    show mild unhood_idle1 at mildunhood
    with fade
    mild_nohood "คือฉันเป็นตัวทดลอง ที่นักวิทยาศาสตร์จับมา
    ที่มาที่ไปชั้นก็ไม่รู้ค่ะ จำอะไรไม่ได้ รู้ตัวอีกทีก็คือตอนก่อนจะหลุดจากหลอดทดลองนั่นสักพักเท่านั้นค่ะ
    "
    show emotion_tear at emotepos
    with dissolve
    mild_nohood "ฉันที่ออกมาก็เตร็ดเตร่ไปตามทาง จนตกลงไป
    ในธารน้ำ ด้วยความที่ฉันไม่มีแรง เลยถูกกระแสน้ำพัดไป ตื่นมาอีกที ก็อยู่แถวๆ นี้
    "
    stop music fadeout 1.0
    hide emotion_tear with dissolve
    manager "เธอน่ะ รู้หรือเปล่าว่าข้างนอกห้องทดลอง เรามีกฎอยู่ว่า"
    play music bright_bgm loop fadein 1.0
    manager "\"ถ้าไม่มีเงินเราก็ไม่ได้กิน\" แล้วจะทำยังไงกับค่าชานมที่เธอกินไปดีนะเนี่ย . ."
    show mild unhood_scared at mildunhood
    show emotion_anger at hoodemote
    with dissolve
    mild_nohood "อะ เอ๊ะ ชะ ฉันก็คิดว่าคุณตั้งใจให้ซะอีก! ฉันไม่มีเงินหรอกนะคะ!"

    menu:
        "ไม่มีเงิน ก็จ่ายด้วยสิ่งนั้นสินะ":
            $ honey_score -= 1
            jump act1_1_shot_4_q1_c1

        "สนใจมาทำงานที่นี่มั้ย":
            $ honey_score += 1
            jump act1_1_shot_4_q1_c2


#choice from shot 5
label act1_1_shot_4_q1_c1:
    manager "ไม่มีเงิน ก็จ่ายด้วยสิ่งนั้นสินะ"
    show mild unhood_blushed at mildunhood
    hide emotion_anger
    with dissolve
    mild_nohood "ระ ร่างกาย"
    show mild unhood_blushed at mildhood
    with moveoutright
    show tsuru maid_dark_smile at leftpostsuru
    with moveinleft
    tsuru "คุณ ผู้-จัด-การรรร-ขาาา~  หนูเรียกตำรวจเลยละกันเนอะ"
    manager "ไม่ช่ายยยยย ฉันล้อเล่นนนนนนนนนนน หยุดก๊อนนนนซึรุ๊ววววววววววว"
    jump act1_1_shot_4_q1_c2

#choice from shot 5
label act1_1_shot_4_q1_c2:
    scene bg2day:
        crop (200,200,1280,720)
        size (1920, 1080)

    show mild unhood_blushed at mildunhood_close
    with dissolve
    manager "เธอสนใจมาทำงานที่นี่มั้ยล่ะ"
    hide emotion_anger
    show mild unhood_idle2 at mildunhood_close
    show emotion_question at hoodemote
    with dissolve
    mild_nohood "คะ???"
    manager "เธอยังไม่มีที่ไปใช่มั้ยล่ะ อีกอย่างถ้าจะทำงานคงจะยากเพราะร่างกายตอนนี้สินะ"
    mild_nohood "หมายความยังไงคะให้ฉันทำงานที่นี่ ได้หรอคะ"
    manager "อื้ม ได้สิ ที่นี่น่าจะช่วยให้เธอใช้ชีวิตได้อย่างไม่มีปัญหานะ มีเงินเดือนให้ สวัสดิการก็มี"
    manager "ที่สำคัญมีห้องให้นอนด้วยนะ แล้วก็....."
    show mild unhood_idle1 at mildunhood_close
    hide emotion_question
    with dissolve
    mild_nohood "ฉันเป็นมิวแทนต์... ไม่กลัวฉันหรอคะ?"
    mild_nohood "ฉันมันแปลกประหลาด... ในโลกใบนี้คนที่มีดวงตาเยอะขนาดนี้ก็คงมีแค่ฉัน....."
    manager "ต่อให้เธอจะมีกี่ตาก็ไม่สำคัญ ฉันที่มี 2 ตา ก็จะมีไว้มองแค่เธอคนเดียว"

    show mild unhood_blushed at mildunhood_close
    show emotion_love at hoodemote
    with dissolve

    manager "เธอจะเป็นยังไงก็ไม่มีปัญหาเลย ขอแค่เป็นเธอ"
    manager "เธอสนใจทำงานที่ร้านนี้รึป่าว?"

    hide emotion_love
    with dissolve
    pause 1.0
    scene bg2day
    show mild unhood_idle1 at mildhood
    show tsuru maid_smile1 at leftpostsuru
    show emotion_question at emotepairpos2
    with fade
    mild_nohood "คือ... ฉันยังไม่รู้เลยว่าที่นี่เป็นร้านแบบไหน.... ก็เลย..."
    tsuru "อ๋าาาา จริงด้วย!! คุณผู้จัดการนี่ล่ะก็ ไปชวนเขามาทำงาน แต่ไม่บอกอะไรเลยเนี่ยน้าาา"

    show tsuru maid_smile2 at leftpostsuru
    tsuru "ร้าน “ฮันนี่รีเวิร์ส” เป็นร้านบริการสไตล์ญี่ปุ่น คล้ายๆร้านเมดคาเฟ่ แต่ทางร้านเราจะมีการเพิ่มเรื่องของการ Roleplay เข้าไปด้วย!"
    tsuru "อย่างซึรุคุณผู้จัดการให้เล่นเป็นน้องสาวน่ะนะ"

    manager "ซึรุน่ะมีออร่าความเป็นน้องสาว ซุ่มซ่าม–"
    scene bg2day:
        crop (100,200,1280,720)
        size (1920, 1080)
    show tsuru maid_angry at tsuru_close
    tsuru "ซึรุไม่ได้ซุ่มซ่ามสักหน่อยยย!!"

    manager "จ้าๆ ขอโทดๆ ก็จะเป็นฉันที่อยู่ในครัว ส่วนสาวๆก็จะเป็นเด็กเสิร์ฟให้บริการลูกค้าน่ะ"

    scene bg2day
    show mild unhood_smile at mildhood
    show tsuru maid_angry at leftpostsuru
    with dissolve
    mild_nohood "แล้วตอนนี้มีแค่คุณกับคุณก้อนเมฆหรอคะ?"
    show tsuru maid_smile1 at leftpostsuru
    with dissolve
    tsuru "คะ คุณก้อนเมฆ? จะว่าไปเรายังไม่ได้แนะนำตัวกันเลยสินะ"
    show tsuru maid_smile2 at leftpostsuru
    with dissolve
    tsuru "อะฮุฮิฮุฮิ คุโมกุ ซึรูรุ เมดก้อนเมฆตัวน้อยยยที่น่ารักจากร้าน “ฮันนี่รีเวิร์ส” พร้อมที่จะมาให้บริการพี่ๆแล้วค่าาา"
    tsuru "เธอเรียกฉันว่า ซึรุ ได้เลยนะ"
    $ renpy.pause(1,modal=False)
    jump act1_1_shot_5

#shot 6 Introduction
label act1_1_shot_5:
    $ povname = renpy.input("ส่วนฉันชื่อ (กรอกชื่อของคุณ)")

    pov "ส่วนฉันชื่อ [povname] เป็นผู้จัดการของร้านนี้"
    pov "แล้วก็มีอีกคนนึง…"
    pov "ไว้รอเจอพรุ่งนี้แล้วกันนะ"
    scene bg2day:
        crop (400,200,1780,720)
        size (1920, 1080)
    show mild unhood_smile at mildunhood_close
    mild_nohood "ฉัน…. ได้รับชื่อมาว่า มายด์-อาร์(Mild-R) ค่ะ"
    mild  "เป็นชื่อที่แปะอยู่บนหลอดทดลองที่ฉันหลุดออกมา"
    pov "ถ้าอย่างงั้นยินดีที่ได้รู้จักนะมายด์  เธอจะช่วยมาทำงานที่ร้านของฉันหน่อยได้มั้ย"
    pov "ร้านของฉันขาดคนพอดี มีชุด มีที่พักอยู่ตรงข้ามห้องของฉัน"
    pov "แล้วเธอก็ไม่มีที่ไปใช่มั้ยล่ะ แถมถ้าเป็นร้านนี้ตัวเธอก็จะไม่ถูกสงสัยด้วยนะ"

    show mild unhood_idle1 at mildunhood_close
    show emotion_question at hoodemote
    with dissolve
    mild "// ยืนคิดอยู่สักพัก"
    mild "ฉะ ฉันอยู่ที่นี่ได้จริงๆใช่มั้ยคะ?"
    pov "แน่นอนสิ ทั้งฉันทั้งซึรุ ก็อยากช่วยรักษาหัวใจที่บอบช้ำของเธอนะ"
    scene bg2day:
        crop (100,200,1480,720)
        size (1920, 1080)
    show tsuru maid_smile at tsuru_close
    with dissolve
    tsuru "อื้มมมม มาทำงานด้วยกันนะ"
    show tsuru maid_smile1 at tsuru_close
    tsuru "เพื่อนเบิ้บบบ"
    scene bg2day
    show mild unhood_smile at mildhood
    show tsuru maid_smile1 at leftpostsuru
    with dissolve
    mild "ถะ ถ้างั้น…. ขอฝากตัวด้วยนะคะ"
    show tsuru maid_smile2 at leftpostsuru
    show emotion_celebrate at emotepairpos1
    with sshake
    tsuru "เย้! มีเพื่อนเพิ่มแย้วววว"
    hide emotion_celebrate
    pov "ไชโยวววววววววว ขอบคุณนะมายด์ ถ้างั้นลองใส่ชุดที่ร้านเลยดีมั้ย?" with lshake
    show tsuru maid_idle2 at leftpostsuru
    with dissolve
    tsuru "นั่นสิๆ ใส่ให้ดูเลยได้มั้ย ฉันว่ามันต้องเหมาะกับเธอแน่ๆเลยย"
    show mild unhood_idle2 at mildhood
    mild "ดะ ได้ค่ะ"
    tsuru "ทางนี้ๆ เดี๋ยวฉันพามายด์ไปแต่งตัวที่ห้องพักพนักงานเอง!"
    hide tsuru maid_idle2
    hide mild hood_idle2
    with moveoutleft
    stop music fadeout 3.5
    scene black
    with fade
    centered "{=centered_text}ผ่านไปสักพัก{/centered_text}"
    scene bg2day
    show tsuru maid_smile1 at leftpostsuru
    tsuru "เสร็จแล้วววว"
    play music maid_bgm loop fadeout 0.5 fadein 0.5
    show mild maid_flustered at rightposmild
    with moveinright

    pov "(นะ น่ารักเกินไปแล้ววว)"
    show tsuru maid_smile at leftpostsuru
    with dissolve
    tsuru "น่ารักมากกกกก ว่าแล้วเชียวว่ามายด์เหมาะกับสีเขียวชมพู"
    show emotion_tear at emotepairpos2
    mild "มะ ไม่ค่อยมั่นใจเลยค่ะ ฉันเปิดร่างกายให้เห็นแบบนี้จะไม่แปลกใช่มั้ยคะ"
    show tsuru maid_idle2 at leftpostsuru
    tsuru "ซึรุบอกแล้วไงมายด์ ว่าไม่ต้องพูดสุภาพน่ะ"
    hide emotion_tear
    show mild maid_idle1 at rightposmild
    with dissolve
    mild "อะ อื้อ"
    show tsuru maid_smile1  with dissolve
    tsuru "ผู้จัดการรรร เป็นงายยยยย มายด์ในชุดของร้านน่ะน่ารักม๊ายยยยย?"
    pov "มะ เหมาะมาก น่ารักสุดๆ เลย"
    show mild maid_flustered at rightposmild
    with dissolve
    mild "..."
    show mild maid_doubt at rightposmild
    show emotion_question at emotepairpos1
    tsuru "ใช่มั้ยล่าาา แล้วพี่ [pov] จะให้มายด์เล่นบทอะไรหรอ"

    pov "ฮื้ม... นั่นสินะยังไม่ได้ตัดสินใจเลย... เอ่อ"

    pov "เมด... เมด... น่ารัก..."
    show emotion_sparkle at emotepairpos2
    with fade
    play sound "<from 0.5 to 3.5>SFX/clock_sfx.mp3" fadein 0.5
    queue sound door_sfx fadein 0.25
    scene bg2day
    with dissolve
    pause 1.0
    show customer_shadow at center:
        ypos 1250
    with fade
    customer "สวัสดีค้าบบ"
    show customer_shadow at right:
        ypos 1250
    with moveinleft
    show tsuru maid_smile1 at leftpostsuru
    with dissolve
    tsuru "อะฮุฮิฮุฮิ สวัสดีค่าพี่ๆ ยินดีต้อนรับค่า เชิญนั่งที่โต๊ะได้เลยนะคะ"

    pov "นี่มายด์ วันนี้ก็ลองดูซึรุเป็นตัวอย่างไปก่อนนะ ฉันขอไปเข้าครัวก่อน"

    jump act1_1_shot_6

#shot 6 First Work
label act1_1_shot_6:
    stop music
    stop sound
    $ quick_menu = False
    play music minigame1_bgm loop fadein 1.0
    call screen tutorial()
    call screen minigame_1(minigame1_act1_1,force_lose = True)
    $ renpy.block_rollback()
    $ quick_menu = True

    scene bg2day with fade
    play music cafe_bgm loop fadein 0.5
    play sound  crowded_sfx fadein 0.5 volume 0.65
    "คนในร้านเริ่มเยอะ จนซึรุวิ่งรับลูกค้าไม่ไหว"
    show tsuru maid_idle2 at rightpostsuru
    with moveinleft
    hide tsuru maid_idle2
    with moveoutright
    show tsuru maid_idle2 at rightpostsuru
    with easeinright
    hide tsuru maid_idle2
    with moveoutleft
    show tsuru maid_idle2 at middlepostsuru
    with easeinleft
    hide tsuru maid_idle2
    with easeoutright
    show tsuru maid_idle2 at leftpostsuru
    with moveinright
    tsuru "พี่จ๋าๆ รับซอสมั้ยคะ เอารูปอะไรดีเอ่ย"
    hide tsuru maid_idle2
    with easeoutright

    pov "ข้าวผัดได้แล้ววววววววว" with sshake
    stop sound fadeout 1.5
    scene bg2day:
        crop (0,240,960,820)
        size (1920, 1080)
    show mild maid_doubt at leftposmild
    with easeinleft
    mild "//เดินมาหาคุณที่ครัว"
    show emotion_question at emotepairpos1
    mild "คุณ [povname] คะ มีอะไรที่ฉันช่วยได้มั้ยคะ…"

    pov "ช่วยเก็บโต๊ะ...… ไม่สิไม่เป็นไร-"
    hide emotion_question with dissolve
    hide mild maid_doubt with easeoutright
    pov "(ไม่ทันจะได้พูดจบ มายด์ก็เดินไปเก็บโต๊ะ)"
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)

    "ระหว่างที่มายด์ช่วยเก็บโต๊ะอยู่สักพักนั้นเอง"
    show mild maid_idle1 at middleposmild
    with dissolve

    customer "คุณเมดครับบบ ขอออเดอร์หน่อยค้าบบ"

    show mild maid_flustered at middleposmild
    show emotion_tear at emotepos
    with dissolve
    mild "//ตกใจเล็กน้อยพร้อมสีหน้าที่เป็นกังวล" with sshake
    mild "ค-ค่ารับอะไรดีคะ"

    customer "เอา ฮันนี่บราวน์ชูก้า 1 แก้ว แล้วก็ออมไรซ์ 1 ที่ครับ"
    hide emotion_tear
    mild "ระ-รับทราบค่ะ ฮันนี่บราวน์ชูก้า 1 แก้ว แล้วก็ออมไรซ์ 1 ที่"
    hide mild maid_idle1 with easeoutleft
    scene bg2day:
        crop (0,240,960,820)
        size (1920, 1080)
    with wiperight
    show mild maid_idle1 at middleposmild
    with easeinright
    mild "//เดินมาที่เค้าเตอร์ครัว"
    mild "เอ่อคือว่า ฮันนี่บราวน์ชูก้า กับ ออมไรซ์ อย่างละ 1 ค่ะ"

    pov "ได้เลยยยยยยยยยยยยยยย" with sshake

    show mild maid_doubt at middleposmild
    show emotion_anger at emotepos
    mild "//มายด์อาร์ยืนมอง [povname] ที่กำลังทำงาน เธอตกตะลึงในความสามารถในการทำอาหารของ [povname]"
    mild "(ทั้งท่าทางในการผัด ทอดและปรุง ที่แสดงถึงความใส่ใจและความปราณีต ของ [povname] ที่กำลังทำอาหารอยู่ข้างหน้าเตาในขณะนี้นั้นดูเท่อย่างมากในสายตาของเธอ)"

    pov "ฮันนี่บราวน์ชูก้า กับ ออมไรซ์ อย่างละ 1 เสร็จแล้ว!" with sshake
    hide emotion_anger
    show mild maid_flustered at middleposmild

    mild "ค-ค่า"
    hide mild maid_doubt with easeoutright
    scene bg2day:
        crop (400,240,1280,720)
        size (1920, 1080)
    show mild maid_idle2 at middleposmild
    show omurice at omu
    with easeinleft

    mild "ฮันนี่บราวน์ชูก้า กับ ออมไรซ์ ได้แล้วค่า รับซอสด้วยมั้ยคะ?"

    customer "รับค้าบบบ"
    show mild maid_idle1 at middleposmild
    hide omurice
    with dissolve
    mild "เอารูปอะไรดีคะ?"

    customer "เอาตามที่คุณเมดอยากวาดให้ได้เลยคับ"
    show mild maid_idle2 at middleposmild
    with dissolve
    mild "รับทราบค่า"
    show omurice_red at truecenter
    with fade
    mild "เรียบร้อยค่ะ"

    customer "คะ คุณเมดวาดรูปอะไรครับเนี่ย"
    show emotion_tear at emotepos
    show omurice_red at omu
    show mild maid_blush2 at middleposmild
    with dissolve
    mild "อ่าา หมีค่า… คือฉันพึ่งเริ่มทำงานเลยยังไม่ค่อยเก่งขอโทษด้วยนะคะ"

    customer "อะ เฮื้อกกกกก น่ารักกกกกกกกกกกกก"

    customer "คะ คือว่าาา คุณเมดชื่ออะไรหรอครับ!!"
    hide emotion_tear
    show mild maid_idle2 at middleposmild
    hide omurice_red
    with dissolve
    mild "ชื่อ มายด์อาร์ ค่ะ ขอฝากตัวด้วยนะคะ…."
    mild "(เอ๊ะ แล้วเราต้องเรียกคุณลูกค้าว่าอะไรดีล่ะ จะเรียกพี่ๆแบบซึรุก็ไม่ได้สินะ ถะ ถ้างั้น)"
    show mild maid_heart at middleposmild
    show emotion_love at emotepos
    mild "ฮะ... ฮันนี่"

    mild "งะ งั้นทานให้อร่อยนะคะ มายฮันนี่"
    hide emotion_love
    show mild maid_idle1 with dissolve
    pause 0.5
    hide mild maid_idle1 with easeoutleft
    "หลังจากมายด์เสิร์ฟลูกค้าโต๊ะนี้ มายด์ไม่รู้เลยว่าตัวเองได้มีแฟนคลับไปซะแล้ว"
    stop music fadeout 0.5
    $ quick_menu = False
    play music minigame2_bgm loop fadein 1.0
    call screen minigame_1(minigame1_act1_1_2)
    $ renpy.block_rollback()
    $ quick_menu = True
    scene black
    with dissolve
    centered "{=centered_text}แล้วเวลาก็ล่วงเลยผ่านไปจนกระทั่งถึงเวลาปิดร้าน{/centered_text}"
    jump act1_1_shot_7

#shot7 End of work
label act1_1_shot_7:
    play music night_bgm loop fadein 0.5
    scene bg2night
    with fade
    show mild maid_wave at middleposmild
    with dissolve
    mild "อะ อะริกาโตะโกไซมัส ขอบคุณที่มาใช้บริการค่ะ แล้วพรุ่งนี้แวะมาอีกนะคะ"
    show mild maid_stunned at middleposmild
    with dissolve
    show tsuru maid_smile at middlepostsuru
    with moveinright
    hide mild maid_stunned
    hide tsuru maid_smile
    with moveoutleft
    tsuru "มายยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยยด์!!!!!!" with lshake
    show mildru_sd_1 at truecenter:
        zoom 0.7
    with fade
    tsuru "สุดยอดเลยยยยยยยยยยย วันแรกก็ทำได้ดีขนาดนี้เลยนะะะะะะ เก่งมากกกก"
    pov "จริงงง เธอทำได้ดีมากเลย การใส่ใจ การตกลูกค้า เธอทำได้ดีเลยนะ"
    hide mildru_sd_1
    show mildru_sd_2 at truecenter:
        zoom 0.7
    with dissolve
    mild "ตะ แต่ว่าฉันยัง คิดว่ายังทำได้ไม่ดีเท่าไหร่…"
    hide mildru_sd_2
    show mildru_sd_1 at truecenter:
        zoom 0.7
    with dissolve
    pov "ไม่หรอกซึรุเองก็สักพักเลยแหละกว่าจะลงตัวได้"
    tsuru"อื้มๆ เธอทำได้ดีจริงๆนะไม่ต้องห่วงง จากนี้ยังมีเวลาพัฒนาอีกเยอะเลย ค่อยๆเป็นค่อยๆไปกันนะ"
    hide mildru_sd_1
    show mildru_sd_2 at truecenter:
        zoom 0.7
    with dissolve
    mild "ขะ ขอบคุณนะคะ จากนี้ก็ฝากตัวด้วยนะ"
    pov "ฉันก็ด้วยนะ เอาละ งั้นเราไปดูห้องเธอกันเลยมั้ย"
    scene bg2night:
        crop (100,200,1480,720)
        size (1920, 1080)
    show mild maid_idle2 at mild_close
    show emotion_love at emoteclose
    with dissolve
    mild "ค-ค่ะ"

    scene black
    with fade
    scene bg5moon
    with walkingVertical
    scene bg6night
    with wiperight
    play music mildroom_bgm loop fadein 0.5
    pov "เอาเป็นว่าเธออยู่ห้องนี้แก้ขัดก่อน เธอขัดข้องตรงไหนรึป่าว?"
    show mild maid_doubt at middleposmild
    show emotion_question at emotepos
    with dissolve
    mild "มะ ไม่เลยค่ะ แต่ว่าฉันสงสัยอย่างนึงค่ะ…"

    pov "อื้มม..ว่าไงถามมาได้เลยนะ ฉันฟังอยู่"
    show mild maid_idle1 at middleposmild
    hide emotion_question
    with dissolve
    mild "คะ คือว่าห้องนี้มันแปลกนิดหน่อยค่ะ… มีเฟอร์นิเจอร์อยู่ครบเลย…"

    pov "อ๋อนี่เป็นห้องของญาติฉันเองแหละ แต่ว่าเค้าต้องไปดูแลกิจการอีกสาขาที่ต่างจังหวัด ก็เลยไม่ค่อยได้กลับมาใช้ห้องนี้แล้วน่ะ"
    pov "(พอดีว่าเขาต้องไปดูแลอีกสาขาน่ะ ก็เลยไม่ค่อยได้กลับมาใช้ห้องนี้แล้ว)"
    show mild maid_flustered at mild_close
    show emotion_stressed at emotepos
    with dissolve
    mild "มันจะ ดะ ดีจริงๆ หรอคะ…"

    pov "เธอทำตัวตามสบายได้เลย"
    pov "//ยิ้มหวาน"
    hide emotion_stressed
    show mild maid_idle2 at mild_close
    with dissolve
    mild "ขะ ขอบคุณจริงๆนะคะ คุณ [povname]"

    pov "จะว่าไปอย่าเรียกฉันว่า คุณจะได้มั้ย เรียกแค่ชื่อของฉันก็พอ"
    pov "ไหนเรียกซิ~ [povname]"
    show mild maid_flustered at mild_close
    mild "คะ-คุณ มะ ไม่สิ [povname] ค่ะ….. // .//////. เขิลอาย"

    pov "อื้มม ขอบคุณมากนะมายด์"
    pov "//มองมายด์แล้วพึ่งนึกได้ว่ามายด์ยังไม่มีชุดใส่"
    pov "จริงด้วยสิ มายด์ ในตู้เสื้อผ้านั่น มีเสื้อผ้าของญาติฉันอยู่ เธอเอาไปใส่ได้เลยนะ แบบนั้นฉันจะขอบคุณมากเลย"
    show mild maid_doubt at mild_close
    show emotion_question at emoteclose
    with dissolve
    mild "ฉะ ฉันใส่ได้หรอคะ?!"

    pov "อื้มม แน่นอน"
    hide emotion_question

    menu:
        "เธอใส่ชุดของญาติได้เลยนะ เธอใส่ได้ตามสบายเลย":
            $ honey_score += 1
            pov "เธอใส่ชุดของญาติได้เลยนะ เธอใส่ได้ตามสบายเลย"

        "หรือจะใส่เสื้อฉันก่อนดีละ":
            $ honey_score -= 1
            pov "หรือจะใส่เสื้อฉันก่อนดีละ"
            show mild maid_flustered at mild_close
            with dissolve
            mild "มะ ไม่เป็นไรค่าาาา!"
    show mild maid_flustered at mild_close
    show emotion_stressed at emotepos
    with dissolve
    pov "เธอไม่ต้องเกรงใจฉันหรอกน่า"
    hide emotion_stressed
    pov "เธอไปอาบน้ำ เปลี่ยนเสื้อผ้า นอนเถอะ"
    show mild maid_idle2 at mild_close
    with dissolve
    mild "ขะ ขอบคุณค่ะ"

    scene bg7light
    with fade
    play music diary_bgm loop fadein 1.0
    show diary
    pov "(หลังจากที่แยกย้ายกัน ฉันที่อาบน้ำอะไรเรียบร้อย ก็ได้มานั่งเขียนไดอารี่ประจำวัน ถึงจะเขียนบ้างไม่ได้เขียนบ้าง แต่ก็ช่วยให้จดจำเรื่องราวที่ผ่านมาในชีวิตได้ดี)"
    show brown_transparent
    nvl clear
    diary "ถึงไดอารี่ วันนี้มีเรื่องราวเกิดขึ้นด้วยล่ะ"
    diary "นั่นก็คือ ฉันได้พนักงานใหม่แล้ว เธอเป็นเด็กผู้หญิงที่น่ารัก"
    diary "มีออร่าบางอย่างที่ทำให้ฉันต้องหันไปมองทุกที ไม่รู้เหมือนกันว่าทำไม"
    diary "แต่โดยรวมแล้วการที่ได้เธอมาช่วยในร้านก็ทำให้หลายๆอย่างดีขึ้น"
    diary "รวมทั้งบรรยากาศใหม่ๆในร้านก็ดีขึ้นด้วย"
    diary "หวังว่าจากนี้จะได้มีความทรงจำที่ดีกับเธอไปเรื่อยๆเลยนะ ส่วนงานในร้านวันนี้.."
    nvl clear
    hide diary
    hide brown_transparent
    play sound cry_sfx fadein 0.5 volume 0.35
    pov "(ระหว่างที่ฉันเขียนไดอารี่เกิดเสียงบางอย่างที่ แปลกประหลาด ทำให้ฉันต้องชะงักจากการเขียนไดอารี่ เสียงบางอย่างที่คล้ายกับเสียงคนร้องไห้ ทรมานด้วยเจ็บปวดอย่างน่าหดหู่)"
    pov "มะ ไม่มั้ง เอาเป็นว่าฉันเขียนไดอารี่แค่นี้ก่อนละกันนะ ไปนอนดีกว่า อะแหะๆๆ…"
    scene bg7night
    with dissolve
    stop sound
    stop music
    scene black with eye_shut
    pov "(หลังจากนั้นฉันก็คลุมโปงทั้งคืนจนหลับไป ...)"
    scene black
    with fade
    stop music
    jump act1_2_shot_1