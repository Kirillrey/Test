screen home_basement():

    default path = "locations/home/basement/home_basement__"


    imagemap:

        if time.is_time(1, 2) and laptop_owned:
            ground path + "day.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.2))

        elif time.is_time(1, 2):
            ground path + "day_nolaptop.png"
            idle path + "day_nolaptop_idle.png"
            hover im.MatrixColor(path + "day_nolaptop_idle.png", im.matrix.brightness(0.2))

        elif time.is_time(3, 4) and laptop_owned:
            ground path + "night.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.1))

        elif time.is_time(3, 4):
            ground path + "night_nolaptop.jpg"
            idle path + "night_nolaptop_idle.png"
            hover im.MatrixColor(path + "night_nolaptop_idle.png", im.matrix.brightness(0.1))



        hotspot (194, 475, 468, 190) action Jump("home_basement_bed")

        if L_home_basement.can_leave:
            hotspot (675, 217, 114, 335) action MoveTo(L_home_livingroom)

        if laptop_owned:
            hotspot (911, 370, 138, 73) focus_mask None action Jump("home_basement_laptop")



    if L_home_basement.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
