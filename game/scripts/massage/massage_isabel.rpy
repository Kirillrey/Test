label isabel_massage_controller:
    python:
        temp_1 = isabel_massage_text(1)
        temp_2 = isabel_massage_text(2)
        temp_3 = isabel_massage_text(3)
        temp_4 = isabel_massage_text(4)
        temp_5 = isabel_massage_text(5)


    menu isabel_massage_menu:

        "Massage #1[temp_1]" if isabel_massage_level >= 1:
            call massage_isa_1
            if isabel_seen_massage_level == 0:
                $ isabel_seen_massage_level = 1
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #2[temp_2]" if isabel_massage_level >= 2:
            call massage_isa_2
            if isabel_seen_massage_level == 1:
                $ isabel_seen_massage_level = 2
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #3[temp_3]" if isabel_massage_level >= 3:
            call massage_isa_3
            if isabel_seen_massage_level == 2:
                $ isabel_seen_massage_level = 3
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #4[temp_4]" if isabel_seen_massage_level >= 4:
            call massage_isa_4
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_pool)


        "Massage #5[temp_5]" if isabel_seen_massage_level >= 5:
            call massage_isa_5
            $ isabel_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_pool)




        "Massage #2 (locked)" if isabel_massage_level < 2:
            jump isabel_massage_menu
        "Massage #3 (locked)" if isabel_massage_level < 3:
            jump isabel_massage_menu
        "Massage #4 (locked)" if isabel_massage_level < 4:
            jump isabel_massage_menu
        "Massage #4 (her room - daytime)" if isabel_massage_level >= 4 and isabel_seen_massage_level == 3:
            jump isabel_massage_menu
        "Massage #5 (locked)" if isabel_massage_level < 5:
            jump isabel_massage_menu
        "Massage #5 (pool - daytime)" if isabel_massage_level >= 5 and isabel_seen_massage_level == 4:
            jump isabel_massage_menu
        "Back":


            jump home_livingroom_isabel








