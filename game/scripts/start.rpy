label splashscreen:

    $ renpy.movie_cutscene("videos/logo2.mkv")

    scene splash 1 with Fade(0.5, 1.5, 1.0)
    pause 4.5

    scene splash 2 with fade
    pause 4.0

    scene black with Fade(1.0, 0.0, 0.5)

    return











label start:

    scene black with fade
    menu:
        "Is this your first time playing Midnight Paradise?"
        "Yes":

            pause 0.5
            lewdlab "Enjoy the game! :)"
        "No":

            lewdlab "You can choose to start at the beginning of the game or choose to start at a later point in the story."
            lewdlab "If you've played a previous version of the game, we really recommend that you try playing the game from the beginning again so you can experience all of the improvements that have been made to the game and scenes in this update."
            menu:
                "Start at the beginning":

                    lewdlab "We hope you enjoy the improved version of Midnight Paradise! :)"
                "Start at a later point in the story":

                    call setname
                    menu:
                        "Skip prologue (start at 0.2)":
                            call skip_v01
                            jump skip_to_v02_start
                        "Start at the beginning of 0.3":

                            call skip_v01
                            call skip_v02
                            jump skip_to_other_start
                        "Start at the beginning of 0.4":

                            call skip_v01
                            call skip_v02
                            call skip_v03
                            jump skip_to_other_start
                        "Start at the beginning of 0.5":

                            call skip_v01
                            call skip_v02
                            call skip_v03
                            call skip_v04
                            jump skip_to_other_start
                        "Start at the beginning of 0.6":

                            call skip_v01
                            call skip_v02
                            call skip_v03
                            call skip_v04
                            call skip_v05
                            jump skip_to_other_start

    call setname
    jump chadgf1_sex



















label skip_v01:

    scene prologue arrival 5 with fade
    menu:
        "Were you disrespectful when meeting Mr. Harding?"
        "Yes":
            $ morality -= 1
        "No":
            pass


    scene prologue arrival 6 with fade
    menu:
        "Did you give in or protest when Mr. Harding demanded his car keys and credit card?"
        "Give in":
            pass
        "Protest":
            $ morality -= 1


    scene prologue arrival mom 5 with fade:
        subpixel True
        yalign 0.0
    menu:
        "How did you compliment Joyce after your arrival?"
        "Complimented Bottom":
            pass
        "Complimented Figure":
            pass
        "Complimented Beauty":
            $ morality += 1


    scene prologue bathroom isabel 6 with fade
    menu:
        "Did you apologize or flirt after walking in on Isabel in the bathroom?"
        "Apologize":
            $ morality += 1
        "Flirt":
            $ morality -= 1


    scene prologue arrival ruby 6 with fade
    menu:
        "Did you compliment Ruby's body or apologize when meeting her?"
        "Compliment":
            $ morality -= 1
        "Apologize":
            $ morality += 1


    scene prologue evening kitchen 5 with fade
    menu:
        "Did you make excuses for failing college or express regret?"
        "Excuses":
            pass
        "Regret":
            $ morality += 1


    scene prologue ruby shower 6 with fade
    menu:
        "Did you try to convince Ruby that watching her showering was fine, or did you blame Ruby for leaving the door open?"
        "Convince her":
            $ morality -= 1
        "It was Ruby's fault":
            pass

    $ persistent._seen_ever["chadgf1_sex"] = True
    $ persistent._seen_ever["ruby1_prologueBed"] = True
    $ persistent._seen_ever["collegesluts1_dream"] = True
    $ persistent._seen_ever["extra_miranda1_bj"] = True
    $ persistent._seen_ever["extra_mom1_bath"] = True
    $ persistent._seen_ever["ruby2_prologueShower"] = True
    $ persistent._seen_ever["isabel_prologueNight"] = True
    $ persistent._seen_ever["ruby3_prologueNight"] = True
    $ persistent._seen_ever["mom2_prologueDressing"] = True

    return



label skip_to_v02_start:
    $ set_time(2)
    $ day_of_week = 1
    $ day_of_week_name = day_of_week_names[day_of_week]
    $ day_count = 1
    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene school_janeoffice__afternoon_jane_ground with slowfade
    $ go_to(L_school_janeoffice)



label skip_to_other_start:
    $ set_time(1)
    $ day_of_week = 1
    $ day_of_week_name = day_of_week_names[day_of_week]
    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene home_livingroom__day with slowfade
    $ go_to(L_home_livingroom)






