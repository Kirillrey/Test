label aunt_2_worktalk_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0

    scene aunt work talk 1 with slowfade
    s "I didn't expect you so soon."
    s "I guess you really need a job, then."
    s "Or...?"
    mc "I came here because I need a favor, actually."

    scene aunt work talk 2 with dissolve
    s "Ah... {w} Of course."
    s "A favor. What kind of favor?"

    scene aunt work talk 5 with dissolve
    mc "You are running a construction comapny."
    mc "And I guess you have trucks. Well, I'm in need of a truck right now."
    s "A truck? What do you need that for?"
    mc "You see, my dad has this kind of competition between me and my brother."
    mc "The one who can show himself as most fitting to run the family business in the future, will be Dad's successor."
    mc "But for that I need to beat Logan, so I'm setting up a company myself to show that I can make something good from scratch."

    scene aunt work talk 3 with dissolve
    s "That's interesting."
    s "So you want to be the top dog? To have all the money and power that comes with such a high position?"
    s "That's actually brilliant by your father. He wants to entrust everything to one of you once he retires..."
    s "So why not make a competition out of it openly, and have you guys get your shit together. Makes sense to me."
    s "So you're starting some kind of moving business? Deliveries maybe?"

    scene aunt work talk 1 with dissolve
    mc "That's exactly right."
    mc "We will deliver product. {w} I mean products. {w} Yeah."


    menu:
        "Look at her feet":
            $ aunt_feet = True

            scene aunt work talk 6 with dissolve
            mc "(That skirt is pretty short...)"
            mc "(And she doesn't have her stockings on today.)"
            mc "(Her pretty legs and feet are on full display.)"

            scene aunt work talk 7 with dissolve
            mc "(I remember I always admired her figure back in the day, but I didn't actually notice how she's such a cougar.)"
            mc "(She obviously takes care of herself.)"
            mc "(But the pretty feet? That's just genetics.)"
            mc "(I'd happily pat them with my shaft, that's for sure...)"

            scene aunt work talk 1 with dissolve
        "Focus on her":

            mc "(I shouldn't get distracted now.)"


    s "Alright, here's the deal."
    s "I don't really give a damn about your little competition with your brother."
    s "I worked hard for what I have and I don't want you to mess anything up with your childish quarrel."

    scene aunt work talk 4 with dissolve
    s "However...{w} If you win, you could be a powerful business ally."
    s "I've never liked your father more than someone can like a robot, and your brother Logan has some positive qualities but he's too much of a daddy's boy."

    s "You on the other hand, are kind of a little shit, but not all's lost. I can see you have some fire in you, boy."
    s "So I guess here's the perfect opportunity to prove yourself."
    s "I'll give you one or two of my trucks to use, but you have to buy them off me. I'll give you a few months time to get the money together."
    s "But that's not all. You asked me a favor. Now I have some favors to ask, too."

    return



