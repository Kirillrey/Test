label nightclub_bar:


    $ renpy.music.play("audio/music/supercar.mp3", loop=True, fadeout=2.0, fadein=2.0, if_changed=True)


    if L_nightclub_bar.first_visit:
        call nc1_intro_dialogue
        if renpy.variant("mobile"):
            scene nightclub_bar__ground
            pause 1.0
            "Hint for Android players: The bar chair and bartender can be tapped to trigger events."
        $ L_nightclub_bar.first_visit = False







    if not nightclub1_complete and (nc1_bartender and nc1_melissa and nc1_tanya and nc1_natsuko2):
        scene nightclub_bar__businessman_ground
    else:
        scene nightclub_bar__ground



    call screen nightclub_bar








label nightclub_bar_chair:

    if not nightclub1_complete:
        call nc1_chair_dialogue
        $ nc1_chair = True
    $ go_to(L_nightclub_bar)






label nightclub_bar_bartender:

    if not nightclub1_complete:
        call nc1_bartender_dialogue
        $ nc1_bartender = True
        $ L_nightclub_bar.can_leave = True
    else:
        call nightclub_bar_bartender_dialogue
    $ go_to(L_nightclub_bar)






label nightclub_bar_door:

    mc "It's locked... I wonder what might be behind that door."
    mc "Maybe I'll be able to find out some other time I'm here."
    $ go_to(L_nightclub_bar)






label nightclub_bar_businessman:

    call nc1_businessman_dialogue
    $ thorne_level = 8
    $ nightclub1_complete = True
    $ L_nightclub_bar.can_leave = True
    $ L_nightclub_bar.toolbar_enabled = True
    $ L_home_pool.unlocked = True
    $ go_to(L_home_basement)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
