label thorneoffice_office:


    if time.is_morning() or time.is_afternoon():

        if thorne_level == 2:
            call thorne_2_lawyer_dialogue
            $ thorne_level = 3
            $ laptop_owned = True
            $ money = 15
            $ increase_time()
            $ go_to(L_home_basement)


        elif thorne_level == 3:
            call thorne_3_gettingcar_dialogue
            $ thorne_level = 4
            $ increase_time()
            $ go_to(L_home_basement)


        elif thorne_level == 4:
            call thorne_4_negotiation_dialogue
            $ thorne_level = 5
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif thorne_level == 6:
            call thorne_6_clubofficeintro_dialogue
            $ thorne_level = 7
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif thorne_level == 8:
            call thorne_8_givepills_dialogue
            $ thorne_level = 9
            $ increase_time()
            $ go_to(L_home_livingroom)



    elif time.is_night():

        if eliana_level == 3:
            call eliana_3_breakin_dialogue
            $ eliana_level = 4
            $ thorne_office_unlocked = True
            $ go_to(L_thorneoffice_office)




    if time.is_morning():
        scene thorneoffice_office__day_thorne_ground

    elif time.is_afternoon() and thorne_office_unlocked:
        scene thorneoffice_office__day_ground
    elif time.is_afternoon():
        scene thorneoffice_office_door_day with fade
        mc "(Hm, looks like Thorne isn't here. And his door is locked...)"

    elif time.is_evening() and thorne_office_unlocked:
        scene thorneoffice_office__evening_ground
    elif time.is_night() and thorne_office_unlocked:
        scene thorneoffice_office__night_ground
    elif time.is_time(3, 4):
        scene thorneoffice_office_door_night with fade
        mc "(Hm, looks like Thorne isn't here. And his door is locked...)"


    call screen thorneoffice_office
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
