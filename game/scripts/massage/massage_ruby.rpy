label ruby_massage_controller:
    python:
        temp_1 = ruby_massage_text(1)
        temp_2 = ruby_massage_text(2)
        temp_3 = ruby_massage_text(3)
        temp_4 = ruby_massage_text(4)
        temp_5 = ruby_massage_text(5)


    menu ruby_massage_menu:

        "Massage #1[temp_1]" if ruby_massage_level >= 1:
            call massage_ruby_1
            if ruby_seen_massage_level == 0:
                $ ruby_seen_massage_level = 1
            $ ruby_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_rubyroom)


        "Massage #2[temp_2]" if ruby_massage_level == 2:
            call massage_ruby_2
            if ruby_seen_massage_level == 1:
                $ ruby_seen_massage_level = 2
            $ ruby_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #2 & 3[temp_3]" if ruby_massage_level >= 3:
            call massage_ruby_3
            if ruby_seen_massage_level == 2:
                $ ruby_seen_massage_level = 3
            $ ruby_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #4[temp_4]" if ruby_massage_level >= 4:
            call massage_ruby_4
            if ruby_seen_massage_level == 3:
                $ ruby_seen_massage_level = 4
            $ ruby_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)


        "Massage #5[temp_5]" if ruby_massage_level >= 5:
            call massage_ruby_5
            if ruby_seen_massage_level == 4:
                $ ruby_seen_massage_level = 5
            $ ruby_massage_counter += 1
            $ increase_time()
            $ go_to(L_home_hall)




        "Massage #2 (locked)" if ruby_massage_level < 2:
            jump ruby_massage_menu
        "Massage #3 (locked)" if ruby_massage_level < 3:
            jump ruby_massage_menu
        "Massage #4 (locked)" if ruby_massage_level < 4:
            jump ruby_massage_menu
        "Massage #5 (locked)" if ruby_massage_level < 5:
            jump ruby_massage_menu
        "Back":


            jump home_kitchen_ruby







label massage_ruby_1:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene ruby store 1 with fade
    mc "Heya, Ruby. How about a massage?"

    if ruby_seen_massage_level == 0:
        ruby "A massage? Like {i}'you'{/i} give {i}'me'{/i} a massage? Wouldn't that be weird?"
        mc "Not at all. C'mon, you'll enjoy it. And I'd like to get on your good side again."

        scene ruby store 4 with dissolve
        ruby "{i}Alriiight.{/i} I guess this is one way to make things up to me."

        scene home massage ruby 1 with fade
        mc "So what do you get up to these days, Ruby?"
        ruby "I-Umm... don't get up to much. Just hang out with friends I guess."

        scene home massage ruby 2 with dissolve
        mc "Oh? I haven't seen any around. Have they been over since I got back?"
        ruby "Uh... No. No, they haven't been around. We-ah, usually meet up somewhere."
        mc "Oh, like the mall or something? That's a little cliche, don't you think?"
        ruby "Maybe a little. But I'm still in my teens you know."
        if lain_mod:
            mc "(Oh, I know. And that makes thinking about you even hotter!)"
        mc "Makes sense, I guess."
        ruby "I think that's enough, thank you."
        mc "(That ended abruptly...)"
    else:

        ruby "This again? I guess."

        scene home massage ruby 1 with fade
        ruby "It doesn't feel all that good, you know. You have big hands."
        mc "I'll be more gentle then, alright?"

        scene home massage ruby 2 with dissolve
        ruby "Yeah, that would be great."
        mc "Why don't you lay down then?"
        ruby "Maybe some other time..."

    scene black with fade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return






