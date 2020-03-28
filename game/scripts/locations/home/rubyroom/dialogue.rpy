label ruby_5_dressup_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home ruby dressup 4
    else:
        scene home ruby dressup 3 with slowfade
        ruby "[mc_name]! You got my text?"
        mc "What the fuck Ruby?"
        mc "I get you a job and now you want me to cover for you on your first day?"

        scene home ruby dressup 4 with dissolve
        ruby "Oh come on, I didn't know I'd have to start so soon!"
        ruby "Honestly, I thought you wouldn't even try to find a job for me!"
        mc "What's so important that you can't go to work today anyway?!"
        ruby "I have to meet my friend later today who is in big trouble..."
        ruby "Please, I don't want to let my friend down like this!"
        mc "So you're going to let me down instead..."
    mc "Fine, but you'll have to do something for me."
    ruby "Okay, I'll do it when I get back, just tell me what it is."
    mc "No, you'll have to do it right now."
    mc "I want you to dress up for me."
    ruby "What?"
    mc "Take it or leave it. I have better things to do than folding clothes all day."

    scene home ruby dressup 5 with dissolve
    ruby "Fine, fine..."
    ruby "I'll do it."
    mc "A pleasure doing business with you, sis."

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene home ruby dressup 6 with dissolve
    mc "So why don't you just start with what you have on now?"

    scene home ruby dressup 7 with dissolve
    ruby "What do you mean?"
    mc "I mean show it off to me."
    ruby "Isn't this... weird?"
    mc "Come on, imagine like you're a model or something, I don't care."
    ruby "F-fine..."

    scene home ruby dressup 8 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause
    mc "Looking good!"
    mc "Now turn around please."

    scene home ruby dressup 9 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause
    ruby "Damn [mc_name], you are staring at my ass!"
    mc "Well, you have a really nice ass, what can I do?"
    mc "Oh wait, I got a great idea!"
    if not lain_mod:
        mc "Get your old high school uniform and put that on!"
    else:
        mc "Get your high school uniform and put that on!"

    scene home ruby dressup 7 with dissolve
    ruby "You're into schoolgirl uniforms?"
    mc "What guy isn't?"
    ruby "I don't know, maybe the ones that aren't huge pervs?"
    mc "Could be. So, what's it gonna be?"
    ruby "Fine..."

    scene home ruby dressup 10 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.03
    pause
    ruby "There, happy now?"
    mc "Wow!"

    scene home ruby dressup 11 with dissolve
    mc "Wait a second..."
    mc "I remember you wearing it differently."
    ruby "Yeah. I wasn't usually wearing the socks or the bra."
    mc "You know what to do..."
    ruby "Ugh..."

    scene home ruby dressup 12 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.03
    pause
    mc "You know that I joked about modeling earlier?"
    mc "I think that might not be just a joke."
    mc "You really are model material, sis!"
    ruby "You really think so?"
    mc "I do. You are a true beauty!"
    ruby "Even from the back?"

    scene home ruby dressup 13 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.06
    pause
    mc "Hot damn!"
    mc "I bet you break all the guys' hearts!"
    mc "Hmm, do you have anything more... spicy?"

    scene home ruby dressup 12 with dissolve:
        subpixel True
        yalign 0.03
    ruby "Spicy?"
    mc "Like how do you dress for a party for example?"
    ruby "Oh, I think I have something you'd like."
    mc "(Wow, once I started complimenting her she became less hostile.)"
    mc "(Maybe she's even into this, but she was just embarrassed?)"

    scene home ruby dressup 14 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.0
    pause
    ruby "How do you like this one?"
    mc "Fuck!"
    mc "That's hot as hell!"
    mc "You're hot as hell, Ruby!"
    mc "I looked at you like a little sister so I never noticed, but I can see now that you're growing into a beautiful young woman!"

    scene home ruby dressup 15 with fade:
        subpixel True
        yalign 0.0
        pause 2.0
        linear 7.0 yalign 1.0
    pause
    ruby "Haha, thank you!"
    mc "You seriously go out like that?"

    scene home ruby dressup 16 with dissolve
    ruby "Sometimes..."
    mc "Damn, you need some bodyguards with you if you wear that outfit to a party!"
    mc "Do you think you can maybe show me-"

    scene home ruby dressup 17 with dissolve
    scene home ruby dressup 17 with vpunch
    ruby "No-no, big brother!"
    ruby "That's enough. I kept my end of the bargain."

    scene home ruby dressup 18 with dissolve
    ruby "I've shown you more than enough, now it's your turn."
    mc "Ugh... alright, alright. I'll go to the boutique now and fill in for your work shift."
    ruby "What was that thing you said? Ah yes, it's a pleasure doing business with you, bro!"
    mc "Ah, you little minx!"
    pause 0.7

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.5 fadein 2.0
    scene black with slowfade

    return






