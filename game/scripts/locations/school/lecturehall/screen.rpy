screen school_lecturehall():

    default path = "locations/school/lecturehall/school_lecturehall__"


    if L_school_lecturehall.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_school_entrance)


    if L_school_lecturehall.toolbar_enabled and all_toolbars_enabled:
        use onlymorningskip_toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
