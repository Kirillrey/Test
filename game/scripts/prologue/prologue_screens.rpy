screen prologue_kitchen():

    default path = "locations/home/kitchen/home_kitchen__"

    if prologue_mom == 0:
        imagemap alpha False:
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

            hotspot (228, 848, 258, 219) action Jump("prologue_livingroom")
    else:
        imagemap alpha False:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))

            hotspot (228, 848, 258, 219) action Jump("prologue_livingroom")





screen prologue_livingroom():

    default path = "locations/home/livingroom/home_livingroom__"

    if prologue_mom == 0:
        imagemap alpha False:
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.2))

            hotspot (80, 530, 224, 91) action Jump("prologue_hall")
            hotspot (91, 673, 221, 89) action Jump("prologue_hall2")
            hotspot (1587, 715, 250, 104) action Jump("prologue_kitchen")

    elif prologue_mom == 1:
        imagemap:
            ground path + "evening_isabel_ground.png"
            idle path + "evening_isabel_idle.png"
            hover im.MatrixColor(path + "evening_isabel_idle.png", im.matrix.brightness(0.2))

            hotspot (80, 530, 224, 91) focus_mask None action Jump("prologue_hall")
            hotspot (91, 673, 221, 89) focus_mask None action Jump("prologue_hall2")
            if prologue_isabel == 1:
                hotspot (769, 483, 196, 134) action Jump("prologue_livingroom_isabel")
            hotspot (1587, 715, 250, 104) focus_mask None action Jump("prologue_kitchen")

    else:
        imagemap alpha False:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.2))

            hotspot (80, 530, 224, 91) action Jump("prologue_hall")
            hotspot (91, 673, 221, 89) action Jump("prologue_hall2")
            hotspot (1587, 715, 250, 104) action Jump("prologue_kitchen")





screen prologue_hall():

    default path = "locations/home/hall/home_hall__"

    if prologue_mom == 0:
        imagemap:
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

            if prologue_ruby == 0:
                hotspot (115, 309, 185, 600) action Jump("prologue_rubyroom")
            if not seen_hall_wallphoto:
                hotspot (341, 325, 180, 352) action Jump("prologue_hall_wallphoto")
            if prologue_isabel == 0:
                hotspot (539, 343, 88, 413) action Jump("prologue_isabelroom")
                hotspot (1318, 343, 316, 413) action Jump("prologue_bathroom")
            hotspot (1501, 842, 348, 43) focus_mask None action Jump("prologue_livingroom")

    else:
        imagemap:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.15))
            if prologue_ruby < 3:
                hotspot (115, 309, 185, 600) action Jump("prologue_rubyroom")
            if not seen_hall_wallphoto:
                hotspot (341, 325, 180, 352) action Jump("prologue_hall_wallphoto")
            if prologue_isabel < 3:
                hotspot (539, 343, 88, 413) action Jump("prologue_isabelroom")
            if prologue_mom < 3:
                hotspot (980, 350, 157, 374) action Jump("prologue_momroom")
            hotspot (1318, 343, 316, 413) action Jump("prologue_bathroom")
            hotspot (1501, 842, 348, 43) focus_mask None action Jump("prologue_livingroom")





screen prologue_hall2():

    default path = "locations/home/hall2/home_hall2__"

    if prologue_mom == 0:
        imagemap:
            ground path + "day_ground.png"
            idle path + "day_idle.png"
            hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.15))

            if not seen_hall2_wallphoto:
                hotspot (711, 293, 228, 291) action Jump("prologue_hall2_wallphoto")
            hotspot (1065, 948, 329, 117) focus_mask None action Jump("prologue_livingroom")

    elif prologue_mom == 1:
        imagemap:
            ground path + "evening_ground.png"
            idle path + "evening_idle.png"
            hover im.MatrixColor(path + "evening_idle.png", im.matrix.brightness(0.15))

            if not seen_hall2_wallphoto:
                hotspot (711, 293, 228, 291) action Jump("prologue_hall2_wallphoto")
            hotspot (1446, 264, 177, 519) action Jump("prologue_basement")
            hotspot (1065, 948, 329, 117) focus_mask None action Jump("prologue_livingroom")

    else:
        imagemap:
            ground path + "night_ground.png"
            idle path + "night_idle.png"
            hover im.MatrixColor(path + "night_idle.png", im.matrix.brightness(0.15))

            if not seen_hall2_wallphoto:
                hotspot (711, 293, 228, 291) action Jump("prologue_hall2_wallphoto")
            if prologue_logan < 1:
                hotspot (1008, 264, 131, 510) action Jump("prologue_loganroom")
            hotspot (1446, 264, 177, 519) action Jump("prologue_basement")
            hotspot (1065, 948, 329, 117) focus_mask None action Jump("prologue_livingroom")





screen prologue_basement():

    default path = "locations/home/basement/home_basement__"

    imagemap:
        ground path + "night_nolaptop.jpg"
        idle path + "night_nolaptop_idle.png"
        hover im.MatrixColor(path + "night_nolaptop_idle.png", im.matrix.brightness(0.1))

        hotspot (192, 475, 470, 252) action Jump("prologue_bed")
        if not (prologue_mom == 3 and prologue_isabel == 3 and prologue_ruby == 3 and prologue_logan == 1):
            hotspot (675, 217, 114, 335) action Jump("prologue_hall2")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
