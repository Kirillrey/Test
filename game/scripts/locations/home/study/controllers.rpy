label home_study:


    if L_home_study.first_visit:
        $ L_home_study.first_visit = False



    if time.is_morning() or time.is_afternoon():
        scene home_study__day_ground
    elif time.is_evening():
        scene home_study__night_ground
    elif time.is_night():
        scene home_study__night_dad_ground


    call screen home_study
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