label ruby_8_chorehotdog_dialogue:

    scene ruby chores 6 with slowfade
    mc "Do you really hate cleaning that much?"
    ruby "Shut up, [mc_name]!"
    pause 0.8


    menu:
        "\"Show more respect!\"":

            $ ruby_influence += 1

            mc "Excuse me?"

            scene ruby chores 7 with dissolve
            ruby "Leave me alone!"
            mc "It feels bad people are not doing what you want them to, huh?"
            mc "Maybe you could show some cooperation and respect, then!"
            mc "I left two years ago, and I left a good sister here."
            mc "You had some problems, sure, but I don't remember having such a brat sister!"
            mc "Just look around this place!"

            scene ruby chores 8 with dissolve
            mc "This is a shithole!"
            mc "No wonder mom is mad at you, if you keep this up it will start to become a health hazard."

            scene ruby chores 7 with dissolve
            ruby "Like you're better at cleaning up your mess!"
            ruby "You're living in a shitty basement!"
            mc "I live in basement by circumstance, not by choice."
            mc "You however chose to have a mess you call your room!"

            scene ruby chores 9 with dissolve
            mc "Also, it's not about me."
            mc "Yes, I am the black sheep of this family, but I'm not about to let you become the second one!"
            ruby "....."
            mc "Now come on, let's go grab something to eat then do your chores."
            ruby "Mhmpf..."
        "\"Let's negotiate\"":



            scene ruby chores 7 with dissolve
            mc "How about we negotiate?"
            ruby "What do you mean?"
            mc "Let's face it..."

            scene ruby chores 8 with dissolve
            mc "This place is a mess..."
            mc "I'm sure it's better to {i}do nothing{/i} in a clean room as well."

            scene ruby chores 9 with dissolve
            mc "How about we get some lunch then you clean up your room."
            ruby "Your treat?"
            mc "My treat."
            ruby "Cool, I want hot dogs!"


    play music "audio/music/playtime.mp3" loop fadeout 2.0 fadein 2.0
    scene ruby chores 10 with slowfade
    mc "Alright, so which one do you-"
    ruby "I fuckin love hot dogs!"
    if not lain_mod:
        mc "(Damn...)"
        mc "Uhm... Alright then."

    scene ruby chores 11 with fade
    clerk "Hi! What can I get you today?"
    mc "Hmm, those hot dogs really look tasty!"

    scene ruby chores 12 with dissolve
    mc "I'll take that one, with mustard please!"

    scene ruby chores 11 with dissolve
    clerk "Alright, and for your girlfriend?"
    pause 0.5
    "[mc_name] & Ruby" "\"Girlfriend?\""

    scene ruby chores 13 with dissolve
    "[mc_name] & Ruby" "....."
    pause 0.5

    scene ruby chores 14 with vpunch
    mc "Hahaha!"
    ruby "Ahahah!"
    mc "Us, together?"
    mc "Haha, she's my little sister!"

    scene ruby chores 15 with dissolve
    if not lain_mod:
        clerk "Oh, sorry, my bad. Two hot dogs then?"
    else:
        clerk "Oh, my bad. You two look like a couple. Two hot dogs then?"
    mc "That's right."

    scene ruby chores 16 with dissolve
    ruby "Girlfriend... {w} Haha."
    ruby "{size=-10}What a silly idea...{/size}"
    clerk "There you go!"
    mc "Keep the change, thanks!"

    scene ruby chores 17 with fade
    mc "It's easy to argue if you have an empty stomach."
    ruby "Thanks for the hot dog!"
    mc "We have a deal then? Will you do your chores?"
    ruby "Alright, alright!"
    mc "Hah, we should do this more often. Seems to have a good effect on you!"
    ruby "Yeah, uhm... {w} That would be nice..."
    pause 1.0

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label ruby_9_pillowfight_dialogue:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby pillowfight 1
    else:
        scene ruby pillowfight 1 with slowfade
    mc "Hey sis, how you doing?"
    ruby "...."

    scene ruby pillowfight 2 with dissolve
    mc "(Is she ignoring me?)"
    mc "(She's so absorbed into her TV screen all the time...)"
    mc "Hello?"

    scene ruby pillowfight 3 with dissolve
    ruby "Oh, hey."
    ruby "I didn't hear you come in."
    mc "What are you watching?"
    ruby "It's a new reality show with a twist. It's about a-"
    mc "Hey, I think you have something on your face."

    scene ruby pillowfight 4 with dissolve
    ruby "What? Where?"
    mc "It's right-"
    pause 0.3

    scene ruby pillowfight 5 with vpunch
    pause 0.7

    scene ruby pillowfight 6 with dissolve
    mc "There! Hahaha!"
    ruby "What?!"
    ruby "I'll get you back for this!"

    scene ruby pillowfight 7 with fade
    ruby "Why'd you sneak up on me like that?"
    mc "It was a surprise attack!"

    scene ruby pillowfight 8 with dissolve
    ruby "So, can't beat me in a fair fight?"
    mc "I could beat you with my eyes closed!"

    scene ruby pillowfight 9 with dissolve
    mc "Too bad you're too pretty for me to not be looking at you."
    ruby "Flattery doesn't help here!"
    ruby "Take this!"
    pause 0.3

    scene ruby pillowfight 10 with vpunch
    ruby "Hyaa!!"

    scene ruby pillowfight 11 with dissolve
    mc "Oh you'll regret this!"
    ruby "I'm the pillow fight champion and you won't take that title from me!"

    scene ruby pillowfight 12 with dissolve
    mc "(We used to do these pillow fights when we were younger.)"
    mc "(And of course, she was the champion.)"
    mc "(I always let her win. It was nice to see her win, she was cute.)"
    mc "(And she was a sore loser so it made sense...)"
    ruby "You're spacing out big bro! Hiyaa!"
    pause 0.2

    scene ruby pillowfight 13 with vpunch
    mc "Oof! Oh shit!! \ (I'm losing my balance!)"
    ruby "Hey! Don't grab m-"

    play music "audio/music/soulhotvintage.mp3" loop fadeout 3.0 fadein 3.0
    scene black with vpunch
    pause 1.0

    scene ruby pillowfight 14 with slowfade
    ruby "Ugh..."
    ruby "Damn that hurt."

    scene ruby pillowfight 15 with dissolve
    ruby "Good thing I landed on something soft..."
    ruby "Are you alright?"

    scene ruby pillowfight 16 with dissolve
    mc "Mhhmhmuuh~"
    ruby "What?"
    mc "Mhi mmhm hmmeahe!"
    mc "(Her pussy is right on my face...)"

    scene ruby pillowfight 17 with dissolve
    ruby "(Ah...)"
    ruby "(What is this tingling sensation down there...)"
    ruby "(Oh! I'm sitting on his face!)"

    scene ruby pillowfight 18 with fade
    ruby "Huh?!"
    ruby "(Is that...?)"

    scene ruby pillowfight 19 with dissolve
    ruby "(His dick got hard because I'm sitting on his face?)"
    ruby "(But I'm his sister...)"
    ruby "(Should we have those reactions to each other?)"

    scene ruby pillowfight 20 with dissolve
    ruby "(.....)"
    ruby "(He is so big... I...)"
    ruby "(His breath feels so good on me...)"
    ruby "(I have to try this... Just don't be awkward, please!)"

    scene Pillowfight with dissolve
    mc "(Oh my God!!)"
    mc "(She's grinding her hips on my face!)"
    mc "(She has definintely noticed my boner by now...)"
    mc "(She's not saying anything... Maybe she's not bothered by it?)"
    ruby "(Ah~ {w} This feeling...)"
    ruby "(But he's not saying anything... {w} What the hell am I doing anyway? He's my brother!)"
    ruby "(I should stop this before it gets any more weird!)"

    scene ruby pillowfight 21 with fade
    ruby "Uuh, I have to go now, see ya!"
    mc "What? Ruby, where are you going?"
    ruby "I need to use the bathroom, then I have to uhm, sleep. And you should too..."
    mc "But..."

    scene ruby pillowfight 22 with fade
    mc "(She left...)"
    mc "(Holy shit, this was intense, awkward... and hot as fuck!)"
    mc "(I hope the boner didn't mess up the situation...)"
    mc "(But she was grinding on my face, so...)"
    mc "(Anyway, I better leave now. She probably doesn't want me to be here when she comes back.)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label ruby_10_spanking_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.5
    if _in_replay:
        call setup_gallery
        scene ruby spank 1
    else:
        scene ruby spank 1 with slowfade
    mc "(There she is, sleeping in again...)"
    mc "(It's almost fucking noon already! Even I wake up earlier than that.)"
    mc "(Shouldn't she be at work anyway?)"
    mc "(Okay, time to end this. Dad said something about disciplinary action...)"

    scene ruby spank 3 with fade
    mc "(I tried to be kind last time, didn't work.)"
    mc "(We'll see how she likes this.)"

    scene ruby spank 4 with dissolve
    mc "Rise and shine, sis!"

    scene ruby spank 5 with dissolve
    mc "If you won't wake up, I'll just drag you out of bed!"
    ruby "Huh?"

    scene ruby spank 6 with fade
    ruby "Wh-"
    ruby "What the fuck are you doing?"

    scene ruby spank 7 with dissolve
    ruby "[mc_name]!"
    ruby "Stop this right now!"
    mc "Oh no, sis. I'm just getting started!"

    scene ruby spank 8 with slowfade
    mc "That's much better."
    mc "Stay like this."

    scene ruby spank 9 with dissolve
    ruby "What the hell? Is this some kind of perverted fantasy of yours?"
    ruby "Having me on your lap while touching my ass?"
    mc "I'm done playing nice, Ruby!"

    scene ruby spank 10 with dissolve
    ruby "What are you talking about?"
    mc "I told you you need to do your chores and clean up this pigsty!"
    mc "I took you out to get some hot dogs and you agreed you'd do it."
    mc "You lied to me, so you're getting the consequences now."

    scene ruby spank 11 with dissolve
    ruby "Don't be ridiculous! I can do whatever I want!"
    ruby "Let me go [mc_name]."


    scene ruby spank 12 with dissolve
    pause 0.4
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 13 with hpunch
    pause 0.8

    scene ruby spank 14 with dissolve
    ruby "Aah!"
    ruby "Did you just spank me?!"

    scene ruby spank 15 with dissolve
    ruby "Let me go right now! It hurts!"
    mc "I don't think you know your place yet!"


    scene ruby spank 12 with dissolve
    pause 0.5
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 13 with hpunch
    ruby "Ah!!"


    scene ruby spank 12 with dissolve
    pause 0.5
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 13 with hpunch
    pause 0.3
    ruby "Stop!!"


    scene ruby spank 12 with dissolve
    pause 0.4
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 13 with hpunch
    pause 0.5
    ruby "Fuck you [mc_name]! I'm not doing what you want me to!"
    ruby "Even if you spank my ass red!"
    mc "Oh? Okay, we'll see about that!"
    pause 0.2


    scene ruby spank 17 with dissolve
    pause 0.7
    mc "Let's get this out of the way..."
    ruby "Wh-"
    pause 0.7

    scene ruby spank 18 with dissolve
    pause 0.7
    ruby "Hey, no! What are you doing?"
    mc "I'm gonna spank your bare little brat ass!"
    pause 0.3


    scene ruby spank 19 with dissolve
    pause 0.4
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 22 with vpunch
    pause 0.2
    ruby "Aaaouch!"


    scene ruby spank 19 with dissolve
    pause 0.5
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 22 with vpunch
    pause 0.4
    ruby "Fuck!"
    mc "Did you have enough?"
    mc "Hmm, on second thought..."
    mc "I think you didn't!"
    pause 0.3


    scene ruby spank 20 with dissolve
    pause 0.5
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 21 with hpunch
    pause 0.2
    ruby "Aaah!"


    scene ruby spank 20 with dissolve
    pause 0.4
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 21 with hpunch
    pause 0.7
    ruby "[mc_name]! Uhh!"


    scene ruby spank 20 with dissolve
    pause 0.4
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 21 with hpunch
    pause 0.7
    ruby "Uhhhn~"


    scene ruby spank 20 with dissolve
    pause 0.5
    play sound "audio/sfx/spank.ogg"
    scene ruby spank 21 with hpunch
    pause 0.3
    ruby "Ahhh!"
    mc "There you fucking go!"


    scene ruby spank 24 with dissolve
    pause 0.7
    ruby "You are out of your fucking mind, h-{w}how dare you do this to me?!"
    ruby "I'm telling mom!"

    scene ruby spank 23 with dissolve
    pause 0.5
    mc "Oh, please do!"
    mc "Let everyone in the house know you got spanked by your brother for not doing your chores like a ten year old!"
    mc "I'm sure they will take it very seriously and won't laugh their asses off!"
    ruby "Fuck y-"

    scene ruby spank 25 with vpunch
    mc "NO!"
    mc "None of that bullshit anymore!"
    mc "You lied to me, now you got disciplined."
    mc "You are a brat and you need to learn some respect and to not act like a bitch towards your family!"
    mc "And you WILL learn to respect me, one way or another!"
    mc "Now do what you told me you would and clean this mess up!"
    ruby "Grr...."
    mc "(I'll just leave her to her sulking, and check back in a few days to see if she did her chores...)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.5
    scene black with slowfade

    return