label massage_ruby_2:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene ruby store 1 with fade
    mc "Heya, Ruby. How about a massage?"
    ruby "This again? I guess."

    scene home massage ruby 1 with fade
    ruby "It doesn't feel all that good, you know. You have big hands."

    scene home massage ruby 2 with dissolve
    mc "I'll be more gentle then, alright?"
    ruby "Yeah, that would be great."
    mc "Why don't you lay down then?"
    ruby "{i}Sigh...{/i} {w} Fine..."

    scene home massage ruby 3 with slowfade
    mc "See, it's much better like this!"
    ruby "Just be gentle..."
    ruby "You can be such a brute sometimes!"
    mc "(Is there anything this girl doesn't have a problem with?)"

    scene home massage ruby 4 with dissolve
    mc "How about now?"
    ruby "Yeah, something like this..."
    mc "(Judging by her breathing, she's relaxed.)"
    mc "(But this stupid top is in the way, I can't do it properly like this.)"
    mc "Sis, I need you get out of your top to be able to this properly."

    scene home massage ruby 5 with dissolve
    ruby "I knew this is just some pervert thing of yours!"
    mc "Have you seen anyone give a proper massage to somone who is clothed?"
    ruby ".....{w} No..."
    ruby "Alright, but don't you dare look!"
    ruby "I've had enough of your pervy ogling for a while!"
    mc "(She's so whiny...)"
    mc "{size=-10}Like I'd wanna look...{/size}"
    ruby "What did you say?"
    mc "Nothing! {w} I mean I said sure, I won't look."

    scene home massage ruby 6 with slowfade
    pause
    mc "(Holy shit, she doesn't have a bra on!)"
    ruby "You better make me feel good now!"
    mc "Yes, princess!"

    scene home massage ruby 7 with dissolve
    pause
    ruby "This is so embarrassing..."
    mc "I'm not forcing you to do anything, why don't you just sa-"
    ruby "Just shut it [mc_name]!"
    mc "..."
    ruby "Yeah, that actually starts to feel good now."

    scene home massage ruby 8 with dissolve
    mc "(Wow, she is so petite...)"
    mc "(Her body disappears under my hands!)"
    mc "(Such a delicate little flower and such a brat at the same time.)"
    ruby "Mh~"
    mc "(I should teach her to have some respect...)"
    mc "Alright, that's all I had in me for today."
    ruby "What? Just when it was starting to feel good?"
    mc "Sorry, sis. Maybe next time."

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return






