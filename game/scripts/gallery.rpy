define config.enter_replay_transition = Fade(0.5, 0.5, 0.5)
define config.exit_replay_transition = Fade(0.5, 0.5, 0.5)
define config.after_replay_callback = stop_replay_music

init -1 python:
    def stop_replay_music():
        renpy.music.play("audio/music/80s_menucut.mp3", loop=True, fadeout=2.0)


default persistent.gallery_name = "Connor"







label setup_gallery:
    if lain_mod and _in_replay:
        $ mc_name = persistent.gallery_name
        $ mc = Character(persistent.gallery_name)
    return
















screen scene_gallery():
    tag menu
    modal True
    add "gallery/7.png"
    text "Scene Gallery" style "title"





    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Return()

    default isabel_unlocked = renpy.seen_label("i_ns_touchtits_dialogue") or renpy.seen_label("i_ns_jerkoff_dialogue") or renpy.seen_label("i_ns_usehand_dialogue") or renpy.seen_label("isabel_1_homedrinkingisabel_dialogue")

    style_prefix "gal_subtitle"



    vbox pos (144, 342):
        if renpy.seen_label("extra_mom1_bath"):
            imagebutton:
                action Show("joyce_p1")
                idle Transform("EP2/home afterdrink mom 1.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP2/home afterdrink mom 1.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "[mom_name]"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP2/home afterdrink mom 1.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"

    vbox pos (570, 342):
        if isabel_unlocked:
            imagebutton:
                action Show("isabel_p1")
                idle Transform("EP2/home massage isa 4.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP2/home massage isa 4.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "Isabel"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP2/home massage isa 4.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"

    vbox pos (996, 342):
        if renpy.seen_label("ruby1_prologueBed"):
            imagebutton:
                action Show("ruby_p1")
                idle Transform("EP5/home massage ruby 16.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP5/home massage ruby 16.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "Ruby"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP5/home massage ruby 16.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"

    vbox pos (1422, 342):
        if renpy.seen_label("tutoring1_makemistake_dialogue"):
            imagebutton:
                action Show("msjane_p1")
                idle Transform("EP1/prologue university 5.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP1/prologue university 5.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "Ms. Jane"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP1/prologue university 5.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"


    vbox pos (144, 694):
        if renpy.seen_label("aunt_2_worktalk_feet_dialogue"):
            imagebutton:
                action Show("sofia_p1")
                idle Transform("EP6/aunt_objective_1.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP6/aunt_objective_1.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "[aunt_name]"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP6/aunt_objective_1.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"

    vbox pos (570, 694):
        if renpy.seen_label("natsuko1_nightclubHj"):
            imagebutton:
                action Show("natsuko_p1")
                idle Transform("EP4/club natsuko 6.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP4/club natsuko 6.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "Natsuko"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP4/club natsuko 6.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"

    vbox pos (996, 694):
        if renpy.seen_label("chadgf1_sex"):
            imagebutton:
                action Show("other_p1")
                idle Transform("EP1/prologue flashback 2.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("EP1/prologue flashback 2.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            text "Other"
        else:
            imagebutton:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("EP1/prologue flashback 2.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
            text "???"










































screen joyce_p1():
    tag menu
    modal True
    add "gallery/8.png"
    text " Joyce -  Page 1" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("joyce_p2")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        if extras_installed and renpy.seen_label("extra_mom1_bath"):
            action Replay("extra_mom1_bath")
            idle Transform("gallery/imgs/extra prologue bath 4_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra prologue bath 4_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra prologue bath 4_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("mom2_prologueDressing")
        idle Transform("EP1/prologue morning mom 5.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP1/prologue morning mom 5.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP1/prologue morning mom 5.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        action Replay("mom_1_bathpeep_dialogue")
        idle Transform("EP2/mom bath 8.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP2/mom bath 8.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP2/mom bath 8.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("m_ns_jerkoff_dialogue")
        idle Transform("gallery/imgs/mom night jerkoff animation 16.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/mom night jerkoff animation 16.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/mom night jerkoff animation 16.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        action Replay("m_ns_usefeet_dialogue")
        idle Transform("gallery/imgs/mom night footfuck C 42.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/mom night footfuck C 42.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/mom night footfuck C 42.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        action Replay("mom_3_homedrinkingmom_dialogue")
        idle Transform("EP2/home drinking mom 3.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP2/home drinking mom 3.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP2/home drinking mom 3.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 694):
        action Replay("mom_massage_2")
        idle Transform("EP2/home massage mom 10.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP2/home massage mom 10.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP2/home massage mom 10.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 694):
        if elite_installed and renpy.seen_label("elite_02_mom_dinner1"):
            action Replay("elite_02_mom_dinner1")
            idle Transform("gallery/imgs/elite dinner mom 17_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/elite dinner mom 17_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/elite dinner mom 17_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    add "gallery/elite_icon.png" pos (442, 354) anchor (0, 0)
    add "gallery/elite_icon.png" pos (1720, 706) anchor (0, 0)




screen joyce_p2():
    tag menu
    modal True
    add "gallery/8.png"
    text " Joyce -  Page 2" style "title" xoffset 8
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("joyce_p3")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("mom_yoga_3")
        idle Transform("EP3/home yoga mom 20.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP3/home yoga mom 20.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP3/home yoga mom 20.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("mom_massage_3")
        idle Transform("EP3/home massage mom 19.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP3/home massage mom 19.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP3/home massage mom 19.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        if elite_installed and renpy.seen_label("elite_03_mom_dinner2"):
            action Replay("elite_03_mom_dinner2")
            idle Transform("gallery/imgs/elite dinner mom 28_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/elite dinner mom 28_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/elite dinner mom 28_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("mom_6_makedinner_dialogue")
        idle Transform("EP4/mom make dinner 18.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP4/mom make dinner 18.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP4/mom make dinner 18.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        action Replay("m_ns_useass_dialogue")
        idle Transform("gallery/imgs/mom night assjob B 49.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/mom night assjob B 49.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/mom night assjob B 49.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        action Replay("mom_yoga_4")
        idle Transform("EP4/home yoga mom 29.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP4/home yoga mom 29.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP4/home yoga mom 29.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 694):
        if extras_installed and renpy.seen_label("extra_04_mom_jane"):
            action Replay("extra_04_mom_jane")
            idle Transform("gallery/imgs/extra jane mom 6_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra jane mom 6_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra jane mom 6_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 694):
        action Replay("mom_7_movienight_dialogue")
        idle Transform("EP5/mom chill night 28.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/mom chill night 28.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/mom chill night 28.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    add "gallery/elite_icon.png" pos (1294, 354) anchor (0, 0)
    add "gallery/elite_icon.png" pos (1294, 706) anchor (0, 0)




screen joyce_p3():
    tag menu
    modal True
    add "gallery/6.png"
    text " Joyce -  Page 3" style "title" xoffset 6
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("joyce_p1")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("mom_massage_4")
        idle Transform("EP5/home massage mom 37.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/home massage mom 37.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/home massage mom 37.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    vbox pos (570, 342):
        imagebutton:
            action Replay("mom_8_morningjerkoff_dialogue")
            idle Transform("EP6/mom morning jerkoff 9.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/mom morning jerkoff 9.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/mom morning jerkoff 9.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (996, 342):
        imagebutton:
            action Replay("mom_9_bathroom2_dialogue")
            idle Transform("EP6/mom bath 21.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/mom bath 21.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/mom bath 21.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (1422, 342):
        imagebutton:
            action Replay("m_ns_titfuck_dialogue")
            idle Transform("gallery/imgs/mom night titfuck A00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/mom night titfuck A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/mom night titfuck A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"


    vbox pos (144, 694):
        imagebutton:
            action Replay("mom_yoga_5")
            idle Transform("EP6/home yoga mom 47.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/home yoga mom 47.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/home yoga mom 47.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (570, 694):
        imagebutton:
            if elite_installed and renpy.seen_label("elite_06_momAunt_cooking"):
                action Replay("elite_06_momAunt_cooking")
                idle Transform("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            else:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (868, 706) anchor (0, 0)







































screen isabel_p1():
    tag menu
    modal True
    add "gallery/8.png"
    text "Isabel -  Page 1" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("isabel_p2")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("i_ns_touchtits_dialogue")
        idle Transform("EP1/prologue night isabel 4.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP1/prologue night isabel 4.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP1/prologue night isabel 4.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("i_ns_jerkoff_dialogue")
        idle Transform("gallery/imgs/isa night jerkoff animation 41.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa night jerkoff animation 41.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa night jerkoff animation 41.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        action Replay("i_ns_usehand_dialogue")
        idle Transform("gallery/imgs/isa night HJ v2 A59.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa night HJ v2 A59.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa night HJ v2 A59.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("isabel_1_homedrinkingisabel_dialogue")
        idle Transform("gallery/imgs/isa morning A00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa morning A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa morning A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        if extras_installed and renpy.seen_label("extra_02_isabel_lotion"):
            action Replay("extra_02_isabel_lotion")
            idle Transform("gallery/imgs/extra isa lotion 5_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra isa lotion 5_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra isa lotion 5_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        action Replay("massage_isa_3")
        idle Transform("EP3/home massage isa 11.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP3/home massage isa 11.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP3/home massage isa 11.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 694):
        action Replay("isabel_4_carpickup_dialogue")
        idle Transform("EP4/isa pickup 11.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP4/isa pickup 11.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP4/isa pickup 11.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 694):
        action Replay("i_ns_usefeet_dialogue")
        idle Transform("gallery/imgs/isa night footfuck A18.png", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa night footfuck A18.png", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa night footfuck A18.png", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    add "gallery/elite_icon.png" pos (442, 706) anchor (0, 0)




screen isabel_p2():
    tag menu
    modal True
    add "gallery/8.png"
    text "Isabel -  Page 2" style "title" xoffset 7
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Prev" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("isabel_p1")

    style_prefix "gal_subtitle"


    vbox pos (144, 342):
        imagebutton:
            action Replay("isabel_5_tvbet1_dialogue")
            idle Transform("EP6/isa bet 13.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/isa bet 13.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/isa bet 13.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    imagebutton pos (570, 342):
        action Replay("isabel_6_stalker_dialogue")
        idle Transform("gallery/imgs/isa thighjob A00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa thighjob A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa thighjob A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        action Replay("massage_isa_4")
        idle Transform("EP5/home massage isa 25.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/home massage isa 25.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/home massage isa 25.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        if extras_installed and renpy.seen_label("extra_05_isabelRuby_pool"):
            action Replay("extra_05_isabelRuby_pool")
            idle Transform("gallery/imgs/extra pool 18_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra pool 18_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra pool 18_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    vbox pos (144, 694):
        imagebutton:
            action Replay("isabel_7_tvbet2_dialogue")
            idle Transform("EP6/isa bet titsuck 6.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/isa bet titsuck 6.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/isa bet titsuck 6.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    imagebutton pos (570, 694):
        action Replay("i_ns_rubpussy_dialogue")
        idle Transform("gallery/imgs/isa night pussy rub animation 20.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/isa night pussy rub animation 20.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa night pussy rub animation 20.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    vbox pos (996, 694):
        imagebutton:
            action Replay("i_ns_assjob_dialogue")
            idle Transform("gallery/imgs/isa night assjob A00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/isa night assjob A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/isa night assjob A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (1422, 694):
        imagebutton:
            action Replay("massage_isa_5")
            idle Transform("EP6/home massage isa 29.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/home massage isa 29.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/home massage isa 29.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (1720, 354) anchor (0, 0)








































screen ruby_p1():
    tag menu
    modal True
    add "gallery/8.png"
    text "  Ruby -  Page 1" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("ruby_p2")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("ruby1_prologueBed")
        idle Transform("EP1/prologue arrival ruby 5.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP1/prologue arrival ruby 5.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP1/prologue arrival ruby 5.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("ruby2_prologueShower")
        idle Transform("EP1/prologue ruby shower 5.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP1/prologue ruby shower 5.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP1/prologue ruby shower 5.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        action Replay("r_ns_gropeass_dialogue")
        idle Transform("gallery/imgs/ruby ass grope animation00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/ruby ass grope animation00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/ruby ass grope animation00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("r_ns_jerkoff_dialogue")
        idle Transform("gallery/imgs/night ruby jerkoff animation 15.png", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/night ruby jerkoff animation 15.png", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/night ruby jerkoff animation 15.png", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        action Replay("r_ns_usefeet_dialogue")
        idle Transform("gallery/imgs/Ruby_Night_Footjob_A00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/Ruby_Night_Footjob_A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/Ruby_Night_Footjob_A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        action Replay("ruby_5_dressup_dialogue")
        idle Transform("EP2/home ruby dressup 18.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP2/home ruby dressup 18.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP2/home ruby dressup 18.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 694):
        if extras_installed and renpy.seen_label("extra_03_ruby_masturbate"):
            action Replay("extra_03_ruby_masturbate")
            idle Transform("gallery/imgs/extra ruby masturbate 17_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra ruby masturbate 17_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra ruby masturbate 17_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 694):
        action Replay("massage_ruby_3")
        idle Transform("EP4/home massage ruby 14.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP4/home massage ruby 14.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP4/home massage ruby 14.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    add "gallery/elite_icon.png" pos (1294, 706) anchor (0, 0)




screen ruby_p2():
    tag menu
    modal True
    add "gallery/8.png"
    text "  Ruby -  Page 2" style "title" xoffset 7
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("ruby_p3")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("ruby_9_pillowfight_dialogue")
        idle Transform("EP4/ruby pillowfight 18.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP4/ruby pillowfight 18.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP4/ruby pillowfight 18.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("r_ns_assjob_dialogue")
        idle Transform("gallery/imgs/ruby_night_assjob_A00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/ruby_night_assjob_A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/ruby_night_assjob_A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        action Replay("ruby_10_spanking_dialogue")
        idle Transform("EP5/ruby spank 19.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/ruby spank 19.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/ruby spank 19.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("massage_ruby_4")
        idle Transform("EP5/home massage ruby 26.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/home massage ruby 26.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/home massage ruby 26.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        if extras_installed and renpy.seen_label("extra_05_isabelRuby_pool"):
            action Replay("extra_05_isabelRuby_pool")
            idle Transform("gallery/imgs/extra pool 18_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra pool 18_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra pool 18_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        if elite_installed and renpy.seen_label("elite_05_ruby_dinner3"):
            action Replay("elite_05_ruby_dinner3")
            idle Transform("gallery/imgs/elite dinner ruby 9_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/elite dinner ruby 9_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/elite dinner ruby 9_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    vbox pos (996, 694):
        imagebutton:
            action Replay("ruby_11_changingroom_dialogue")
            idle Transform("EP6/ruby changing booth 2.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/ruby changing booth 2.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/ruby changing booth 2.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (1422, 694):
        imagebutton:
            action Replay("r_ns_fingerpussy_dialogue")
            idle Transform("EP6/ruby night fingering 5.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/ruby night fingering 5.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/ruby night fingering 5.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (442, 706) anchor (0, 0)
    add "gallery/elite_icon.png" pos (868, 706) anchor (0, 0)




screen ruby_p3():
    tag menu
    modal True
    add "gallery/3.png"
    text "  Ruby -  Page 3" style "title" xoffset 6
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("ruby_p1")

    style_prefix "gal_subtitle"


    vbox pos (144, 342):
        imagebutton:
            action Replay("massage_ruby_5")
            idle Transform("EP6/home massage ruby 43.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/home massage ruby 43.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/home massage ruby 43.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (570, 342):
        imagebutton:
            action Replay("ruby_12_spanking2_dialogue")
            idle Transform("EP6/ruby spank 40.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/ruby spank 40.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/ruby spank 40.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (996, 342):
        imagebutton:
            if extras_installed and renpy.seen_label("extra_06_ruby_shave"):
                action Replay("extra_06_ruby_shave")
                idle Transform("gallery/imgs/extra ruby shave 11_thumb.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("gallery/imgs/extra ruby shave 11_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            else:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra ruby shave 11_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (1294, 354) anchor (0, 0)

































screen msjane_p1():
    tag menu
    modal True
    add "gallery/8.png"
    text "Ms. Jane -  Page 1" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Next" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("msjane_p2")

    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("tutoring1_makemistake_dialogue")
        idle Transform("gallery/imgs/tutoring breathing A 25.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/tutoring breathing A 25.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/tutoring breathing A 25.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("tutoring2_makemistake_dialogue")
        idle Transform("gallery/imgs/tutoring tits shake A 05.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/tutoring tits shake A 05.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/tutoring tits shake A 05.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        if extras_installed and renpy.seen_label("extra_02_jane_store"):
            action Replay("extra_02_jane_store")
            idle Transform("gallery/imgs/extra store jane 14_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra store jane 14_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra store jane 14_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        action Replay("tutoring3_dialogue")
        idle Transform("gallery/imgs/tutoring tits shake A 23.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/tutoring tits shake A 23.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/tutoring tits shake A 23.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        action Replay("tutoring4_dialogue")
        idle Transform("EP3/tutoring 20.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP3/tutoring 20.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP3/tutoring 20.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 694):
        action Replay("tutoring4_gropetits_dialogue")
        idle Transform("gallery/imgs/tutoring tits grope A090.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/tutoring tits grope A090.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/tutoring tits grope A090.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 694):
        action Replay("jane_9_masturbate_dialogue")
        idle Transform("gallery/imgs/jane masturbate C 41.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/jane masturbate C 41.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/jane masturbate C 41.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 694):
        if extras_installed and renpy.seen_label("extra_04_mom_jane"):
            action Replay("extra_04_mom_jane")
            idle Transform("gallery/imgs/extra jane mom 6_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra jane mom 6_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra jane mom 6_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    add "gallery/elite_icon.png" pos (1294, 354) anchor (0, 0)
    add "gallery/elite_icon.png" pos (1720, 706) anchor (0, 0)




screen msjane_p2():
    tag menu
    modal True
    add "gallery/2.png"
    text "Ms. Jane -  Page 2" style "title" xoffset 6
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")
    frame style "nextbtn_outline":
        has frame style "backbtn_main"
        text "Prev" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("msjane_p1")

    style_prefix "gal_subtitle"


    vbox pos (144, 342):
        imagebutton:
            action Replay("jane_12_masturbate2_dialogue")
            idle Transform("EP6/jane masturbate 20.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/jane masturbate 20.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/jane masturbate 20.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (570, 342):
        imagebutton:
            action Replay("jane_14_continueteaching_dialogue")
            idle Transform("EP6/tutoring 36.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/tutoring 36.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/tutoring 36.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"




















screen sofia_p1():
    tag menu
    modal True
    add "gallery/4.png"
    text "[aunt_name] -  Scenes" style "title" xoffset 8
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")





    style_prefix "gal_subtitle"


    vbox pos (144, 342):
        imagebutton:
            action Replay("aunt_2_worktalk_feet_dialogue")
            idle Transform("EP6/aunt foot massage 13.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/aunt foot massage 13.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/aunt foot massage 13.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (570, 342):
        imagebutton:
            action Replay("aunt_2_worktalk_ass_dialogue")
            idle Transform("EP6/aunt ass massage 7.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("EP6/aunt ass massage 7.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("EP6/aunt ass massage 7.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (996, 342):
        imagebutton:
            action Replay("aunt_ns_jerkoff_dialogue")
            idle Transform("gallery/imgs/aunt night jerkoff A00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/aunt night jerkoff A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/aunt night jerkoff A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    vbox pos (1422, 342):
        imagebutton:
            action Replay("aunt_ns_thighjob_dialogue")
            idle Transform("gallery/imgs/aunt niight thighjob A00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/aunt niight thighjob A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/aunt niight thighjob A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"


    vbox pos (144, 694):
        imagebutton:
            if elite_installed and renpy.seen_label("elite_06_momAunt_cooking"):
                action Replay("elite_06_momAunt_cooking")
                idle Transform("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            else:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("gallery/imgs/elite mom aunt cooking 21_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (442, 706) anchor (0, 0)














screen natsuko_p1():
    tag menu
    modal True
    add "gallery/2.png"
    text "Natsuko -  Scenes" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")





    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("natsuko1_nightclubHj")
        idle Transform("gallery/imgs/natsuko hj A 03.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/natsuko hj A 03.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/natsuko hj A 03.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    vbox pos (570, 342):
        imagebutton:
            action Replay("natsuko_1_nightkitchen_dialogue")
            idle Transform("gallery/imgs/natusko kitchen footjob A00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/natusko kitchen footjob A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/natusko kitchen footjob A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"


























screen other_p1():
    tag menu
    modal True
    add "gallery/6.png"
    text "Other  Scenes" style "title"
    frame style "backbtn_outline":
        has frame style "backbtn_main"
        text "Back" style "btn_text"
        imagebutton align (0.5, 0.5) auto "gallery/btn_%s.png" action Show("scene_gallery")





    style_prefix "gal_subtitle"


    imagebutton pos (144, 342):
        action Replay("chadgf1_sex")
        idle Transform("gallery/imgs/prologue bar sex A000.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/prologue bar sex A000.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/prologue bar sex A000.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (570, 342):
        action Replay("collegesluts1_dream")
        idle Transform("gallery/imgs/MP prologue flashback handjob A00.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("gallery/imgs/MP prologue flashback handjob A00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("gallery/imgs/MP prologue flashback handjob A00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (996, 342):
        if extras_installed and renpy.seen_label("extra_miranda1_bj"):
            action Replay("extra_miranda1_bj")
            idle Transform("gallery/imgs/extra prologue flashback 12_thumb.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/extra prologue flashback 12_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra prologue flashback 12_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    imagebutton pos (1422, 342):
        if elite_installed and renpy.seen_label("elite_03_jenna_pool"):
            action Replay("elite_03_jenna_pool")
            idle Transform("gallery/imgs/jenna pool nude 00.jpg", zoom=0.184)
            hover Transform(im.MatrixColor("gallery/imgs/jenna pool nude 00.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        else:
            action NullAction()
            idle Transform(im.MatrixColor(im.Blur("gallery/imgs/jenna pool nude 00.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)


    imagebutton pos (144, 694):
        action Replay("thorne_9_cartheft_dialogue")
        idle Transform("EP5/car theft 30.jpg", zoom=0.184)
        hover Transform(im.MatrixColor("EP5/car theft 30.jpg", im.matrix.brightness(0.13)), zoom=0.184)
        insensitive Transform(im.MatrixColor(im.Blur("EP5/car theft 30.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)

    vbox pos (570, 694):
        imagebutton:
            if extras_installed and renpy.seen_label("extra_06_tanya_boobs"):
                action Replay("extra_06_tanya_boobs")
                idle Transform("gallery/imgs/extra tanya boobs 12_thumb.jpg", zoom=0.184)
                hover Transform(im.MatrixColor("gallery/imgs/extra tanya boobs 12_thumb.jpg", im.matrix.brightness(0.13)), zoom=0.184)
            else:
                action NullAction()
                idle Transform(im.MatrixColor(im.Blur("gallery/imgs/extra tanya boobs 12_thumb.jpg", 12), im.matrix.brightness(-0.1)), zoom=0.184)
        text "New in 0.6!"

    add "gallery/elite_icon.png" pos (1294, 354) anchor (0, 0)
    add "gallery/elite_icon.png" pos (1720, 354) anchor (0, 0)
    add "gallery/elite_icon.png" pos (868, 706) anchor (0, 0)









style title is text:
    size 100
    color "#cf0fe0"
    font "gui/fonts/Lazer84.ttf"
    align (0.5, 0.1)

style gal_subtitle_text is text:
    size 32
    font "gui/fonts/Louis George Cafe Light.ttf"
    color "#fff"
    xalign 0.5

style gal_subtitle_vbox is vbox:
    spacing 28







style backbtn_outline is frame:
    align (0.975, 0.05)
    padding (2, 2)
    background "#fff"

style backbtn_main is frame:
    background "#363636"
    xsize 132
    ysize 66


style nextbtn_outline is frame:
    align (0.975, 0.14)
    padding (2, 2)
    background "#fff"















style btn_text is text:
    size 30
    font "gui/fonts/Louis George Cafe.ttf"
    align (0.5, 0.6)

    idle_color "#fff"
    color "#fff"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
