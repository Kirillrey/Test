screen home_kitchen():

    default path = "locations/home/kitchen/home_kitchen__"


    imagemap:

        if time.is_morning() and mom_yoga_level > mom_seen_yoga_level:
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

        elif time.is_morning():
            ground path + "day_mom_ground.png"
            idle path + "day_mom_idle.png"
            hover im.MatrixColor(path + "day_mom_idle.png", im.matrix.brightness(0.15))

            hotspot (991, 290, 236, 515) action Jump("home_kitchen_mom")


        elif time.is_afternoon() and ruby_logan_in_kitchen:
            ground path + "day_ruby_ground.png"
            idle path + "day_ruby_idle.png"
            hover im.MatrixColor(path + "day_ruby_idle.png", im.matrix.brightness(0.15))

            hotspot (826, 212, 280, 511) action Jump("home_kitchen_ruby")

        elif time.is_afternoon():
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))


        elif time.is_evening() and ruby_logan_in_kitchen:
            ground path + "evening_logan_ground.png"
            idle path + "evening_logan_idle.png"
            hover im.MatrixColor(path + "evening_logan_idle.png", im.matrix.brightness(0.2))

            hotspot (699, 280, 170, 235) action Jump("home_kitchen_logan")

        elif time.is_evening():
            ground "locations/home/kitchen/home_kitchen_evening_mom.jpg"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))


        else:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))


        if L_home_kitchen.can_leave:
            hotspot (228, 848, 258, 219) action MoveTo(L_home_livingroom) focus_mask None

            if L_home_pool.unlocked:
                hotspot (1526, 256, 323, 441) action MoveTo(L_home_pool) focus_mask None





    if time.is_evening() and not sleeping_pills.used:
        imagebutton pos (847, 416) auto "gui/themes/interact_%s.png" action Jump("home_kitchen_sleepingpillsfood")



    if L_home_kitchen.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
