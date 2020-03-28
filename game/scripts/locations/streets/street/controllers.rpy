label streets_street:


    if time.is_morning() or time.is_afternoon():

        if thorne_level == 1:
            call thorne_1_kyleenvelopesjail_dialogue
            $ thorne_level = 2
            $ set_time(4)
            $ go_to(L_home_basement)


    if time.is_afternoon():

        if thorne_level == 9:
            call thorne_9_cartheft_dialogue
            $ thorne_level = 10
            $ money += 20000
            $ increase_time()
            $ go_to(L_home_livingroom)




    scene streets_street__day_ground



    call screen streets_street
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
