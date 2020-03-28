label home_livingroom:


    if time.is_afternoon():

        if renpy.variant("mobile") and L_home_livingroom.first_visit:
            scene home_livingroom__day
            pause 0.5
            "Hint for Android players: The living room TV remote can be tapped when it's {b}afternoon{/b} to watch TV."
            $ L_home_livingroom.first_visit = False


        elif aunt_level == 1 and mom_level >= 8:
            call aunt_1_meeting_dialogue
            $ aunt_level = 2
            $ increase_time()
            $ go_to(L_home_livingroom)


        elif lain_mod and extras_installed and ruby_level >= 9 and not lm_extra_03_ruby_masturbate:
            call extra_03_ruby_masturbate
            $ lm_extra_03_ruby_masturbate = True
            $ set_time(4)
            $ go_to(L_home_livingroom)



    elif time.is_night():
        $ renpy.music.play("audio/music/soul.mp3", loop=True, fadeout=2.0, fadein=2.0, if_changed=True)

        if renpy.variant("mobile") and (isabel_level == 5 or isabel_level == 7) and isabel_delay == 0:
            scene home_livingroom__night
            pause 0.5
            mc "(Hm, I wonder if there's anything to watch on TV.)"




    if time.is_morning() or time.is_afternoon():
        scene home_livingroom__day
    elif time.is_evening() and not ((mom_level == 3 or isabel_level == 1) and mom_massage_counter > 0 and isabel_massage_counter > 0 and isabel_tv_counter > 0 and mom_tv_counter > 0):
        scene home_livingroom__evening_isabel
    elif time.is_evening():
        scene home_livingroom__night
    elif time.is_night():
        scene home_livingroom__night



    call screen home_livingroom






label home_livingroom_isabel:
    menu:
        "Talk About Night" if isabel_level == 2:
            call isabel_2_afterdrink_dialogue
            $ isabel_level = 3
            $ isabel_massage_level = 2
            $ increase_time()
            $ mp_notify("Isabel - New Massage Level Unlocked!")
            $ go_to(L_home_livingroom)
        "Massage":

            jump isabel_massage_controller
        "Exit":

            $ go_to(L_home_livingroom)






label home_livingroom_tv:
    python:
        temp_1 = mom_tv_text(1)
        temp_2 = isabel_tv_text(1)
        temp_3 = ruby_tv_text(1)
        temp_4 = mc_tv_text(1)

    menu:
        "Watch TV with Mom[temp_1]":
            call tv_mom_1_dialogue
            if mom_seen_tv_level == 0:
                $ mom_seen_tv_level = 1
            $ mom_tv_counter += 1
            $ increase_time()
        "Watch TV with Isabel[temp_2]":

            call tv_isabel_1_dialogue
            if isabel_seen_tv_level == 0:
                $ isabel_seen_tv_level = 1
            $ isabel_tv_counter += 1
            $ increase_time()
        "Watch TV with Ruby[temp_3]":

            call tv_ruby_1_dialogue
            if ruby_seen_tv_level == 0:
                $ ruby_seen_tv_level = 1
            $ ruby_tv_counter += 1
            $ increase_time()
        "Watch TV alone[temp_4]":

            call tv_alone_1_dialogue
            if mc_seen_tv_level == 0:
                $ mc_seen_tv_level = 1
            $ mc_tv_counter += 1
            $ increase_time()
        "Back":

            pass

    $ go_to(L_home_livingroom)






label home_livingroom_tv_night:

    menu:
        "Watch TV (New!)" if isabel_level == 5:
            call isabel_5_tvbet1_dialogue
            $ isabel_level = 6
            $ isabel_tv_counter += 1

        "Watch TV (New!)" if isabel_level == 7:
            call isabel_7_tvbet2_dialogue
            $ isabel_level = 8
            $ isabel_tv_counter += 1
        "Back":

            pass

    $ go_to(L_home_livingroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
