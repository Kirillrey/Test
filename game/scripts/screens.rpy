










init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")



init -1 style button:
    properties gui.button_properties("button")





init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"
    default path = theme_path("textbox")

    window:
        id "window"
        background path + "textbox.png"

        xpos 120
        yoffset -10
        xsize 1680
        ysize 247

        if who is not None:

            window:
                id "namebox"
                has fixed:

                    xpos 334
                    ypos -21
                    xysize (371, 60)

                add path + "namebox.png"
                text who id "who" font "gui/fonts/" + persistent.font_name xoffset 10 color "#ffffff"


        text what id "what" font "gui/fonts/" + persistent.font_name size persistent.font_size xpos 208




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox_label is say_label

init -1 style window:
    yalign gui.textbox_yalign
    ysize gui.textbox_height

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

















init -501 screen choice(items):
    default path = theme_path("textbox")
    default hovering_on = ""

    vbox:
        spacing 22
        xpos 1433
        ypos 744 - (len(items) * 78)

        for i in items:
            $ disabled = i.kwargs.get("disabled", False)

            button:
                xysize (292, 67)
                padding (0, 0, 0, 0)

                background path + "button.png"

                if hovering_on == i.caption and not disabled:
                    add path + "hover.png" xoffset -32
                else:
                    add path + "idle.png" xoffset -32

                text i.caption:
                    xalign 0.5 yalign 0.5
                    if disabled:
                        idle_color "#777"
                        hover_color "#777"


                hovered SetScreenVariable("hovering_on", i.caption)
                unhovered SetScreenVariable("hovering_on", "")
                action If(not disabled, i.action, NullAction())
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"






















































define -1 config.narrator_menu = True






init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = False

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    default path = theme_path("navigation")

    imagebutton:
        idle path + "savegame_idle.png"
        hover path + "savegame_hover.png"
        insensitive path + "savegame_ground.png"

        action ShowMenu("save")
        focus_mask None
        xpos 131
        ypos 929
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "loadgame_idle.png"
        hover path + "loadgame_hover.png"
        insensitive path + "loadgame_ground.png"

        action ShowMenu("load")
        focus_mask None
        xpos 396
        ypos 929
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "settings_idle.png"
        hover path + "settings_hover.png"
        insensitive path + "settings_ground.png"

        action ShowMenu("preferences")
        focus_mask None
        xpos 665
        ypos 929
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "mainmenu_idle.png"
        hover path + "mainmenu_hover.png"
        insensitive path + "mainmenu_ground.png"

        action MainMenu()
        focus_mask None
        xpos 906
        ypos 929
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "return_idle.png"
        hover path + "return_hover.png"
        insensitive path + "return_ground.png"

        action Return()
        focus_mask None
        xpos 1641
        ypos 935
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"







init -501 screen main_menu():
    tag menu
    default path = theme_path("main_menu")
    default items = [
        ["start", Start()],
        ["continue", ShowMenu("load")],
        ["settings", ShowMenu("preferences")],
        ["extra", ShowMenu("scene_gallery")],
        ["about", ShowMenu("about")],
        ["help", ShowMenu("help")],
        ["patreon", OpenURL("https://www.patreon.com/lewdlab")],
        ["exit", Quit()],
    ]



    add path + "bg.png"

    vbox:
        spacing 17
        xpos 162
        ypos 286

        for i, j in items:
            imagebutton:
                idle path + i + "_idle.png"
                hover path + i + "_hover.png"
                insensitive path + i + "_ground.png"
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

                action j

    text "[config.version]" xalign 1.0 yalign 1.0










init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation_old

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









init -501 screen about():
    tag menu


    default path = theme_path("about")
    add path + "bg.png"

    vbox pos (787, 233) maximum (955, 660):
        label "[config.name!t]"
        text _("Version [config.version!t]\n")


        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

    imagebutton:
        idle path + "return_idle.png"
        hover path + "return_hover.png"

        action Return()
        xpos 1494
        ypos 922






define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():

    tag menu

    use file_slots(_("Save"))

init -501 screen load():

    tag menu

    use file_slots(_("Load"))

init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")








