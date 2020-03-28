label thorne_1_kyleenvelopesjail_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    scene streets kyle 1 with fade
    mc "(Alright, this should be the area Kyle said to meet him at. He said he'd be at the bottom of some stairs beneath a raised walkway...)"
    mc "(There he is.)"
    mc "Hey, Kyle."

    scene streets kyle 2 with dissolve
    kyle "[mc_name], bud, you found me. Good."
    mc "Of course I found you; it wasn't hard."
    kyle "It's good to know you can find vague locations then."
    kyle "But hey, before we get down to business... man it's good to be back hangin' out! It's been so boring without someone as mischievous as me around."
    mc "Haha Yeah, it's definitely been too long, man."
    kyle "Alright, so, you wanted to get makin' some dough, right?"
    mc "Hell yeah. After my dad confiscated all my money, I'm in need of it."
    kyle "Excellent. Excellent. I got the perfect gig lined up for you."

    scene streets kyle 3 with dissolve
    kyle "All you need to do is deliver these envelopes and the guys receiving them will give you cash."
    mc "That's all? Just deliver these envelopes and they'll pay me on the spot?"
    kyle "That's all. Just a {i}drop-&-grab{/i}, easy as pie."
    mc "You're not starting a postal service are you? Becoming a postman wasn't really the job I was hoping for."
    kyle "Ha. Nah, man, nothing like that. Although, the postal service has a damn good pension plan."
    mc "Never pegged you for the \"thinking of the future\" type, Kyle."
    kyle "Hey, planning for the future is important. So, you're up for it?"

    scene streets kyle 4 with dissolve
    mc "What's actually in the envelopes?"
    kyle "I couldn't tell ya, man. But I do know people will pay prime cash for what's in them."
    mc "Hmmm... alright, man, gimme those. Really can't turn down a good opportunity when it stares me in the face."
    kyle "That's why you're my boi."



    scene streets deal 1 with slowfade
    mc "(That's two down, just a couple more to go.)"
    mc "(I really don't know why they can't just put actual addresses on these instead of having me use landmarks to find the locations.)"
    mc "(And some of these people are weird as shit. But I suppose I really can't complain; not with all the cash in my pocket.)"

    scene streets deal 2 with fade
    play music "audio/music/menacingstalker.mp3" loop fadeout 2.0 fadein 2.0
    mc "(Finally at the last location. Geeze, this place is kind of a shit hole.)"
    mc "(Looks more like a drug den than where someone would actually live.)"

    scene streets deal 3 with dissolve
    mc "(Hopefully no one tries to jump me in here; I didn't think to bring a weapon.)"
    mc "(Ah, this looks like the place.)"

    scene streets deal 4 with dissolve
    "*knock knock knock*"

    scene streets deal 5 with dissolve
    shady "You're the guy?"
    mc "Yeah, I'm 'the guy'. I have an envelope for you."
    shady "Perfect. Give it here."
    mc "You have my..."

    scene streets deal 6 with vpunch
    mc "*slam* ...money."
    mc "What the fuck? Hey, I think you forgot to pay me for that."

    scene streets deal 7 with dissolve
    mc "*KNOCK KNOCK* HEY!"
    mc "(Oh this fucking asshole is gonna get it.)"

    scene streets deal 8 with dissolve
    detective "Well well well, it seems we have another vagrant hanging about."
    mc "Vagrant? I ain't no vagrant."
    detective "Oh, I'm sorry. I guess that makes you one of the local lowlifes then."
    mc "Do I really look like someone that would live around here?"
    mc "Look, I don't know what your deal is, but I'm just gonna go."
    wolfe "I don't think so. I'm Special Agent Wolfe, and you'll be coming with us."
    mc "What? Why?"

    scene streets deal 9 with dissolve
    wolfe "You've found yourself in some deep shit, kid."
    mc "What are you even talking about?"
    wolfe "Do you really think your activities this evening have gone unnoticed? We've been trailing you since your last drop."
    mc "I don't know what it is you think I've been doing, but I haven't done anything wrong."

    scene streets deal 10 with dissolve
    wolfe "Save it, kid. Just come with us quietly and you won't get hurt."
    mc "(Fuck, these guys are being serious. What the hell is going on here?)"
    mc "(No point trying to escape this; I'd really rather not get shot today.)"



    scene jail 1 with slowfade
    mc "When are you going to tell me what I've done wrong? You can't keep me here."
    mc "Do you even {i}know{/i} who my father is?"

    scene jail 2 with dissolve
    wolfe "With the kind of shit you're in, kid, money won't help you get out of it. No matter how much 'daddy' is worth."

    scene jail 3 with fade
    mc "(Shit. This is not good.)"
    mc "(My father is going to be furious. I can only imagine what he's going to say about this.)"
    mc "(He might even disown me, or at least threaten it.)"

    scene jail 5 with dissolve
    mc "(I wonder when someone will even be able to come get me?)"
    mc "(Or how they'll even know I'm here, for that matter. Since these dickheads won't give me my phone call.)"

    scene jail 6 with dissolve
    mc "(This isn't the first time I've been in a holding cell. But this seems much more serious than those previous times.)"
    mc "(I don't want to go to jail, and certainly not for Kyle's stupid shit.)"
    mc "(What the fuck has that moron even gotten into if I got arrested for it?)"
    mc "(Makes me wonder how much that asshole actual knew before handing me those envelopes.)"
    mc "(One thing's for sure... I'll owe him a right hook to the face after this.)"

    scene jail 7 with dissolve
    thorne "Feeling comfortable over there?"
    thorne "I can leave if you just want to sleep."

    scene jail 8 with dissolve
    mc "What? Who are you?"
    thorne "I'm your attorney."
    mc "My dad sent you?"

    scene jail 9 with dissolve
    thorne "I don't think Mr. Harding would be pleased to learn that his son is in jail."
    thorne "You got yourself into some deep shit kid, but I might have something of interest in that pool of shit you're swimming in."
    mc "What do you want?"
    thorne "You'll owe me one. I think that'll be enough for now."

    scene jail 10 with dissolve
    mc "Wait, that's it?"
    mc "What about that hardass special cop?"
    thorne "Taken care of, for now."
    mc "Just like that?"

    scene jail 11 with dissolve
    thorne "Look, kid."
    thorne "I called on some important favors to get you out of this."
    thorne "Don't make me regret my decision. Start walking."

    scene jail 12 with slowfade
    mc "Thanks, for getting me out of there, but who the fuck are you?"
    thorne "Isaac Thorne. Here's my card."
    thorne "Drop by my office if you need some work."

    pause 0.5
    play music "audio/music/soul.mp3" loop fadeout 3.0 fadein 2.5
    scene black with slowfade

    return






