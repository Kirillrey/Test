label home_hall:


    if time.is_morning() or time.is_afternoon():
        scene home_hall__day
    else:
        scene home_hall__night


    call screen home_hall
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