label skip_v02:

    python:
        day_count = 12
        money = 5
        ruby_logan_in_kitchen = True
        sleeping_pills.purchased = True
        sleeping_pills.own_item = True
        sleeping_pills.used = True
        sleeping_pills.delivery_delay = 0
        L_home_study.unlocked = True
        L_home_study.first_visit = False

        thorne_level = 3
        laptop_owned = True

        mom_level = 5
        mom_massage_level = 2
        mom_seen_massage_level = 2
        mom_massage_counter = 2
        mom_yoga_level = 2
        mom_seen_yoga_level = 2
        mom_yoga_counter = 2
        mom_seen_tv_level = 1
        mom_tv_counter = 1
        mom_night_counter = 1

        isabel_level = 3
        isabel_massage_level = 2
        isabel_seen_massage_level = 2
        isabel_massage_counter = 2
        isabel_seen_tv_level = 1
        isabel_tv_counter = 1

        ruby_level = 7
        ruby_massage_level = 2
        ruby_seen_massage_level = 2
        ruby_massage_counter = 2
        ruby_seen_tv_level = 1
        ruby_tv_counter = 1

        jane_level = 5
        jane_tutoring_counter = 4

        mc_seen_tv_level = 1
        mc_tv_counter = 1


        persistent._seen_ever["mom_1_bathpeep_dialogue"] = True
        persistent._seen_ever["m_ns_jerkoff_dialogue"] = True
        persistent._seen_ever["m_ns_usefeet_dialogue"] = True
        persistent._seen_ever["mom_3_homedrinkingmom_dialogue"] = True
        persistent._seen_ever["mom_massage_2"] = True
        persistent._seen_ever["elite_02_mom_dinner1"] = True

        persistent._seen_ever["i_ns_touchtits_dialogue"] = True
        persistent._seen_ever["i_ns_jerkoff_dialogue"] = True
        persistent._seen_ever["i_ns_usehand_dialogue"] = True
        persistent._seen_ever["isabel_1_homedrinkingisabel_dialogue"] = True
        persistent._seen_ever["extra_02_isabel_lotion"] = True

        persistent._seen_ever["r_ns_gropeass_dialogue"] = True
        persistent._seen_ever["r_ns_jerkoff_dialogue"] = True
        persistent._seen_ever["r_ns_usefeet_dialogue"] = True
        persistent._seen_ever["ruby_5_dressup_dialogue"] = True

        persistent._seen_ever["tutoring1_makemistake_dialogue"] = True
        persistent._seen_ever["tutoring2_makemistake_dialogue"] = True
        persistent._seen_ever["extra_02_jane_store"] = True

    return






label skip_v03:

    scene thorne negotiation 3 with fade
    menu:
        "When Mikey mocked you in Thorne's office did you stay silent, insult him, or threaten him?"
        "Stayed silent":
            pass
        "Insulted":
            $ morality -= 1
        "Threatened":
            $ morality -= 3
            $ mikey_threatened = True


    scene thorne negotiation 9 with fade
    menu:
        "During Mikey's argument with Thorne did you stay silent or hit Mikey?"
        "Stayed silent":
            $ morality += 1
        "Hit Mikey":
            $ mikey_violence = True


    scene home yoga mom 36 with fade
    menu:
        "Did you say Joyce's yoga session could have been better or did you compliment her?"
        "Could have been better":
            pass
        "Compliment":
            $ mom_yoga3_complimented = True




    python:
        day_count = 24

        thorne_level = 5

        mom_level = 6
        mom_massage_level = 3
        mom_seen_massage_level = 3
        mom_massage_counter = 3
        mom_yoga_level = 3
        mom_seen_yoga_level = 3
        mom_yoga_counter = 3

        isabel_level = 4
        isabel_massage_level = 3
        isabel_seen_massage_level = 3
        isabel_massage_counter = 3

        jane_level = 7
        jane_tutoring_counter = 9
        jane_on_sick_leave = True
        tutoring4_liftdress_seen = True
        tutoring4_touchbutt_seen = True
        tutoring4_feet_seen = True
        tutoring4_caress_seen = True


        persistent._seen_ever["mom_yoga_3"] = True
        persistent._seen_ever["mom_massage_3"] = True
        persistent._seen_ever["elite_03_mom_dinner2"] = True

        persistent._seen_ever["massage_isa_3"] = True

        persistent._seen_ever["extra_03_ruby_masturbate"] = True

        persistent._seen_ever["tutoring3_dialogue"] = True
        persistent._seen_ever["tutoring4_dialogue"] = True
        persistent._seen_ever["tutoring4_gropetits_dialogue"] = True

        persistent._seen_ever["elite_03_jenna_pool"] = True

    return


