label massage_isa_1:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home afterdrink isa 1 with fade
    mc "Hey, Isa. You look a little tense. How about a massage?"
    isa "I could say the same thing about you. How about \"I\" give \"you\" a massage instead."

    scene home massage isa 1 with fade
    isa "You have quite the knot here, [mc_name]."
    mc "Hsssh, what are you using back there, a baseball bat?"

    scene home massage isa 2 with dissolve
    isa "Oh don't be such a baby. So how's the brotherly competition going?"
    mc "Oh just swell. You know how I love research and responsibility."
    isa "Haha. I figured as much. Well if you need a hand- or one of my lovely massages- just let me know."
    mc "Ahh, thanks, sis. I'll- ahh- keep that in mind."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label massage_isa_2:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene home afterdrink isa 1 with fade
    mc "Hey sis. You're lookin' a little tense. Want me to give you a massage?"
    isa "Hey, since you're offering, would you mind giving me a foot massage? High heels are not as comfortable as they want you to believe."

    scene home massage isa 3 with fade
    mc "Sure, sis, I'll massage your pretty feet."

    scene home massage isa 4 with dissolve
    isa "I guess that means you're not one of those people that hate feet?"
    mc "Not when they're as pretty as yours. So how's work been going?"

    scene home massage isa 5 with dissolve
    isa "It's the same old. People come in, ask me about financing a house, or a new RV, or a boat, or a car, and most of them can't really afford it but they want it anyway."
    mc "I can imagine."
    isa "So how have you been? How's the competition going?"
    mc "It's so much fun! I'm sooo glad dad could bestow these tasks upon me."

    scene home massage isa 6 with dissolve
    isa "Haha. I'm sure that's really the case."
    isa "Well if it would help you relieve some stress, you can come give me a foot massage anytime."

    scene home massage isa 7 with dissolve
    mc "(I totally would; her feet are damn sexy!)"
    mc "(Buuut...)"
    mc "Just a foot massage? Nothing else?"

    scene home massage isa 6 with dissolve
    isa "I guess you'll just have to wait and see what other parts of my body need tension release."
    mc "(Goddamn she's such a tease!)"
    mc "If I didn't know better, I might think you're flirting with me, miss!"
    isa "Ahaha, you wish a girl like me would flirt with you?"
    mc "I had my fair share of model company, you know!"
    isa "So you think I'm a model type?"
    isa "Sweet of you to think so highly of me, little brother!"
    isa "Now I have to finish some reports. I'll let you when I need your helping hands again!"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label massage_isa_3:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0

    if _in_replay:
        call setup_gallery
        scene home afterdrink isa 1
    else:
        scene home afterdrink isa 1 with fade
    mc "Hey, Isa. You look a little tense. How about a massage?"
    isa "I'll take a foot massage again, thanks!"

    scene home massage isa 4 with fade
    isa "You're really into this. Wanna work as a massage therapist?"

    scene home massage isa 5 with dissolve
    mc "Do you know about any job openings?"
    mc "It's always been my dream to massage old ladies!"
    isa "Ahaha, I knew it!"
    isa "But really, you're good at this."
    isa "Mind if I doze off a bit? I don't get enough sleep lately..."
    mc "Not at all, maybe I could work on your calves in the meantime?"

    scene home massage isa 6 with dissolve
    isa "Alright!"
    isa "Oh, I see where this is going..."
    isa "Now I have to take off my pants, right?"
    mc "No, I-"
    isa "Alright, I'll do it!"
    isa "Just keep doing it the way you are now... {w} And don't wake me up!"

    play music "audio/music/red.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    scene home massage isa 8 with slowfade
    mc "(My God...)"
    mc "(She really has no inhibition.)"

    scene home massage isa 9 with dissolve
    mc "(She took off her pants in front of me like it's nothing.)"
    mc "(Well, maybe it is just that. Nothing.)"

    scene home massage isa 10 with dissolve
    mc "(Growing up in a house with so many siblings, you kind of get used to see each other in all kinds of situations.)"
    mc "(It's a bit different now, after years of living apart and of course, all being young adults.)"
    mc "(Seeing how beautiful of a girl - a woman, really - she's become.)"

    scene home massage isa 11 with dissolve
    mc "(And not just seeing, but feeling it...)"
    mc "(I can't resist massaging her firm thighs.)"

    scene home massage isa 12 with dissolve
    mc "(This is truly a magnificent body!)"
    mc "(And she knows it. {w} She's also not afraid to show it.)"
    mc "(She was always every guy's dream girl.)"
    mc "(When I was a kid I used to imagine that I'd have a girlfriend like her.)"

    scene home massage isa 13 with dissolve
    isa "Mhmm~"
    mc "(As tempting as her body is...)"
    mc "(I should probably let her have some sleep peacefully.)"

    scene home massage isa 14 with dissolve
    mc "(Sweet dreams, sis.)"
    mc "(We'll continue this another time...)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label massage_isa_4_failed:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene home massage isa 4 with fade
    mc "Hey, Isa. You look a little tense. How about a massage?"
    isa "I'll take a foot massage again, thanks!"

    scene home massage isa 3 with dissolve
    isa "You're really into this. Wanna work as a massage therapist?"

    scene home massage isa 5 with dissolve
    mc "Do you know about any job openings?"
    mc "It's always been my dream to massage old ladies!"
    isa "Ahaha, I knew it!"
    isa "But really, you're good at this."
    isa "Mind if I doze off a bit? I don't get enough sleep lately..."
    mc "Not at all, maybe I could work on your calves in the meantime?"

    scene home massage isa 6 with dissolve
    isa "Alright!"
    isa "Oh, I see where this is going..."
    isa "Now I have to take off my pants, right?"
    mc "No, I-"
    isa "Alright, I'll do it!"
    isa "Just keep doing it the way you are now... {w} And don't wake me up!"

    scene black with slowfade

    scene home massage isa 15 with fade
    mc "(Oh man, I can barely contain myself...)"
    mc "(I'm higher up her thighs than I've ever been! {w} Including weed!)"
    mc "(But if I go further than this she will surely wake up and possibly murder me.)"
    isa "Mhh~ {w} Oh!"

    scene home massage isa 16 with fade
    isa "I have an idea!"
    mc "(Thank God I didn't try anything stupid!)"
    mc "You're awake!"
    isa "Of course I am!"
    isa "Listen, since the pool is finished, we should continue this outside!"

    scene home massage isa 17 with dissolve
    isa "Do you have sunscreen?"


    mc "Uhm, no."
    isa "Oh, alright."
    isa "Let's get back to this when you do!"
    mc "(Damn... I need to buy some sunscreen. I could do that online on my laptop.)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return



