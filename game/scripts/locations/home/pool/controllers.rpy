label home_pool:


    if time.is_morning() or time.is_afternoon():

        if isabel_massage_level >= 5 and isabel_seen_massage_level == 4:
            call massage_isa_5
            $ isabel_seen_massage_level = 5
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_pool)

        elif lain_mod and extras_installed and isabel_level >= 9 and ruby_level >= 13 and not lm_extra_05_isabelRuby_pool:
            call extra_05_isabelRuby_pool
            $ lm_extra_05_isabelRuby_pool = True
            $ increase_time()
            $ go_to(L_home_pool)



    if time.is_morning():
        scene home_pool__day_logan_ground
    elif time.is_afternoon():
        scene home_pool__day_ground
    elif time.is_evening():
        scene home_pool__evening_dad_ground
    elif time.is_night():
        scene home_pool__night_ground


    call screen home_pool





label home_pool_logan:

    if logan_level == 1:
        call logan_1_poolmorningconflict_dialogue
        $ logan_level = 2
        $ increase_time()

    elif not logan_insulted:
        $ temp_1 = renpy.random.randint(1, 6)
        call logan_insults_pool_dialogue
        $ logan_insulted = True
    else:

        mc "(I don't want to talk to him right now.)"

    $ go_to(L_home_pool)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
