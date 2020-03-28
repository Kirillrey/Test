label aunt_night:

    if not (renpy.seen_label("aunt_ns_jerkoff_dialogue") and renpy.seen_label("aunt_ns_thighjob_dialogue")):
        mc "(With the code my aunt sent me, I can use my phone's NFC to open the door to enter her apartment building.)"
        mc "(She must have not thought about the drawbacks of that...)"





    play music "audio/music/red.mp3" loop fadeout 2.0 fadein 2.0
    scene aunt night 1 with slowfade
    mc "(And here I am in her bedroom.)"
    mc "(This was a piece of cake.)"
    mc "(Being able to get in here unnoticed is probably going to come in handy later, but for now it's just for my own amusement.)"
    mc "(These nightly visits are a weird part of me now. A kind of fetish, I guess. An addiction?)"
    mc "(It's the adrenaline... The excitement of the possibility of getting caught any time, and the high stakes.)"
    mc "(Any mistake would be disastrous, but that's why the payoff is so much more satisfying.)"

    scene aunt night 2 with dissolve
    mc "(There she is under the covers.)"
    mc "(I have to be even more careful not to wake her up.)"
    mc "(Doing it at home is one thing, but this is breaking and entering, at the very least.)"

    scene aunt night 3 with dissolve
    mc "(I can hear her breathing as I get closer and the rhythmic ticking of the clock on the wall.)"
    mc "(She's lying there, completely motionless, aside from her chest slowly raising and lowering by her breathing.)"
    mc "(She appears to be in deep sleep.)"
    mc "(I'll use this chance to lift the covers and take a look at her.)"

    scene aunt night 4 with dissolve
    mc "(Holy-)"
    mc "(She's not really wearing pajamas, it's more like a sexy, red bodice.)"
    mc "(I'm not sure about that being comfortable sleepwear, but each to their own, I guess.)"
    mc "(I'm certainly not complaining.)"


    python:
        temp_1 = True
        temp_2 = True

    jump aunt_nightscene_look




label aunt_nightscene_look:
    scene aunt night 4 with dissolve

    menu:
        "Look down" if temp_1:
            scene aunt night 5 with dissolve
            mc "(Her long, slender legs are completely bare, opened just enough to see her crotch.)"
            mc "(There's a pretty nice view from down here.)"

            if aunt_feet:
                scene aunt night 9 with dissolve
                mc "(Her sexy little feet are resting as well now.)"
                mc "(I can't believe I was sucking on them...)"

            scene aunt night 7 with dissolve
            mc "(Her clothes barely hide her crotch, sticking to her figure.)"
            mc "(How many people must want to get in there each day...)"
            mc "(I can almost see the outlines of her pussy through that dress. It was clearly a good choice if the goal is to make anyone horny who looks at her.)"

            $ temp_1 = False
            jump aunt_nightscene_look


        "Look up" if temp_2:
            scene aunt night 6 with dissolve
            mc "(I have to admit. My aunt is fucking hot.)"
            mc "(Her slender waist and round ass and hips, with those massive boobs is just perfect.)"
            mc "(She has a body of a perfect fuckdoll.)"

            scene aunt night 8 with dissolve
            mc "(She's sleeping so peacefully.)"
            mc "(It almost makes me forget how she was with me when I came to her for help.)"

            $ temp_2 = False
            jump aunt_nightscene_look


        "Continue" if temp_1 or temp_2:
            pass



    mc "(Let's see...)"
    mc "(I shouldn't push anything too much for now. I'm just trying to figure out how far I can go with her without risking her waking up.)"
    mc "(So what should I do?)"

    menu:
        "Jerk off":
            call aunt_ns_jerkoff_dialogue
            $ aunt_ns_jerkoff.seen = True
        "Thighjob":

            call aunt_ns_thighjob_dialogue
            $ aunt_ns_thighjob.seen = True

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    $ go_to(L_home_livingroom)











