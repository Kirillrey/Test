screen home_livingroom():

    default path = "locations/home/livingroom/home_livingroom__"


    imagemap:
        alpha False

        if time.is_morning() or time.is_afternoon():
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.2))

            if time.is_afternoon():
                hotspot (648, 615, 322, 127) action Jump("home_livingroom_tv") focus_mask True

        elif time.is_evening() and not ((mom_level == 3 or isabel_level == 1) and mom_massage_counter > 0 and isabel_massage_counter > 0 and isabel_tv_counter > 0 and mom_tv_counter > 0):
            ground path + "evening_isabel_ground.png"
            idle path + "evening_isabel_idle.png"
            hover im.MatrixColor(path + "evening_isabel_idle.png", im.matrix.brightness(0.2))

            hotspot (769, 483, 196, 134) action Jump("home_livingroom_isabel") focus_mask True

        elif time.is_evening():
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))

        elif time.is_night():
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))

            if (isabel_level == 5 or isabel_level == 7) and isabel_delay == 0:
                hotspot (648, 615, 322, 127) action Jump("home_livingroom_tv_night") focus_mask True



        if L_home_livingroom.can_leave:
            hotspot (80, 530, 224, 91) action MoveTo(L_home_hall)
            hotspot (91, 673, 221, 89) action MoveTo(L_home_hall2)
            hotspot (1587, 715, 250, 104) action MoveTo(L_home_kitchen)



    if L_home_livingroom.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
