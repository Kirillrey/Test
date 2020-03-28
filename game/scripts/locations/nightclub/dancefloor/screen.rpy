screen nightclub_dancefloor():

    default path = "locations/nightclub/dancefloor/nightclub_dancefloor__"


    imagemap:

        if not nc1_melissa:
            ground path + "melissa_ground.png"
            idle path + "melissa_idle.png"
            hover im.MatrixColor(path + "melissa_idle.png", im.matrix.brightness(0.2))

            hotspot (920, 340, 210, 631) action Jump("nightclub_dancefloor_melissa")

        else:



            ground path + "melissa_ground.png"
            idle path + "melissa_idle.png"
            hover im.MatrixColor(path + "melissa_idle.png", im.matrix.brightness(0.2))


    if L_nightclub_dancefloor.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_nightclub_bar)
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_nightclub_lounge)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
