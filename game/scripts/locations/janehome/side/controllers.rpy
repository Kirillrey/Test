label janehome_side:

    scene janehome_side__night_ground


    call screen janehome_side






label janehome_side_window:

    if jane_level == 9:
        call jane_9_masturbate_dialogue
        $ jane_level = 10
        $ L_janehome_porch.toolbar_enabled = True
        $ increase_time()

    elif jane_level == 12:
        call jane_12_masturbate2_dialogue
        $ jane_level = 13
        $ increase_time()

    $ go_to(L_janehome_side)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
