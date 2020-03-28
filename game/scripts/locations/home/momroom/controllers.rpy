label home_momroom:


    if time.is_afternoon():

        if mom_level == 6 and mom_delay == 0:
            call mom_6_makedinner_dialogue
            $ mom_level = 7
            $ mom_yoga_level = 4
            $ m_ns_useass.unlocked = True
            $ persistent._seen_ever["extra_04_mom_jane"] = True
            $ set_time(4)
            $ mp_notify("Mom - New Yoga Level Unlocked!")
            $ go_to(L_home_basement)


    elif time.is_night():

        if mom_visited_tonight:
            mc "(I shouldn't disturb her anymore tonight.)"
            $ go_to(L_home_hall)

        elif sleeping_pills.used and mom_night_counter == 0:
            call mom_nightscene_first_dialogue
            $ mom_night_counter += 1
            $ mom_visited_tonight = True
            $ go_to(L_home_hall)

        elif not sleeping_pills.used:
            mc "(Maybe I can sneak inside Mom's room tonight?)"
            scene black
            show home_momroom__night_parents_ground
            with fade
            pause 0.5
            mc "(Damn, Dad is still awake...)"
            $ mom_visited_tonight = True




    if time.is_morning() and mom_yoga_level > mom_seen_yoga_level and mom_seen_yoga_level >= 2:
        scene home_momroom__day_momyoga2_ground
    elif time.is_morning() and mom_yoga_level > mom_seen_yoga_level and mom_seen_yoga_level < 2:
        scene home_momroom__day_momyoga1_ground
    elif time.is_morning() or time.is_afternoon():
        scene home_momroom__day_ground

    elif time.is_evening() and mom_level >= 7:
        scene black
        show home_momroom__evening_mom_ground
    elif time.is_evening():
        scene black
        show home_momroom__evening_ground

    elif time.is_night() and mom_night_counter > 0:
        scene home_momroom__night_mom_ground
    elif time.is_night():
        scene black
        show home_momroom__night_parents_ground



    call screen home_momroom






label home_momroom_mom_yoga:

    if mom_seen_yoga_level == 0:
        call mom_yoga_1
        $ mom_seen_yoga_level = 1

    elif mom_seen_yoga_level == 1:
        call mom_yoga_2
        $ mom_seen_yoga_level = 2

    elif mom_seen_yoga_level == 2:
        call mom_yoga_3
        $ mom_seen_yoga_level = 3

    elif mom_seen_yoga_level == 3:
        call mom_yoga_4
        $ mom_seen_yoga_level = 4

    elif mom_seen_yoga_level == 4:
        call mom_yoga_5
        $ mom_seen_yoga_level = 5

    $ mom_yoga_counter += 1
    $ increase_time()
    $ go_to(L_home_momroom)






label home_momroom_momsleep:

    call m_ns_intro_dialogue
    menu:
        "Reveal breasts":
            call m_ns_revealbreasts_dialogue

            menu:
                "Jerk off[m_ns_jerkoff.text]":
                    call m_ns_jerkoff_dialogue
                    $ m_ns_jerkoff.seen = True


                "Titfuck[m_ns_titfuck.text]" if m_ns_titfuck.unlocked:
                    call m_ns_titfuck_dialogue
                    $ m_ns_titfuck.seen = True

                "Titfuck (locked)" if not m_ns_titfuck.unlocked:
                    pass
        "Turn her around":


            call m_ns_turnheraround_dialogue

            menu:
                "Use feet[m_ns_usefeet.text]":
                    call m_ns_usefeet_dialogue
                    $ m_ns_usefeet.seen = True


                "Use ass[m_ns_useass.text]" if m_ns_useass.unlocked:
                    call m_ns_useass_dialogue
                    $ m_ns_useass.seen = True

                "Use ass (locked)" if not m_ns_useass.unlocked:
                    pass



    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    $ mom_night_counter += 1
    $ mom_visited_tonight = True
    $ go_to(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
