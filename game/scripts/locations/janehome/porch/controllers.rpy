label janehome_porch:


    if time.is_time(1, 2):
        scene janehome_porch__day_ground
    else:
        scene janehome_porch__night_ground


    call screen janehome_porch






label janehome_porch_door:

    if jane_level == 8:
        call jane_8_frontdoor_dialogue
        $ jane_level = 9
        $ L_janehome_porch.can_leave = True


    elif jane_level == 11 and jane_vibrator.own_item:
        if time.is_time(1, 2):
            call jane_11_gifttoy_dialogue
            $ jane_level = 12
            $ jane_vibrator.used = True
        else:
            mc "(I can't put the gift in front of her door when she's home! I need to come back when she isn't here.)"

    $ go_to(L_janehome_porch)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
