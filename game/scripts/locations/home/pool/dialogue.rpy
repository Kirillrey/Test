label logan_1_poolmorningconflict_dialogue:

    stop music fadeout 2.0
    play sound "audio/sfx/birds.ogg" loop fadein 2.0
    scene logan morning pool 1 with slowfade
    logan "Look, the prodigal son finally woke up!"
    logan "How was your sleep, basement-dweller?"
    mc "You've got a big mouth, little brother."
    mc "If you're not careful I'll wipe that cheeky grin off your face with my fist."

    scene logan morning pool 2 with dissolve
    logan "Spoken like a true caveman, when you're outwitted you resort to violence."
    mc "Outwitted? You have no idea what I have in store!"
    logan "Oh, I have a nice idea about that."

    scene logan morning pool 3 with dissolve
    logan "I see you've been having fun. {w} Dicking around."
    logan "You even have a new car! Hah!"
    logan "Was it a raffle prize at the Failure Meeting Group?"

    scene logan morning pool 4 with dissolve
    logan "You even reconnected with your old friend, that redhead!"
    logan "Ah, what a tragic love story!"
    logan "Pure hearted girl falls in love with a lowlife imbecile!"
    mc "Have you been spying on me?"
    logan "I just observe, big brother."
    logan "And while you're running around in circles, I'm ready to start my company before I even got my masters degree!"
    logan "I'd tell you how my new bio-engineering startup will change the future, but of course a shit-for-brains like you wouldn't be able to comprehend it."

    scene logan morning pool 5 with dissolve
    logan "So keep doing what you do."
    logan "It just makes it so much easier for me. Not that it ever was a challenge."

    scene logan morning pool 6 with dissolve
    logan "And when I have everything..."
    logan "Everyone will finally know who's really worthy, and I'll get the respect I deserve."
    logan "See you {i}from{/i} the top, [mc_name]!"

    scene logan morning pool 7 with fade
    mc "(This shithead...)"
    mc "(But as hard as it is to admit, he's right.)"
    mc "(I've been dicking around - quite literally - while he is locked up in his room probably jerking off to his brilliant mind.)"
    mc "(Problem is, he really has a mind of a genius. I don't doubt he truly has some amazing stuff in the works to impress dad.)"
    mc "(And he's been looking at what I've been doing, too.)"
    mc "(I have to get my plan moving and have to do it soon or I really will be the failure here...)"

    stop sound fadeout 1.0
    play music "audio/music/soul.mp3" loop fadein 2.5
    scene black with slowfade

    return






label logan_insults_pool_dialogue:

    play sound "audio/sfx/birds.ogg" loop fadein 2.0
    scene logan morning pool 1 with fade

    if temp_1 == 1:
        mc "How's it feel to be the unattractive brother?"
        logan "But we're twins!"
        mc "Exactly!{w} Wait..."

    elif temp_1 == 2:
        logan "You know, I remember when Dad told me about the day when we got home from the hospital...{w} they had a buy-one-get-one-free deal going on."
        mc "Fuck you..."

    elif temp_1 == 3:
        mc "The only woman to tell you she loves you is mom."
        mc "She does it out of pity."

    elif temp_1 == 4:
        mc "When anti-vaxxers talk about vaccines causing autism, you're the illustration."

    elif temp_1 == 5:
        mc "Did mom ever tell you that you were raised on toilet water?"
        logan "Very funny. We'll see who gets to laugh when you're begging for a job at MY company."
        logan "There's always a need for janitors, I suppose..."

    elif temp_1 == 6:
        logan "No brain, no personality..."
        logan "Tell me, what's it like now that Dad took back his money, the only attractive thing about you?"
        mc "You prick..."

    stop sound fadeout 1.0
    scene home_pool__day_logan_ground with fade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
