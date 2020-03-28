screen home_pool():

    default path = "locations/home/pool/home_pool__"


    if time.is_morning():
        imagemap:
            ground path + "day_logan_ground.png"
            idle path + "day_logan_idle.png"
            hover im.MatrixColor(path + "day_logan_idle.png", im.matrix.brightness(0.25))

            hotspot (136, 352, 392, 276) action Jump("home_pool_logan")


    if L_home_pool.can_leave:
        imagebutton align (0.06, 0.7) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_home_kitchen)


    if L_home_pool.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
