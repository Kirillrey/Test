label nightclub_bar_bartender_dialogue:
    scene nightclub bartender 1 with fade
    mc "Hey, I'd like to have drink!"
    mc "Just a beer, for now."

    scene nightclub bartender 2 with dissolve
    pause 0.5

    scene nightclub bartender 3 with dissolve
    bartender "There you go!"

    scene nightclub bartender 4 with dissolve
    mc "Thanks!"

    return








label nc1_intro_dialogue:

    scene nightclub_bar__ground with Fade(1.0, 1.0, 1.0)
    mc "(Here we go, back to the nightlife!)"
    mc "(It's been a while...)"
    mc "(The 'Tempest Club' huh?)"
    mc "(Alright, let's see if I can get some of this magical pill.)"
    mc "(I should see if I can talk to someone who might be able to help out.)"

    return






label nc1_chair_dialogue:

    scene nightclub bartender 1 with fade
    mc "Hey, I'd like to have drink!"
    mc "Just a beer, for now."

    scene nightclub bartender 2 with dissolve
    pause 0.5

    scene nightclub bartender 3 with dissolve
    bartender "There you go!"

    scene nightclub bartender 4 with dissolve
    mc "Thanks!"

    scene nightclub bartender 5 with dissolve

    if not nc1_bartender and not nc1_melissa and not nc1_tanya and not nc1_natsuko2:
        mc "(Fucking Thorne...{w} Leaving me in this shit.)"
        mc "(How the fuck am I supposed to get Halo without any money?)"
        mc "(Even if money wasn't a problem, it looks like the thing is so rare most people have a hard time getting their hands on them.)"
        mc "(I should look around the club and see who could help me...)"

    if nc1_natsuko2:
        mc "(Fuck, this place is intense.)"
        mc "(One moment I'm trying to find the most wanted drug in the city and the next a hot girl is blabbering about weird shit and jacking me off...)"
        mc "(She looked serious though...{w} And what task was she talking about?)"
        mc "(I don't know which is better, if she's just a lunatic or if she's actually telling the truth about some mysterious task.)"

    if nc1_melissa:
        mc "(If Melissa wasn't enough, Ruby shows up?)"
        mc "(Just what the hell...)"
        mc "(I don't think mom and dad knows she's out, and they certainly don't know she's in a place like this.)"
        mc "(Well... She's an adult now, I guess.)"
        mc "(And Melissa... {w} Fuck!)"
        mc "(She's gonna be a problem.)"

    if nc1_tanya:
        mc "(Tanya... {w} Looks like trouble.)"
        mc "(She knows I'm working for Thorne.)"
        mc "(I just hope I won't get too deep into this underworld shit.)"

    if nc1_bartender:
        mc "(At least I know who I'm looking for now.)"
        mc "(Guy with a golden tooth.)"
        mc "(I hope he smiles a lot...)"

    mc "(Anyways... Back to finding what I came here for.)"

    return






label nc1_bartender_dialogue:

    scene nightclub bartender 1 with fade
    bartender "Hey, new around here?"
    mc "In Midnight City? {w}Not really. It's just been a while."
    bartender "And the club?"
    mc "First time."
    bartender "How do you like it so far?"
    mc "Not bad at all!"
    bartender "Need another drink?"
    mc "Actually, I'm looking for something else..."
    bartender "Aaah..."
    bartender "The thing everyone is looking for nowadays."
    mc "Are they?"
    bartender "You kidding me?"
    bartender "Ever since it popped up, there have been rumors all about it, and people are out to get it."
    mc "Have you tried it yourself?"
    bartender "Nah, I'm not into that type of shit."
    bartender "Besides, they don't pay me nearly enough to afford that."
    mc "I see...{w} Do you know where I could get some?"
    bartender "Rich boy, eh?"
    bartender "....."

    scene nightclub bartender 6 with dissolve
    bartender "There's sometimes a guy here who has it."
    bartender "You'll know when you see him - dude's got a golden tooth."

    scene nightclub bartender 1 with dissolve
    bartender "Haven't seen him around tonight though. Yet."
    mc "Thanks, man."
    bartender "If you need some liquor, I'm here."

    return






label nc1_businessman_dialogue:

    scene club businessman 4 with slowfade
    bman "You look like someone who's looking for something..."
    mc "Nah man, I'm not g-"
    mc "(Wait a minute!)"
    mc "(The guy with the golden tooth!)"
    mc "Actually..."

    scene club businessman 1 with dissolve
    bman "Heheh, of course you are."
    bman "Everyone is."
    mc "How do you have it when no one does?"
    bman "Money, my friend. Money can buy everything!"
    mc "Are you selling?"
    bman "Hah, you couldn't pay enough..."
    bman "But tell you what...{w} I've seen that you're close with Ms Tanya."
    mc "(I wouldn't call our relationship close by any means, but he doesn't need to know that...)"
    bman "A favor from the Russians is always handy..."
    bman "I'll ask you for a favor someday. Or maybe you'll never see me again."
    bman "Here..."

    scene club businessman 2 with dissolve
    bman "Be careful with this, kid."

    scene club businessman 3 with dissolve
    bman "It's got some kick to it, hehehe."
    mc "(Shit, this is it, finally!)"
    mc "Is this the real stuff?"

    scene club businessman 4 with dissolve
    bman "As real as it gets, hehehe!"
    bman "Now if you'll excuse me, I have three amazing women waiting for me..."
    bman "See you around!"

    stop music fadeout 5.0
    scene black with fade
    mc "(Yes, I got this shit!)"
    mc "(And that's my cue to leave!)"

    play music "audio/music/soul.mp3" loop fadein 2.5
    scene home_basement__night with fade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