label aunt_ns_jerkoff_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/red.mp3" loop fadeout 2.0 fadein 2.0
        scene aunt night 4
        menu:
            "Look down":
                scene aunt night 5 with dissolve
                mc "(Her long, slender legs are completely bare, opened just enough to see her crotch.)"
                mc "(There's a pretty nice view from down here.)"

                scene aunt night 9 with dissolve
                mc "(Her sexy little feet are resting as well now.)"
                mc "(I can't believe I was sucking on them...)"

                scene aunt night 7 with dissolve
                mc "(Her clothes barely hide her crotch, sticking to her figure.)"
                mc "(How many people must want to get in there each day...)"
                mc "(I can almost see the outlines of her pussy through that dress. It was clearly a good choice if the goal is to make anyone horny who looks at her.)"
            "Look up":

                scene aunt night 6 with dissolve
                mc "(I have to admit. My aunt is fucking hot.)"
                mc "(Her slender waist and round ass and hips, with those massive boobs is just perfect.)"
                mc "(She has a body of a perfect fuckdoll.)"

                scene aunt night 8 with dissolve
                mc "(She's sleeping so peacefully.)"
                mc "(It almost makes me forget how she was with me when I came to her for help.)"
            "Continue":

                pass


    mc "(Simply jerking off on her is the safe bet here.)"

    scene AuntNightJerkoff1 with dissolve
    pause
    mc "(And there's plenty to see and jerk off to...)"
    mc "(Her body is truly amazing.)"
    mc "(I can only imagine what it would be like to have her kneeling on the floor, looking up with her tongue out.)"
    mc "(Just waiting to receive my load all on her face and in her mouth.)"
    mc "(Begging to receive my cum...)"
    mc "(But today I have to be content with just shooting a load on her massive tits.)"
    mc "(Even skin soft as hers needs some night moisturizer.)"
    mc "(It doesn't take long to get close to cumming, with the excitement and the view.)"
    mc "(Shit, I need to shoot my load on her!)"
    mc "(I'll do it carefully not to mess up her dress-)"
    mc "(Ah fuck, here we go-)"
    pause

    scene aunt night jerkoff cum 1 with hpunch
    scene aunt night jerkoff cum 1 with hpunch
    mc "(Take it, aunt!)"

    scene aunt night jerkoff cum 1 with hpunch
    mc "(Aaaah!!)"
    mc "(That felt good...{w} And I managed to pool my cum between her tits.)"
    mc "(I'll do a little cleanup, then leave. Hopefully she won't notice anything odd in the morning.)"

    $ renpy.end_replay()

    return






label aunt_ns_thighjob_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/red.mp3" loop fadeout 2.0 fadein 2.0
        scene aunt night 4
        menu:
            "Look down":
                scene aunt night 5 with dissolve
                mc "(Her long, slender legs are completely bare, opened just enough to see her crotch.)"
                mc "(There's a pretty nice view from down here.)"

                scene aunt night 9 with dissolve
                mc "(Her sexy little feet are resting as well now.)"
                mc "(I can't believe I was sucking on them...)"

                scene aunt night 7 with dissolve
                mc "(Her clothes barely hide her crotch, sticking to her figure.)"
                mc "(How many people must want to get in there each day...)"
                mc "(I can almost see the outlines of her pussy through that dress. It was clearly a good choice if the goal is to make anyone horny who looks at her.)"
            "Look up":

                scene aunt night 6 with dissolve
                mc "(I have to admit. My aunt is fucking hot.)"
                mc "(Her slender waist and round ass and hips, with those massive boobs is just perfect.)"
                mc "(She has a body of a perfect fuckdoll.)"

                scene aunt night 8 with dissolve
                mc "(She's sleeping so peacefully.)"
                mc "(It almost makes me forget how she was with me when I came to her for help.)"
            "Continue":

                pass


    mc "(The way she has her leg bent gave me an idea...)"
    mc "(If she doesn't have her pussy out... I might be able to fold myself one.)"

    scene AuntNightThighjob1 with dissolve
    pause
    mc "(I grab her thigh and place the head of my cock in the bend of her leg.)"
    mc "(I move my dick in and out while her leg is clamping down on my shaft.)"
    mc "(It's not the tightest grip, but I won't complain.)"
    mc "(The skin at the back of her knee feels soft against my member, but so does the skin on anywhere I've touched her so far.)"
    mc "(I dare not move her legs too much, instead I'm moving in and out of her makeshift pussy.)"

    scene AuntNightThighjob2 with dissolve
    pause
    mc "(I move my cock higher up in the fold and the grip of her leg around me tightens.)"
    mc "(My cock is now properly hugged by her skin each time I do a pull or push.)"
    mc "(Her skin feels silky smooth, and with the added pressure, she's going to make me cum soon without her even knowing it.)"
    mc "(Her breathing is getting heavier and so does mine!)"
    mc "(Damn it, I didn't think about where to shoot my load!)"
    mc "(I'll try to get as much on her skin as possible - easier to clean up. And way hotter...)"
    mc "(Ah... Here it is aunt!)"
    pause

    scene aunt night thighjob cum 1 with vpunch
    scene aunt night thighjob cum 1 with vpunch
    mc "(Fuck!!)"
    mc "(Ah... That was great.)"
    mc "(It's surprising how many places a man can push his cock into and still get satisfaction.)"
    mc "(I'll do a little cleanup, then leave. Hopefully she won't notice anything odd in the morning.)"

    $ renpy.end_replay()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
