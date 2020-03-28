





screen toolbar():

    default path = theme_path("top_bar")


    frame:
        xysize (1661, 78)
        align (0.5, 0.0)
        background path + "bg.png"

        text "[store.time_of_day_name]" pos (147, 20) font "gui/fonts/Louis George Cafe.ttf" size 28
        text "[store.money]" pos (452, 20) font "gui/fonts/Louis George Cafe.ttf" size 28
        text "Day [store.day_count]  -  [store.day_of_week_name]" pos (740, 20) font "gui/fonts/Louis George Cafe.ttf" size 28


    if not time.is_night():
        imagebutton:
            auto path + "skiptime_%s.png"
            pos (1080, 18)
            action SkipTime()


    imagebutton:
        auto path + "objective_%s.png"
        pos (1330, 18)
        action ShowMenu("objective_screen")


    imagebutton:
        auto path + "map_%s.png"
        pos (1600, 18)
        action ToggleScreen("map_screen")






screen onlymorningskip_toolbar():

    default path = theme_path("top_bar")


    frame:
        xysize (1661, 78)
        align (0.5, 0.0)
        background path + "bg.png"

        text "[store.time_of_day_name]" pos (147, 20) font "gui/fonts/Louis George Cafe.ttf" size 28
        text "[store.money]" pos (452, 20) font "gui/fonts/Louis George Cafe.ttf" size 28
        text "Day [store.day_count]  -  [store.day_of_week_name]" pos (740, 20) font "gui/fonts/Louis George Cafe.ttf" size 28


    if time.is_morning():
        imagebutton:
            auto path + "skiptime_%s.png"
            pos (1080, 18)
            action SkipTime()


    imagebutton:
        auto path + "objective_%s.png"
        pos (1330, 18)
        action ShowMenu("objective_screen")


    imagebutton:
        auto path + "map_%s.png"
        pos (1600, 18)
        action ToggleScreen("map_screen")







screen map_toolbar():

    default path = theme_path("top_bar")


    frame:
        xysize (1661, 78)
        align (0.5, 0.0)
        background path + "bg.png"

        text "[store.time_of_day_name]" pos (147, 20) font "gui/fonts/Louis George Cafe.ttf" size 28 style_prefix None
        text "[store.money]" pos (452, 20) font "gui/fonts/Louis George Cafe.ttf" size 28 style_prefix None
        text "Day [store.day_count]  -  [store.day_of_week_name]" pos (740, 20) font "gui/fonts/Louis George Cafe.ttf" size 28 style_prefix None


    imagebutton:
        auto path + "objective_%s.png"
        pos (1330, 18)
        action ShowMenu("objective_screen")


    imagebutton:
        auto path + "map_%s.png"
        pos (1600, 18)
        action ToggleScreen("map_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
