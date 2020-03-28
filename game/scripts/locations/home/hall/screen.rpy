screen home_hall():

    default path = "locations/home/hall/home_hall__"


    imagemap:

        if time.is_morning() or time.is_afternoon():
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

        else:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.15))


        hotspot (115, 309, 185, 600) action MoveTo(L_home_rubyroom)
        hotspot (539, 343, 88, 413) action MoveTo(L_home_isabelroom)
        hotspot (980, 350, 157, 374) action MoveTo(L_home_momroom)
        hotspot (1318, 343, 316, 413) action MoveTo(L_home_bathroom)
        hotspot (1501, 842, 348, 43) action MoveTo(L_home_livingroom) focus_mask None


    if L_home_hall.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
