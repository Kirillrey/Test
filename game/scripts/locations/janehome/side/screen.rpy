screen janehome_side():

    default path = "locations/janehome/side/janehome_side__"


    if jane_level == 9 or jane_level == 12:
        imagebutton pos (1403, 385) auto "gui/themes/interact_%s.png" action Jump("janehome_side_window")



    if L_janehome_side.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_janehome_porch)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
