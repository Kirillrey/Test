label school_lecturehall:


    if time.is_morning() and time.is_weekday():

        if jane_on_sick_leave:
            scene school_lecturehall__afternoon_ground
            mc "(I guess Ms. Jane isn't teaching class today...)"
        else:
            jump school_lecturehall_morning_janeteach


    elif time.is_morning() and time.is_weekend():

        scene school_lecturehall__afternoon_ground
        mc "(Ms. Jane doesn't teach class on the weekend.)"




    if time.is_morning() and time.is_weekday() and not jane_on_sick_leave:
        scene school_lecturehall__morning_jane_ground
    else:
        scene school_lecturehall__afternoon_ground



    call screen school_lecturehall





label school_lecturehall_morning_janeteach:
    menu:
        "Sit down":
            $ increase_time()
            call school_lecturehall_sitdown_dialogue

            if days_since_been_to_class >= 3:
                $ days_since_been_to_class = 0
                call school_lecturehall_skippedclass_dialogue

                menu:
                    "Do tutoring":
                        $ current_room = L_school_janeoffice.name
                        jump school_janeoffice_msjane
                    "Not today":

                        mc "Sorry Ms. Jane, but I'm too busy to be tutored today."
                        jane "No problem, I understand. Just remember that I'm here to help if you need it."
                        $ go_to(L_school_hall)
            else:

                $ days_since_been_to_class = 0
                scene school_lecturehall__afternoon_ground with slowfade
                $ go_to(L_school_lecturehall)
        "Exit":


            call screen school_lecturehall
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
