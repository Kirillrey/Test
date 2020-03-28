screen school_hall():

    default path = "locations/school/hall/school_hall__"


    if L_school_hall.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_school_janeoffice)
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_school_library)
        imagebutton align (0.65, 0.42) auto "gui/themes/arrowright_%s.png" action MoveTo(L_school_entrance)


    if L_school_hall.toolbar_enabled and all_toolbars_enabled:
        use onlymorningskip_toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
