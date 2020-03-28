screen nightclub_bar():

    default path = "locations/nightclub/bar/nightclub_bar__"


    imagemap:

        if nightclub1_complete:
            ground path + "ground.png"
            idle path + "idle.png"
            hover im.MatrixColor(path + "idle.png", im.matrix.brightness(0.2))


            hotspot (1567, 361, 233, 462) action Jump("nightclub_bar_door")
            hotspot (776, 442, 113, 185) action Jump("nightclub_bar_bartender")



        elif nc1_bartender and nc1_melissa and nc1_tanya and nc1_natsuko2:
            ground path + "businessman_ground.png"
            idle path + "businessman_idle.png"
            hover im.MatrixColor(path + "businessman_idle.png", im.matrix.brightness(0.2))

            hotspot (865, 496, 249, 532) action Jump("nightclub_bar_businessman")

        else:
            ground path + "ground.png"
            idle path + "idle.png"
            hover im.MatrixColor(path + "idle.png", im.matrix.brightness(0.2))

            hotspot (443, 707, 207, 350) focus_mask None action Jump("nightclub_bar_chair")
            hotspot (1567, 361, 233, 462) action Jump("nightclub_bar_door")
            if nc1_chair and not nc1_bartender:
                hotspot (776, 442, 113, 185) action Jump("nightclub_bar_bartender")



    if L_nightclub_bar.can_leave:
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_nightclub_dancefloor)



    if L_nightclub_bar.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
