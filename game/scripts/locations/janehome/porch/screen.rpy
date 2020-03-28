screen janehome_porch():

    default path = "locations/janehome/porch/janehome_porch__"


    if jane_level == 8 or (jane_level == 11 and jane_vibrator.own_item):
        imagebutton pos (1027, 503) auto "gui/themes/interact_%s.png" action Jump("janehome_porch_door")



    if L_janehome_porch.can_leave and time.is_time(3, 4):
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_janehome_side)


    if L_janehome_porch.toolbar_enabled and all_toolbars_enabled:
        use toolbar()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