label massage_isa_4_2ndtry:

    scene home massage isa 4 with fade
    mc "Hey, Isa. You look a little tense. How about a massage?"
    isa "Sure!"

    scene home massage isa 17 with dissolve
    isa "But I have an idea!"
    isa "Listen, since the pool is finished, we should do this outside!"
    isa "Do you have sunscreen?"
    mc "Yes."
    isa "Awesome! Then let's go!"
    isa "I'll change into my bikini and meet you outside."

    scene black with fade
    show text "{size=72}{color=#dc38bf}A few minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene home massage isa 18 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause

    mc "Holy shit!"

    scene home massage isa 19 with dissolve
    isa "Ahah, what, you've never seen a girl in a bikini?"
    isa "Now that the pool is finally finished you better get used to it!"

    scene home massage isa 20 with dissolve
    mc "I've never seen a girl {i}as beautiful as you{/i} in a bikini before."
    isa "Ah, such a charmer!"
    isa "Well, mom and Ruby will be out here a lot as well I assume, I'll have some competition!"

    scene home massage isa 21 with dissolve
    mc "I'm not sure if anyone can compete with you, Isa!"
    isa "Alright, alright! I'll blush if you keep this up!"
    isa "Now where were we..."
    isa "Ah yes, please spread some sunscreen over me, I don't wanna get sunburn out here."
    mc "Gladly!"

    scene home massage isa 22 with slowfade
    mc "...."
    mc "(Any guy who has laid eyes on her is already a lucky one - not to mention the luck you have if you also get laid.)"
    isa "Is something wrong? You're just standing there!"

    scene home massage isa 23 with dissolve
    mc "Shit, sorry!"
    mc "I was just uhm... {w} Thinking."
    mc "But I'll get right to it."
    isa "Haha, okay!"
    isa "Start with my back please!"

    scene home massage isa 24 with fade
    isa "I'm so happy they finally finished renovating the yard."
    isa "The new pool is amazing! Can't wait to jump in soon!"
    mc "If you have sunscreen on and go swimming, you know you have to reapply the sunscreen, right?"

    scene home massage isa 25 with dissolve
    isa "I know! Luckily, I have my dear brother who can does it for me so selflessly!"
    mc "Hah! That's right!"
    mc "We have to be careful your beauty isn't shadowed by sunburn, right?"
    isa "Yes, exactly! How am I going to be on the cover of magazines otherwise!"

    scene home massage isa 26 with dissolve
    mc "Haha, rest assured if I owned Playdude magazine I'd put you on the cover in no time!"
    isa "Is that the kind of magazine you'd think I'd be on the cover of?"
    mc "I mean... Why not?"
    isa "Hahaha, you are bold, [mc_name]!"

    scene home massage isa 27 with fade
    isa "Alright, thank you for helping me out here [mc_name]. I can get the rest myself."
    isa "I'll let you go, I bothered you enough already."
    mc "It's never a bother, sis!"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return



