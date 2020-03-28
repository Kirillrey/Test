label natsuko1_nightclubHj:

    if _in_replay:
        call setup_gallery
        play music "audio/music/supercar.mp3" loop fadeout 2.0 fadein 2.0
        scene club natsuko 7
    else:
        scene club natsuko 1 with slowfade
        mc "(Ah, there she is.)"
        mc "(She can't disappear now.)"

        scene club natsuko 2 with fade:
            subpixel True
            yalign 1.0
            pause 2.0
            linear 7.0 yalign 0.05
        pause
        mc "(I haven't noticed it from afar before but...)"
        mc "(Damn she's hot!)"
        mc "(She looks 'different' than most people here for sure.)"
        mc "(Maybe she can help me out? I guess I have to try.)"

        scene club natsuko 3 with fade
        mc "Hey, I'm-"
        "???" "I know who you are, [mc_name]."
        mc "Do I know you?"
        nat "I'm Natsuko."

        scene club natsuko 4 with dissolve
        nat "And no you don't... But I know a few things about you."
        mc "Okay, this is starting to sound creepy."
        nat "You are an important piece in the grand puzzle, [mc_name]."
        nat "But you refuse to fall into your place."

        scene club natsuko 5 with dissolve
        nat "You won't be able to complete the task like this."
        mc "(Ok, even if she doesn't have Halo I'm pretty sure she's on some kind of stuff...)"
        mc "Look Nat, I have no idea what you're talking about. I'm just here to get some of that new stuff that's been going around."
        mc "If you can't help with that I'm afraid I have to leave you to your uhm... puzzle."

        scene club natsuko 6 with dissolve
        nat "I don't expect you to understand."
        nat "We weren't supposed to meet yet."
        nat "But rest assured, I'm on your side. {w}You will understand when the time comes."
        nat "Or maybe you won't. Only the task matters to me."

        scene club natsuko 7 with dissolve
    nat "I need you to focus..."
    nat "But right now you're not using {i}this{/i} properly."

    scene club natsuko 8 with dissolve
    nat "Because there's too much going on {i}here{/i}..."
    mc "Oh!"
    mc "(Yeah, the hotter they are, the crazier they get in the head.)"
    mc "(But I like where this is going so far!)"
    nat "I'll help you regain your focus."

    scene black with fade

    scene NatsukoHj1 with dissolve
    pause 3.0
    mc "Oh shit, I didn't know you were talking about this kind of help!"
    nat "You are clearly focusing on the wrong things... This will probably help a little bit with that."
    nat "To see clearly."
    mc "(Oh I can see her perky tits with those pretty nipples clearly enough!)"
    pause

    scene NatsukoHj2 with dissolve
    pause 3.0
    mc "(Here's hoping nobody walks in. Would they care in a place like this though?)"
    nat "I need you to release, [mc_name]."
    nat "To clear your head..."
    mc "Then squeeze the {i}head{/i} a little and-"
    mc "Oh fuck, that's it!"
    mc "I'm cumming!!"
    pause

    scene club natsuko 9
    with flash
    with vpunch
    pause 0.2

    scene club natsuko 9
    with flash
    with vpunch
    pause 1.0
    nat "Yes, good!"


    scene club natsuko 11 with slowfade
    nat "That should do it for now."
    nat "Get yourself together."
    mc "Thank I guess. But uhm...{w} What is this task you keep talking about?"
    nat "Pay attention to your surroundings. Not everything's as it seems. Your home...{w} It's different."
    nat "I can't tell you much yet... You have to find things out on your own."
    nat "But you have to act soon."
    nat "I have to go now..."
    mc "Will I see you again? Wait!"

    scene black with fade
    pause 0.5

    scene club natsuko 12 with fade
    mc "(Damn, she's already gone.)"
    mc "(I got a handjob from a hot girl, that's awesome.)"
    mc "(A lunatic told me to focus on a task and not everything's as it seems and talks about {b}my home?{/b} That's some creepy ass shit.)"
    mc "(The two together?)"
    mc "(.....)"
    mc "(Yeah... Kind of hot.)"
    mc "(I need to find out what she meant by this... damn!)"
    mc "(I should focus on the task {i}at hand{/i} first though, I need to get some of that Halo thing... I should keep searching.)"

    $ renpy.end_replay()

    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
