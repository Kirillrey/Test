label home_isabelroom:


    if time.is_morning() or time.is_afternoon():

        if isabel_level == 3:
            call isabel_3_crying_dialogue
            $ isabel_level = 4
            $ isabel_massage_level = 3
            $ increase_time()
            $ mp_notify("Isabel - New Massage Level Unlocked!")
            $ go_to(L_home_isabelroom)


        elif isabel_massage_level >= 4 and isabel_seen_massage_level == 3:

            if isabel_sunscreen_failed and not isabel_sunscreen.own_item:
                scene home_isabelroom__day_ground
                mc "(I need to buy some sunscreen for Isabel.)"

            elif not isabel_sunscreen_failed and not isabel_sunscreen.own_item:
                call massage_isa_4_failed
                $ isabel_sunscreen_failed = True
                $ isabel_massage_counter += 1
                $ increase_time()
                $ go_to(L_home_isabelroom)

            elif isabel_sunscreen.own_item:
                if isabel_sunscreen_failed:
                    call massage_isa_4_2ndtry
                else:
                    call massage_isa_4
                $ isabel_sunscreen.used = True
                $ isabel_seen_massage_level = 4
                $ isabel_massage_counter += 1
                $ increase_time()
                $ go_to(L_home_pool)



    elif time.is_night():

        if isabel_visited_tonight:
            mc "(I shouldn't disturb her anymore tonight.)"
            $ go_to(L_home_hall)
        elif isabel_level == 5 or isabel_level == 7:
            mc "(Hm, it looks like Isabel hasn't fallen asleep yet.)"
            $ go_to(L_home_hall)




    if time.is_morning() or time.is_afternoon():
        scene home_isabelroom__day_ground
    elif time.is_evening():
        scene black
        show home_isabelroom__night_ground
    elif time.is_night():
        scene black
        show home_isabelroom__night_isabel_ground



    call screen home_isabelroom







label home_isabelroom_isabelsleep:

    call i_ns_intro_dialogue
    menu:
        "Touch tits[i_ns_touchtits.text]":
            call i_ns_touchtits_dialogue
            $ i_ns_touchtits.seen = True
        "Jerk off[i_ns_jerkoff.text]":


            call i_ns_jerkoff_dialogue
            $ i_ns_jerkoff.seen = True
        "Use hand[i_ns_usehand.text]":


            call i_ns_usehand_dialogue
            $ i_ns_usehand.seen = True


        "Use feet[i_ns_usefeet.text]" if i_ns_usefeet.unlocked:
            call i_ns_usefeet_dialogue
            $ i_ns_usefeet.seen = True
        "Use feet (locked)" if not i_ns_usefeet.unlocked:
            pass


        "Rub pussy[i_ns_rubpussy.text]" if i_ns_rubpussy.unlocked:
            call i_ns_rubpussy_dialogue
            $ i_ns_rubpussy.seen = True
        "Rub pussy (locked)" if not i_ns_rubpussy.unlocked:
            pass


        "Assjob[i_ns_assjob.text]" if i_ns_assjob.unlocked:
            call i_ns_assjob_dialogue
            $ i_ns_assjob.seen = True
        "Assjob (locked)" if not i_ns_assjob.unlocked:
            pass



    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    $ isabel_night_counter += 1
    $ isabel_visited_tonight = True
    $ go_to(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