label massage_isa_4:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home massage isa 4
    else:
        scene home massage isa 4 with fade
    mc "Hey, Isa. You look a little tense. How about a massage?"
    isa "I'll take a foot massage again, thanks!"

    scene home massage isa 3 with dissolve
    isa "You're really into this. Wanna work as a massage therapist?"

    scene home massage isa 5 with dissolve
    mc "Do you know about any job openings?"
    mc "It's always been my dream to massage old ladies!"
    isa "Ahaha, I knew it!"
    isa "But really, you're good at this."
    isa "Mind if I doze off a bit? I don't get enough sleep lately..."
    mc "Not at all, maybe I could work on your calves in the meantime?"

    scene home massage isa 6 with dissolve
    isa "Alright!"
    isa "Oh, I see where this is going..."
    isa "Now I have to take off my pants, right?"
    mc "No, I-"
    isa "Alright, I'll do it!"
    isa "Just keep doing it the way you are now... {w} And don't wake me up!"

    scene black with slowfade

    scene home massage isa 15 with fade
    mc "(Oh man, I can barely contain myself...)"
    mc "(I'm higher up her thighs than I've ever been! {w} Including weed!)"
    mc "(But if I go further than this she will surely wake up and possibly murder me.)"
    isa "Mhh~ {w} Oh!"

    scene home massage isa 16 with fade
    isa "I have an idea!"
    mc "(Thank God I didn't try anything stupid!)"
    mc "You're awake!"
    isa "Of course I am!"
    isa "Listen, since the pool is finished, we should continue this outside!"

    scene home massage isa 17 with dissolve
    isa "Do you have sunscreen?"
    mc "Yes."
    isa "Awesome! Then let's go!"
    isa "I'll change into my bikini and meet you outside."

    scene black with fade
    show text "{size=72}{color=#dc38bf}A few minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene home massage isa 18 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause

    mc "Holy shit!"

    scene home massage isa 19 with dissolve
    isa "Ahah, what, you've never seen a girl in a bikini?"
    isa "Now that the pool is finally finished you better get used to it!"

    scene home massage isa 20 with dissolve
    mc "I've never seen a girl {i}as beautiful as you{/i} in a bikini before."
    isa "Ah, such a charmer!"
    isa "Well, mom and Ruby will be out here a lot as well I assume, I'll have some competition!"

    scene home massage isa 21 with dissolve
    mc "I'm not sure if anyone can compete with you, Isa!"
    isa "Alright, alright! I'll blush if you keep this up!"
    isa "Now where were we..."
    isa "Ah yes, please spread some sunscreen over me, I don't wanna get sunburn out here."
    mc "Gladly!"

    scene home massage isa 22 with slowfade
    mc "...."
    mc "(Any guy who has laid eyes on her is already a lucky one - not to mention the luck you have if you also get laid.)"
    isa "Is something wrong? You're just standing there!"

    scene home massage isa 23 with dissolve
    mc "Shit, sorry!"
    mc "I was just uhm... {w} Thinking."
    mc "But I'll get right to it."
    isa "Haha, okay!"
    isa "Start with my back please!"

    scene home massage isa 24 with fade
    isa "I'm so happy they finally finished renovating the yard."
    isa "The new pool is amazing! Can't wait to jump in soon!"
    mc "If you have sunscreen on and go swimming, you know you have to reapply the sunscreen, right?"

    scene home massage isa 25 with dissolve
    isa "I know! Luckily, I have my dear brother who can does it for me so selflessly!"
    mc "Hah! That's right!"
    mc "We have to be careful your beauty isn't shadowed by sunburn, right?"
    isa "Yes, exactly! How am I going to be on the cover of magazines otherwise!"

    scene home massage isa 26 with dissolve
    mc "Haha, rest assured if I owned Playdude magazine I'd put you on the cover in no time!"
    isa "Is that the kind of magazine you'd think I'd be on the cover of?"
    mc "I mean... Why not?"
    isa "Hahaha, you are bold, [mc_name]!"

    scene home massage isa 27 with fade
    isa "Alright, thank you for helping me out here [mc_name]. I can get the rest myself."
    isa "I'll let you go, I bothered you enough already."
    mc "It's never a bother, sis!"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label massage_isa_5:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home massage isa 28
    else:
        scene home massage isa 28 with slowfade
    isa "You know, since we already talked about these things..."
    isa "I've been dying to get a proper massage in other...{w} areas."

    scene home massage isa 29 with dissolve
    isa "You seem to like them a lot anyways..."
    mc "(Holy shit!)"
    mc "Hell yeah I do!"

    scene home massage isa 30 with dissolve
    mc "Who wouldn't?"
    mc "Isabel, you are gorgeous!"
    isa "Haha, alright, but let's just keep everything clean, right?"

    scene home massage isa 32 with dissolve
    mc "(The only thing I won't be able to keep clean are my fantasies.)"
    isa "You know what?"
    isa "Let's just skip the back massage entirely."
    isa "I need your hands at the front."
    mc "I second this!"

    scene home massage isa 33 with dissolve
    isa "I think this will do. You can reach {i}everything{/i} from there, right?"
    mc "(She's so damn flirty, I didn't think she would be like this after the boundaries are set.)"

    scene home massage isa 34 with dissolve
    mc "(It's gonna be hard to keep it cool and not cream my pants if she's like this.)"
    mc "(But if anyone can do it, it's me! Right?)"
    mc "(God...{w} She looks so fit and hot and beautiful and sexy and-)"

    scene home massage isa 35 with dissolve
    mc "(I better not fuck this up. Concentrate, [mc_name]!)"
    mc "I think I can reach almost everything like this, yeah."
    isa "Whatever you don't reach, you probably shouldn't either."
    mc "(Fair enough.)"

    scene home massage isa 36 with dissolve
    isa "Mmm, that's nice. Finally!"
    mc "('Mmm' indeed! Her breasts are so firm and tight and big!)"
    mc "(I can't believe I'm doing this. I always knew I had the sexiest sister ever, but to be able to fondle her breasts...)"
    mc "(And she's enjoying it? This is the best.)"

    scene home massage isa 37 with dissolve
    isa "Having them this big is not all that great. You guys love it of course, always want them bigger."
    isa "But try carrying them around all day."
    mc "I can carry them for you anytime, sis. I could be your personal bra!"

    scene home massage isa 38 with dissolve
    mc "(Oh fuck, this view! This feeling!)"
    mc "(Pushing them together like this makes me want to massage her with a different body part...)"
    mc "(But then she would be massaging me, instead.)"

    scene home massage isa 39 with dissolve
    mc "(Shit, I can't pop a woody right here, it would poke her right in the back of her head!)"
    isa "Mmmh..."

    scene home massage isa 40 with dissolve
    mc "(I guess I'm doing something good!)"
    mc "(Her breathing is becoming faster. {w} Isn't a massage supposed to be calming?)"

    scene home massage isa 41 with dissolve
    isa "Ah, thanks [mc_name], that was great."
    mc "(Ah, just when I started to make myself familiar with her beautiful breasts...)"
    isa "But I think that's enough, I feel much better."
    mc "Anytime!"
    mc "(And many more times, hopefully!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
