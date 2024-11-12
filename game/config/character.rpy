init python:
    manager = Character("ฮันนี่",color="#88483b")
    pov = Character("[povname]",color="#88483b")
    hooded_figure = Character("ร่างสวมฮู้ด",color="#afefdb")
    mild_nohood = Character("หญิงสวมฮู้ด",color="#afefdb")
    mild = Character("มายด์",color="#afefdb")
    mild_nvl = Character("มายด์",kind=nvl,color="#afefdb")
    del_nvl = Character("เดบิรุน",kind=nvl,color="#433ed5")
    tsuru = Character("ซึรุรุ",color="#4ddbf4")
    tsuru_pov = Character("{color=#4ddbf4}ซึรุรุ{/color} & {color=#88483b}[povname]{/color}")
    tsuru_debirun = Character("{color=#4ddbf4}ซึรุรุ{/color} & {color=#433ed5}เดบิรุน{/color}")
    unknow_debirun = Character("???",color="#433ed5")
    debirun = Character("เดบิรุน",color="#433ed5")
    mild_debirun = Character("{color=#afefdb}มายด์{/color} & {color=#433ed5}เดบิรุน{/color}")
    mild_tsuru_debirun = Character("{color=#afefdb}มายด์{/color} & {color=#4ddbf4}ซึรุ{/color} & {color=#433ed5}เดบิรุน{/color}")
    pov_tsuru_debirun = Character("{color=#88483b}[povname]{/color} & {color=#4ddbf4}ซึรุ{/color} & {color=#433ed5}เดบิรุน{/color}")
    diary = nvl_narrator
    ami = Character("บุคคลปริศนา2",color="#e3f5f5")
    ashy = Character("บุคคลปริศนา1",color="#ea6e2f")
    customer = Character("ลูกค้า",color="#8e8f92")
    employee = Character("พนักงาน",color="#484646")
    researcher = Character("นักวิจัย",color="#f7f7f7")
    pixchan = Character("ลูกค้า1",color="#f05f9e")
    zoulfia = Character("ลูกค้า2",color="#698dac")
    other = Character("คนรอบๆ",color="#8e8f92")
    restaurant_staff = Character("พนักงานร้านอาหาร",color="#484646")

## Sprite #####################################################################
# Mild-R Hood
image mild hood_idle1 = "images/character/Mild-R/Mild Hood Idle 1.png"
image mild hood_idle2 = "images/character/Mild-R/Mild Hood Idle 2.png"
image mild hood_scared = "images/character/Mild-R/Mild Hood.png"

# Mild-R Unhood
image mild unhood_idle1 = "images/character/Mild-R/Mild Unhood Idle 1.png"
image mild unhood_idle2 = "images/character/Mild-R/Mild Unhood Idle 2.png"
image mild unhood_blushed = "images/character/Mild-R/Mild Unhood blushed.png"
image mild unhood_sad = "images/character/Mild-R/Mild Unhood Sad.png"
image mild unhood_scared = "images/character/Mild-R/Mild Unhood Scared.png"
image mild unhood_smile = "images/character/Mild-R/Mild Unhood Smile.png"
image mild unhood_blush2 = "images/character/Mild-R/mild_unhood_blush_2.png"
image mild unhood_blush3 = "images/character/Mild-R/mild_unhood_blush_3.png"
image mild unhood_blush4 = "images/character/Mild-R/mild_unhood_blush_4.png"
image mild unhood_blush5 = "images/character/Mild-R/mild_unhood_blush_5.png"
image mild unhood_flustered = "images/character/Mild-R/mild_unhood_flustered.png"
image mild unhood_gloomy2 = "images/character/Mild-R/mild_unhood_gloomy_2.png"
image mild unhood_scared2 = "images/character/Mild-R/mild_hood_au_eo_mo.png"

