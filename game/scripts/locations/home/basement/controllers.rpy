label home_basement:


    if time.is_afternoon() or time.is_evening():

        if renpy.variant("mobile") and laptop_owned and L_home_basement.first_visit:
            scene black
            show home_basement__night
            pause 0.5
            "Hint for Android players: The laptop can be tapped and used to buy things."
            $ L_home_basement.first_visit = False



    if time.is_morning():

        if sleeping_pills.check_morning_event():
            call deliver_sleepingpills_dialogue
            $ sleeping_pills.own_item = True

        elif isabel_sunscreen.check_morning_event():
            call deliver_sunscreen_dialogue
            $ isabel_sunscreen.own_item = True

        elif jane_vibrator.check_morning_event():
            call deliver_vibrator_dialogue
            $ jane_vibrator.own_item = True



        elif ruby_level == 4:
            call ruby_4_textintrodressup_dialogue
            $ ruby_level = 5


        elif mom_level == 5 and thorne_level >= 4:
            call mom_5_carbreakdown_dialogue
            $ mom_level = 6
            $ mom_massage_level = 3
            $ mom_yoga_level = 3
            $ mom_delay = 3
            $ persistent._seen_ever["elite_03_mom_dinner2"] = True
            $ persistent._seen_ever["elite_03_jenna_pool"] = True
            $ increase_time()
            $ mp_notify("Mom - New Yoga & Massage Levels Unlocked!")
            $ go_to(L_home_livingroom)


        elif thorne_level == 5 and ruby_level == 10:
            call thorne_5_clubtextmessage_dialogue
            $ thorne_level = 6


        elif eliana_level == 1 and nightclub1_complete:
            call eliana_1_meeting_dialogue
            $ eliana_level = 2
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif eliana_level == 2 and tanya_level >= 2:
            call eliana_2_talkplan_dialogue
            $ eliana_level = 3
            $ increase_time()
            $ go_to(L_home_basement)


        elif eliana_level == 4:
            call eliana_4_lead_dialogue
            $ eliana_level = 5
            $ persistent._seen_ever["extra_05_isabelRuby_pool"] = True
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif jane_level == 13:
            call jane_13_textmessage_dialogue
            $ jane_level = 14



    elif time.is_afternoon():

        if eliana_level == 5 and aunt_level == 2:
            call eliana_5_pooltalk_dialogue
            $ eliana_level = 6
            $ increase_time()
            $ go_to(L_home_basement)


        elif isabel_level == 8 and eliana_level >= 6:
            call isabel_8_relationshiptalk_dialogue
            $ isabel_level = 9
            $ isabel_massage_level = 5
            $ i_ns_rubpussy.unlocked = True
            $ i_ns_assjob.unlocked = True
            $ increase_time()
            $ mp_notify("Isabel - New Massage & Night Scenes Unlocked!")
            $ go_to(L_home_basement)



    elif time.is_evening():

        if isabel_level == 4 and thorne_level >= 4:
            call isabel_4_carpickup_dialogue
            $ isabel_level = 5
            $ isabel_delay = 2
            $ i_ns_usefeet.unlocked = True
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif mom_level == 8:
            call mom_8_morningjerkoff_dialogue
            $ mom_level = 9
            call setup_next_day
            $ go_to(L_home_livingroom)



    elif time.is_night():

        if tanya_level == 1 and thorne_level >= 10:
            call tanya_1_nightmeeting_dialogue
            $ tanya_level = 2
            $ go_to(L_home_livingroom)





    if time.is_time(1, 2) and laptop_owned:
        scene home_basement__day
    elif time.is_time(1, 2):
        scene home_basement__day_nolaptop
    elif time.is_time(3, 4) and laptop_owned:
        scene black
        show home_basement__night
    elif time.is_time(3, 4):
        scene home_basement__night_nolaptop



    call screen home_basement






label home_basement_bed:

    if not time.is_night():
        mc "(I'm not tired right now.)"


    elif natsuko_level == 1 and eliana_level >= 6:
        mc "Time for me to get some sleep."
        scene black with Fade(0.5, 1.2, 0.0)

        call natsuko_1_nightkitchen_dialogue
        $ natsuko_level = 2
        $ persistent._seen_ever["extra_06_tanya_boobs"] = True

        scene black
        show home_basement__night
        with fade
        call home_basement_bed_sleep_dialogue
        call setup_next_day
    else:


        call home_basement_bed_sleep_dialogue
        call setup_next_day

    $ go_to(L_home_basement)






label setup_next_day:
    python:
        time_of_day = 1
        time_of_day_name = time_of_day_names[time_of_day]

        day_of_week = (day_of_week + 1) % 7
        day_of_week_name = day_of_week_names[day_of_week]

        if time.is_weekday():
            days_since_been_to_class += 1

        day_count += 1

        mom_visited_tonight = False
        isabel_visited_tonight = False
        ruby_visited_tonight = False
        aunt_visited_tonight = False
        logan_insulted = False

        if mom_delay > 0:
            mom_delay -= 1

        if isabel_delay > 0:
            isabel_delay -= 1

        sleeping_pills.calc_delivery()
        isabel_sunscreen.calc_delivery()
        jane_vibrator.calc_delivery()

        lain_mod_saw_laptop_scene = False

    return






label home_basement_laptop:

    if sleeping_pills.purchased and isabel_sunscreen.purchased and jane_vibrator.purchased and not lain_mod:
        mc "(There's nothing to do right now.)"
        "--- Under Development ---"
        $ go_to(L_home_basement)

    elif lain_mod_saw_laptop_scene:
        mc "(That was super embarrassing... I should just go to bed.)"
        $ go_to(L_home_basement)


    menu:
        "Order sleeping pills" if not sleeping_pills.purchased:
            $ sleeping_pills.buy()
            call purchase_sleepingpills_dialogue

        "Buy sunscreen" if isabel_level >= 6 and not isabel_sunscreen.purchased:
            $ isabel_sunscreen.buy()
            call purchase_sunscreen_dialogue

        "Buy vibrator" if jane_level == 11 and not jane_vibrator.purchased:
            if money >= 100:
                $ jane_vibrator.buy()
                call purchase_vibrator_dialogue
            else:
                mc "(I don't have enough money to buy that gift...)"

        "Watch porn" if lain_mod and time.is_night():
            $ temp_1 = renpy.random.randint(1, 3)
            call lain_mod_laptop_jerkoff
            $ lain_mod_saw_laptop_scene = True
        "Exit":

            $ go_to(L_home_basement)


    $ increase_time()
    $ go_to(L_home_basement)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
