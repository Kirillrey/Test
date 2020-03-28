screen nightclub_restroom():

    default path = "locations/nightclub/restroom/nightclub_restroom__"


    imagemap:

        if nc1_natsuko1 and not nc1_natsuko2:
            ground path + "natsuko_ground.png"
            idle path + "natsuko_idle.png"
            hover im.MatrixColor(path + "natsuko_idle.png", im.matrix.brightness(0.2))

            hotspot (1248, 337, 145, 408) action Jump("nightclub_restroom_natsuko")

        else:
            ground path + "ground.png"
            idle path + "idle.png"
            hover im.MatrixColor(path + "idle.png", im.matrix.brightness(0.2))


            if L_nightclub_restroom.can_leave:
                hotspot (658, 279, 107, 453) focus_mask None action MoveTo(L_nightclub_lounge)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