# Mild-R Maid
image mild maid_idle1 = "images/character/Mild-R/Mild Maid Idle.png"
image mild maid_idle2 = "images/character/Mild-R/Mild Maid Idle 2.png"
image mild maid_idle3 = "images/character/Mild-R/mild_maid_idle_2_2.png"
image mild maid_idle4 = "images/character/Mild-R/mild_maid_idle_2_1.png"
image mild maid_wave = "images/character/Mild-R/Mild Maid Wave.png"
image mild maid_doubt = "images/character/Mild-R/Mild Maid Doubt.png"
image mild maid_flustered = "images/character/Mild-R/Mild Maid Flustered.png"
image mild maid_heart = "images/character/Mild-R/Mild Maid Heart.png"
image mild maid_stunned = "images/character/Mild-R/Mild Maid Stunned.png"
image mild maid_blush1 = "images/character/Mild-R/mild_maid_blush_p1.png"
image mild maid_blush2 = "images/character/Mild-R/mild_maid_blush_p2.png"
image mild maid_grumpy = "images/character/Mild-R/mild_maid_grumpy.png"
image mild maid_smile1 = "images/character/Mild-R/mild_maid_smile_au_ec_mc.png"
image mild maid_smile2 = "images/character/Mild-R/mild_maid_idle_2_3.png"
image mild maid_smile3 = "images/character/Mild-R/mild_maid_smile_1_2.png"
image mild maid_smile4 = "images/character/Mild-R/mild_maid_smile_au_em_mc.png"
image mild maid_smile5 = "images/character/Mild-R/mild_maid_smile_2_1.png"
image mild maid_smile6 = "images/character/Mild-R/mild_maid_smile_2_2.png"
image mild maid_smile7 = "images/character/Mild-R/mild_maid_smile_2_3.png"
image mild maid_smile8 = "images/character/Mild-R/mild_maid_smile_2_4.png"
image mild maid_smile9 = "images/character/Mild-R/mild_maid_smile_2_6.png"
image mild maid_smile10 = "images/character/Mild-R/mild_maid_smile_3_1.png"
image mild maid_smile11 = "images/character/Mild-R/mild_maid_smile_3_2.png"
image mild maid_sorry = "images/character/Mild-R/mild_maid_sorry.png"

#Mild-R pajamas
image mild pajamas_angry1 = "images/character/Mild_Paja/mild_pajamas_angry_1.png"
image mild pajamas_angry2 = "images/character/Mild_Paja/mild_pajamas_angry_2.png"
image mild pajamas_biao = "images/character/Mild_Paja/mild_pajamas_biao.png"
image mild pajamas_cooldere = "images/character/Mild_Paja/mild_pajamas_cooldere.png"
image mild pajamas_doubt = "images/character/Mild_Paja/mild_pajamas_doubt.png"
image mild pajamas_flustered1 = "images/character/Mild_Paja/mild_pajamas_flustered_1.png"
image mild pajamas_flustered2 = "images/character/Mild_Paja/mild_pajamas_flustered_2.png"
image mild pajamas_grumpy = "images/character/Mild_Paja/mild_pajamas_grumpy.png"
image mild pajamas_idle1 = "images/character/Mild_Paja/mild_pajamas_idle_1.png"
image mild pajamas_idle2= "images/character/Mild_Paja/mild_pajamas_idle_2_1.png"
image mild pajamas_idle3 = "images/character/Mild_Paja/mild_pajamas_idle_2_2.png"
image mild pajamas_shock = "images/character/Mild_Paja/mild_pajamas_shock.png"
image mild pajamas_sleep = "images/character/Mild_Paja/mild_pajamas_sleep.png"
image mild pajamas_smile1 = "images/character/Mild_Paja/mild_pajamas_smile_1.png"
image mild pajamas_smile2 = "images/character/Mild_Paja/mild_pajamas_smile_2.png"
image mild pajamas_smile3 = "images/character/Mild_Paja/mild_pajamas_smile_3.png"
image mild pajamas_smile4 = "images/character/Mild_Paja/mild_pajamas_smile_4.png"
image mild pajamas_smile5 = "images/character/Mild_Paja/mild_pajamas_smile_5.png"
image mild pajamas_smile6 = "images/character/Mild_Paja/mild_pajamas_smile_6.png"
image mild pajamas_smile7 = "images/character/Mild_Paja/mild_pajamas_smile_7.png"
image mild pajamas_smile8 = "images/character/Mild_Paja/mild_pajamas_smile_8.png"
image mild pajamas_sorry = "images/character/Mild_Paja/mild_pajamas_sorry.png"
image mild pajamas_stunned = "images/character/Mild_Paja/mild_pajamas_stunned.png"
image mild pajamas_tsundere = "images/character/Mild_Paja/mild_pajamas_tsudere.png"

