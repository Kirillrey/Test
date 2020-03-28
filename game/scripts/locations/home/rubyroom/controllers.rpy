label home_rubyroom:


    if time.is_morning():

        if ruby_level == 5:
            call ruby_5_dressup_dialogue
            $ ruby_level = 6
            $ ruby_massage_level = 2
            $ increase_time()
            $ mp_notify("Ruby - New Massage Level Unlocked!")
            $ go_to(L_home_rubyroom)

        elif ruby_level == 8:
            call ruby_8_chorehotdog_dialogue
            $ ruby_level = 9
            $ ruby_massage_level = 3
            $ increase_time()
            $ mp_notify("Ruby - New Massage Level Unlocked!")
            $ go_to(L_home_rubyroom)


    elif time.is_evening():

        if ruby_level == 9:
            call ruby_9_pillowfight_dialogue
            $ ruby_level = 10
            $ r_ns_assjob.unlocked = True
            $ increase_time()
            $ go_to(L_home_basement)


    elif time.is_night():

        if ruby_visited_tonight:
            mc "(I shouldn't disturb her anymore tonight.)"
            $ go_to(L_home_hall)


    if time.is_morning() or time.is_afternoon():

        if ruby_level == 12:
            call ruby_12_spanking2_dialogue
            $ ruby_level = 13
            $ persistent._seen_ever["extra_06_ruby_shave"] = True
            $ increase_time()
            $ go_to(L_home_hall)




    if time.is_morning() and dad_level >= 2:
        scene home_rubyroom__morning_ruby_ground
    elif time.is_morning():
        scene prologue arrival ruby 1
    elif time.is_afternoon():
        scene home_rubyroom__day_ground
    elif time.is_evening():
        scene home_rubyroom__night_ground
    elif time.is_night():
        scene home_rubyroom__night_ruby_ground







    call screen home_rubyroom





label home_rubyroom_morning_rubysleep:

    if ruby_level == 10 and dad_level >= 2:
        call ruby_10_spanking_dialogue
        $ ruby_level = 11
        $ ruby_massage_level = 4
        $ persistent._seen_ever["elite_05_ruby_dinner3"] = True
        $ increase_time()
        $ mp_notify("Ruby - New Massage Level Unlocked!")
        $ go_to(L_home_hall)
    else:

        mc "(I probably shouldn't wake her up...)"
        $ go_to(L_home_rubyroom)





label home_rubyroom_rubysleep:

    if (r_ns_gropeass.unlocked and not r_ns_gropeass.seen) or (r_ns_assjob.unlocked and not r_ns_assjob.seen):
        $ temp_1 = " (New)!"
    else:
        $ temp_1 = ""
    call r_ns_intro_dialogue

    menu:
        "Pull down shorts[temp_1]":
            call r_ns_pulldownshorts_dialogue

            menu:
                "Grope ass[r_ns_gropeass.text]":
                    call r_ns_gropeass_dialogue
                    $ r_ns_gropeass.seen = True


                "Assjob[r_ns_assjob.text]" if r_ns_assjob.unlocked:
                    call r_ns_assjob_dialogue
                    $ r_ns_assjob.seen = True
                "Assjob (locked)" if not r_ns_assjob.unlocked:
                    pass
        "Jerk off[r_ns_jerkoff.text]":


            call r_ns_jerkoff_dialogue
            $ r_ns_jerkoff.seen = True
        "Use feet[r_ns_usefeet.text]":


            call r_ns_usefeet_dialogue
            $ r_ns_usefeet.seen = True


        "Finger pussy[r_ns_fingerpussy.text]" if r_ns_fingerpussy.unlocked:
            call r_ns_fingerpussy_dialogue
            $ r_ns_fingerpussy.seen = True
        "Finger pussy (locked)" if not r_ns_fingerpussy.unlocked:
            pass



    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    $ ruby_night_counter += 1
    $ ruby_visited_tonight = True
    $ go_to(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
