screen home_hall2():

    default path = "locations/home/hall2/home_hall2__"


    imagemap:

        if time.is_morning() or time.is_afternoon():
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

        elif time.is_evening():
            ground path + "evening_ground.png"
            idle path + "evening_idle.png"
            hover im.MatrixColor(path + "evening_idle.png", im.matrix.brightness(0.15))

        else:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.15))


        if L_home_study.unlocked:
            hotspot (155, 251, 462, 702) action MoveTo(L_home_study)
        if L_home_loganroom.unlocked:
            hotspot (1008, 264, 131, 510) action MoveTo(L_home_loganroom)
        hotspot (1446, 264, 177, 519) action MoveTo(L_home_basement)
        hotspot (1065, 948, 329, 117) action MoveTo(L_home_livingroom) focus_mask None


    if L_home_hall2.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
