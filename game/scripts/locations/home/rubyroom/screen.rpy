screen home_rubyroom():

    default path = "locations/home/rubyroom/home_rubyroom__"



    if time.is_morning() and dad_level >= 2:
        imagemap:
            ground path + "morning_ruby_ground.png"
            idle path + "morning_ruby_idle.png"
            hover im.MatrixColor(path + "morning_ruby_idle.png", im.matrix.brightness(0.2))

            hotspot (712, 536, 734, 448) action Jump("home_rubyroom_morning_rubysleep")


    elif time.is_night() and not ruby_visited_tonight:
        imagemap:
            ground path + "night_ruby_ground.jpg"
            idle path + "night_ruby_idle.png"
            hover im.MatrixColor(path + "night_ruby_idle.png", im.matrix.brightness(0.12))

            hotspot (854, 589, 553, 271) action Jump("home_rubyroom_rubysleep")



    if L_home_rubyroom.can_leave:
        imagebutton align (0.06, 0.9) auto "gui/themes/arrowleft_%s.png" action MoveTo(L_home_hall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
