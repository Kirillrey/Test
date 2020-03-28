screen home_isabelroom():

    default path = "locations/home/isabelroom/home_isabelroom__"


    if time.is_night() and not isabel_visited_tonight:
        imagemap:
            ground path + "night_isabel_ground.png"
            idle path + "night_isabel_idle.png"
            hover im.MatrixColor(path + "night_isabel_idle.png", im.matrix.brightness(0.11))

            hotspot (528, 569, 760, 511) action Jump("home_isabelroom_isabelsleep")


    if L_home_isabelroom.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
