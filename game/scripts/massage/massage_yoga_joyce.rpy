label mom_yoga_controller:

    menu mom_yoga_menu:

        "Yoga #1" if mom_seen_yoga_level >= 1:
            call mom_yoga_1
            $ mom_yoga_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Yoga #2" if mom_seen_yoga_level >= 2:
            call mom_yoga_2
            $ mom_yoga_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Yoga #3" if mom_seen_yoga_level >= 3:
            call mom_yoga_3
            $ mom_yoga_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Yoga #4" if mom_seen_yoga_level >= 4:
            call mom_yoga_4
            $ mom_yoga_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Yoga #5" if mom_seen_yoga_level >= 5:
            call mom_yoga_5
            $ mom_yoga_counter += 1
            $ increase_time()
            $ go_to(L_home_basement)




        "Yoga #1 (locked)" if mom_seen_yoga_level < 1:
            jump mom_yoga_menu
        "Yoga #2 (locked)" if mom_seen_yoga_level < 2:
            jump mom_yoga_menu
        "Yoga #3 (locked)" if mom_seen_yoga_level < 3:
            jump mom_yoga_menu
        "Yoga #4 (locked)" if mom_seen_yoga_level < 4:
            jump mom_yoga_menu
        "Yoga #5 (locked)" if mom_seen_yoga_level < 5:
            jump mom_yoga_menu
        "Back":


            jump home_kitchen_mom






label mom_massage_controller:
    python:
        temp_1 = mom_massage_text(1)
        temp_2 = mom_massage_text(2)
        temp_3 = mom_massage_text(3)
        temp_4 = mom_massage_text(4)
        temp_5 = mom_massage_text(5)


    menu mom_massage_menu:

        "Massage #1[temp_1]" if mom_massage_level >= 1:
            call mom_massage_1
            if mom_seen_massage_level == 0:
                $ mom_seen_massage_level = 1
            $ mom_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Massage #2[temp_2]" if mom_massage_level >= 2:
            call mom_massage_2
            if mom_seen_massage_level == 1:
                $ mom_seen_massage_level = 2
            $ mom_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Massage #3[temp_3]" if mom_massage_level >= 3:
            call mom_massage_3
            if mom_seen_massage_level == 2:
                $ mom_seen_massage_level = 3
            $ mom_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)


        "Massage #4[temp_4]" if mom_massage_level >= 4:
            call mom_massage_4
            if mom_seen_massage_level == 3:
                $ mom_seen_massage_level = 4
            $ mom_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_momroom)




        "Massage #2 (locked)" if mom_massage_level < 2:
            jump mom_massage_menu
        "Massage #3 (locked)" if mom_massage_level < 3:
            jump mom_massage_menu
        "Massage #4 (locked)" if mom_massage_level < 4:
            jump mom_massage_menu
        "Back":


            jump home_kitchen_mom