#Mild-R Normal
image mild normal_blush1 = "images/character/Mild_Normal/mild_normal_blush_1.png"
image mild normal_blush2 = "images/character/Mild_Normal/mild_normal_blush_2.png"
image mild normal_doubt = "images/character/Mild_Normal/mild_normal_doubt.png"
image mild normal_flustered = "images/character/Mild_Normal/mild_normal_flustered.png"
image mild normal_idle1 = "images/character/Mild_Normal/mild_normal_idle_1.png"
image mild normal_idle2 = "images/character/Mild_Normal/mild_normal_idle_2_1.png"
image mild normal_idle3 = "images/character/Mild_Normal/mild_normal_idle_2_2.png"
image mild normal_shock = "images/character/Mild_Normal/mild_normal_shock.png"
image mild normal_sleep = "images/character/Mild_Normal/mild_normal_sleep.png"
image mild normal_smile1 = "images/character/Mild_Normal/mild_normal_smile_1_1.png"
image mild normal_smile2 = "images/character/Mild_Normal/mild_normal_smile_1_2.png"
image mild normal_smile3 = "images/character/Mild_Normal/mild_normal_smile_1_3.png"
image mild normal_smile4 = "images/character/Mild_Normal/mild_normal_smile_1_4.png"
image mild normal_smile5= "images/character/Mild_Normal/mild_normal_smile_1_5.png"
image mild normal_smile6 = "images/character/Mild_Normal/mild_normal_smile_1_6.png"
image mild normal_smile7 = "images/character/Mild_Normal/mild_normal_smile_2_1.png"
image mild normal_smile8 = "images/character/Mild_Normal/mild_normal_smile_2_2.png"
image mild normal_smi10 = "images/character/Mild_Normal/mild_normal_smile_2_4.png"
image mild normal_smile11 = "images/character/Mild_Normal/mild_normal_smile_2_5.png"
image mild normal_smile12 = "images/character/Mild_Normal/mild_normal_smile_3_1.png"
image mild normal_smile13 = "images/character/Mild_Normal/mild_normal_smile_3_2.png"

## Tsuru Maid
image tsuru maid_idle1 = "images/character/Tsu_maid/Tsuru Maid Idle 1.png"
image tsuru maid_idle2 = "images/character/Tsu_maid/Tsuru Maid Idle 2.png"
image tsuru maid_angry = "images/character/Tsu_maid/Tsuru Maid Angry.png"
image tsuru maid_dark_smile = "images/character/Tsu_maid/Tsuru Maid Dark Smile.png"
image tsuru maid_smile1 = "images/character/Tsu_maid/Tsuru Maid Smile 1_1.png"
image tsuru maid_smile2 = "images/character/Tsu_maid/Tsuru Maid Smile 2_1.png"
image tsuru maid_smile3 = "images/character/Tsu_maid/Tsuru Maid Smile 1_2.png"
image tsuru maid_smile4 = "images/character/Tsu_maid/Tsuru Maid Smile 2_2.png"
image tsuru maid_smile5 = "images/character/Tsu_maid/Tsuru Maid Smile 1_3.png"
image tsuru maid_smile6 = "images/character/Tsu_maid/Tsuru Maid Smile 2_3.png"
image tsuru maid_shocked = "images/character/Tsu_maid/Tsuru Maid Shocked.png"
image tsuru maid_smile = "images/character/Tsu_maid/Tsuru Maid Grin.png"
image tsuru maid_wow = "images/character/Tsu_maid/Tsuru Maid Wow.png"
image tsuru maid_frog1 = "images/character/Tsu_maid/tsururu_maid_smile_1_frog.png"
image tsuru maid_frog2 = "images/character/Tsu_maid/tsururu_maid_smile_2_frog.png"
image tsuru maid_frog3 = "images/character/Tsu_maid/tsururu_maid_smile_4_frog.png"
image tsuru maid_frog4 = "images/character/Tsu_maid/tsururu_maid_smile_5_frog.png"
image tsuru maid_drunk1 = "images/character/Tsu_maid/tsururu_maid_smile_1_drunk.png"
image tsuru maid_drunk2 = "images/character/Tsu_maid/tsururu_maid_smile_2_drunk.png"
image tsuru maid_drunk3 = "images/character/Tsu_maid/tsururu_maid_smile_4_drunk.png"
image tsuru maid_drunk4 = "images/character/Tsu_maid/tsururu_maid_idle_2_drunk.png"

