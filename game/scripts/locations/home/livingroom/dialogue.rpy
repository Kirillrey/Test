label tv_mom_1_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home tv mom 1 with fade
    mom "Oh, [mc_name]!"
    mom "You are watching the news! Finally not those violent movies."
    mc "You mean action movies? How are they voilent?"
    "The mayoral election in Midnight City will soon begin. Experts say there won't be much of a competition due to the popularity of one of the-"

    scene home tv mom 2 with dissolve
    mc "What movies do you like then?"
    mom "Hmm. I guess comedies, and romantic films."
    mom "Romantic comedies the most, probably."
    mc "Ugh... Not my thing."
    mom "Well then, you have to enjoy watching the TV most likely alone, [mc_name]."

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene black with fade

    return





label tv_isabel_1_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home tv isabel 1 with fade
    isa "So... [mc_name], what are we watching?"
    isa "News, really?"

    scene home tv isabel 2 with dissolve
    mc "It's not my fault there aren't any other channels on!"
    isa "True, it's not. But not doing anything about it and letting your sister suffer through these boring news broadcasts instead of cozying up with a nice show on..."
    isa "Now that's your fault."
    mc "Right..."
    mc "I'll see what I can do about that."
    isa "Let me know when you've figured it out! Maybe I'll even share my blanket with you, haha!"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene black with fade

    return





label tv_ruby_1_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home tv ruby 1 with fade
    ruby "Ugh! Really?!"
    ruby "That's some quality programme you're watching bro!"
    ruby "I didn't know you were educated enough for this."
    mc "Look who's talking!"
    mc "At least I'm going to college!"
    ruby "Which you failed."
    mc "Honest mistake. Won't happen again. I'll get my degree and I'll be the head of Harding Enterprises."
    ruby "Hah, you think you can take on Logan? He doesn't have a life at all, it's not like you can beat him with hard work, he's miles ahead of you."

    scene home tv ruby 2 with dissolve
    mc "Some people work hard. Some work smart."
    mc "Speaking of work, how's it going for you?"
    ruby "Oh shut up!"
    "The new drug is most popular among the wealthy young adults in Midnight City, although police reports that a cheaper 'knock-off' is on the market as well."
    "The meteoric rise of this new substance called-"
    mc "So what are you-"
    ruby "Damn it [mc_name], I can't hear the TV!"
    mc "What? I thought you didn't care about the news channel!"
    ruby "Well, now I don't..."
    mc "Whatever, Ruby!"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene black with fade

    return





label tv_alone_1_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home tv alone 1 with fade
    mc "(It's nice to relax once in a while.)"
    mc "(Well, I guess I relax most of the time, hehe.)"
    mc "(But this cable is pitiful...)"
    mc "(Nothing here but news channels. The old man probably wants to save money on these while he's being a millionare.)"
    mc "(I guess that's how you get to be a millionare though.)"
    mc "(One of dad's friends told me once, 'Money is easy to come by. Keeping it is what's hard.')"
    mc "(Of course it's hard to keep when there's so much good shit to spend it on!)"
    mc "(Whatever!)"
    mc "(I should probably get some more content on the screen somehow.)"
    mc "(I could maybe even get some SheFlix and chill action going on then.)"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene black with fade

    return






label isabel_2_afterdrink_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene home afterdrink isa 1 with dissolve
    mc "Hey sis!"
    isa "Hey! Came to watch some TV?"

    scene home afterdrink isa 2 with dissolve
    mc "Actually, I came to talk about the night we were drinking together."
    isa "What about it?"
    mc "I know it may sound funny, but it was nice sleeping next to you..."

    scene home afterdrink isa 3 with dissolve
    isa "Oh, that..."
    isa "Yeah it was... nice."
    isa "You didn't feel uhm..."
    isa "Didn't feel weird afterwards?"
    mc "Not at all. Maybe we should do it again sometime."
    if not lain_mod:
        mc "But without the booze, haha!"
        isa "Y-yeah."
        mc "(She's visibly uncomfortable talking about this.)"
        mc "(I better let this go for now.)"
    mc "Anyways, just wanted to tell you that. I'll leave you to do your thing."

    scene black with slowfade

    return






