label home_bathroom:


    if time.is_morning():

        if isabel_level == 6 and thorne_level >= 9:
            scene home_bathroom__isabel_ground with fade
            pause 0.8
            mc "(Well, I wanted to take a shower, but of course Isabel is in here.)"
            mc "(Maybe if I just ask her she'll let me have some time in the bathroom for once.)"

        elif lain_mod and extras_installed and isabel_level >= 6 and not lm_extra_02_isabel_lotion:
            call extra_02_isabel_lotion
            $ lm_extra_02_isabel_lotion = True
            $ increase_time()
            $ go_to(L_home_bathroom)



    if time.is_afternoon():

        if lain_mod and elite_installed and ruby_level >= 13 and not lm_elite_05_ruby_dinner3:
            call elite_02_mom_dinner1
            call elite_03_mom_dinner2
            call elite_05_ruby_dinner3
            $ lm_elite_05_ruby_dinner3 = True
            $ increase_time()
            $ go_to(L_home_rubyroom)



    elif time.is_evening():

        if mom_level == 1:
            call mom_1_bathpeep_dialogue
            $ mom_level = 2
            $ increase_time()
            $ go_to(L_home_basement)

        elif mom_level == 9:
            call mom_9_bathroom2_dialogue
            $ mom_level = 10
            $ mom_yoga_level = 5
            $ m_ns_titfuck.unlocked = True
            $ increase_time()
            $ mp_notify("Mom - New Yoga & Night Scenes Unlocked!")
            $ go_to(L_home_bathroom)

        elif lain_mod and extras_installed and ruby_level >= 13 and not lm_extra_06_ruby_shave:
            call extra_06_ruby_shave
            $ lm_extra_06_ruby_shave = True
            $ increase_time()
            $ go_to(L_home_bathroom)




    if time.is_morning():
        scene home_bathroom__isabel_ground
    elif time.is_evening():
        scene home_bathroom__ruby_ground
    else:
        scene home_bathroom__ground


    call screen home_bathroom






label home_bathroom_isabel:

    if isabel_level == 6 and thorne_level >= 9:
        call isabel_6_stalker_dialogue
        $ isabel_level = 7
        $ isabel_massage_level = 4
        $ increase_time()
        $ mp_notify("Isabel - New Massage Level Unlocked!")
        $ go_to(L_home_basement)
    else:

        scene bonus isa bathroom 1 with fade
        isa "Do you need something, [mc_name]?"
        mc "Um, no just looking around."

        scene home_bathroom__isabel_ground with fade

    $ go_to(L_home_bathroom)




label home_bathroom_ruby:
    scene bonus ruby hairdryer 1 with dissolve
    ruby "Go away, [mc_name]. I'm busy."
    mc "Oh, sorry..."

    $ go_to(L_home_bathroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