## Tsuru Normal
image tsuru normal_abuse_ec = "images/character/Tsu_Normal/tsuru_normal_abuse_ec.png"
image tsuru normal_crying = "images/character/Tsu_Normal/tsuru_normal_crying.png"
image tsuru normal_doubt = "images/character/Tsu_Normal/tsuru_normal_doubt.png"
image tsuru normal_grumpy1 = "images/character/Tsu_Normal/tsuru_normal_grumpy_1.png"
image tsuru normal_grumpy2 = "images/character/Tsu_Normal/tsuru_normal_grumpy_2.png"
image tsuru normal_idle1 = "images/character/Tsu_Normal/tsuru_normal_idle_1.png"
image tsuru normal_idle1_1 = "images/character/Tsu_Normal/tsuru_normal_idle_2_1.png"
image tsuru normal_idle1_2 = "images/character/Tsu_Normal/tsuru_normal_idle_2_2.png"
image tsuru normal_idle2_1 = "images/character/Tsu_Normal/tsuru_normal_idle_2_ec_1.png"
image tsuru normal_idle2_2 = "images/character/Tsu_Normal/tsuru_normal_idle_2_ec_2.png"
image tsuru normal_smile1 = "images/character/Tsu_Normal/tsuru_normal_smile_1.png"
image tsuru normal_smile2 = "images/character/Tsu_Normal/tsuru_normal_smile_2.png"
image tsuru normal_smile3 = "images/character/Tsu_Normal/tsuru_normal_smile_3.png"
image tsuru normal_smile4 = "images/character/Tsu_Normal/tsuru_normal_smile_4.png"
image tsuru normal_smile5 = "images/character/Tsu_Normal/tsuru_normal_smile_5.png"
image tsuru normal_smile6 = "images/character/Tsu_Normal/tsuru_normal_smile_6.png"
image tsuru normal_smug = "images/character/Tsu_Normal/tsuru_normal_smug.png"
image tsuru normal_sorry = "images/character/Tsu_Normal/tsuru_normal_sorry.png"
image tsuru normal_stunned = "images/character/Tsu_Normal/tsuru_normal_stunned.png"
image tsuru normal_dark = "images/character/Tsu_Normal/tsuru_normal_grumpy_2_1.png"

## Debirun Maid
image del maid_abuse = "images/character/Del_maid/del_maid_abuse.png"
image del maid_crying = "images/character/Del_maid/del_maid_crying.png"
image del maid_doubt = "images/character/Del_maid/del_maid_doubt.png"
image del maid_gloomy1 = "images/character/Del_maid/del_maid_groomy_1.png"
image del maid_gloomy2 = "images/character/Del_maid/del_maid_groomy_2.png"
image del maid_idle1 = "images/character/Del_maid/del_maid_idle_1.png"
image del maid_idle2 = "images/character/Del_maid/del_maid_idle_2.png"
image del maid_shock = "images/character/Del_maid/del_maid_shock.png"
image del maid_smile1 = "images/character/Del_maid/del_maid_smile_1.png"
image del maid_smile2 = "images/character/Del_maid/del_maid_smile_2.png"
image del maid_smile3 = "images/character/Del_maid/del_maid_smile_3.png"
image del maid_smile4 = "images/character/Del_maid/del_maid_smile_4.png"
image del maid_smile5 = "images/character/Del_maid/del_maid_smile_5.png"
image del maid_smile6 = "images/character/Del_maid/del_maid_smile_6.png"
image del maid_stunned = "images/character/Del_maid/del_maid_stunned.png"
image del maid_wave = "images/character/Del_maid/del_maid_wave.png"

## Debirun Normal
image del normal_abuse1 = "images/character/Del_Normal/del_normal_abuse_1.png"
image del normal_abuse2 = "images/character/Del_Normal/del_normal_abuse_2.png"
image del normal_police = "images/character/Del_Normal/del_normal_call_police.png"
image del normal_crying1 = "images/character/Del_Normal/del_normal_crying_1.png"
image del normal_crying2 = "images/character/Del_Normal/del_normal_crying_2.png"
image del normal_doubt1 = "images/character/Del_Normal/del_normal_doubt_1.png"
image del normal_doubt2 = "images/character/Del_Normal/del_normal_doubt_2.png"
image del normal_gloomy1 = "images/character/Del_Normal/del_normal_gloomy_1.png"
image del normal_gloomy2 = "images/character/Del_Normal/del_normal_gloomy_2.png"
image del normal_gloomy3 = "images/character/Del_Normal/del_normal_gloomy_3.png"
image del normal_idle1 = "images/character/Del_Normal/del_normal_idle_1.png"
image del normal_idle2 = "images/character/Del_Normal/del_normal_idle_2.png"
image del normal_smile1 = "images/character/Del_Normal/del_normal_smile_1.png"
image del normal_smile2 = "images/character/Del_Normal/del_normal_smile_2.png"
image del normal_smile3 = "images/character/Del_Normal/del_normal_smile_3.png"
image del normal_smile4 = "images/character/Del_Normal/del_normal_smile_4.png"
image del normal_smile5 = "images/character/Del_Normal/del_normal_smile_5.png"
image del normal_smile6 = "images/character/Del_Normal/del_normal_smile_6.png"
image del normal_smile7 = "images/character/Del_Normal/del_normal_smile_7.png"
image del normal_smile8 = "images/character/Del_Normal/del_normal_smile_8.png"
image del normal_smile9 = "images/character/Del_Normal/del_normal_smile_9.png"
image del normal_sorry = "images/character/Del_Normal/del_normal_sorry.png"
image del normal_stunned1 = "images/character/Del_Normal/del_normal_stunned_1.png"
image del normal_stunned2 = "images/character/Del_Normal/del_normal_stunned_2.png"