label ruby_12_spanking2_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby spank 26
    else:
        scene ruby spank 26 with slowfade
    mc "Hey Ruby."
    ruby "Mhm..."

    scene ruby spank 29 with dissolve
    mc "You still haven't cleaned up your room..."
    mc "(I'm going to look like a fool in front of dad if I can't get her to do it.)"

    scene ruby spank 27 with dissolve
    ruby "I'll do it later! What's it matter to you anyways?"
    ruby "You're acting like I must do what you tell me..."

    scene ruby spank 28 with dissolve
    ruby "It's not like you're my dad..."
    mc "(I can be daddy alright.)"

    scene ruby spank 30 with dissolve
    mc "(I get it why mom and dad are so frustrated with her...)"
    mc "(She's a total brat.)"
    mc "I might not be dad, but you know what dad told me?"

    scene ruby spank 31 with dissolve
    ruby "What?"
    mc "That I can, and I should make you do what you're supposed to do in this house."
    mc "Remember what I did last time?"

    scene ruby spank 32 with dissolve
    ruby "You spanked me..."
    mc "That's right. You didn't like that, did you?"
    ruby "No..."
    mc "And you still didn't do what I asked you to do."
    ruby "..."
    mc "So you know what happens next?"

    scene ruby spank 33 with dissolve
    ruby "Spanking?"
    mc "Spanking it is."

    scene ruby spank 34 with dissolve
    ruby "Do you... Really have to?"
    ruby "Can't you just let it go?"
    mc "How else will you learn?"

    scene ruby spank 35 with fade
    ruby "Fine..."
    ruby "Let's get this over quick, then."

    scene ruby spank 36 with dissolve
    mc "(This is surprising.)"
    mc "(No protesting this time, she's just bending over and letting me spank her ass.)"
    mc "(Just like that...)"
    mc "(But something is missing. Maybe this will convince her.)"
    mc "I see you won't protest now like you did last time. You know it's coming."

    scene ruby spank 37 with dissolve
    mc "But I think you're forgetting something."
    ruby "What?"
    mc "You still have your panties on."
    ruby "You've got to be kidding me, again?"
    ruby "That sounds like it has some kind of a sexual underton-"
    mc "Ruby... Don't make me say it again."
    ruby ".....................{w}.........."

    scene ruby spank 38 with fade
    ruby "Fine! There you go!"
    ruby "I hope you are enjoying the view, fucking pervert!"
    ruby "Is this what you wanted?"
    mc "(I'm very much enjoying it. Although I can't just tell her that.)"
    mc "(Her little bubble of a butt can easily make any man's dick rock solid in a heartbeat.)"
    pause

    scene ruby spank 39 with dissolve
    mc "(But this is not good.)"
    mc "(She's choosing the punishment instead of not doing what she's being punished for in the first place. Being a lazy brat, that is.)"
    mc "(I have a choice here.)"
    mc "(I can spank her again, maybe harder this time, and hope she will find it unpleasant and humiliating enough that she will do as asked.)"
    mc "(Or I can let it go this time and just have her display her bottom to me like that.)"
    mc "(Maybe by giving a less severe punishment it will trigger her sympathy and she will do as asked.)"


    menu:
        "Spank her":

            $ ruby_influence += 1
            $ morality -= 1

            mc "(I'll go with the more hands on approach. She needs to learn. {w} And she will.)"


            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch

            ruby "Aaaah!!!"
            mc "You better talk to me with more respect!"


            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch
            pause 0.5

            ruby "Oooow!!"
            ruby "You're doing it much harder than last time!"
            mc "That's what you get when you're being a brat!"


            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch

            ruby "AAah!!"
            ruby "Fuck! Stop!"
            mc "Will you do your chores?"
            mc "It's just a room for fuck's sake, how hard is it to clean it?"
            ruby "You can't just coerce me into doing what you tell me with this!"
            mc "Watch me..."


            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch

            ruby "Aaaaaah!!!"


            scene ruby spank 42 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch
            pause 0.2

            scene ruby spank 42 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch
            pause 0.2

            scene ruby spank 42 with dissolve
            pause 0.2
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch
            pause 0.5

            ruby "Ooooow!!! Aaah! It hurts!!!"
            ruby "Fuck yo-"


            scene ruby spank 43 with dissolve
            pause 0.6
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch
            mc "Just-"


            scene ruby spank 43 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch
            mc "Do-"

            scene ruby spank 43 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch
            mc "What-"

            scene ruby spank 43 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch
            mc "You're-"


            scene ruby spank 43 with dissolve
            pause 0.3
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch
            mc "TOLD!"
            pause 0.8
            ruby "Hnnng~"
            mc "(She's breathing heavily, but she's still keeping her ass in place.)"
            mc "(She hasn't moved an inch...)"
            mc "(She could just get up anytime and walk away, really.)"
            mc "(Is she...)"
            pause 1.0

            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch
            pause 0.5
            ruby "Mhahh~"
            mc "(If she's getting off on this...)"
            mc "(No, there's no way.)"
            mc "(I'm hitting hard this time.)"
            mc "(I'll give her a couple more and call it a day.)"
            mc "(She probably won't be able to sit for a day or two after this...)"

            scene ruby spank 42 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 40 with hpunch

            ruby "Ah~"

            scene ruby spank 43 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch

            ruby "AAhhh~"

            scene ruby spank 43 with dissolve
            pause 0.5
            play sound "audio/sfx/spank.ogg"
            scene ruby spank 41 with hpunch

            ruby "Mmhh~"
            pause 1.0
            mc "Alright, that's enough."


            scene ruby spank 44 with dissolve
            ruby "Grr..."
            mc "Do you want more?"
            ruby "Fuck you!"
            ruby "This really hurt! You're out of your mind..."
            mc "Your ass will remind you for a couple of days what you need to do."
            mc "I'll be back and if I don't get results, I won't go that easy on you next time."
            mc "I'm doing this for you."
            mc "More respect and a clean room. Understand?"
            ruby "Leave me alone!"
            ruby "Just go!"
        "Let her be":



            $ morality += 2

            mc "(I'll see if I can get to her by showing some forgiveness.)"
            mc "You know what, I've changed my mind."
            mc "Maybe spanking you last time wasn't such a good idea."
            ruby "Really?"
            ruby "I mean-"
            ruby "Can I put my panties back on then?"

            scene ruby spank 38 with dissolve
            mc "No, no. Just stay there as you are."
            mc "I still have to punish you."
            mc "I just decided to go easy on you."
            mc "Stay there like that for a little bit."
            ruby "What?"
            ruby "While you are staring at my-... my bottom?"
            ruby "Are you getting excited by this? You're...{w} You're disgusting!"
            mc "Just shut the fuck up, Ruby! We can get to the end of this faster if you do."

            scene ruby spank 43 with dissolve
            pause
            mc "(Despite being so angry, she shut her mouth after that.)"
            mc "(She's keeping still, pushing her ass out towards me like that.)"
            mc "(I can see her beautiful rosebud at the top, nearly winking at me as she breathes.)"
            mc "(And her pure little pussy underneath, both holes are well kept and looked after.)"
            mc "(She either doesn't grow any hair down there, which would be unlikely, or she keeps that region in perfect condition all the time.)"
            mc "(I'm getting hard just by looking at her backside, so I should just let her go before she notices and throws more insults at me about how sick I am.)"
            mc "Alright, we're done."

            scene ruby spank 45 with fade
            ruby "Wait, that was it?"
            ruby "For real?"
            mc "Are you disappointed?"
            ruby "What? N-no!"
            ruby "I just thought...{w} I thought you were going to trick me or something."
            mc "The trick here is that if you'll be a good girl and do your chores then we won't have to do this again."
            mc "I'll check back in a couple of days."
            ruby "Sure..."
            pause 1.0


    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
