label prologue_kitchen:

    if prologue_mom == 0 and prologue_isabel == 1 and prologue_ruby == 1:
        $ prologue_mom = 1
        jump prologue_met_logan_in_kitchen
    elif prologue_mom == 1 and prologue_isabel == 2 and prologue_ruby == 2:
        $ prologue_mom = 2
        jump prologue_dinner

    if prologue_mom == 0:
        scene home_kitchen__day
    else:
        scene black
        show home_kitchen__night

    call screen prologue_kitchen






label prologue_livingroom:

    if prologue_mom == 0:
        scene home_livingroom__day_ground
    elif prologue_mom == 1:
        scene home_livingroom__evening_isabel
    else:
        scene home_livingroom__night

    call screen prologue_livingroom




label prologue_livingroom_isabel:

    call prologue_evening_isabel_couch
    $ prologue_isabel = 2

    jump prologue_livingroom






label prologue_hall:

    if prologue_mom == 0:
        scene home_hall__day_ground
    else:
        scene home_hall__night

    call screen prologue_hall




label prologue_rubyroom:

    if prologue_ruby == 0:
        call ruby1_prologueBed
        $ prologue_ruby = 1
    elif prologue_mom >= 2 and prologue_ruby == 2:
        call ruby3_prologueNight
        $ prologue_ruby = 3
    else:
        if prologue_mom == 1 and prologue_isabel == 2 and prologue_ruby == 2:
            mc "(I think dinner is ready now.)"
        else:
            mc "(I should do something else.)"

    jump prologue_hall




label prologue_hall_wallphoto:

    if not seen_hall_wallphoto:
        show black:
            alpha 0.75
        show ruby_isa_photo_1
        with dissolve
        pause
        mc "(My sisters, Ruby and Isabel.)"
        mc "(They've had a fairly typical relationship: not bad, not too great either.)"
        mc "(They always had each others' backs when it mattered though, and that's what's important.)"
        mc "(I used to get on better with Ruby before, but a lot has changed since then.)"
        mc "(I don't play favorites.)"
        $ seen_hall_wallphoto = True

    jump prologue_hall




label prologue_isabelroom:

    if prologue_mom >= 2 and prologue_isabel == 2:
        call isabel_prologueNight
        $ prologue_isabel = 3
    else:
        if prologue_mom == 0:
            mc "(I think I'll say hi to Isabel after I use the bathroom.)"
        elif prologue_mom == 1 and prologue_isabel == 2 and prologue_ruby == 2:
            mc "(I think dinner is ready now.)"
        else:
            mc "(I should do something else.)"

    jump prologue_hall




label prologue_momroom:

    if prologue_mom == 2:
        call prologue_night_parents_room
        $ prologue_mom = 3
    else:
        if prologue_mom == 1 and prologue_isabel == 2 and prologue_ruby == 2:
            mc "(I think dinner is ready now.)"
        else:
            mc "(I should do something else.)"

    jump prologue_hall




label prologue_bathroom:

    if prologue_isabel == 0:
        call prologue_isabel_bathroom_scene
        $ prologue_isabel = 1
    elif prologue_mom == 1 and prologue_ruby == 1:
        call ruby2_prologueShower
        $ prologue_ruby = 2
    else:
        if prologue_mom == 1 and prologue_isabel == 2 and prologue_ruby == 2:
            mc "(I think dinner is ready now.)"
        else:
            mc "(I should do something else.)"

    jump prologue_hall







label prologue_hall2:

    if prologue_mom == 0:
        scene home_hall2__day_ground
    elif prologue_mom == 1:
        scene home_hall2__evening
    else:
        scene home_hall2__night

    call screen prologue_hall2




label prologue_loganroom:

    if prologue_mom >= 2 and prologue_logan == 0:
        call prologue_night_logan_room
        $ prologue_logan = 1
    else:
        mc "(I should do something else.)"

    jump prologue_hall2




label prologue_hall2_wallphoto:

    if not seen_hall2_wallphoto:
        show black:
            alpha 0.75
        show raymond_portrait_1
        with dissolve
        pause
        mc "(The man himself!)"
        mc "(Our family was always well off, but he prides himself on elevating it to a whole new level.)"
        mc "(Having a huge portrait of himself hung up like this in the house really tells you something about him.)"
        $ seen_hall2_wallphoto = True

    jump prologue_hall2






label prologue_basement:

    if prologue_mom == 0:
        mc "(I should do something else.)"
        jump prologue_hall2

    scene home_basement__night_nolaptop

    call screen prologue_basement




label prologue_bed:

    if prologue_mom == 3 and prologue_isabel == 3 and prologue_ruby == 3 and prologue_logan == 1:
        jump prologue_next_day_morning
    else:
        mc "(I should do something else.)"

    jump prologue_basement
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
