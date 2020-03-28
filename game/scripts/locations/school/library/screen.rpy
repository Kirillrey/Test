screen school_library():

    default path = "locations/school/library/school_library__"


    if L_school_library.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_school_hall)


    if L_school_library.toolbar_enabled and all_toolbars_enabled:
        use onlymorningskip_toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