label massage_ruby_3:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby store 1
    else:
        scene ruby store 1 with fade
    mc "Heya, Ruby. How about a massage?"
    ruby "This again? I guess."

    scene home massage ruby 1 with fade
    ruby "It doesn't feel all that good, you know. You have big hands."

    scene home massage ruby 2 with dissolve
    mc "I'll be more gentle then, alright?"
    ruby "Yeah, that would be great."
    mc "Why don't you lay down then?"
    ruby "{i}Sigh...{/i} {w} Fine..."

    scene home massage ruby 3 with slowfade
    mc "See, it's much better like this!"
    ruby "Just be gentle..."
    ruby "You can be such a brute sometimes!"
    mc "(Is there anything this girl doesn't have a problem with?)"

    scene home massage ruby 4 with dissolve
    mc "How about now?"
    ruby "Yeah, something like this..."
    mc "(Judging by her breathing, she's relaxed.)"
    mc "(But this stupid top is in the way, I can't do it properly like this.)"
    mc "Sis, I need you get out of your top to be able to this properly."

    scene home massage ruby 5 with dissolve
    ruby "I knew this is just some pervert thing of yours!"
    mc "Have you seen anyone give a proper massage to somone who is clothed?"
    ruby ".....{w} No..."
    ruby "Alright, but don't you dare look!"
    ruby "I've had enough of your pervy ogling for a while!"
    mc "(She's so whiny...)"
    mc "{size=-10}Like I'd wanna look...{/size}"
    ruby "What did you say?"
    mc "Nothing! {w} I mean I said sure, I won't look."

    scene home massage ruby 6 with slowfade
    pause
    mc "(Holy shit, she doesn't have a bra on!)"
    ruby "You better make me feel good now!"
    mc "Yes, princess!"

    scene home massage ruby 7 with dissolve
    pause
    ruby "This is so embarrassing..."
    mc "I'm not forcing you to do anything, why don't you just sa-"
    ruby "Just shut it [mc_name]!"
    mc "..."
    ruby "Yeah, that actually starts to feel good now."

    scene home massage ruby 8 with dissolve
    mc "(Wow, she is so petite...)"
    mc "(Her body disappears under my hands!)"
    mc "(Such a delicate little flower and such a brat at the same time.)"
    ruby "Mh~"
    mc "(Alright, time to take things a bit further...)"

    scene home massage ruby 9 with dissolve
    mc "(The next step would be to go lower with the massage so...)"
    mc "(Time to get these pants off!)"

    scene home massage ruby 10 with dissolve
    ruby "What the hell are you doing?"
    mc "Uhm...{w} Pulling your pants down?"

    scene home massage ruby 11 with dissolve
    ruby "Why do you want to do that? Am I not naked enough already?"
    mc "I wanted to massage your legs and feet too but..."
    mc "I could just stop, though."

    scene home massage ruby 12 with dissolve
    ruby "......."
    ruby "Fine!"
    ruby "This better be worth it!"
    mc "Okay, I'll start with your feet then."

    scene home massage ruby 13 with fade
    mc "(Oh my God!)"
    mc "(That's a tiny little ass if I ever seen one!)"
    mc "(I shouldn't get distracted though...)"
    mc "(I'll give her the massage of her life, I want her to beg for more sessions!)"
    mc "Am I doing good?"

    scene home massage ruby 14 with dissolve
    ruby "Mhhm..."
    ruby "Surprisingly enough..."
    mc "(Man...)"
    mc "(I wanna spank her ass when she talks to me like that.)"
    mc "(But slow and steady wins the race...)"

    scene home massage ruby 15 with dissolve
    mc "Ah, my hands are becoming tired."
    ruby "What? After making me almost completely naked you just walk?"
    ruby "You should finish what you started!"
    mc "Whenever you're being condescending to me somehow my hands get tired really fast..."
    mc "Maybe next time, sis!"
    ruby "*tsk*"

    $ renpy.end_replay()

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return





