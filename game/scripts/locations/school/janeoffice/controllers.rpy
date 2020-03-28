label school_janeoffice:


    if time.is_afternoon():

        if jane_level == 7:
            call jane_7_schoolmissing_dialogue
            $ jane_level = 8
            $ increase_time()
            $ go_to(L_janehome_porch)

        elif jane_level == 10:
            call jane_10_stopteaching_dialogue
            $ jane_level = 11
            $ increase_time()
            $ go_to(L_home_livingroom)

        elif jane_level == 14:
            call jane_14_continueteaching_dialogue
            $ jane_level = 15
            $ jane_on_sick_leave = False
            $ increase_time()
            $ go_to(L_home_livingroom)

        elif lain_mod and extras_installed and jane_level >= 15 and mom_level >= 10 and not lm_extra_04_mom_jane:
            call extra_04_mom_jane
            $ lm_extra_04_mom_jane = True
            $ increase_time()
            $ go_to(L_home_livingroom)



    if time.is_morning():
        scene school_janeoffice__morning_ground
    elif time.is_afternoon() and jane_on_sick_leave:
        scene school_janeoffice__morning_ground
    elif time.is_afternoon():
        scene school_janeoffice__afternoon_jane_ground
    elif time.is_evening():
        scene school_janeoffice__evening_ground:
            zoom 1.1
            align (0.0, 1.0)
    elif time.is_night():
        scene black
        show school_janeoffice__night_ground


    call screen school_janeoffice






label school_janeoffice_msjane:

    if jane_level == 1 or jane_level == 2:
        call tutoring1_intro_dialogue

        menu:
            "Concentrate":
                call tutoring1_concentrate_dialogue
                $ jane_level = 2
            "Stare at her tits":

                call tutoring1_stareathertits_dialogue

            "Make mistake" if jane_level == 2:
                call tutoring1_makemistake_dialogue
                $ jane_level = 3



    elif jane_level == 3 or jane_level == 4:
        call tutoring2_intro_dialogue

        menu:
            "Concentrate":
                call tutoring2_concentrate_dialogue
                $ jane_level = 4
            "Stare at her tits":

                call tutoring2_stareathertits_dialogue

            "Make mistake" if jane_level == 4:
                call tutoring2_makemistake_dialogue
                $ jane_level = 5



    elif jane_level == 5:
        call tutoring3_dialogue
        $ jane_level = 6



    elif jane_level == 6:
        call tutoring4_dialogue

        if tutoring4_liftdress_seen and tutoring4_touchbutt_seen and tutoring4_feet_seen and tutoring4_caress_seen:
            call tutoring4_gropetits_dialogue
            $ jane_level = 7
            $ jane_on_sick_leave = True
        else:
            call tutoring4_notseenall_dialogue



    elif jane_level == 15:
        menu:
            "Tutoring #1":
                call tutoring1_makemistake_dialogue
            "Tutoring #2":

                call tutoring2_makemistake_dialogue
            "Tutoring #3":

                call tutoring3_dialogue
            "Tutoring #4":

                call tutoring4_gropetits_dialogue
            "Exit":

                $ go_to(L_school_janeoffice)



    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    $ jane_tutoring_counter += 1
    $ increase_time()
    $ go_to(L_school_janeoffice)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