label skip_v04:

    scene ruby chores 6 with fade
    menu:
        "When Ruby wouldn't do her chores did you tell her to show more respect or did you negotiate with her?"
        "Show more respect":
            $ ruby_influence += 1
        "Negotiate":
            pass


    scene isa pickup 11 with fade
    menu:
        "Did you make a risky move or play it safe with Isabel in the car?"
        "Risky move":
            $ isabel_lust += 2
        "Played it safe":
            $ isabel_lust += 1


    python:
        day_count = 36

        thorne_level = 8
        nc1_chair = True
        nc1_bartender = True
        nc1_melissa = True
        nc1_tanya = True
        nc1_natsuko1 = True
        nc1_natsuko2 = True
        nightclub1_complete = True
        L_nightclub_bar.first_visit = False
        L_nightclub_bar.toolbar_enabled = True
        L_nightclub_bar.can_leave = True
        L_home_pool.unlocked = True

        mom_level = 7
        mom_yoga_level = 4
        mom_seen_yoga_level = 4
        mom_yoga_counter = 4
        m_ns_jerkoff.seen = True
        m_ns_usefeet.seen = True
        m_ns_useass.unlocked = True
        mom_night_counter = 2

        isabel_level = 5
        i_ns_touchtits.seen = True
        i_ns_jerkoff.seen = True
        i_ns_usehand.seen = True
        i_ns_usefeet.unlocked = True
        isabel_night_counter = 3

        ruby_level = 10
        ruby_massage_level = 3
        ruby_seen_massage_level = 3
        ruby_massage_counter = 3
        r_ns_gropeass.seen = True
        r_ns_jerkoff.seen = True
        r_ns_usefeet.seen = True
        r_ns_assjob.unlocked = True
        ruby_night_counter = 3

        jane_level = 10
        L_janehome_porch.can_leave = True
        L_janehome_porch.toolbar_enabled = True





        persistent._seen_ever["mom_6_makedinner_dialogue"] = True
        persistent._seen_ever["m_ns_useass_dialogue"] = True
        persistent._seen_ever["mom_yoga_4"] = True
        persistent._seen_ever["extra_04_mom_jane"] = True

        persistent._seen_ever["isabel_4_carpickup_dialogue"] = True
        persistent._seen_ever["i_ns_usefeet_dialogue"] = True

        persistent._seen_ever["massage_ruby_3"] = True
        persistent._seen_ever["ruby_9_pillowfight_dialogue"] = True
        persistent._seen_ever["r_ns_assjob_dialogue"] = True

        persistent._seen_ever["jane_9_masturbate_dialogue"] = True
        persistent._seen_ever["extra_04_mom_jane"] = True

        persistent._seen_ever["natsuko1_nightclubHj"] = True

    return




label skip_v05:

    scene tanya meeting intro 3 with fade
    menu:
        "Did you threaten Viktor when he pushed you or did you let it go?"
        "Threatened":
            $ morality -= 2
            $ viktor_threatened = True
        "Let it go":
            $ morality += 2


    python:
        money = 18500
        day_count = 48
        thorne_office_unlocked = True

        thorne_level = 10

        mom_level = 8
        mom_massage_level = 4
        mom_seen_massage_level = 4
        mom_massage_counter = 4
        m_ns_useass.seen = True
        mom_night_counter = 3



        isabel_massage_level = 4
        isabel_seen_massage_level = 4
        isabel_massage_counter = 4
        i_ns_usefeet.seen = True
        isabel_night_counter = 4
        isabel_sunscreen.purchased = True
        isabel_sunscreen.own_item = True
        isabel_sunscreen.used = True
        isabel_sunscreen.delivery_delay = 0

        ruby_level = 11
        ruby_massage_level = 4
        ruby_seen_massage_level = 4
        ruby_massage_counter = 4
        r_ns_assjob.seen = True
        ruby_night_counter = 4

        eliana_level = 5
        tanya_level = 2
        dad_level = 2
        logan_level = 2





        persistent._seen_ever["mom_7_movienight_dialogue"] = True
        persistent._seen_ever["mom_massage_4"] = True

        persistent._seen_ever["isabel_5_tvbet1_dialogue"] = True
        persistent._seen_ever["isabel_6_stalker_dialogue"] = True
        persistent._seen_ever["massage_isa_4"] = True
        persistent._seen_ever["extra_05_isabelRuby_pool"] = True

        persistent._seen_ever["ruby_10_spanking_dialogue"] = True
        persistent._seen_ever["massage_ruby_4"] = True
        persistent._seen_ever["extra_05_isabelRuby_pool"] = True
        persistent._seen_ever["elite_05_ruby_dinner3"] = True

        persistent._seen_ever["thorne_9_cartheft_dialogue"] = True



    return









label setname:
    if lain_mod:
        if not renpy.mobile:
            $ mc_name = renpy.input("Enter your name:", "Connor").strip()
            $ mc = Character(mc_name)
            $ persistent.gallery_name = mc_name
        else:
            menu:
                "Set name as \"Connor\"":
                    pass
                "Input custom name":
                    $ mc_name = renpy.input("Enter your name:", "Connor").strip()
                    $ mc = Character(mc_name)
                    $ persistent.gallery_name = mc_name
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
