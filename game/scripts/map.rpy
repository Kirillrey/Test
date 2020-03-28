image map_bg = "gui/themes/default/map/bg.jpg"




screen map_screen():
    modal True
    default path = theme_path("map")
    add path + "bg.jpg"
    style_prefix "map_screen"


    button:
        text "Harding Residence"
        pos (100, 800)
        action [Function(clear_map), Hide("map_screen"), MoveTo(L_home_livingroom)]

        xysize (64, 64)
        idle_background path + "map_idle.png"
        hover_background path + "map_hover.png"
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"



    if thorne_level >= 2:
        button:
            text "Thorne's Office"
            pos (800, 530)
            action [Function(clear_map), Hide("map_screen"), MoveTo(L_thorneoffice_office)]

            xysize (64, 64)
            idle_background path + "map_idle.png"
            hover_background path + "map_hover.png"
            hover_sound "audio/sfx/hover.wav"
            activate_sound "audio/sfx/click.ogg"



    if jane_level >= 10:
        button:
            text "Ms{k=7.0}.{/k}Jane's Home"
            pos (300, 150)
            action [Function(clear_map), Hide("map_screen"), MoveTo(L_janehome_porch)]

            xysize (64, 64)
            idle_background path + "map_idle.png"
            hover_background path + "map_hover.png"
            hover_sound "audio/sfx/hover.wav"
            activate_sound "audio/sfx/click.ogg"



    if time.is_morning() or time.is_afternoon():

        button:
            text "Midnight University"
            pos (1300, 630)
            action [Function(clear_map), Hide("map_screen"), MoveTo(L_school_entrance)]

            xysize (64, 64)
            idle_background path + "map_idle.png"
            hover_background path + "map_hover.png"
            hover_sound "audio/sfx/hover.wav"
            activate_sound "audio/sfx/click.ogg"

        if thorne_level == 1:
            button:
                text "Streets" yoffset 30
                pos (250, 500)
                action [Function(clear_map), Hide("map_screen"), MoveTo(L_streets_street)]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

        if ruby_level >= 3:
            button:
                text "Boutique" yoffset 30
                pos (1383, 938)
                action [Function(clear_map), Hide("map_screen"), MoveTo(L_boutique_store)]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

        if aunt_level == 2 and eliana_level >= 6:
            button:
                text "Aunt's Home"
                pos (150, 150)
                action [Function(clear_map), Hide("map_screen"), Jump("aunt_house_controller")]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"



    if time.is_afternoon():

        if thorne_level == 9:
            button:
                text "Streets" yoffset 30
                pos (250, 500)
                action [Function(clear_map), Hide("map_screen"), MoveTo(L_streets_street)]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"



    if time.is_night():

        if thorne_level >= 7 and eliana_level != 3:
            button:
                text "Nightclub" yoffset 30
                pos (650, 150)
                action [Function(clear_map), Hide("map_screen"), MoveTo(L_nightclub_bar)]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

        if aunt_level >= 3:
            button:
                text "Aunt's Home"
                pos (150, 150)
                action [Function(clear_map), Hide("map_screen"), Jump("aunt_house_controller")]

                xysize (64, 64)
                idle_background path + "map_idle.png"
                hover_background path + "map_hover.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"



    use map_toolbar()





style map_screen_text is text:
    size 16
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    align (0.5, 1.0)
    yoffset 50
    text_align 0.5




init python:
    def clear_map():
        renpy.scene()
        renpy.show("map_bg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
