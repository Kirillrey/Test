screen home_momroom():

    default path = "locations/home/momroom/home_momroom__"


    if time.is_morning() and mom_yoga_level > mom_seen_yoga_level:

        imagemap:

            if mom_seen_yoga_level >= 2:
                ground path + "day_momyoga2_ground.png"
                idle path + "day_momyoga2_idle.png"
                hover im.MatrixColor(path + "day_momyoga2_idle.png", im.matrix.brightness(0.2))

                hotspot (360, 319, 273, 761) action Jump("home_momroom_mom_yoga")

            elif mom_seen_yoga_level < 2:
                ground path + "day_momyoga1_ground.png"
                idle path + "day_momyoga1_idle.png"
                hover im.MatrixColor(path + "day_momyoga1_idle.png", im.matrix.brightness(0.2))

                hotspot (357, 319, 276, 761) action Jump("home_momroom_mom_yoga")


    if time.is_night() and mom_night_counter > 0 and not mom_visited_tonight:
        imagemap:
            ground path + "night_mom_ground.png"
            idle path + "night_mom_idle.png"
            hover im.MatrixColor(path + "night_mom_idle.png", im.matrix.brightness(0.11))

            hotspot (952, 477, 906, 338) action Jump("home_momroom_momsleep")



    if L_home_momroom.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
