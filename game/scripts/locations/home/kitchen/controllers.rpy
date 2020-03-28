label home_kitchen:


    if time.is_morning():

        if ruby_level == 7:
            call ruby_7_choresargument_dialogue
            $ ruby_level = 8
            $ go_to(L_home_kitchen)

        if dad_level == 1 and nightclub1_complete:
            call dad_1_rent_dialogue
            $ dad_level = 2
            $ money -= 1500
            $ go_to(L_home_kitchen)



    elif time.is_afternoon():

        if mom_level == 7:
            call mom_7_movienight_dialogue
            $ mom_level = 8
            $ mom_massage_level = 4
            call setup_next_day
            if mom_yoga_level > mom_seen_yoga_level:
                $ set_time(2)
            $ mp_notify("Mom - New Massage Level Unlocked!")
            $ go_to(L_home_momroom)

        elif lain_mod and elite_installed and aunt_level >= 3 and not lm_elite_06_momAunt_cooking:
            call elite_06_momAunt_cooking
            $ lm_elite_06_momAunt_cooking = True
            $ increase_time()
            $ go_to(L_home_kitchen)



    elif time.is_evening():

        if (mom_level == 3 or isabel_level == 1) and mom_massage_counter > 0 and isabel_massage_counter > 0 and isabel_tv_counter > 0 and mom_tv_counter > 0:
            call mom_3_isabel_1_homedrinking_dialogue
            menu:
                "Go with Mom" if mom_level == 3:
                    call mom_3_homedrinkingmom_dialogue
                    $ mom_level = 4
                    $ persistent._seen_ever["elite_02_mom_dinner1"] = True
                    $ increase_time()
                    $ go_to(L_home_hall)

                "Stay with Isabel" if isabel_level == 1:
                    call isabel_1_homedrinkingisabel_dialogue
                    $ isabel_level = 2
                    $ persistent._seen_ever["extra_02_isabel_lotion"] = True
                    call setup_next_day
                    $ go_to(L_home_isabelroom)




    if time.is_morning() and mom_yoga_level > mom_seen_yoga_level:
        scene home_kitchen__day
    elif time.is_morning():
        scene home_kitchen__day_mom

    elif time.is_afternoon() and ruby_logan_in_kitchen:
        scene home_kitchen__day_ruby
    elif time.is_afternoon():
        scene home_kitchen__day

    elif time.is_evening() and ruby_logan_in_kitchen:
        scene black
        show home_kitchen__evening_logan
    elif time.is_evening():
        scene home_kitchen_evening_mom

    elif time.is_night():


        scene home_kitchen__night_ground



    call screen home_kitchen






label home_kitchen_mom:
    menu:
        "Talk About Night" if mom_level == 4:
            call mom_4_afterdrink_dialogue
            $ mom_level = 5
            $ mom_massage_level = 2
            $ increase_time()
            $ mp_notify("Mom - New Massage Level Unlocked!")
            $ go_to(L_home_kitchen)
        "Massage":

            jump mom_massage_controller
        "Yoga":

            jump mom_yoga_controller
        "Exit":

            $ go_to(L_home_kitchen)






label home_kitchen_ruby:
    menu:
        "Ruby's Job" if ruby_level == 2:
            call ruby_2_askjob_dialogue
            $ ruby_level = 3
            $ increase_time()
            $ go_to(L_home_kitchen)
        "Massage":

            jump ruby_massage_controller
        "Exit":

            $ go_to(L_home_kitchen)






label home_kitchen_logan:

    if logan_insulted:
        mc "(I don't want to talk to him right now.)"
    else:
        $ temp_1 = renpy.random.randint(1, 8)
        call logan_insults_kitchen_dialogue
        $ logan_insulted = True

    $ go_to(L_home_kitchen)






label home_kitchen_sleepingpillsfood:
    if sleeping_pills.own_item:
        call mom_2_sleepingpillsfood_dialogue
        $ mom_level = 3
        $ mom_yoga_level = 2
        $ ruby_level = 2
        $ ruby_logan_in_kitchen = True
        $ sleeping_pills.used = True
        $ increase_time()
        $ go_to(L_home_basement)
    else:

        mc "(I think I have an idea on how I could get into Mom's room at night.)"
        if thorne_level == 1:
            mc "(I need some money first though. Kyle said he had a simple job lined up for me, I should go downtown tomorrow and see what he wants.)"
        elif not laptop_owned:
            mc "(I still need some money first though. Maybe I should go check out that Thorne guy's office tomorrow.)"
        elif not sleeping_pills.purchased:
            mc "(I need to order something online using my laptop first though.)"
        elif not sleeping_pills.own_item:
            mc "(When those sleeping pills are delivered I could slip them into Dad's food at night!)"
            mc "(I just wish they'd get here faster...)"
        $ go_to(L_home_kitchen)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
