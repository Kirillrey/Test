label nightclub_lounge:


    if not nc1_natsuko1:
        scene nightclub_lounge__natsukotanya_ground
    else:
        scene nightclub_lounge__tanya_ground


    call screen nightclub_lounge






label nightclub_lounge_tanya:
    if not nightclub1_complete:
        call nc1_tanya_dialogue
        $ nc1_tanya = True
    $ go_to(L_nightclub_lounge)






label nightclub_lounge_natsuko:
    if not nightclub1_complete:
        call nc1_natsuko1_dialogue
        $ nc1_natsuko1 = True
    $ go_to(L_nightclub_lounge)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