label aunt_2_worktalk_feet_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
        scene aunt work talk 1
        menu:
            "Look at her feet":
                scene aunt work talk 6 with dissolve
                mc "(That skirt is pretty short...)"
                mc "(And she doesn't have her stockings on today.)"
                mc "(Her pretty legs and feet are on full display.)"
                scene aunt work talk 7 with dissolve
                mc "(I remember I always admired her figure back in the day, but I didn't actually notice how she's such a cougar.)"
                mc "(She obviously takes care of herself.)"
                mc "(But the pretty feet? That's just genetics.)"
                mc "(I'd happily pat them with my shaft, that's for sure...)"
                scene aunt work talk 1 with dissolve
        s "Alright, here's the deal."
        s "I don't really give a damn about your little competition with your brother."
        s "I worked hard for what I have and I don't want you to mess anything up with your childish quarrel."
        scene aunt work talk 4 with dissolve
        s "However...{w} If you win, you could be a powerful business ally."
        s "I've never liked your father more than someone can like a robot, and your brother Logan has some positive qualities but he's too much of a daddy's boy."
        s "You on the other hand, are kind of a little shit, but not all's lost. I can see you have some fire in you, boy."
        s "So I guess here's the perfect opportunity to prove yourself."
        s "I'll give you one or two of my trucks to use, but you have to buy them off me. I'll give you a few months time to get the money together."
        s "But that's not all. You asked me a favor. Now I have some favors to ask, too."

    play music "audio/music/red.mp3" loop fadeout 1.5 fadein 3.0
    s "I noticed, you're a little fucking pervert, aren't you?"
    mc "What?"
    s "Play dumb and I swear to God I'll throw you out of here in a second."
    s "I saw you sizing me up at your mom's house, checking out my tits."
    s "And now you keep glancing at my feet while shifting in your seat."
    s "Don't try to fool me. You want to fuck me, don't you?"
    mc "(How the fuck can she read me so well after only a couple of minutes of conversation?)"
    mc "(No wonder she has the reputation of a terrific negotiator.)"
    mc "(That doesn't change the fact that I'm in deep shit now. Just what the hell does she want?)"
    mc "(It's clear that if she thinks I'm bullshitting I'm out of here without a truck.)"
    mc "(I have to go balls to the walls with this. All or nothing.)"
    mc "Yeah, so what? I'm guessing it's not something new. I bet a lot of men look at you that way."
    s "They do. But they aren't my nephew."
    s "Tsk tsk tsk... {w} Naughty boy."
    s "Since you like my feet so much, why don't you give me a foot massage then?"
    s "Here, I'll take my skirt off for you..."

    scene aunt foot massage 1 with dissolve
    mc "Are you for real?"
    s "What does it look like?"
    s "Now why don't you get to it?"

    scene aunt foot massage 2 with dissolve
    mc "It's just... You're my aunt and all."
    s "Oh, look!"
    s "You checking me out and having a fucking hardon for me is normal, but giving your aunty a foot massage is not?"

    scene aunt foot massage 3 with dissolve
    s "You asked me a favor."
    s "I delivered. Now you do me a favor and massage my feet."
    s "I know you like my feet so I don't see a reason you should protest."

    scene aunt foot massage 4 with dissolve
    mc "(Damn, when she said she's taking her skirt off I thought I'm gonna see her panties, or maybe even more if she didn't wear one.)"
    mc "(But I see she has this bodice- or whatever it's called.)"
    mc "(Fuck, this went from zero to a hundred real quick.)"

    scene aunt foot massage 5 with dissolve
    mc "(I guess I'll do what she asks for now.)"
    mc "(She's right about me liking her feet and all that. But I'm surprised she's so sexual and not bothered by our relationship.)"
    s "You don't have to go easy on me."
    s "I like a man with strong hands."

    scene aunt foot massage 8 with dissolve
    pause
    s "Yeah, that's it."
    mc "(Her feet are nicely shaped, they fit into my hands perfectly.)"
    mc "(I can feel that she's freshly shaved, or better yet, waxed.)"
    mc "(Her calf is tight and muscular despite her age and she seems to wear high heels a lot, but that doesn't show on her feet.)"
    mc "(I guess she isn't new to foot stuff, she must have pedicures regularly.)"

    scene aunt foot massage 9 with dissolve
    s "Is that a bump I'm feeling?"
    s "Oh, someone's almost ready to come out to play!"

    scene aunt foot massage 10 with dissolve
    s "How about that... {w} Your dick is getting hard just from massaging my feet."
    mc "(This is getting weird, fast. I'm more used to being the one who wants to grope the ladies, not the lady insisting I grope her.)"
    mc "(Besides, it's not just from the massage.)"
    mc "(She's been rubbing her feet on my crotch the entire time, and her pussy is almost on display!)"

    scene aunt foot massage 12 with dissolve
    s "Tell me, have you ever sucked a woman's toes?"
    mc "No. And there's no way you're into this!"
    s "Why? Only you can be a twisted little pervert?"
    s "Or maybe I get off on seeing you like this, made uncomfortable by my advances, even though you really want to do it."
    s "I've had my fair share of men and most of them are boring. I like to play."

    scene aunt foot massage 11 with dissolve
    s "So why don't you play along?"
    s "Or are you one of those guys that like to smell them first?"

    scene aunt foot massage 13 with dissolve
    s "Here, take them..."
    s "I know you want to suck on my toes, and lick them all over."
    s "...push your tongue between my pedicured little toes..."
    mc "This is weird as hell but...{w} Fuck it!"

    scene aunt foot massage 14 with dissolve
    s "Ah yes, that's it boy!"
    s "Suck on them, lick them all over!"

    scene aunt foot massage 15 with dissolve
    s "Ahaha~ {w} I never expected your return home to be this much fun!"
    s "I can see you're getting off on this, getting off from licking my little feet!"
    mc "(I can't believe I'm doing this...)"
    mc "(It's wrong, and it {i}doesn't{/i} feel right, but I have my reasons.)"
    mc "(The truck. And her pretty fucking feet!)"

    scene aunt foot massage 16 with dissolve
    mc "(I'm moving my tongue over her big toe, circling around it, savoring it, tasting her feet.)"
    mc "(I can feel the bulge in my pants throb harder as I flick my tongue over to her toe, while having the sole of her foot firmly in my hand.)"
    s "You're getting into it... Yes!"
    s "Do you want me to moan? You dirty pervert, you're making your aunt moan like a dirty whore with your tongue..."

    scene aunt foot massage 17 with dissolve
    s "Mhhhm~"
    s "Ah yes... My foot is so wet from your saliva..."
    mc "(She's a natural born seductress...)"
    mc "(Like a succubus, she's making me want more and more!)"

    scene aunt foot massage 18 with dissolve
    s "Mmmmh~"
    s "You're so good at this. I bet you've fantasized about sucking on women's feet..."
    s "How does it feel to have your fantasy fulfilled, huh?"
    mc "Good..."
    s "Is that so?"

    scene aunt foot massage 15 with dissolve
    s "Then how about this?"
    s "You keep being a good boy and keep doing me favors, and we'll have a great time together..."
    s "Now go home and jerk off while thinking of my feet in your mouth, will you?"
    s "I'll be in touch. Ahahah~"
    mc "(Damn, I don't want to let her order me around like a little bitch. Patience, [mc_name]...)"
    mc "(I'll get back at her at a later time when I have more leverage.)"

    $ renpy.end_replay()

    return