label massage_ruby_4:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby store 1
    else:
        scene ruby store 1 with fade
    mc "Hey Ruby, want one my great massages?"
    ruby "...{w}Fine."
    mc "(Holy shit, that was quick!)"
    mc "(Maybe she was already expecting this?)"
    scene home massage ruby 16 with slowfade
    ruby "Turn around while I take off my clothes!"
    mc "Take them all off?"
    ruby "Don't be stupid! I'm leaving my panties on!"
    mc "(Worth a try!)"

    scene home massage ruby 18 with dissolve
    ruby "If you peek you'll regret it [mc_name]!"
    mc "You worry too much!"
    mc "I'm a respectful guy, you know. I respect women."

    scene home massage ruby 19 with dissolve
    ruby "Yeah, that's what you're famous for..."
    mc "What?"
    ruby "Nothing..."

    scene home massage ruby 21 with slowfade
    ruby "I'm on the bed..."
    ruby "You can turn around."
    mc "Alright!"

    scene home massage ruby 20 with dissolve
    mc "(Hot damn!)"
    mc "(She's such a hot little vixen!)"
    mc "(Her petite frame gets me everytime.)"

    scene home massage ruby 22 with dissolve
    mc "(And that butt...)"
    mc "(It's always tempting me.)"

    scene home massage ruby 23 with dissolve
    mc "I'll start with your legs then."
    ruby "Mmm-hmm."

    scene home massage ruby 21 with fade
    ruby "You're really into these massages..."
    mc "Aren't you?"
    ruby "We're not talking about me right now..."
    ruby "Where does this come from?"
    mc "Can't I just be happy that I make you feel good?"
    ruby "It just seems so... {w} {size=-12}Intimate.{/size}"
    mc "What was that?"
    ruby "Nothing... just keep going."

    scene home massage ruby 24 with dissolve
    mc "Alright, I'll go for this leg now."
    mc "Let me know if anything uhm, tickles or something."

    scene home massage ruby 30 with dissolve
    ruby "Mhm... {w} Sure..."

    scene home massage ruby 26 with dissolve
    mc "(She seems relaxed.)"
    mc "(That's good, I'm actually happy I can make her a ease up a bit.)"
    mc "(She still has to learn 'her place' with that attitude of hers.)"
    mc "(But I feel like she's bottling up a lot of emotions.)"
    mc "(Well, that's something I have to talk to her about another time. It's time to turn this up a notch.)"

    scene home massage ruby 27 with dissolve
    mc "Time to work on your inner thighs a bit."
    mc "(I can feel the heat radiating from her crotch...)"
    mc "(She doesn't close her legs when I get higher or tense up.)"

    scene home massage ruby 25 with dissolve
    ruby "Mhm~"
    ruby "{i}*inhales heavily*{/i}"
    mc "(Oh, I guess she likes that!)"

    scene home massage ruby 28 with fade
    mc "And now your glutes..."
    mc "(Or in other words, your magnificent little butt!)"

    scene home massage ruby 29 with dissolve
    mc "(Maybe I really should be a massage therapist...)"
    mc "('Dirty masseur...')"
    mc "(Anyway... I have to concentrate. If I just keep fondling her ass that's not too professional.)"
    mc "(I feel like I took it far enough for now but...)"
    mc "(I have an idea for a nice finishing touch.)"

    scene home massage ruby 31 with dissolve
    mc "I think I left out this part, I'll return to it real quick."
    mc "(My God! The heat from her pussy got even more intense.)"

    scene home massage ruby 32 with dissolve
    ruby "Mhmm~"
    ruby "[mc_name]..."
    ruby "You're getting me...{w} I mean, it's too close to my..."

    scene home massage ruby 31 with dissolve
    mc "Oh sorry about that!"
    mc "(Shit, I think she's turned on by this!)"
    mc "(She not exactly over the edge though...)"
    mc "(I don't want to push her too soon.)"
    mc "Alright, my hands are a bit tired anyway so let's wrap this up."
    mc "I'm looking forward to the next one!"

    scene home massage ruby 32 with dissolve
    ruby "The next..."
    ruby "Yeah..."

    $ renpy.end_replay()

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return






