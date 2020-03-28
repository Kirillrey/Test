screen school_entrance():

    default path = "locations/school/entrance/school_entrance__"


    imagemap:
        ground path + "day_ground.jpg"
        idle path + "day_idle.png"
        hover im.MatrixColor(path + "day_idle.png", im.matrix.brightness(0.2))

        if L_school_entrance.can_leave:
            if time.is_afternoon():
                hotspot (595, 433, 189, 231) action MoveTo(L_school_janeoffice)
            else:
                hotspot (595, 433, 189, 231) action MoveTo(L_school_hall)

            hotspot (1217, 461, 162, 191) action MoveTo(L_school_lecturehall)


    if L_school_entrance.toolbar_enabled and all_toolbars_enabled:
        use onlymorningskip_toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
