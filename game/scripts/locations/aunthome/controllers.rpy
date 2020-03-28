label aunt_house_controller:


    if time.is_morning() or time.is_afternoon():

        if aunt_level == 2 and eliana_level >= 6:
            call aunt_2_worktalk_dialogue
            if aunt_feet:
                call aunt_2_worktalk_feet_dialogue
            else:
                call aunt_2_worktalk_ass_dialogue
            call aunt_2_worktalk_outro_dialogue

            $ aunt_level = 3
            $ persistent._seen_ever["aunt_2_worktalk_feet_dialogue"] = True
            $ persistent._seen_ever["aunt_2_worktalk_ass_dialogue"] = True
            $ persistent._seen_ever["elite_06_momAunt_cooking"] = True
            $ increase_time()
            $ go_to(L_home_basement)
        else:

            mc "I don't have anything to do there right now."


    elif time.is_night():

        if aunt_visited_tonight:
            mc "(I shouldn't disturb her anymore tonight.)"

        elif aunt_level >= 3:
            $ aunt_visited_tonight = True
            jump aunt_night
        else:

            mc "I don't have anything to do there right now."
    else:


        mc "I don't have anything to do there right now."



    $ go_to(L_home_livingroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
