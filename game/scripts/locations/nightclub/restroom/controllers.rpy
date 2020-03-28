label nightclub_restroom:


    if nc1_natsuko1 and not nc1_natsuko2:
        scene nightclub_restroom__natsuko_ground
    else:
        scene nightclub_restroom__ground


    call screen nightclub_restroom






label nightclub_restroom_natsuko:
    if not nightclub1_complete:
        call natsuko1_nightclubHj
        $ nc1_natsuko2 = True
        $ L_nightclub_bar.can_leave = False
    $ go_to(L_nightclub_restroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