init -501 screen preferences(page="text"):

    tag menu

    default path = theme_path("settings")
    default current_page = page

    add path + "bg.png"

    imagebutton:
        idle path + "text_idle.png"
        hover path + "text_hover.png"
        selected_idle path + "text_hover.png"
        selected_hover path + "text_idle.png"

        focus_mask None
        action SetScreenVariable("current_page", "text")
        xpos 1258
        ypos 206
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "audio_idle.png"
        hover path + "audio_hover.png"
        selected_idle path + "audio_hover.png"
        selected_hover path + "audio_idle.png"

        focus_mask None
        action SetScreenVariable("current_page", "audio")
        xpos 1420
        ypos 206
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "gameplay_idle.png"
        hover path + "gameplay_hover.png"
        selected_idle path + "gameplay_hover.png"
        selected_hover path + "gameplay_idle.png"

        focus_mask None
        action SetScreenVariable("current_page", "gameplay")
        xpos 1604
        ypos 206
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"

    default text_buttons = [
        ["serif", SetField(persistent, "font_name", "CrimsonText-Regular.ttf"), 227, 392],
        ["sans", SetField(persistent, "font_name", "Louis George Cafe.ttf"), 568, 392],
        ["normal", SetField(persistent, "font_size", 30), 227, 463],
        ["large", SetField(persistent, "font_size", 40), 568, 463],
        ["enabled", SetField(persistent, "notify_users", True), 629, 776],
        ["disabled", SetField(persistent, "notify_users", False), 971, 776]
    ]
    default gameplay_buttons = [
        ["windowed", Preference("display", "window"), 262, 442],
        ["fullscreen", Preference("display", "fullscreen"), 603, 442],
        ["afterchoices", Preference("after choices", "toggle"), 262, 592],
        ["transitions", InvertSelected(Preference("transitions", "toggle")), 603, 592],
        ["unreadtext", Preference("skip", "toggle"), 262, 664],
        ["monochrome", [SetField(persistent, "current_theme", "monochrome"), ShowMenu("preferences", page="gameplay")], 994, 592],
        ["default", [SetField(persistent, "current_theme", "default"), ShowMenu("preferences", page="gameplay")], 1335, 592]
    ]
    default text_sliders = [
        [Preference("text speed"), 1075, 441],
        [Preference("auto-forward time"), 1075, 649]
    ]
    default music_sliders = [
        [Preference("music volume"), 685, 487],
        [Preference("sound volume"), 685, 702],
    ]

    if current_page == "text":
        add path + "settings_text.png"

        for i, j, x, y in text_buttons:
            imagebutton:
                idle path + i + "_idle.png"
                hover path + i + "_hover.png"
                selected_idle path + i + "_selected_idle.png"
                selected_hover path + i + "_selected_hover.png"
                insensitive path + i + "_ground.png"

                focus_mask None
                action j
                xpos x
                ypos y
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

        for j, x, y in text_sliders:
            bar:
                right_bar path + "slider_empty.png"
                left_bar path + "slider_full.png"
                xysize (618, 24)
                thumb None

                value j
                xpos x
                ypos y

    elif current_page == "audio":
        add path + "settings_audio.png"

        for j, x, y in music_sliders:
            bar:
                right_bar path + "slider_empty.png"
                left_bar path + "slider_full.png"
                xysize (618, 24)
                thumb None

                value j
                xpos x
                ypos y

    elif current_page == "gameplay":
        add path + "settings_gameplay.png"

        for i, j, x, y in gameplay_buttons:
            imagebutton:
                idle path + i + "_idle.png"
                hover path + i + "_hover.png"
                selected_idle path + i + "_selected_idle.png"
                selected_hover path + i + "_selected_hover.png"
                insensitive path + i + "_ground.png"

                focus_mask None
                action j
                xpos x
                ypos y
                hover_sound "audio/sfx/hover.wav"
                activate_sound "audio/sfx/click.ogg"

    use navigation









init -501 screen history():
    tag menu
    default path = theme_path("history")


    predict False


    add path + "bg.png"

    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        xpos 650
        ypos 190
        xmaximum 675
        ymaximum 700

        side_yfill True

        has vbox:
            spacing 10
        for h in _history_list:
            vbox:
                spacing 5
                if h.who:
                    label h.who:

                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                if h.who:
                    text "    " + what:
                        substitute False
                else:
                    text what:
                        substitute False

    if not _history_list:
        label _("The dialogue history is empty.")

    imagebutton:
        idle path + "return_idle.png"
        hover path + "return_hover.png"

        action Return()
        xpos 1161
        ypos 953



define -1 gui.history_allow_tags = set()

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():

    tag menu

    default path = theme_path("help")

    add path + "bg.png"
    add path + "help_text.png"

    imagebutton:
        idle path + "return_idle.png"
        hover path + "return_hover.png"

        action Return()
        xpos 1494
        ypos 922


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    default path = theme_path("prompt")
    add path + "bg.png"

    frame:
        background None
        padding (0, 0, 0, 0)
        xpos 649
        ypos 414
        xysize (620, 109)

        text _(message) text_align 0.5 xalign 0.5 yalign 0.5

    imagebutton:
        idle path + "yes_idle.png"
        hover path + "yes_hover.png"

        focus_mask None
        action yes_action
        xpos 748
        ypos 587
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"
    imagebutton:
        idle path + "no_idle.png"
        hover path + "no_hover.png"

        focus_mask None
        action no_action
        xpos 748
        ypos 675
        hover_sound "audio/sfx/hover.wav"
        activate_sound "audio/sfx/click.ogg"


    key "game_menu" action no_action








init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    default path = theme_path("icons")

    add path + "skipbar.png" xpos 19 ypos 10 at delayed_blink(0.0, 1.0)



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 0.01 action Play("sound", "audio/sfx/notification1.mp3")
    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 675



transform -1 quickmenu_text_alpha:
    alpha 0.5

init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.0
        yalign 1.0

        textbutton _("Back") action Rollback() at quickmenu_text_alpha

        textbutton _("Auto") action Preference("auto-forward", "toggle") at quickmenu_text_alpha

    hbox:
        style_prefix "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Menu") action ShowMenu() at quickmenu_text_alpha






init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 900





init -501 screen save_file_name(okay=NullAction()):
    modal True
    default path = theme_path("naming_saves")

    add path + "bg.png" alpha 0.5

    key "mouseup_3" action NullAction()

    on "show":
        action [SetVariable("save_name", "::"+game_type), MouseMove(900, 550, 0.1)]

    frame:
        xalign .5
        yalign .5
        background path + "frame.png"
        padding (0, 0, 0, 0)
        xysize (840, 182)

        has button:
            id "save_name_input"
            xysize (756, 57)
            action NullAction()
            add Input(size=40, color="#0856A4", default="", changed=name_func, length=25, button=renpy.get_widget("save_file_name","save_name_input")) yalign 1.0

            xpos 48
            ypos 83

    imagebutton:
        idle path + "accept_idle.png"
        hover path + "accept_hover.png"

        action [okay, Hide("save_file_name")]

        xpos 1098
        ypos 616




init -501 screen navigation_old():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing


        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):


            textbutton _("Quit") action Quit(confirm=not main_menu)






























init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
