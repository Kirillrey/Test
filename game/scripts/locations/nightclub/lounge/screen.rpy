screen nightclub_lounge():

    default path = "locations/nightclub/lounge/nightclub_lounge__"


    imagemap:

        if nightclub1_complete:
            ground path + "tanya_ground.png"
            idle path + "tanya_idle.png"
            hover im.MatrixColor(path + "tanya_idle.png", im.matrix.brightness(0.2))




            if L_nightclub_lounge.can_leave:
                hotspot (63, 360, 99, 265) focus_mask None action MoveTo(L_nightclub_restroom)


        elif not nc1_natsuko1:
            ground path + "natsukotanya_ground.png"
            idle path + "natsukotanya_idle.png"
            hover im.MatrixColor(path + "natsukotanya_idle.png", im.matrix.brightness(0.2))

            hotspot (63, 360, 99, 265) focus_mask None action MoveTo(L_nightclub_restroom)
            hotspot (636, 397, 103, 324) action Jump("nightclub_lounge_natsuko")
            if not nc1_tanya:
                hotspot (1302, 516, 108, 219) action Jump("nightclub_lounge_tanya")

        else:
            ground path + "tanya_ground.png"
            idle path + "tanya_idle.png"
            hover im.MatrixColor(path + "tanya_idle.png", im.matrix.brightness(0.2))

            hotspot (63, 360, 99, 265) focus_mask None action MoveTo(L_nightclub_restroom)
            if not nc1_tanya:
                hotspot (1302, 516, 108, 219) action Jump("nightclub_lounge_tanya")



    if L_nightclub_lounge.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_nightclub_dancefloor)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
