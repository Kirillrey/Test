label home_hall2:


    if time.is_morning() or time.is_afternoon():
        scene home_hall2__day
    elif time.is_evening():
        scene home_hall2__evening
    else:
        scene home_hall2__night




    if mom_night_counter > 0 and L_home_study.first_visit:
        $ L_home_study.unlocked = True


    call screen home_hall2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