label mom_yoga_1:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home yoga mom 1 with fade
    mc "(Oh wow, mom is doing yoga!)"
    mc "(I guess that's why she's in such a good shape.)"

    scene home yoga mom 2 with dissolve
    mc "(Those leggings are really tight...)"
    mc "(Just like her body is, damn!)"
    mc "(I should probably just ask her if she needs any help instead of ogling her like a creep.)"

    scene home yoga mom 8 with dissolve
    mc "Hey mom!"
    mom "Oh hey [mc_name]! I didn't see you there."
    menu:
        "Surprised":
            mc "Didn't think you'd be much of a yoga woman."
            mc "I'm surprised acutally, but good for you!"
            mom "Well yeah, I'm trying to keep in shape, you know."
        "No wonder with that figure":

            mc "No wonder you're the best looking mom out there!"
            mc "I see you like to take care of your body."
            mom "You really think so?"
            mom "You're sweet, [mc_name]. Thanks!"

    scene home yoga mom 9 with dissolve
    mc "So how's it going?"
    mom "I've just started doing it recently, but I like it so far."
    mom "It's not as easy as it looks!"
    mc "Do you need some help?"
    mom "You're sweet but I don't want to waste your time."
    mc "Not at all! I'm happy to help. Is that pose from before the one you had trouble with?"
    mom "Yeah... I should be able to go further, but it's a bit hard to do."
    mc "Alright, let's get to it then!"

    scene home yoga mom 4 with dissolve
    mc "Okay, I think I'm getting the hang of how it should be."
    mom "This is where I should go lower."

    scene home yoga mom 3 with dissolve
    mc "So if I do this..."
    mc "And a gentle push here..."

    scene home yoga mom 5 with dissolve
    mc "Do you think it's working?"
    mom "Yeah, it actually helps!"
    mom "Keep it up!"
    mc "(Oh man, I'm almost touching her ass!)"
    mc "(I better be careful not to pop a woody here, that would be at the very least embarrassing.)"

    scene home yoga mom 7 with dissolve
    mom "Yeah, that's it! We did it!"
    mc "Awesome!"

    scene home yoga mom 10 with dissolve
    mom "Thanks for the help [mc_name]."
    mc "Anytime, mom!"
    mom "I'll hold you to that!"
    mc "Sure, haha!"
    mc "(I'd be happy to be held onto instead... Ah, I better clear my head.)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_yoga_2:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene home yoga mom 1 with slowfade
    mc "(There she is, doing yoga again!)"
    mc "(Maybe I can help her out one more time? I'm really getting into this.)"
    mc "Hey, mom!"
    mc "Need some help?"
    mom "Oh hey [mc_name]!"
    mom "Yeah, it's that pose again, thank you!"

    scene home yoga mom 11 with slowfade
    mom "Push like last time, please."
    mom "But come a little bit closer, it's a better angle that way."
    mc "You got it!"
    mc "(Oh man...)"

    scene home yoga mom 12 with dissolve
    mc "(My crotch is touching her butt...)"
    mc "(It's hard to concentrate like this.)"
    mc "(I hope that's the only thing that gets hard.)"

    scene home yoga mom 13 with dissolve
    mom "Yeah, like that!"
    mom "I'm almost there, keep pushing!"
    mc "Like this?"
    mom "Yeah, don't stop!"
    mc "(Why does she have to talk like that... Oh God!)"

    scene home yoga mom 14 with dissolve
    mom "Yes, that's good!"
    mom "I did it! {w} Or I should say, we did it."
    mom "Thank you [mc_name]!"
    mc "It's my pleasure! Maybe I'll even join you one day, haha!"
    mom "Oh, you're taking it seriously?"
    mc "Why wouldn't I?"
    mom "Uh, nevermind!"
    mom "You're a good partner, you joining me is a great idea!"
    mc "I can't, I don't have yoga clothes like you do."
    mom "Ah, don't worry about those, you don't need them."
    mc "But you have them on..."
    mom "Oh come on... {w} Just come and join me next time, and I'll show you that you don't need all this stuff."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return





