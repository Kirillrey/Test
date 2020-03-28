label extra_02_isabel_lotion:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene extra isa lotion 1
    else:
        scene extra isa lotion 1 with slowfade
    isa "Hey [mc_name]!"
    mc "Oh shit, sorry!"

    scene extra isa lotion 2 with dissolve
    isa "How long have you been standing there?"
    mc "What? I just came here, I swear!"

    scene extra isa lotion 3 with dissolve
    isa "Since you're here, why don't you help me a little bit?"
    isa "I can't put lotion on my back so... Please?"

    scene extra isa lotion 4 with dissolve
    mc "(Holy shit!)"
    mc "Uh, you don't have a problem with me..."
    mc "You know, seeing you like this?"

    scene extra isa lotion 5 with dissolve
    isa "I can't make you unsee this, can I?"
    isa "Besides, my back is facing you so... It's alright."
    mc "(Oh it's a memory I'll cherish dearly that's for sure!)"
    mc "I'm happy to help!"

    scene extra isa lotion 6 with dissolve
    isa "Okay, start at my shoulders and work your way down from there."

    scene extra isa lotion 7 with dissolve
    mc "(Oh I'd work my way all the way down...)"
    mc "(That ass is top notch!)"

    scene extra isa lotion 8 with dissolve
    isa "You're doing good!"
    isa "Make sure you get every spot!"
    mc "(Does she not realize she's standing in front of a mirror and I could see everything right up until she put her hands over her tits?)"
    mc "(Maybe she did realize and that's why she did it.)"

    scene extra isa lotion 9 with dissolve
    isa "Okay, let me bend over a bit-"
    isa "You need to get my lower back as well."
    isa "Told you, not to miss a spot."

    scene extra isa lotion 10 with dissolve
    isa "I take care of my skin very carefully."
    mc "Oh yeah I can see that."
    mc "I won't miss a spot, you can be sure of that."

    scene extra isa lotion 11 with dissolve
    mc "Very beautiful skin indeed..."

    scene extra isa lotion 12 with dissolve
    mc "Is it good like this?"
    isa "Yeah!"
    isa "Well..."

    scene extra isa lotion 13 with dissolve
    isa "That's not exactly my lower back, but I guess that area needs body lotion as well."
    mc "I'm taking this seriously, you know. I'm a very thorough guy."
    isa "I can see that... Haha!"
    isa "Okay, that's enough."

    scene extra isa lotion 14 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause

    mc "(Holy fuckin shit!)"
    isa "Now..."

    scene extra isa lotion 15 with dissolve
    isa "Since you've been kind enough to help me, I think this is a fair reward, right?"
    isa "Not that you didn't see it already from the mirror before..."

    scene extra isa lotion 16 with dissolve
    mc "(That's it...)"
    mc "(She's a goddess!)"
    mc "(And she's got me in her grasp!)"


    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label extra_02_jane_store:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0

    if _in_replay:
        call setup_gallery
        scene store mc 1
    else:
        scene store mc 1 with fade
    mc "(Fuckin Ruby, making me cover for her in this shitty store...)"
    mc "(At least now I know working in retail isn't my true calling in life, that's for sure.)"

    scene extra store jane 2 with dissolve
    mc "(Hmmm...)"
    mc "(It's so boring here, I guess I must be seeing things now.)"

    scene extra store jane 1 with dissolve
    mc "(I heard that without any stimulus, the brain starts to conjure up images to entertain itself.)"
    mc "(Guess huge jugs are pretty entertaining to my brain.)"
    jane "[mc_name]? Are you alright?"

    scene extra store jane 3 with dissolve
    mc "(Now I even hear voices...)"
    mc "(Man, this job is killing me.)"
    mc "(I really should ask Ruby for something spectacularly awesome for this...)"
    jane "[mc_name]!!"

    scene extra store jane 4 with vpunch
    mc "Oh, Ms Jane!"
    mc "Hi!"
    mc "I didn't notice you there!"

    scene extra store jane 5 with dissolve
    jane "I didn't know you're working here!"
    jane "Way to go [mc_name], having a part time job."
    mc "Actually, I'm just covering for my sister."
    jane "That's admirable as well."
    jane "I picked out a few pieces of clothing, can I try them on?"
    mc "Here? Well, sure! I mean-"
    jane "In the changing booth, [mc_name]..."
    mc "Oh, right, go ahead it's right over there."
    jane "Thanks!"

    scene extra store jane 6 with dissolve
    mc "(Daaamn, she's hot!)"
    mc "(And she's getting all nude in the changing room right now!)"
    pause 0.7
    scene extra store jane 6 with vpunch
    jane "Aaaah!"
    mc "(What the ef?)"

    scene extra store jane 7 with dissolve
    mc "Ms Jane, are you okay in there?"
    mc ".........."
    mc "Hello? Ms Jane?"
    mc "(Shit, no answer...)"
    mc "(Should I go in?)"
    mc "I'm coming in now, okay?"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene extra store jane 8 with fade
    mc "Holy shit!"
    mc "Ms Jane, are you alright?"

    scene extra store jane 9 with dissolve
    mc "(Fuck, I guess she slipped and fell on something while trying on the clothes?)"
    mc "(She's breathing, so that's good. What do I do?)"
    mc "(Call an ambulance?)"

    scene extra store jane 10 with dissolve
    mc "(That would be a waste of resources for them probably, she looks okay, must have just lost consciousness for a bit.)"
    mc "(I better try to wake her.)"

    scene extra store jane 11 with dissolve
    mc "Ms Jane?{w} Are you okay?"
    mc "Wake up!"
    jane "Mhmrl..."
    mc "(Okay, so she's definitely alright, just sleeping.)"
    mc "Hello?"
    jane "Later... Connawr..."
    mc "(Fine then.)"
    mc "(Hmmm...)"
    mc "(Maybe I should...)"
    mc "(Yeah...{w} Let's do that.)"
    pause 0.8

    scene extra store jane 12 with dissolve
    scene extra store jane 12 with vpunch
    mc "(Damn!!)"
    mc "(That's a nice rack right there!)"

    scene extra store jane 13 with dissolve
    mc "(I should probably take a closer inspection, hehe.)"
    if not lain_mod:
        mc "(I wonder who's the lucky guy who gets to whip his dong between those cushions every day!)"

    scene extra store jane 14 with dissolve
    mc "(She seems fine then.)"
    mc "(And her nipples... I wonder what they taste like!)"
    mc "(Well, that's maybe for another day.)"
    mc "(But I can't just leave them like that without a little bit of touching first.)"

    scene extra store jane 15 with dissolve
    mc "(Oh wow, they are rock hard!)"
    mc "(Maybe she's having a naughty dream?)"
    mc "(Well, it couldn't be naughtier than this...)"
    mc "(I'm such a fucking perv.)"
    mc "(At least I acknowledge it.)"
    mc "(Let's give this baby a tug!)"

    scene extra store jane 16 with hpunch
    pause 0.5
    mc "(Holy shit, these tits are really huge!)"
    mc "(One day... I'll get them around my cock, I swear!)"

    scene extra store jane 17 with dissolve
    jane "Mhmm.."
    if _in_replay:
        jane "[mc_name], is that you?"
    else:
        jane "Ngh, w-who's there...?"
    mc "(Oh shit!)"
    mc "(Time to take a swift leave!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