label isabel_5_tvbet1_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene isa bet 5
    else:
        scene isa bet 1 with slowfade
        isa "Hey [mc_name]!"
        isa "What are you watching?"

        scene isa bet 2 with dissolve
        mc "Oh hey!"
        mc "Ah, just this reality tv bullshit."
        mc "\"The Big Bachelor.\""

        scene isa bet 3 with dissolve
        isa "Oh, I like that, actually."
        mc "Do you?"
        isa "Yeah, is it so surprising?"

        scene isa bet 4 with dissolve
        mc "Someone unironically watching, or even liking a reality TV show? Yeah, that is surprising."
        isa "It's not that bad..."
        isa "It's kind of romantic, actually."
        mc "It's anything but romantic."
        isa "Then why are you watching it?"
        mc "Cause it's funny! Watching this mindless drama is fun. And there are so many idiots on the show it's hard not to be amused."
        isa "...{w} Anyway."
        isa "Who do you think gets a rose this time?"
        mc "Well that Molly girl is surely out."

        scene isa bet 6 with dissolve
        mc "The guy is deciding between her and the blonde with the big tits. Guess who's getting a rose haha."
        isa "No way! That girl is an airhead... Molly is totally a winner here!"
        mc "Might be an airhead, but you know, big tits. Guys like that."
        isa "I think you're wrong."
        mc "Guys like big tits though."
        isa "It's the kind of girl that matters, not just tits!"
        mc "Oh, wanna bet?"
        isa "Sure! What's the wager?"
        mc "Hah, you can ask for anything, it doesn't matter. Because I'll surely win!"
        isa "We'll see about that! If you lose you have to take me to work and pick me up for a week!"
        mc "Ooooh, okay, so we're going for the big bets. Alright."
        mc "But if I win, I get to touch your tits. Without the top on!"

        scene isa bet 7
        isa "You've got some nerve, haven't you little brother?"
        isa ".........."
        isa "But it isn't a good bet without a good wager. Deal."

        scene isa bet 5 with slowfade
    mc "Yeees! Go for it dude!"
    mc "Give it to Ms Milkbags!"
    isa "Molly is obviously going to win, come on!"
    pause 0.5

    scene isa bet 8 with hpunch
    isa "What??"
    mc "Hahahaha!"
    mc "I told you, boobie-girl wins! Yeah!"
    isa "I can't believe this!"

    scene isa bet 9 with dissolve
    mc "Haha, I told you I'd win."
    mc "Big tits just gets guys' attention."

    scene isa bet 10 with dissolve
    isa "Do you really want this as the reward?"
    isa "And here?"
    mc "Oh, you're not backing down now, are you?"

    scene isa bet 11 with dissolve
    isa "No, it's just..."
    isa "We're in the living room!"
    isa "Fine, fine. But let's be quick about it!"

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene isa bet 12 with fade
    pause
    isa "There you go..."
    mc "Wow!"
    mc "They're amazing!"

    scene isa bet 13 with dissolve
    isa "You really think so?"
    mc "(This is amazing! I can finally see her topless!)"
    mc "(Those are funbags straight form heaven!)"

    scene isa bet 14 with dissolve
    isa "But don't you think they're...{w} Ah, never mind."
    mc "What? You don't like them?"
    isa "No, it's just. I've seen girls with implants and their breasts aren't hanging as much as mine."

    scene isa bet 15 with dissolve
    pause 1.0
    mc "(She probably has one of the best pair of tits in the country, and she's complaining.)"
    mc "(Women...)"
    mc "(I can see her nipples harden as we speak.)"
    mc "(It could be because of the cold... {w} Except it's not cold in here.)"
    mc "(The beautiful shape of her large tits mesmerizes me.)"

    scene isa bet 16 with dissolve
    mc "Your breasts are fine as they are, Isa."
    mc "They're the best pair I've ever seen!"

    scene isa bet 17 with dissolve
    mc "Can I touch them?"
    isa "That was the bet, and I'm a woman of my word so...{w} Go ahead."

    scene isa bet 18 with dissolve
    pause 1.0
    isa "Ah~"
    mc "Oh wow..."
    mc "I'll be honest... I've been dreaming about this ever since I came back and saw you in the bathroom."

    scene isa bet 19 with dissolve
    isa "You can't be serious... Really?"
    mc "Yeah. You're just-{w} The perfect kind of woman, I guess."
    mc "(Her breast feels wonderful in my hand.)"
    pause 0.5

    scene isa bet 20 with dissolve
    pause 1.0
    mc "(As I lift it a little, I can feel the heavy weight of it, and that despite how big they are, it feels firm.)"
    mc "(Not as much as an implant would feel, but definitely full and firm.)"

    scene isa bet 21 with dissolve
    isa "Oh I...{w} I just hope no one sees us."

    scene isa bet 22 with dissolve
    isa "So you said before that guys like big tits..."
    isa "Do you like my big tits?"
    mc "(Oh man!)"
    mc "Like them? {w} I love 'em!"

    scene isa bet 23 with dissolve
    mc "It feels to me you're a bit insecure about them."
    mc "And you shouldn't be. These are awesome!"
    isa "You're sweet..."
    isa "So you'd give me a rose if we were on The Big Bachelor?"
    mc "Hell yeah!"

    scene isa bet 24 with dissolve
    mc "(As I gently massage hear breast with my hand I can feel the tension rising, despite the light-hearted conversation.)"
    mc "(If I'm starting to get aroused, she must be feeling the same...{w} Right?)"
    mc "(Maybe I can try to advance furth-)"

    scene isa bet 25 with fade
    isa "I should probably cover up, before anyone sees us like this."
    isa "I think I honored the bet properly. What do you think?"
    mc "Oh I think we should make bets more often."
    isa "Ahahah! Maybe next time you'll lose!"
    pause 0.8

    scene isa bet 26 with dissolve
    pause 1.0
    mc "With a sister like you, I'm already a winner."
    isa "Oh God...{w} Does that really work on the girls?"
    mc "Does it work on you?"
    isa "Okay, stop, I'm putting my shirt back on and I'm gonna go to bed before I have to hear any more of your cheesiness!"
    isa "Haha~ {w} Good night, [mc_name]!"
    mc "See you next time, The Big Bachelor continues on Channel 6!"

    scene isa bet 27 with fade
    mc "(What a lucky motherfucker I am...)"
    mc "(She's amazing!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label isabel_7_tvbet2_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene isa bet 7
    else:
        scene isa bet 1 with slowfade
        isa "Hey [mc_name]!"
        isa "What are you watching?"

        scene isa bet 2 with dissolve
        mc "Oh hey!"
        mc "Our 'favorite' show, The Big Bachelor again."

        scene isa bet 3 with dissolve
        isa "Oh, mind if I join?"
        mc "I'd be happy to have you on the couch here with me sis!"

        scene isa bet 4 with dissolve
        isa "Wanna bet again?"
        mc "You don't learn from defeat? Sure, I'll happily take my reward!"
        mc "This guy is an open book to me."
        isa "Same as last time?"
        mc "For you, maybe. But since I won last time, I need something more to keep it exciting."
        isa "More than fondling my...{w} What do you want?"
        mc "I want to suck on them."
        isa "Suck on them? For real?"
        mc "Men like that."
        isa "Men like a lot of things..."
        isa "Fine, it doesn't matter. I'll win this time anyway."
        mc "Deal!"

        scene black with fade
        show text "{size=72}{color=#dc38bf}After [mc_name] won again...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve

        scene isa bet 7 with dissolve
        isa "Is this the second time this is airing? Have you seen this before?"
    isa "How did you know again who's getting a rose?"
    mc "Accusing me of cheating?"
    mc "I haven't seen this. I'm just good at this kind of thing I guess."
    mc "So, you've lost the bet..."
    isa "Fine... But let's be quick!"

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene isa bet titsuck 1 with fade
    pause 1.0
    mc "I don't want it to be quick though!"
    isa "If anyone found us here, just imagine what would happen!"
    isa "Mom or dad would freak out..."
    isa "They'd probably throw you out."

    scene isa bet titsuck 2 with dissolve
    pause
    isa "And me, especially if they saw me enjoying you sucking on my ti-"
    isa "Uhm-"
    mc "Oh? So you enjoy that?"
    isa "Ah damnit [mc_name], forget I said anything."
    isa "Just come here and put your mouth on my nipple!"
    mc "Your wish is my com-"

    scene isa bet titsuck 3 with Dissolve(0.3)
    scene isa bet titsuck 3 with hpunch
    pause 1.2
    mc "Mhmm!"
    mc "(She pulled me onto her tits!)"
    mc "(So she's getting enjoyment out of this afterall.)"
    mc "(That's awesome!)"
    pause 0.5

    scene isa bet titsuck 4 with dissolve
    pause 0.5
    isa "Ah...~"
    isa "You're so gentle with it..."
    isa "I like that."


    scene isabettitsuckanim1 with dissolve
    pause 1.5
    mc "(She said she likes it!)"
    mc "(What's even more awesome then her enjoying it is the fact that my sister's nipple is in my mouth!)"
    mc "(I can feel it hardening as I flick my tongue over it.)"
    pause

    scene isabettitsuckanim2 with dissolve
    pause
    isa "Ahh~"
    mc "(I'm sucking on her tits like I'm expecting milk to come out, rolling and twisting my tongue over her areolas.)"
    mc "(I'm gently biting her nipple a little bit now and then, while tasting her wonderful breast...)"
    isa "[mc_name]..."
    isa "You have to stop!"


    scene isa bet titsuck 9 with dissolve
    mc "Did I do something wrong?"
    isa "No it's just..."
    mc "(She's so close to me I can feel her breath on my face.)"

    scene isa bet titsuck 10 with dissolve
    pause 1.0
    isa "I just started to get... excited."
    mc "What if I want you to be excited..."
    isa "I...{w} I have to get dressed, anyone could come out here at anytime. It's not even late in the night."
    mc "Alright. I don't want to do anything you're not comfortable with."
    isa "I know... And I'm thankful for that."
    isa "It's all so exhilirating and the rush of it is... My brain is going numb."
    isa "Just...{w} Give me some time to think, please."
    mc "Whatever you need, Isa."
    isa "I'll see you later..."

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label aunt_1_meeting_dialogue:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene aunt intro 1 with slowfade
    mom "Oh, I thought you might have found someone by now!"
    s "No, the last one turned out to be an idiot too."
    s "Looks like I'm drawing in all the assholes somehow."

    scene aunt intro 2 with dissolve
    mom "But he seemed like such a nice guy. What was his name...{w} Joe?"
    s "Jerome...{w} Don't even mention it."

    scene aunt intro 3 with dissolve
    s "He was flaunting his car, an old beemer. His jaw dropped when he saw my new Benz in the garage."
    s "He just couldn't accept that I was making more than him with his law degree."
    s "It's hard to find men who aren't self-conscious around you when you make 7 figures on your own, sis."
    s "But it's not like you're doing bad either. No one can come close to the almighty business magnate Raymond of course."
    s "But how's business for you at the magazine? And the kids? Now that all of them are back in the nest it must be hard on you."

    scene aunt intro 2 with dissolve
    mom "It's fine, honestly."
    mom "[mc_name] helps out a lot, he even made me dinner the other day!"

    scene aunt intro 4 with dissolve
    s "[mc_name]? Made you dinner?"
    s "Haha, that's rich!"

    scene aunt intro 5 with dissolve
    s "I can't imagine that spoiled little brat doing anything like that."
    s "You know you spoiled him too much, right?"
    s "Logan is okay I guess, but he's weird. Is he still so introverted?"
    s "The only one who turned out right is Isabel, honestly."
    mom "Sofia! It's my children you're talking about!"
    mc "(Hmm, that woman looks familiar...)"

    scene aunt intro 6 with dissolve
    mom "Oh, [mc_name]!"
    mom "We were just talking about how sweet you were the other day to make me dinner."
    mc "Oh? And who is our guest?"

    scene aunt intro 8 portrait with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.05
    pause

    s "You've been away so long you don't even recognize your own aunt?"
    s "That's not what I expected from my dear little nephew..."

    scene aunt intro 7 with dissolve
    mc "Aunt Sofia?"
    s "In the flesh, kid."
    mc "(It's been a while since I have last seen her or even talked to her.)"
    mc "(She's my aunt from my mom's side of the family.)"
    mc "(She never spent a lot of time with us, but she visited once or twice a month and brought us all gifts everytime.)"
    mc "(Everyone was excited when we heard she was coming over.)"
    mc "(She lives at the other part of town, close to her business. She made her own company and built it from the ground up herself.)"
    mc "(She's rather proud of that, and never fails to let everybody else know of it.)"
    mc "(I guess the regular visits have been going on the same way while I was away.)"

    scene aunt intro 9 with dissolve
    s "Hmmm, you've really changed, at least on the outside."
    s "You're taller now. I bet the girls like that."
    mc "I guess they do. I can't complain."

    scene aunt intro 10 with dissolve
    s "A bit cocky, too."
    s "I wonder where that comes from."
    s "I heard the reason you came back is because you failed college."
    s "That must have been disappointing. {w} To your parents, I mean."


    menu:
        "Insult" if morality < 0:
            mc "Yeah, just as disappointing as your manners are aunty."
            s "Insolent...{w} but fair enough."


        "Insult" if morality > 0:
            pass
        "Level headed":


            mc "It wasn't a pleasant experience for either of us, but I'm sure I can improve."
            s "I hope you'll prove us all wrong."


    mc "(Dude, that's messed up that she's coming down on me so hard in the first 30 seconds of our meeting after 2 years.)"
    mc "(I remember she was always a no-bullshit kind of person, but she should tone it down, really.)"

    scene aunt intro 11 with dissolve
    mc "(What I don't remember is those big fuckin jugs she's pushing together under that sweater right now.)"
    mc "(Maybe I wasn't as 'attentive' back then or simply her tits got bigger but damn, that's a nice pair!)"

    scene aunt intro 12 with dissolve
    pause 1.8

    scene aunt intro 13 with dissolve
    mc "(Shit, was it that obvious that I'm looking at them?)"
    s "Interesting..."
    s "Ahah~ {w} This might be fun."

    scene aunt intro 14 with dissolve
    mom "Don't be so hard on him."
    mom "People make mistakes. Ever since he came back he's doing okay."
    mom "He's finishing his degree at Midnight University instead under Raymond's supervision."
    mom "He even bough his own car and took me to work in the morning!"
    mc "(That piece of shit car, and even that was gifted to me by that sleazeball Thorne.)"
    mc "(I need to get my shit together...)"
    mc "(Mom is talking so nice about me. Maybe I'm genuinely impressing her...)"
    mc "(Or she's just trying to paint me in a positive light in front of Sofia.)"

    scene aunt intro 15 with dissolve
    s "Well [mc_name], sounds like someone beat some sliver of responsibility in you."
    s "If you need a job, just drop by. I'm sure I can find something suitable for you..."
    s "Now if you'll excuse me, I just dropped by for a little during my lunch break, I need to get back to work."
    s "I don't dare leave them unsupervised for long..."
    mc "Pleasure seeing you aunty."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
