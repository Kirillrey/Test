screen school_janeoffice():

    default path = "locations/school/janeoffice/school_janeoffice__"


    if time.is_afternoon() and time.day_count() != 1 and not jane_on_sick_leave:
        imagemap:
            ground path + "afternoon_jane_ground.png"
            idle path + "afternoon_jane_idle.png"
            hover im.MatrixColor(path + "afternoon_jane_idle.png", im.matrix.brightness(0.2))

            hotspot (794, 408, 213, 188) focus_mask None action Jump("school_janeoffice_msjane")


    if L_school_janeoffice.can_leave:
        if time.is_afternoon():
            imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_school_entrance)
        elif not time.is_evening():
            imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_school_hall)


    if L_school_janeoffice.toolbar_enabled and all_toolbars_enabled:
        use onlymorningskip_toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