label aunt_2_worktalk_ass_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
        scene aunt work talk 4
        s "You on the other hand, are kind of a little shit, but not all's lost. I can see you have some fire in you, boy."
        s "So I guess here's the perfect opportunity to prove yourself."
        s "I'll give you one or two of my trucks to use, but you have to buy them off me. I'll give you a few months time to get the money together."
        s "But that's not all. You asked me a favor. Now I have some favors to ask, too."

    play music "audio/music/red.mp3" loop fadeout 1.5 fadein 3.0
    s "I noticed, you're a little fucking pervert, aren't you?"
    mc "What?"
    s "Play dumb and I swear to God I'll throw you out of here in a second."
    s "I saw you sizing me up at your mom's house, checking out my tits."
    s "And now you're looking at me like a hungry wolf..."
    s "Don't try to fool me. You want to fuck me, don't you?"
    mc "(How the fuck can she read me so well after only a couple of minutes of conversation?)"
    mc "(No wonder she has the reputation of a terrific negotiator.)"
    mc "(That doesn't change the fact that I'm in deep shit now. Just what the hell does she want?)"
    mc "(It's clear that if she thinks I'm bullshitting I'm out of here without a truck.)"
    mc "(I have to go balls to the walls with this. All or nothing.)"
    mc "Yeah, so what? I'm guessing it's not something new. I bet a lot of men look at you that way."
    s "They do. But they aren't my nephew."
    s "Tsk tsk tsk... {w} Naughty boy."
    s "Since I turn you on so much, why don't you give me a massage then?"
    s "Here, I'll take my skirt off for you..."

    scene aunt ass massage 1 with dissolve
    mc "What the hell is happening?"
    s "Oh, you're surprised?"
    mc "Damn right I am, you just stripped and asked me to massage your ass!"

    scene aunt ass massage 2 with dissolve
    s "You asked me a favor. Now I'm asking you one."
    s "Besides, it's not like I'm asking something you don't want to do."

    scene aunt ass massage 3 with dissolve
    s "I could see it the moment you laid eyes on me the other day."
    s "You didn't have it in you two years ago. But it looks like my little nephew has grown some balls."

    scene aunt ass massage 4 with dissolve
    s "But you're still a little pervert who salivates over his aunt."
    s "But that's okay. This will be our little secret."
    s "You get to fulfill your sick little fantasies and I get to have some fun while ordering you around."

    scene aunt ass massage 5 with fade
    s "I don't have all day so let's get to it."
    mc "(This is fuckin crazy.)"
    mc "(One moment I'm talking to my aunt and the next she turns into a fucking freak with a control fetish.)"
    mc "(Man this is messed up.)"
    mc "(One thing I can't argue with though... {w} That ass is sweet!)"
    mc "(She's getting me what I want so I guess I'll have to follow her lead...{w} For now.)"

    scene aunt ass massage 7 with dissolve
    mc "I'll start here if that's okay."
    s "Takin' it slow? How considerate of you."
    s "Do what you will, but don't make it boring."

    scene aunt ass massage 6 with dissolve
    mc "Do you like it soft or hard?"
    mc "The massage, I mean."
    mc "(God...{w} why am I doing that?)"

    scene aunt ass massage 8 with dissolve
    s "The massage...{w} Of course."
    s "You don't have to go easy on me. I like a man with strong hands."
    mc "(Doesn't seem like it. She seems pretty domineering.)"
    mc "(But maybe she wants someone to take on her instead.)"

    scene aunt ass massage 9 with dissolve
    mc "(She's probably not used to people standing up to her.)"
    mc "(Building such a construction behemoth company from the ground up is no small feat, especially for a woman in that sector.)"
    mc "(She's considered among Midnight City's finest, right up there with dad, yet she lives in an apartment instead of a house.)"
    mc "(It's closer to her office, she says. Well I can say she has one of the finest asses!)"

    scene aunt ass massage 10 with dissolve
    s "Oh, now we're talking!"
    s "How do you like it?"
    s "You are groping my ass like I'm some kind of frat house slut."
    s "Want me to moan for you?"

    scene aunt ass massage 11 with dissolve
    mc "(Just how weird is this going to get...)"
    s "Mmm~"
    s "You're making your aunt moan by groping her. Are you proud of yourself, you pervert?"
    mc "Stop calling me a pervert!"
    s "Shut up and keep touching my ass!"
    s "I know you're getting hard already, so stop pretending you don't like this."
    mc "(I like her ass, I just don't like the way she's talking to me. Fuck!)"
    mc "(I'd gladly pop it in her though!)"

    scene aunt ass massage 12 with dissolve
    s "Mhaha~"
    s "You're not bad at this, nephew..."
    s "Now tell me...{w} Do you like my ass? And don't you lie to me!"
    mc "Yes..."
    s "Is that so?"

    scene aunt ass massage 13 with dissolve
    s "Then how about this?"
    s "You keep being a good boy and keep doing me favors, and we'll have a great time together..."
    s "Now go home and jerk off while thinking of worshipping my ass, will you?"
    s "I have some other things to do. I trust you can see yourself out."
    s "I'll be in touch. Ahahah~"
    mc "(Damn, I don't want to let her order me around like a little bitch. Patience, [mc_name]...)"
    mc "(I'll get back at her at a later time when I have more leverage.)"

    $ renpy.end_replay()

    return



label aunt_2_worktalk_outro_dialogue:
    stop music fadeout 10.0
    scene eliana pool talk 1 with Fade(1.0, 1.0, 1.0)
    play sound "audio/sfx/sms.ogg"
    mc "(Hmmm...{w} Sofia sent me a message after I left.)"
    mc "(It's the NFC unlock code for her apartment complex.)"
    mc "(This might come in handy later.)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with Fade(1.0, 0.5, 0.5)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