label mom_yoga_3:

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0

    if _in_replay:
        call setup_gallery
        $ mom_seen_yoga_level = 2
        scene home yoga mom 36
    else:
        scene home yoga mom 36 with slowfade

    mom "Ready to do some yoga?"
    mc "Oh wow, new outfit?"

    scene home yoga mom 35 with dissolve
    mom "Just removed the sweater."
    mom "I told you I'd show that you don't need fancy yoga clothes to participate."
    mom "Now, will you help me out?"

    scene home yoga mom 15 with slowfade
    mc "Oh, I think I know how to do this."
    mom "Yeah, it's that pose again, thank you!"

    scene home yoga mom 16 with slowfade
    mom "Push like last time, please."
    mom "You know, closer!"
    mc "You got it!"
    mc "(Oh man...)"

    scene home yoga mom 17 with dissolve
    mc "(My crotch is touching her butt...)"
    mc "(Now I can even feel her skin!)"
    mc "(It's hard to concentrate like this.)"
    mc "(I hope that's the only thing that gets hard.)"

    scene home yoga mom 18 with dissolve
    mom "Yeah, like that!"
    mom "I'm almost there, keep pushing!"
    mc "Like this?"
    mom "Yeah, don't stop!"
    mc "(Why does she have to talk like that... Oh God!)"

    scene home yoga mom 19 with dissolve
    mc "(Oh man...)"
    mc "(This is getting hotter by the minute.)"
    mc "(I can't believe her body is so fit!)"
    mc "(The hard work and dedication being put into it is inspiring, really.)"

    scene home yoga mom 20 with dissolve
    mom "You're awfully quiet, [mc_name]. Everything okay?"
    mc "Yeah, I'm just... {w} Admiring your body. You are really fit!"
    mom "Oh I... Uhm... {w} Thank you."
    mom "Okay, let's do something else now."
    mom "I want you to participate now."
    mc "I'm participating already, helping you."
    mom "Not like that. I want you to do it with me, don't worry it's easy."
    mom "Take off your shirt."
    mc "(Oh boy...)"

    scene home yoga mom 34 with slowfade
    mom "I'm not sure if you know, but yoga is not all about stretches and difficult poses."
    mom "It's about bringing your body and mind to a calm, balanced state."
    mc "Uh-huh..."
    mom "Come on, do as I do."

    scene home yoga mom 21 with fade
    mom "This is called the Lotus."
    mc "(I'd rather be having a different 'lotus' now... {w} It actually hurts a bit sitting like this.)"
    mom "If you can't do a full Lotus, you can do it like you're doing it now."
    mc "What's a full Lotus?"

    scene home yoga mom 22 with dissolve
    mom "Having your legs up here, where I do."
    mc "Damn... {w} It's slighlty uncomfortable sitting like this already."
    mom "That means you're very stiff!"
    mom "Your pants are probably not helping with this either..."
    mc "....."
    mc "It's not that I'm stiff, it's that you're more flexabile than average!"
    mom "Haha!"

    scene home yoga mom 23 with dissolve
    mom "This is a fairly easy pose once you stretch a few times."
    mom "But thanks!"
    mom "Now focus on your breathing..."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mc "(This is actually good.)"
    mc "(I feel... {w} peaceful.)"
    mom "Try to block your thoughts and just concentrate on your breathing, on my voice."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."

    scene home yoga mom 24 with dissolve
    mom "You're doing great, [mc_name]!"
    mom "How do you feel?"
    mc "It feels...{w} good."
    mc "It cleared my head, I think."
    mom "That's great, that's what it is supposed to do!"
    mom "You might be a natural at this!"

    scene home yoga mom 36 with slowfade
    mom "Alright, so that wasn't so bad, was it?"

    if mom_seen_yoga_level == 2:
        menu:
            "Could be better":

                mc "Well, not totally bad but... {w} Could have been better."
                mom "Oh, I see."
                mom "Maybe next time will be better?"
                mc "Maybe..."
                mom "Anyways... {w} Thank you for joining me."
                mc "Thank you too."
            "Compliment":



                $ mom_yoga3_complimented = True

                mc "It was great!"
                mc "I didn't think I would enjoy it, but you're a great at teaching this!"
                mom "Oh wow, thank you! That's really good to hear!"
                mc "See you next time?"
                mom "You bet! Let's do a new pose next time, only if you're willing to help your mom out again of course."
                mc "Anytime, mom!"

    elif mom_yoga3_complimented:
        mc "It was great!"
        mc "I didn't think I would enjoy it, but you're a great at teaching this!"
        mom "Oh wow, thank you! That's really good to hear!"
        mc "See you next time?"
        mom "You bet! Let's do a new pose next time, only if you're willing to help your mom out again of course."
        mc "Anytime, mom!"
    else:

        mc "Well, not totally bad but... {w} Could have been better."
        mom "Oh, I see."
        mom "Maybe next time will be better?"
        mc "Maybe..."
        mom "Anyways... {w} Thank you for joining me."
        mc "Thank you too."


    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_yoga_4:

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home yoga mom 34
    else:
        scene home yoga mom 34 with slowfade
    mom "Alright, [mc_name]!"
    mom "Let's start with the lotus again, to get focused."
    mc "Okay."

    scene home yoga mom 21 with fade
    mom "You have good form. {w} Straighten your back a little."
    mom "That's it!"

    scene home yoga mom 22 with dissolve
    mc "I still can't do that with my legs, though."
    mom "That'll come later."
    mom "If you still can't do it later I'll help you with it."

    scene home yoga mom 23 with dissolve
    mom "Now focus on your breathing..."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mc "(I feel... {w} peaceful.)"
    mom "Try to block your thoughts and just concentrate on your breathing, on my voice."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."

    scene home yoga mom 24 with dissolve
    mom "You're doing great, [mc_name]!"
    mom "How do you feel?"
    mc "It feels...{w} good."
    mc "It cleared my head, I think."
    mom "That's great, that's what it is supposed to do!"
    mom "I have a new pose I need some help with if you are up for it!"
    mc "Of course!"

    scene home yoga mom 25 with slowfade
    mc "(Holy shit!)"
    mom "I can't really get the form right yet, can you help me out with that?"

    scene home yoga mom 26 with dissolve
    mc "Sure!"
    mc "Just be careful not to hurt yourself, mom!"
    mom "Haha, don't worry about that."

    scene home yoga mom 27 with dissolve
    mom "I have you here to protect me."
    mc "So what should I do?"
    mom "Grab my leg and slowly help me straighten it out."

    scene home yoga mom 28 with dissolve
    mc "(Man... Her body is incredible!)"
    mc "(It takes some dedication to do these exercises too!)"
    mc "Alright, here we go!"

    scene home yoga mom 29 with fade
    mom "Yeah, that's it [mc_name], slowly!"
    mc "(Oh God...)"
    mc "(My crotch is touching her again..)"

    scene home yoga mom 30 with dissolve
    mc "(If this was a sex pose...)"
    mc "(I might be able to put it in, even!)"
    mc "(Ah shit, the last thing I need is for her to feel my boner!)"

    scene home yoga mom 31 with dissolve
    mc "(Especially since things are going so nicely with her...)"
    mc "(.....)"
    mc "(Her tits are huge... I can only imagine what it would be like doing this naked.)"

    scene home yoga mom 33 with dissolve
    mc "(The both of us, fully naked...{w} and sweaty...)"
    mc "(Our bodies sliding on top of each other in a hot embrace...)"
    mc "(Sliding her breasts around every inch of my-)"

    scene home yoga mom 32 with dissolve
    mom "Ahh!"
    mom "Yes, we did it!"
    mc "(Oh shit, I got lost in my thoughts!)"
    mom "You can stop now, [mc_name]."

    scene home yoga mom 36 with slowfade
    mom "Whew, thanks a lot [mc_name]!"
    mom "Another pose we got in the bag together!"
    mc "I was happy to help, mom!"
    mom "I'm looking forward to our next time!"
    mc "Me too!"
    mc "(My penis certainly does as well... Damn!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_yoga_5:

    stop music fadeout 10.0
    if _in_replay:
        call setup_gallery
        scene home yoga mom 34
    else:
        scene home yoga mom 34 with slowfade
    mom "Alright, let's do some yoga!"
    mom "I see you still haven't got any yoga gear."
    mom "Those jeans are not going be comfortable."
    mc "Didn't you tell me last time that we don't really need proper equipment for this?"
    mc "That resonated with me. We only need our bodies to reap the benefits of yoga."

    scene home yoga mom 38 with dissolve
    mom "It's true I said that but..."
    mom "Hmm..."

    scene home yoga mom 39 with dissolve
    mom "(I was just about to protest there but...)"
    mom "(He's already seen me. And I said I would be more 'helpful' with his interests.)"
    mom "(Ah, why not? It's just yoga anyway.)"

    scene home yoga mom 40 with dissolve
    mom "Alright then, Mr! Out of your clothes!"

    scene home yoga mom 41 with fade
    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0

    mom "We're doing naked yoga this time."
    mc "(Oh.{w} My.{w} God.)"
    mc "(I'm staring right at her boobs. Did I hear that correctly? Naked yoga?)"
    mc "Oh wow!"
    mc "I mean, you're beautiful as ever, mom."

    scene home yoga mom 42 with dissolve
    mom "Thank you, just...{w} Make sure the door is locked."
    mom "We wouldn't want anyone to, you know-"
    mc "Disturb our peaceful yoga session."
    mom "Exactly."

    scene home yoga mom 43 with fade
    mom "I'll be leaving the panties on for now."
    mc "Why?"
    mom "Sometimes, women leave them on. And that's enough talk about that."
    mc "Ah, okay. I get it."
    mom "Now, about your cloth- Oh!"

    scene home yoga mom 44 with dissolve
    mc "Eh... Sorry."
    mc "It's just... You look so great."

    scene home yoga mom 45 with dissolve
    mom "Oh..."
    mom "(Jesus, it's huge!)"
    mom "(I can't get used to seeing it.)"
    mom "(I remember when it slid into my mouth after our movie night...)"
    mom "(Oh God... What am I thinking. I have to focus.)"
    mom "Is that my fault?"
    mom "We'll have to deal with that."
    mom "You can't do yoga when you're that stiff."
    mc "(Oh! Is this it? Is this happening?)"

    scene home yoga mom 46 with dissolve
    mom "A little bit of meditation will solve everything."
    mc "Oh..."
    mc "Yes, of course. Meditation, haha."
    mc "(Damn...)"
    mc "(I shouldn't complain though.)"
    mc "(One of the hottest women I've ever seen is standing before me in just her panties.)"
    mc "(And we're about to do some hot yoga together.)"

    scene home yoga mom 47 with fade
    mom "Alright, so remember how I taught you before..."
    mom "Empty your mind."
    mom "When your thoughts wander, bring them back and concentrate on your breathing."
    mom "We'll get that huge-{w} *cough-cough*"
    mom "I mean, that will take care of your erection, I'm sure."

    scene home yoga mom 48 with dissolve
    mom "Now focus on your breathing..."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mc "(I feel... {w} peaceful.)"
    mom "Try to block your thoughts and just concentrate on your breathing, on my voice."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."
    mom "In{w=0.5}.{w=0.5}.{w=0.5}."
    mom "And out{w=0.5}.{w=0.5}.{w=0.5}."

    scene home yoga mom 49 with dissolve
    mc "(This is working, surprisingly.)"
    mc "(Even though there's a different kind of in-and-out I'd like to do, it feels like I can control my erection more.)"
    mc "(Who would have thought...)"
    mom "Alright, good job [mc_name]!"
    mom "Now, let me stretch my back a bit, then we can start."

    scene home yoga mom 50 with dissolve
    mom "Ahh~"
    mom "Just like that, up and down..."

    scene home yoga mom 51 with dissolve
    mom "I'd like you to help me with new poses this time."
    mom "And maybe on our next session you could do some yourself!"
    mc "I'm not sure I can do it..."
    mom "I'll help you, don't worry."

    scene home yoga mom 52 with dissolve
    mc "Wow, mom, your stomach is really toned!"
    mc "It must have been a lot of work to get that result."
    mc "(I can't believe I'm casually chatting with her like this.)"
    mc "(But if she's cool enough to do this, the least I can do is to agree to her rules and not pop a woody again.)"
    mom "Okay, first one is hard, so pay attention. I'll need you to hold me."

    scene home yoga mom 53 with slowfade
    mom "That's it [mc_name], hold me a bit until I get my balance."
    mc "(Holy shit, this is a weird pose!)"

    scene home yoga mom 54 with dissolve
    mc "(It reminds me of a different kind of pose though...)"
    mc "(How could she do this without my help?)"
    mc "(Well, maybe I'm really helping then and not just gawking.)"

    scene home yoga mom 55 with dissolve
    mom "Almost..."
    mc "I got you, mom."
    mc "(She's really taking it seriously.)"
    mc "(As she's balancing herself, her crotch is bumping against my cock a little bit.)"

    scene home yoga mom 56 with dissolve
    mc "(Shit...)"
    mc "(Only a tiny bit of fabric is between her sex and mine.)"
    mc "(I don't think I can handle the excitement...)"
    mom "I think I need a bit more support-"

    scene home yoga mom 57 with dissolve
    mc "(Ow, there it is.)"
    mc "(My erection is pushing against her crotch as my cock is filling up with blood.)"
    mom "I wasn't expecting that kind of support. Alright, let's change positions."

    scene home yoga mom 58 with slowfade
    mom "Alright, you're doing good."
    mom "Make sure you're keeping my form straight."
    mc "Yeah, I'm trying."

    scene home yoga mom 59 with dissolve
    mc "(I'm trying not to shove it right inside her...)"
    mc "(Fuck, this is so sexy!)"
    mc "(So this could be what it's like to have sex with a yoga girl.)"
    mc "(All the regular poses but with an added bit of flexibility and hotness.)"

    scene home yoga mom 60 with dissolve
    mc "(My cock fits right between her asscheeks like this.)"
    mc "(There's no way she can't feel that, but she's not saying anything about it.)"
    mc "(I can see a small layer of sweat gathering on her body. As much fun as it is for me, it must not be so easy for her to do all these.)"
    mc "(Some time ago I never would have thought this could happen... Resting my cock on mom's ass with her permission.)"
    mc "(Damn, my mom is great. Yoga is great. Life is fuckin' great!)"

    scene home yoga mom 61 with dissolve
    mom "(Ah... This pose is not one of my favorites, but I guess he likes it.)"
    mom "(Judging by his penis resting between my asscheeks, I'm SURE he likes it.)"
    mom "(So I can hold it for a little longer for him. He's been really helpful lately.)"

    scene home yoga mom 62 with dissolve
    mom "(I can feel the small twitches of his...{w} Thing-)"
    mom "(Oh, who am I kidding... It's his large cock.)"
    mom "(It's a dangerous game I'm playing. Letting him do all this, no, even encouraging him - this could all end in a horrible way.)"

    scene home yoga mom 63 with dissolve
    mom "(But then...)"
    mom "(Why do I enjoy it so much?)"
    mom "Alright, that's enough for now."

    scene home yoga mom 46 with fade
    mom "Well..."
    mom "I think we're going to have to work on your 'control' a bit next time."
    mc "Ah, sorry. You're just too hot of a yoga girl for me, mom."
    mom "(A yoga {i}girl{/i}? And not an old woman?)"
    mom "That's sweet of you to say."
    mom "Now... I'm sure you have something to do to take care of that."
    mom "So let's continue next time."
    mc "Sure, thanks mom!"
    mom "(Now he's going to go and masturbate while thinking about what we just did. About me.)"
    mom "(I think I need to lie down a bit, too...)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return