label thorne_9_cartheft_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
        scene car theft 13
    else:
        play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
        scene car theft 1 with slowfade
        pause 0.3

        scene car theft 2 with vpunch
        pause 1.0

        scene car theft 3 with dissolve
        mc "(Looks like this is the place.)"
        mc "(I can't believe I'm doing this, like a fuckin common criminal!)"
        mc "(But twenty thousand dollars though...)"

        scene car theft 4 with dissolve
        mc "(I could start a small business of sorts.)"
        mc "(Maybe an online one?)"
        mc "(Yeah. I could start selling stickers or some shit. People love that.)"
        mc "(Uh, anyways. I'll have plenty of time to think about this once I'm done counting my money.)"
        mc "(I better get this done ASAP.)"

        scene car theft 5 with dissolve
        mc "(According to the note, this is the garage...)"
        mc "(Let's see...)"

        scene car theft 6 with dissolve
        mc "(That's it!)"
        mc "(It's pretty dark in there, but I think I can see it!)"
        mc "(Alright, time to go to town on this bitch!)"

        stop music fadeout 5.0
        scene car theft 7 with slowfade
        mc "Come on now, you piece of shit!"
        mc "Hnnng!"

        scene car theft 8 with dissolve
        play music "audio/music/comedy.mp3" loop
        m "[mc_name]! What a surprise! I didn't know I'd see you here!"

        scene car theft 9 with hpunch
        mc "Shit!"
        m "Shit?! Is that how you want to talk to me?"

        scene car theft 10 with dissolve
        mc "Oh, Melissa! {w} He-heh, I didn't know it was you."
        mc "(What the fuck is she doing here? And right now?)"
        mc "(Thankfully she's dumb enough to not cause a huge problem.)"
        mc "(Or rather, she probably couldn't imagine I'm up to no good.)"
        mc "(But how should I get rid of her?)"

        scene car theft 9 with dissolve
        mc "Uh, you kinda scared me a bit."

        scene car theft 8 with dissolve
        mc "(Maybe if I ignore her she will go away...)"
        m "Oh I see."
        m "What are you doing?"
        mc "I'm trying to open the door."
        m "Why? Forgot your keys? {w} I didn't know your dad had another garage here."

        scene car theft 9 with dissolve
        mc "{i}Another{/i} garage?"
        m "Yeah, like that one on Starlight Avenue."
        mc "(Interesting... Better put that into the memory bank.)"
        mc "Yeah, exactly. I'm trying to get in becuase I forgot to bring the keys."

        scene car theft 11 with dissolve
        m "And you're getting in with that big rod in your hands?"
        m "Mmm, you're so strong! I've always loved that about you!"
        pause 1.0
        "*Clank!*" with vpunch

        scene car theft 12 with dissolve
        mc "Fuck yeah, finally!"
        m "You did it!"
        mc "Let's take a look inside!"

        scene car theft 13 with dissolve
    mc "(Damn, dude!)"
    mc "(Now that's a car! It must be worth a shit ton of dough.)"
    "*Click*"

    scene car theft 14 with dissolve
    m "Oh my!"
    m "Is this your new car?"
    mc "Nah, it's uh...{w} My dad's car, yes."
    mc "Wait, why did you turn on the lights?"
    mc "(Shit, someone might notice.)"

    scene car theft 15 with slowfade
    m "So you see this!"
    m "Your dream girl is laying on top of a sports car..."

    scene car theft 16 with dissolve
    m "Doesn't that make you excited, [mc_name]?"
    mc "(Oh for fucks sake, her heels are on the hood!)"
    mc "If you damage the paint my father will kill us both! You know he would do it!"

    scene car theft 17 with fade
    m "How about this, then?"
    m "Why don't you try to get {i}in here{/i}, with that big hard {i}rod{/i} of yours?"

    scene car theft 18 with dissolve
    m "I know you miss this ass..."
    m "Because I miss you filling it up everyday!"
    mc "(This is fuckin unbelievable!)"
    mc "(Turth be told, her body is fine as hell, but with her, the looney-meter is off the charts!)"

    scene car theft 19 with dissolve
    mc "Woman, I'm trying to stea- {w} To bring my dad's car where he wants it!"
    "*Thunk*" with hpunch

    stop music fadeout 25.0
    scene car theft 20 with dissolve
    mc "(Shit!)"
    mc "(Someone's coming!)"
    mc "You know what, let's go for a ride!"
    m "Finally, I wanted to ride your co-"

    scene car theft 21 with dissolve
    mc "Get in the car, Mel!"
    m "You got the keys?"
    mc "They were on the counter. Now come on!"
    m "Fine!"

    scene car theft 22 with fade
    mc "(Good thing the key was left out in the open on a shelf, as the note says.)"
    mc "(I guess the owner is pretty confident their car wouldn't get stolen. Well, I'm here to change that!)"
    m "Oh wow, this car is nice!"
    m "Do you think maybe your dad would let you borrow it from time to time?"
    mc "(Even if it was his, he would never let me drive it.)"


    scene car theft 23 with dissolve
    mc "I hope so!"

    scene car theft 24 with dissolve
    mc "(Finally, not that piece of shit I'm driving daily!)"
    mc "Are you ready? Here we go!"

    scene black with slowfade
    show text "{size=72}{color=#dc38bf}Later that day...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    scene car theft 25 with slowfade
    m "Wow, this was awesome!"
    m "Your dad really owns a lot of garages... This is another one?"
    mc "Yeah, you know how he is..."
    mc "It's time for me to go, so..."

    scene car theft 26 with fade
    mc "Thanks for joining me for the ride and all."
    mc "(Not like I was asking for it... Whatever.)"

    play music "audio/music/red.mp3" loop fadeout 2.0 fadein 2.0
    scene car theft 27 with dissolve
    m "You know, [mc_name]..."
    m "Since you left... It's not just you that changed."
    mc "What do you mean?"

    scene car theft 28 with dissolve
    pause 0.5

    scene car theft 29 with dissolve
    pause 1.0
    m "*Slurp*"
    mc "What are you-"

    scene car theft 30 with dissolve
    mc "(Ah fuck, my dick is getting hard already!)"
    mc "(Her technique is truly amazing, even just on my finger!)"

    scene car theft 27 with dissolve
    m "People change..."
    m "Maybe you'll notice it one day."

    scene car theft 31 with fade
    m "See you around, [mc_name]..."
    pause 1.0
    mc "(Yeah, the fuckin crazies...)"
    mc "(I better wrap this up...)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 4.0 fadein 3.0
    scene black with Fade(1.0, 1.0, 1.0)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