label massage_ruby_5:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby store 1
    else:
        scene ruby store 1 with fade
    mc "Hey Ruby, want one my great massages?"
    ruby "...{w}Fine."
    scene home massage ruby 16 with slowfade
    ruby "Turn around while I take off my clothes!"
    mc "(Holy shit, that was quick!)"
    mc "(Maybe she was already expecting this?)"
    mc "Take them all off now."
    ruby "Don't be stupid! I leave my panties on!"
    mc "No, not this time."

    scene home massage ruby 33 with fade
    ruby "What? Why do you want me to be completely naked?!"
    ruby "That's not needed for a massage!"
    mc "Sure, but it does make it a lot better."

    scene home massage ruby 34 with dissolve
    ruby "How so?"
    mc "Your underwear won't get in the way at all. You know how good I am with my hands..."
    mc "(Especially after the dressing room incident...)"
    mc "(She is so hot, of course I wanna see her without the underwear!)"
    mc "(She might need a little bit of an encouragement first, though...)"
    mc "You know what, I'll take my clothes off as well, so you can feel more comfortable!"

    scene home massage ruby 35 with fade
    ruby "Wait, I didn't tell you you could turn around!"
    mc "Ruby, I've seen you already, remember? In the booth!"
    ruby "That doesn't mean you can see me anytime you want!"
    mc "Don't be so whiny all the time..."
    mc "I just wanted to make you feel better..."

    scene home massage ruby 36 with dissolve
    ruby "I'm...{w} Feeling okay, thanks. Just as long you leave the underwear on."
    mc "Does that mean you will leave it on too...?"
    ruby "Ugh...{w} You're not gonna leave me alone until I take it off, right?"
    mc "(Actually, I was just about to drop the whole thing...)"
    ruby "Fine, but turn around, and don't you dare look!"

    scene home massage ruby 37 with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.03
    pause
    ruby "If you look I swear I'll kick your balls so har-"
    mc "Alright, alright! I won't look!"
    mc "But wait, how am I going to massage you if I-"

    scene home massage ruby 38 with dissolve
    ruby "Just shut the hell up, [mc_name]!"
    ruby "I'll tell you when I'm ready... This better be worth it!"
    pause 1.0

    scene home massage ruby 39 with dissolve
    ruby "I'm-{w} I'm ready!"
    pause
    mc "(Sweet baby Jesus!)"
    mc "(My little sister is laying in front of me completely naked, and she's only waiting for my touch.)"
    mc "(I'm already getting pretty ha-)"
    ruby "Are you gonna start or what?"

    scene home massage ruby 40 with dissolve
    mc "Geez, fine!"
    ruby "You're not looking, are you?"
    mc "But I've already seen-"
    mc "Besides, I can't massage you if I'm not loo-"
    ruby "Just tell me you won't you dumbass!"
    mc "Oh, I won't. {w} Of course I won't."
    mc "Why would I look anyways?"

    scene home massage ruby 41 with dissolve
    ruby "Excuse me?"
    mc "Nothing, nothing."
    mc "Just enjoy the massage!"
    ruby "Mhm..."
    pause 1.0

    scene home massage ruby 42 with dissolve
    pause
    mc "(Oh man, these sweet little buns between my hands feel fabulous!)"
    mc "(It feels like I'm massaging my dreams!)"
    mc "(So I dream of asses?)"
    mc "(Yeah, that seems right.)"
    mc "(Hmmm... What if I...)"

    scene home massage ruby 43 with dissolve
    pause
    mc "(Oh yes!)"
    mc "(Pulling her asscheeks open reveals more of her tiny butthole, and I can even see a tiny bit of her pussy from up here.)"

    scene home massage ruby 44 with dissolve
    pause
    mc "(She truly has a fantastic body.)"




    scene home massage ruby 45 with dissolve
    pause

    mc "(I'm pulling her asscheeks apart, she's probably realized that by now.)"





    scene home massage ruby 47 with dissolve
    pause
    mc "(I should get back to massaging it a little before she tells me how sick and perverted I am...)"
    mc "(But man...)"
    mc "(I can hardly keep my dick in my pants at this point.)"

    scene home massage ruby 48 with dissolve
    ruby "Mmhmm~"
    mc "(Oh?)"
    mc "(She likes it?)"
    mc "Ah, sorry, I couldn't get a good angle. But I'll keep massaging somewhere else."
    ruby "N-no, it's good."
    ruby "Maybe this will help get a better angle...?"
    pause 0.5

    scene home massage ruby 49 with vpunch
    pause 1.0
    mc "(Oh fuck, she just pushed her ass up a little bit for me!)"
    mc "Yeah, it definitely helps."

    scene home massage ruby 50 with dissolve
    mc "(Jesus, my little slutty sis!)"
    mc "(She's probably doing this to tease me!)"
    mc "(If she is, then I gotta admit, she's doing it pretty well!)"

    scene home massage ruby 51 with dissolve
    mc "(A weaker person might already have shoved their cock right into her little hole.)"
    mc "(Not me though...)"
    mc "(I'm playing the long game here. I just hope I don't pop in my pants in the meantime...)"

    ruby "Not a bad massage, it was more grabbing than massaging this time, though."
    ruby "Next time maybe put in some more effort if I went and undressed for you?"
    mc "(The sass...{w} But she got me this time.)"
    mc "Sorry, I must have zoned out a little bit."
    ruby "Uhum..."
    mc "(I'm so full of shit... And she knows it...)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
