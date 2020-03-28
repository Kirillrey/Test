label boutique_store:


    if time.is_morning() or time.is_afternoon():

        if ruby_level == 3:
            call ruby_3_storejob_dialogue
            $ ruby_level = 4
            $ increase_time()
            if time.is_afternoon():
                $ go_to(L_boutique_store)
            else:
                $ go_to(L_home_livingroom)


        elif ruby_level == 6:
            if lain_mod and extras_installed:
                call extra_02_jane_store
            else:
                call ruby_6_workshift_dialogue
            $ ruby_level = 7
            $ persistent._seen_ever["extra_02_jane_store"] = True
            $ persistent._seen_ever["extra_03_ruby_masturbate"] = True
            $ increase_time()
            if time.is_afternoon():
                $ go_to(L_boutique_store)
            else:
                $ go_to(L_home_livingroom)


        elif ruby_level == 11:
            call ruby_11_changingroom_dialogue
            $ ruby_level = 12
            $ ruby_massage_level = 5
            $ r_ns_fingerpussy.unlocked = True
            $ increase_time()
            $ mp_notify("Ruby - New Massage & Night Scenes Unlocked!")
            if time.is_afternoon():
                $ go_to(L_boutique_store)
            else:
                $ go_to(L_home_livingroom)




    scene boutique_store__day_manager



    call screen boutique_store
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
