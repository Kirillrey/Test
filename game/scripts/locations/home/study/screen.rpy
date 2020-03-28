screen home_study():

    default path = "locations/home/study/home_study__"


    if L_home_study.can_leave:
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_home_hall2)


    if L_home_study.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