label mom_massage_1:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene home afterdrink mom 1 with fade
    mc "Hi, mom. You're looking a little stressed. Would you like a massage?"


    if mom_seen_massage_level == 0:
        mom "Actually, yes. I could really use a shoulder massage."

        scene home massage mom 1 with fade
        mc "Well you're in luck; I'd like to think I'm quite good at giving massages."

        scene home massage mom 2 with dissolve
        mom "Ooh, right there. You {i}are{/i} good at this, [mc_name]."
        mc "Told ya so. So I wanted to tell you that I'm actually enjoying being back home, mom."

        scene home massage mom 3 with dissolve
        mom "I'm glad to hear that, hun. It's nice to have all my kids back home. And I'm so glad that you and I can spend time together again."
        mc "Me too, mom. Maybe we can do other things together?"
        mom "Uhm, what kinds of things... hunny?"

        scene home massage mom 4 with dissolve
        mc "Well, anything really. You're still into yoga, right? I could be your yoga partner."
        mom "Sure, that would be nice. If you don't find yoga too girly."
        mc "Not at all, mom. Yoga certainly has it's appeal!"
        mom "Alright, thank you [mc_name]. I have some things to do now."
        mc "If you need a massage anytime, just let me know!"
    else:

        mom "Actually, yes. I could really use one of your massages!"

        scene home massage mom 1 with fade
        mc "Well you're in luck! I'll make you feel better in no time!"

        scene home massage mom 2 with dissolve
        mom "Ooh, right there."

        scene home massage mom 3 with dissolve
        mom "Yeah, that feels nice!"

        scene home massage mom 4 with dissolve
        mom "After all these massages, I feel like I should return the favor sometime."
        mc "Oh, I'm happy to help out."
        mc "(Although it could actually be nice to get massaged by her...)"
        mc "On second thought...{w} I might take you up on that in the future!"
        mom "Haha, alright!"


    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_massage_2:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home afterdrink mom 1
    else:
        scene home afterdrink mom 1 with fade
    mc "Hi, mom. You're looking a little stressed. Would you like a massage?"
    mom "Actually, yes. I could really use one of your massages!"

    scene home massage mom 1 with fade
    mc "Well you're in luck! I'll make you feel better in no time!"

    scene home massage mom 2 with dissolve
    mom "Ooh, right there."

    scene home massage mom 3 with dissolve
    mom "Yeah, that feels nice!"

    scene home massage mom 4 with dissolve
    mom "After all these massages, I feel like I should return the favor sometime."
    mc "Oh, I'm happy to help out."
    mc "(Although it could actually be nice to get massaged by her...)"
    mc "On second thought...{w} I might take you up on that in the future!"
    mom "Haha, alright!"
    mc "So... how about we go further with the massage?"
    mom "Umm..."
    mc "C'mon, lay down. You're always up and doing something, let me give you a leg massage."

    scene home massage mom 5 with dissolve
    mom "I {i}could{/i} use a good massage. But..."
    mom "(I don't know about having my son touch me in such an intimate way...)"

    scene home massage mom 6 with dissolve
    mom "(But our relationship has been getting so much closer. I can't make this seem weird and risk pushing him away.)"
    mc "I already have the lotion..."

    scene home massage mom 7 with dissolve
    mom "I guess that'd be okay. I mean, how can I say no to a free massage. Right?"
    mc "It'll be good, don't worry."

    scene home massage mom 8 with dissolve
    mc "(Not gonna lie, I can't wait to get my hands on those magnificent legs!)"
    mc "I'll just put the lotion on my hands first so you won't get a cold shock."

    scene home massage mom 9 with dissolve
    mc "(Her skin is even softer than I expected! So silky smooth but solid and toned at the same time.)"
    mom "(Mmm, this feels really good. I've missed being pampered like this. It's been far too long.)"

    scene home massage mom 10 with dissolve
    mom "(It's just kind of sad that it had to be my son doing this for me and not my own husband.)"
    mc "(I can't resist it... I have to go a little higher than that!)"


    if mom_seen_massage_level == 1:
        scene home massage mom 11 with dissolve
        mom "*Oh!*"
        mc "(Dang, she closed her legs. ...but she's also not stopping me.)"
        mc "Ah, sorry, I didn't mean to make you uncomfortable."
        mom "No it's fine, uhm... {w} It just felt better on my lower leg."

        scene home massage mom 12 with dissolve
        mom "But uhm, thank you for the massage, but I just remembered that I have to run some errands."
        mc "Ah, okay, mom."
        mc "(Yeah, better not push my luck more now anyway.)"
    else:



        scene home massage mom 11 with dissolve
        mom "*Oh!*"
        mom "(He just went higher up my leg! Should I stop him? What if he keeps going higher?)"
        mc "(Dang, she closed her legs. But... she's also not stopping me. I'm even starting to hear little moans from her!)"
        mom "(Mmm... god this feels good! I'm starting to feel it in other places too and it's getting me all hot and bothered.)"

        scene home massage mom 12 with dissolve
        mom "*Ahem* [mc_name], hunny? It feels great but I think we should stop here."
        mc "(Dang. I guess that's as far as I can take it. For now...)"
        mc "Okay, mom."
        mom "(Aw, I knew he'd be a little disappointed if I stopped him. But I couldn't risk it going any farther. That just wouldn’t be right... even if it did feel good.)"


    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_massage_3:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home afterdrink mom 1
    else:
        scene home afterdrink mom 1 with fade
    mc "Hi, mom. You're looking a little stressed. Would you like a massage?"
    mom "Actually, yes. I could really use one of your massages!"

    scene home massage mom 1 with fade
    mc "Well you're in luck! I'll make you feel better in no time!"

    scene home massage mom 2 with dissolve
    mom "Ooh, right there."

    scene home massage mom 3 with dissolve
    mom "Yeah, that feels nice!"

    scene home massage mom 4 with dissolve
    mom "After all these massages, I feel like I should return the favor sometime."
    mc "Oh, I'm happy to help out."
    mc "(Although it could actually be nice to get massaged by her...)"
    mc "On second thought...{w} I might take you up on that in the future!"
    mom "Haha, alright!"

    scene home massage mom 4 with dissolve
    mc "So... how about we go further with the massage?"
    mom "Ah, the leg massage?"
    mom "I'm really getting used to it."

    scene home massage mom 5 with fade
    mom "Those heels are taking a toll on my legs..."

    scene home massage mom 6 with dissolve
    mc "Well, that's the price of beauty!"

    scene home massage mom 7 with dissolve
    mc "I'll make sure to get them both relaxed."

    scene home massage mom 8 with dissolve
    mc "(Not gonna lie, I can't wait to get my hands on those magnificent legs!)"
    mc "I'll just put the lotion on my hands first so you won't get a cold shock."

    scene home massage mom 9 with dissolve
    mc "(Her skin... So silky smooth but solid and toned at the same time.)"

    scene home massage mom 10 with dissolve
    mom "Mhmm..."
    mom "You have great hands, [mc_name]."
    mc "(I can't resist it... I have to go a little higher than this!)"

    scene home massage mom 11 with dissolve
    mom "*Oh!*"
    mc "Ah, sorry, I didn't mean to make you uncomfortable."
    mom "No it's fine..."

    scene home massage mom 12 with dissolve
    mom "It's just... {w} Tickles sometimes."

    scene home massage mom 13 with fade
    mc "To be able to do this properly, I need to get those thighs as well."
    mc "I'm just telling you in advance, so you won't get ticklish!"

    scene home massage mom 14 with dissolve
    mom "Alright...{w} Thanks for the heads-up..."

    scene home massage mom 15 with dissolve
    mc "(Ah man...)"
    mc "(Now this is getting to a place where I really need to control myself.)"
    mc "(Pop a weird boner here, and I'm ruined for life.)"

    scene home massage mom 16 with dissolve
    mom "Mhmm..."
    mom ".{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}."

    scene home massage mom 14 with fade
    pause

    scene home massage mom 17 with dissolve
    mc "(Wow!)"
    mc "(She just opened her legs... Slowly...)"

    scene home massage mom 18 with dissolve
    mc "(My God!)"
    mc "(Looks like I'm doing good!)"

    scene home massage mom 19 with dissolve
    mc "(I must not get carried away...)"
    mc "(Giving a proper massage is key.)"
    mc "(I need to change grip...)"
    mc "(Well, if this doesn't make her scream pervert, then I'm golden.)"
    mc "(Here we go!)"

    scene home massage mom 20 with dissolve
    pause 0.5

    scene home massage mom 22 with dissolve
    mom "{size=-10}Hah~{/size}"

    scene home massage mom 20 with dissolve
    mc "(Oh man!)"
    mc "(I'm working on her inner thighs...)"

    scene home massage mom 21 with dissolve
    mc "(I can even feel the heat radiating from her crotch.)"
    mc "(This is getting intense!)"
    mc "(I pushed rather far already...)"
    mc "(The smart move here is to retreat, and come back at a later time for more.)"
    mc "Ah, my hands are a bit tired, can we continue this later, mom?"

    scene home massage mom 22 with fade
    mom "Oh..."
    mom "I mean, yes, of course. {w} Later, then."

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label mom_massage_4:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene home afterdrink mom 1
    else:
        scene home afterdrink mom 1 with fade
    mc "Hi, mom. You're looking a little stressed. Would you like a massage?"
    mom "Actually, yes. I could really use one of your massages!"

    scene home massage mom 23 with fade
    mc "Well you're in luck! I'll make you feel better in no time!"
    mc "However, I think to relax you properly and to relieve more stress, I need to focus on more than just your legs."

    scene home massage mom 24 with dissolve
    mom "Oh, I see."
    mom "What do you have in mind?"
    mc "(All or nothing, I guess.)"
    mc "I should massage your entire body, but that's hard to do clothed of course."

    scene home massage mom 25 with dissolve
    mom "Oh, yeah I understand."
    mom "I'll slip out of my dress then but uhm, please turn around."
    mc "Of course, I'm a professional! Haha!"

    scene home massage mom 26 with slowfade
    mom "Alright, I'm leaving my underwear on."
    mom "I'll lay on the bed."

    scene home massage mom 27 with dissolve
    mc "Sure, I'll try to work around the underwear situation."
    mc "Although the bra can be in the way when I'm doing your back."

    scene home massage mom 29 with fade
    mom "Oh, sometimes I don't wear a bra. I don't today, so that's not going to be in the way."
    mc "(Damn!)"
    mom "Alright, you can start in a sec!"

    scene home massage mom 32 with slowfade
    mc "I'll go over your legs first."
    mc "{i}*gulp*{/i}"
    mc "(This went zero to a hundred real quick!)"

    scene home massage mom 28 with dissolve
    mc "(Containing a boner at this stage is going to be near-impossible!)"
    mc "(Those yoga sessions are definitely paying off...)"

    scene home massage mom 31 with dissolve
    mc "(She feels much more comfortable with this now.)"
    mc "(Well, her being almost completely naked is a good indicator.)"
    mc "(But her body language suggests the same.)"
    mc "(Oh and how much I wanna speak that {i}body language{/i}!)"
    mc "I'll do the other leg now. I'm getting on the bed."
    mom "Alright honey, I leave it to you. You are good at this!"

    scene home massage mom 33 with slowfade
    mc "(Ah man...)"
    mc "(This is so hot!)"
    mc "(She doesn't close her legs anymore, even though I'm massaging her inner thigs.)"
    mc "(But I shouldn't be all too touchy-feely too soon.)"

    scene home massage mom 34 with dissolve
    mc "I realized that I didn't do your feet last time."
    mom "Mhmmm, that's great!"
    mc "Is it good like this? I'm not pressing too hard, am I?"

    scene home massage mom 35 with dissolve
    mom "Oh you can go hard on me, I can take it."
    mc "(Fuuck! I bet she can!)"
    mc "(My perverted fantasies can't take too much more though!)"

    scene home massage mom 36 with dissolve
    mom "Mhmmm~"
    mom "I can feel your jeans touching my legs."
    mom "I hope you're not going to get massage oil all over your clothes, [mc_name]."
    mom "You should have dressed accordingly."
    mc "Ah, yeah. I didn't think about that."
    mom "I think it's already too late for your jeans, but at least take your T-shirt off. You always wear those long ones, we don't want it to get oily as well..."
    mc "Sure, you're right."
    mc "(Oh God...)"

    scene home massage mom 37 with slowfade
    mom "Mmmm~"
    mom "You're really talented."
    mom "I was reluctant at first but... This is just too good to give up!"

    scene home massage mom 38 with dissolve
    mc "Reluctant?"
    mc "You don't have to be. I'm not saying I'm an expert, but I'm not a newbie when it comes to massages either."

    scene home massage mom 39 with dissolve
    mom "I can feel that."
    mom "Mmm, yeah I feel refreshed already!"
    mom "Thank you honey!"
    mc "(Aw, this is ending too soon... I could massage her all day!)"
    mom "And bring proper clothes next time!"
    mc "(Ah, it's music to my ears... There's always sweet next time.)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
