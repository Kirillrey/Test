label nc1_natsuko1_dialogue:

    mc "There's lots of people here. I guess I'll see if this chick knows anything."
    pause 0.5

    scene nightclub_lounge__tanya_ground with dissolve
    pause 0.5
    mc "Huh? Damn, I guess I lost her in the crowd. I wonder where she went."

    return






label nc1_tanya_dialogue:

    scene nightclub boss 1 with dissolve
    guard "Step back, punk!"
    mc "Whoa, what the fuck is your problem?"
    guard "Nobody gets close to Ms Tanya while I'm here!"

    scene nightclub boss 2 with dissolve
    tanya "Viktor!"
    tanya "Let the boy through."

    scene nightclub boss 3 with dissolve
    tanya "This shithole is boring, I need some company."
    tanya "He looks interesting, ahaha~"

    scene nightclub boss 4 with dissolve
    mc "(They both talk with a heavy Russian accent...)"
    viktor "I'm watching you..."
    mc "Thanks... I guess?"
    mc "(Geez...)"
    mc "(This woman is hot! And having this ape of a bodyguard probably means she's important, too.)"

    scene nightclub boss 6 with dissolve
    tanya "You must be Thorne's little minion!"
    mc "(How does she know that? And who is this Ms Tanya anyway?)"
    mc "I have no idea what you're talking about."
    tanya "Oh? {w} Ahaha~"
    tanya "Sit down, I don't bite... {w} Too much."

    scene nightclub boss 7 with fade
    tanya "Now, boy, don't play dumb with me."
    tanya "I hate that. I know what you're here for."
    mc "I don't know what you're-"
    tanya "Let's get something straight."
    tanya "If you lie to my face one more time I'll have Viktor here cut your tongue out."
    mc "(What the fuck have I gotten myself into...)"
    tanya "Clear?"
    mc "...Clear."
    tanya "Good."

    scene nightclub boss 8 with dissolve
    pause 0.4

    scene nightclub boss 9 with dissolve
    tanya "Thorne sent you to look for Halo, right?"
    mc "I..."
    tanya "Everyone is after that shit now. No surprise that little worm wants it too."
    tanya "Have you found it yet?"
    mc "No..."

    scene nightclub boss 10 with dissolve
    pause 1.0

    scene nightclub boss 9 with dissolve
    tanya "Thought so..."
    tanya "If you find one, bring it to me. I'll pay you much more than that idiot."
    tanya "But then again, if you came to me you'd be a little traitor. Right?"
    mc "What is this all about?"
    mc "And who the hell are you?"
    tanya "Looks like you're not very familiar with how things work in this city..."
    tanya "I run things around here, boy."
    tanya "You're a little fly. As long as you stay like that, you have nothing to worry about."
    mc "(She talks like...)"
    mc "(Is she mafia? Well, I better not ask that directly.)"
    mc "(If Viktor over there doesn't crumple me into a piece of paper- I'd call that a win.)"
    mc "(It's best to stay cool and don't tell them anything, she already knows what I'm here for.)"
    mc "(I can ask Thorne later about her.)"
    tanya "Hm..."

    scene nightclub boss 10 with dissolve
    pause 0.5

    scene nightclub boss 9 with dissolve
    tanya "You have a cute face, I like you."
    tanya "As I said, if you find Halo, bring it to me and you'll be rewarded."
    tanya "But tell your old fart of a 'friend' to not get any more funny ideas. I'll let this one slide, because you're a cute little boy."
    tanya "Now get out of here."
    mc "My pleasure!"

    if not nc1_natsuko1:
        scene nightclub_lounge__natsukotanya_ground with slowfade
    else:
        scene nightclub_lounge__tanya_ground with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
