screen home_bathroom():

    default path = "locations/home/bathroom/home_bathroom__"


    if time.is_morning():
        imagebutton pos (1236, 522) auto "gui/themes/interact_%s.png" action Jump("home_bathroom_isabel")

    elif time.is_evening():
        imagebutton pos (1206, 418) auto "gui/themes/interact_%s.png" action Jump("home_bathroom_ruby")


    if L_home_bathroom.can_leave:
        imagebutton align (0.94, 0.9) auto "gui/themes/arrowright_%s.png" action MoveTo(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
