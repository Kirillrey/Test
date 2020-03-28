label home_basement_bed_sleep_dialogue:

    mc "Time for me to get some sleep."
    if laptop_owned:
        scene home_basement__day with Fade(0.5, 1.2, 0.5)
    else:
        scene home_basement__day_nolaptop with Fade(0.5, 1.2, 0.5)

    return






label purchase_sleepingpills_dialogue:

    scene mc laptop 2 with dissolve
    mc "(I think I have an idea on how I could get into Mom's room at night.)"
    mc "(Dad's always working late at night in their bedroom, since his study is being renovated.)"
    mc "(But I think some good old sleeping pills should do the trick.)"
    if sleeping_pills.delivery_delay == 1:
        mc "(One-day shipping too, great!)"
    else:
        pause 0.5
        mc "(Damn, I just missed the deadline for one-day shipping. It says it'll be delivered the day after tomorrow.)"

    return


label deliver_sleepingpills_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene sleeping pill 1 with dissolve
    mc "(Sweet, the sleeping pills were delivered!)"
    mc "(And it's not that homeopathic bullshit either.)"

    scene sleeping pill 2 with dissolve
    mc "(It's the real deal!)"
    mc "(I guess I'll find out how well it works soon enough though...)"

    scene sleeping pill 3 with dissolve
    mc "(Dad should probably get some sleep every once in a while anyways.)"
    mc "(The old man works way too hard.)"

    scene home_basement__day with fade

    return


label purchase_sunscreen_dialogue:

    scene mc laptop 2 with dissolve
    if isabel_sunscreen_failed:
        mc "(Alright, time to buy some sunscreen for Isabel. Thank god I can order this shit online.)"
    else:
        mc "(Hmm... looks like there's a sale on sunscreen.)"
        mc "(Maybe that will come in handy soon?)"

    if isabel_sunscreen.delivery_delay == 1:
        mc "(One-day shipping too, great!)"
    else:
        pause 0.5
        mc "(Damn, I just missed the deadline for one-day shipping. It says it'll be delivered the day after tomorrow.)"

    return


label deliver_sunscreen_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene sleeping pill 1 with dissolve
    mc "(The sunscreen arrived. They weren't joking about the express delivery!)"
    if isabel_sunscreen_failed:
        mc "(I should talk to Isabel in her room now that I've got the sunscreen.)"

    scene home_basement__day with fade

    return


label purchase_vibrator_dialogue:

    scene mc laptop 2 with dissolve
    mc "(Alright, I think it's time to turn Ms Jane on.)"
    mc "(Women like gifts. And I have an idea for a proper gift.)"
    mc "(Let's see... {w} bigbazookatoys.com)"
    mc "(.............)"
    mc "(Hmm, this one's called 'The Sleek Stick')"
    mc "(That'll do I guess.)"
    if jane_vibrator.delivery_delay == 1:
        mc "(One-day shipping too, great!)"
    else:
        pause 0.5
        mc "(Damn, I just missed the deadline for one-day shipping. It says it'll be delivered the day after tomorrow.)"

    return


label deliver_vibrator_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    mc "(The package containing Ms Jane's vibrator arrived!)"
    mc "(Great! Now I need to deliver it to Ms Jane, personally.)"

    return






label ruby_4_textintrodressup_dialogue:

    scene home ruby dressup 1 with dissolve
    mc "Ahh..."
    pause 0.5
    play sound "audio/sfx/sms.ogg"
    "Phone" "* beep *"
    mc "Oh come on, \"beep boop\" already when I just opened my eyes!"

    scene home ruby dressup 2 with dissolve
    mc "It's a text from... Ruby?"
    mc "She says she wants me to...{w} What the hell??"
    mc "I need to go her room and talk to her right now!"

    scene home_basement__day with fade

    return






label mom_5_carbreakdown_dialogue:

    play music "audio/music/playtime.mp3" loop fadeout 2.0 fadein 2.0
    pause 0.8
    scene mom car breakdown 1 with slowfade
    mc "...."

    scene mom car breakdown 1:
        subpixel True
        align (0.5, 0.5)
        linear 1.0 zoom 1.04
    mc "*inhales*"

    scene mom car breakdown 1:
        subpixel True
        align (0.5, 0.5)
        zoom 1.04
        linear 1.0 zoom 1.0
    mc "*exhales*"

    scene mom car breakdown 2 with dissolve
    mc "(What a beautiful morning!)"
    mc "(No Thorne, no family bullshit, just me and the birds chirping.)"

    scene mom car breakdown 3 with dissolve
    mc "(I should do this more often.)"
    mc "(Enjoy the small things in life, I mean.)"
    mc "(No wonder this family is a disfunctional mess, everybody is so stressed out all the time.)"

    stop music
    play sound "audio/sfx/dj-stop.mp3"
    scene mom car breakdown 4 with dissolve
    mom "This is bullshit!"
    mom "This piece of shit of a car!"

    scene mom car breakdown 5 with dissolve
    mc "(Ah shit, here we go again... {w} So much for the zen morning...)"
    mc "(Sounds like mom needs some help, I better check it out.)"

    play music "audio/music/comedy.mp3" loop fadein 2.5
    scene mom car breakdown 6 with fade
    mom "...and Raymond already left... Gah!"
    mom "I'll be late!"

    scene mom car breakdown 7 with dissolve
    mom "He has all that money, why can't he pay a proper mechanic to service the car?!"
    mom "He's always like \"I'll do it myself\" but he never does!"
    mc "Morning, mom! What's the problem?"

    scene mom car breakdown 8 with dissolve
    mom "The car won't start, and I'm already late for work!"
    mom "Now I have to call a cab and I'll be even more late!"
    mc "(She's a bit scary when she's angry, but not any less beautiful.)"
    mc "(I better not tell her that though, that would just be adding fuel to the flames.)"
    mc "I can take you to work."
    mom "Very funny [mc_name], you don't even have a car."
    mc "But I do!"

    scene mom car breakdown 9 with dissolve
    mom "Really? {w} And you'd take me?"
    mom "I don't want to waste your time but... {w} I'll take you up on that offer. I really need to get to work fast."
    mc "Sure, I'm happy to help!"

    scene mom car breakdown 10 with slowfade
    mc "It's not as luxurious as yours, but it's functional."
    mom "No it's... {w} Well..."
    mom "Exactly. It's functional."
    mc "....."
    mom "....."
    mom "Alright then, I'll hop right in, we have to hurry."
    mc "Right!"

    scene mom car breakdown 11 with dissolve
    mom "I didn't know you bought yourself a car!"
    mom "I'm proud of you, son!"
    mc "Yeah, thanks..."
    mc "(It's not even something I bought.)"
    mc "(If Thorne didn't give it to me I could only be offering my company on a bus right now...)"
    mc "(Damn, I need to get my shit together.)"
    mc "So, how's work?"

    scene mom car breakdown 12 with dissolve
    mom "It takes up so much of my time..."
    mom "The company is expanding and the people at the top want me right at the center of it."
    mom "I mean, it's nice that I have an important position at the company, but it's mostly boring things on the computer."
    mom "All my kids are home and I can't spend any time with them..."
    mc "(Position... Top, right, center...)"
    mom "Are you all right, [mc_name]?"
    mc "Yeah, sorry I was just thinking."
    mc "(She really works a lot, I guess she'd rather spend some time home.)"
    mc "(With Harding Enterprises, it's not like we need more money anyways...)"
    mc "Why don't you do some home office? You have a laptop, right?"
    mom "Hmmm... {w} That's actually not a bad idea!"
    mc "I can also help out with a few things at home until..."
    mc "Well, right now I have kind of a flexible job."
    mom "That's very sweet of you [mc_name], but the maid should be back soon to take care of the chores."
    mom "Oh, pull over right there please!"

    scene mom car breakdown 13 with slowfade
    mom "Thank you for the ride, [mc_name]!"
    mc "Anytime, mom."
    mom "I'll see what I can do about that home office thing."

    scene mom car breakdown 14 with dissolve
    mom "Thank you again, you really helped me out [mc_name]. {w} I owe you one!"
    "*kiss*"
    mom "Drive safe!"

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return






label isabel_4_carpickup_dialogue:

    if _in_replay:
        call setup_gallery
        scene isa pickup 6
        stop music fadeout 2.0
    else:
        play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
        scene isa pickup 1 with slowfade
        mc "...."
        mc "(Hmm, \"Building a Business for Dummies\"?)"
        mc "(Might just be where I need to start...)"
        mc "(Not that I'm a dummy, of course.)"

        scene isa pickup 2 with dissolve
        mc "(But my ass of a brother Logan is probably really ahead of me with the technicality of running a business.)"
        mc "(Hah, too bad you can't learn street smarts from your room, Logan!)"
        mc "(If I ever want to run Harding Enterprises though, I'll need some kind of a plan to show dad I'm not just a good-for-nothing like they think.)"
        pause 0.8
        play sound "audio/sfx/ringtone.ogg"
        pause 1.0
        mc "(Isabel is calling? At a time like this?)"

        scene isa pickup 3 with fade
        play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
        mc "Hello?"
        isa "[mc_name]..."
        isa "I'm sorry to ask you this but uhm..."
        mc "(Her voice sounds distressed.)"
        mc "Is there a problem?"
        isa "No, no... But..."
        isa "Can you pick me up and take me home?"
        mc "Sure, where are you?"
        isa "I'll text you the address."
        mc "Alright, on my way!"


        scene black with fade
        show text "{size=72}{color=#dc38bf}20 minutes later...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve


        scene isa pickup 4 with slowfade
        mc "(There she is!)"
        mc "(What is she doing out here in the middle of the night?)"

        scene isa pickup 5 with slowfade
        isa "Thanks for picking me up, [mc_name]!"
        mc "Yeah, don't mention it."
        mc "But why did I have to pick you up in the first place?"
        mc "Are you alright?"

        scene isa pickup 6 with dissolve
        isa "I was at my boyfriend's place..."
        isa "Or I guess, ex-boyfriend now..."
        mc "Oh?"
        mc "What happened?"
        isa "I.. {w} Not right now, [mc_name]."
        mc "Okay, okay."
    mc "Time to fire up the GPS to home-"

    scene isa pickup 7 with vpunch
    pause 1.0
    mc "Ah shit, I dropped my phone."
    mc "Damn, where the hell is it?"
    isa "Let me help!"

    scene isa pickup 8 with dissolve
    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    mc "I uhm..."
    isa "I'll find it in a second!"

    scene isa pickup 9 with fade
    mc "(She's getting dangerously close to-)"
    mc "(Oh man, her tits are all over my leg!)"

    scene isa pickup 10 with fade
    mc "(That ass is worth its weight in gold, that's for sure!)"
    isa "It really is tight!"
    mc "Yeah, I'm sure! {w} Wait, what?"
    isa "The space in here, it's hard to get to your phone, but give me some time, I'll get it!"
    mc "Oh, haha...{w} Right."
    mc "(Shit, I can't stop myself. I have to feel it a bit!)"

    scene isa pickup 11 with dissolve
    mc "Are you okay, sis?"
    isa "Yeah, a little more!"
    mc "(Wow, it's really firm and round! I can feel the tension of her jeans, struggling to held that magnificent ass inside them!)"
    mc "(She doesn't seem bothered with my hand there...)"
    mc "(And I'm sure anyone could have found the phone in there by now. Is she doing this on purpose?)"
    mc "(That must be it! Maybe I can take this further...)"


    menu:
        "Slide hand between legs":

            $ isabel_lust += 2

            scene isa pickup 12 with dissolve
            mc "(Oh damn, I'm really doing this!)"
            isa "....."
            mc "(She didn't say anything!)"

            scene isa pickup 13 with dissolve
            mc "(She must be loving this as much as I do right now, holy shit!)"
            mc "(I can feel the heat radiating form her crotch through her jeans!)"

            scene isa pickup 14 with dissolve
            mc "(Maybe I could start massaging it a little bit?)"
            mc "(I'm about to pop the biggest boner in history right now, she'll definitely notice my dick poking her tits...)"
            isa "Found it!"

            scene isa pickup 15 with fade
            isa "And don't you think you're going too far, [mc_name]?"
            isa "I get that you have urges but come on, I'm your sister..."
            mc "Yeah I uh... I don't know what got into me there, I'm sorry."
            isa "It's fine, just drive me home please."
            mc "(Shit, I fucked up!)"
            isa "Having your hand on my ass felt better. For now, anyways..."
            mc "(Or did I? What? She liked my hand on her ass afterall!)"
            isa "Start driving you dummy!"
            mc "Haha, of course!"
        "Leave hand on ass":


            $ isabel_lust += 1

            mc "(I better not risk having to register as a sex offender for the rest of my life...)"
            mc "(It's already risky as it is, I'm about to pop a huge boner..)"
            mc "(If me touching her ass might have gone somehow unnoticed, my dick poking her tits sure won't!)"
            isa "Found it!"

            scene isa pickup 15 with fade
            isa "And thanks for the '{i}support{/i}' from the back..."
            mc "And thank you for bending over backwards for finding my phone!"
            mc "(Smooth as shit, [mc_name]...)"
            mc "(Picking up cuties at the bar is nothing, but flirting with your sister is that much of a challenge?)"
            mc "(Well... I guess her being my sister makes it a tiny bit harder, yeah.)"
            isa "Start driving you dummy!"
            mc "Haha, of course!"


    scene black with fade
    show text "{size=72}{color=#dc38bf}Some time later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve


    scene isa pickup 16 with slowfade
    isa "Not your usual night I guess..."
    mc "Picking up hot chicks and bringing them home?"
    mc "Pretty usual to me!"
    isa "Wow, [mc_name], you're such a cool guy!"
    mc "Really?"
    isa "No..."

    scene isa pickup 17 with dissolve
    isa "But thank you for bringing me home."
    isa "{b}That{/b} was certainly cool of you to do."
    mc "You know you can count on Cool [mc_name]!"
    isa "I know..."
    isa "It's time for both of us to get some sleep."
    mc "(That warm smile she just gave me was worth the whole ride.)"
    mc "(And the ass! Let's not forget that magnificent ass!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label thorne_5_clubtextmessage_dialogue:

    scene nightclub intro 0 with slowfade
    play sound "audio/sfx/sms.ogg"
    mc "(A message from Thorne...)"
    mc "(He wants me to meet him in his office.)"
    mc "(Let's see what he wants now.)"

    scene home_basement__day with fade

    return






label eliana_1_meeting_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.5
    scene eliana breakin 2 with slowfade
    play sound "audio/sfx/doorbell.ogg"
    "*Ding-dong*"
    mc "(Hmm, someone's at the door.)"
    mc "(The girls are out, only Logan is at home. I doubt he will answer.)"
    mc "(Fine, I'll get it.)"

    scene eliana first 2 with slowfade
    mc "(I wonder who this might be...)"

    scene eliana first 4 portrait with dissolve:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.02
    pause
    mc "(Damn, what a cute redhead!)"
    mc "(What is she doing at the house though?)"

    scene eliana first 5 with dissolve
    e "[mc_name]?!"
    mc "Yes... Wait-"
    mc "Eliana?!"

    scene eliana first 6 with dissolve
    e "Oh my God, it's been so long!"
    mc "What the hell? I thought you were away on that student exchange program or whatever."
    mc "(It's Eliana!)"
    mc "(She's my childhood friend - my best friend in fact.)"
    mc "(Although we've never really talked about it or admitted it. It's not cool to have a girl as a best friend in high school...)"
    mc "(Our relationship was always like... {w} It didn't really matter if we didn't see each other for weeks or months.)"
    mc "(When we met again, we just continued where we left off.)"
    mc "(It's been a while since we last met.)"
    mc "(I left the city to go to college and last I heard she was out of town as well, doing a student exchange program in some remote town.)"
    e "I'm back already!"
    e "You should have told me you're back in town!"
    mc "I know, I know. {w} Come on, let's go inside."

    scene eliana first 7 with slowfade
    mc "So how was it at Nowhere-town?"
    e "Hey, it wasn't {i}that{/i} remote!"
    e "But compared to Midnight City..."
    e "It was a nice change of pace."
    mc "Did you make some friends?"

    scene eliana first 8 with dissolve
    e "Yeah, a few."
    if not lain_mod:
        e "I had a roommate as well and..."
        e "..."
        mc "And...?"
        e "Hmm, nothing."
    e "So what have you been up to lately?"
    e "I heard you failed coll-"
    mc "That - {w} Was unfortunate, yes."
    mc "But I'm back on track now. {w} Sort of."
    e "Oh?"
    mc "I've been getting some uh, private tutoring to help me catch up and be able to get my degree this time."

    scene eliana first 9 with dissolve
    e "Nice! Finally it seems like you're putting in some effort."
    mc "Yeah, thanks to my father's 'competition'."
    e "You dad's what? Tell me more!"
    mc "Alright, alright...{w} So it goes like this-"

    scene black with fade
    show text "{size=72}{color=#dc38bf}A few minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve


    scene eliana first 10 with Dissolve(1.0)
    mc "So that's about all that happened to me since coming back home."

    scene eliana first 11 with dissolve
    e "Wow..."
    e "You have a lot to do then, you have to pass Logan to win, right?"
    e "And this Halo thing... {w} Why do you help Thorne?"
    mc "I owe him. He got me out of jail, remember?"
    e "Yeah, so what? It's not like he can put you back..."
    mc "It was implied that he can. It's probably a bluff though."
    e "Just...{w} be careful, [mc_name]."
    e "And know that I'm here for you whenever you need me."
    mc "I know. Thank you."
    e "I have to go now, but let's keep in touch!"
    pause 0.8

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label tanya_1_nightmeeting_dialogue:

    stop music fadeout 2.5
    scene viktor pickup 1 with slowfade
    mc "(Thorne wasn't lying, the money was there when I arrived.)"
    mc "(Twenty thousand bucks...)"

    scene viktor pickup 2 with dissolve
    mc "(My chances at winning this thing just improved by a lot.)"
    mc "(Man, having all of Harding Enterprises to myself...)"
    mc "(That's \"fuck you money\" level.)"
    mc "(Maybe when I-)"
    scene viktor pickup 2 with hpunch
    pause 0.5

    play music "audio/music/menacingstalker.mp3" loop fadein 4.0
    scene viktor pickup 3 with dissolve
    mc "(Hmm...)"
    mc "(What was that noise?)"

    scene viktor pickup 4 with dissolve
    viktor "I need you to come with me."
    mc "You!"
    mc "What the fuck are you doing on my property?!"
    mc "I should call the cops!"

    scene viktor pickup 5 with dissolve
    viktor "Don't do anything stupid."
    viktor "By the way, do you also want to tell the police you're a thief?"

    scene viktor pickup 6 with dissolve
    mc "I don't know what you're talking about..."
    mc "You better get the fuck awa-"

    scene viktor pickup 5 with dissolve
    viktor "The boss sent me, she wants to meet you."
    viktor "This isn't optional."
    viktor "Get in the car."
    mc "(Fuck!)"

    scene viktor pickup 7 with slowfade
    mc "Why the hell does Tanya want to meet in the middle of the night?"
    viktor "The boss told me to bring you, so I bring you."
    viktor "Now shut up."
    mc "(Maybe she found out I got my hands on Halo and she wants a piece?)"
    mc "(She couldn't possibly know I had the real ones... Unless Thorne somehow leaked the info.)"
    mc "(But even then...)"
    mc "(Fuck, I better just wait and see where this goes...)"


    scene tanya meeting intro 1 with Fade(1.0, 1.5, 1.0)
    mc "Nice office you got here. Good to know you Russian people have interior design tastes."

    scene tanya meeting intro 2 with dissolve
    scene tanya meeting intro 2 with hpunch
    viktor "Stop looking and move, blyat!"

    scene tanya meeting intro 3 with dissolve
    mc "(This motherfucker...)"


    menu:
        "Threaten":

            $ morality -= 2
            $ viktor_threatened = True

            pause 0.2
            scene tanya meeting intro 4 with hpunch
            mc "Touch me one more time and I'll crush your bald fucking head."
            viktor "Mh..."
            viktor "Boss is waiting."
        "Let it go":


            $ morality += 2

            scene tanya meeting intro 5 with dissolve
            mc "(Meh, it's not worth playing tough right now.)"
            mc "(I don't know what they're up to. I'll just let this one slide.)"
            viktor "Boss is waiting."


    scene tanya meeting intro 6 with fade
    play sound "audio/sfx/door_open.ogg"
    pause 1.0

    scene tanya meeting intro 7 with Dissolve(1.0)
    tanya "Boy!"
    tanya "Long time no see!"

    scene tanya meeting 1 portrait with fade:
        subpixel True
        yalign 1.0
        pause 2.0
        linear 7.0 yalign 0.03
    pause
    tanya "Come on, take a seat."

    scene tanya meeting intro 8 with dissolve
    mc "Yeah, long time no see! I guess you really missed me, sending your dog after me in the middle of the night to, what, have a little chat?"
    mc "Why don't you tell me what this is all about?"

    scene tanya meeting intro 9 with dissolve
    tanya "That's what I'm trying to do. Now..."
    tanya "Sit. {w} The fuck. {w} Down. {w} Boy."

    scene tanya meeting 3 with dissolve
    tanya "Now let's make something very clear."
    tanya "You talk to me like that again, and Viktor will put a bullet in your pretty head."
    tanya "Understood?"

    scene tanya meeting 2 with dissolve
    mc "(Fuck, maybe I've overstepped my boundaries a bit here...)"
    mc "(Are these guys for real?)"
    mc "(I can tell that meathead would gladly do anything this woman tells him...)"
    pause 0.5

    scene tanya meeting 4 with hpunch
    pause 0.5
    tanya "I asked you a question, boy!"
    mc "Shit, alright!"
    mc "(I have to play along here... This bitch is giving me cold vibes...)"
    mc "Understood."

    scene tanya meeting 5 with dissolve
    tanya "Good."
    tanya "Now tell me..."
    tanya "Do you think it is a good idea to steal from me?"
    tanya "You know what I'm talking about, don't you?"
    mc "Stealing? I didn't steal any-"
    mc "Oh fuck!"
    tanya "Ah, looks like you finally caught up."

    scene tanya meeting 6 with dissolve
    tanya "The car you stole today belongs to us."
    mc "(Shit!)"
    mc "(I've never heard of someone who stole from the Russian mob and got away just fine...)"
    mc "(Did Thorne set me up? I'll kill that motherfucker!)"
    mc "(If I leave here in one piece, that is.)"
    tanya "Do you know what happens to those who steal from us?"

    scene tanya meeting 7 with dissolve
    mc "I think I got a pretty good idea."
    tanya "Hmph..."
    tanya "Tell me one reason then, why I shouldn't kill you?"
    mc "(There's only one thing I can try...)"

    scene tanya meeting 8 with dissolve
    mc "Is this a good enough reason?"
    tanya "Oh? Let me have a look..."

    scene tanya meeting 9 with fade
    tanya "Yes... This is just like..."
    tanya "Finally, I can go back..."

    scene tanya meeting 10 with fade:
        subpixel True
        align (0.5, 0.5)
        pause 2.0
        linear 4.0 zoom 1.03
    tanya "Ahahahahah~"
    tanya "Oh, little boy! You are very lucky today!"

    scene tanya meeting 11 with dissolve
    tanya "A pill for your life!"
    tanya "You got yourself a pretty good deal!"
    tanya "But you won't get off that easily..."
    tanya "I see you are competent."
    tanya "You work for me now!"
    mc "What?"
    tanya "That pesky lawyer..."
    tanya "I want you to report his every move to me from now on!"

    scene tanya meeting 12 with dissolve
    tanya "What do you say...{w} It's better than what your situation looked like 5 minutes ago, right? Ahahah~"
    mc "Ouch! {w} Okay, fine!"
    tanya "Let me warn you..."
    tanya "Do anything stupid, and I'll cut your balls off myself."

    scene tanya meeting 10 with dissolve
    tanya "Ahahah, this is such a nice day!"
    tanya "Go now... And not a word to the lawyer."
    tanya "We'll contact you. {w} Ahahah~"

    scene tanya meeting 13 with slowfade
    mc "(Fuck!)"
    mc "(This was a close call... They probably would have really iced me if I didn't have the second pill of Halo.)"
    mc "(She wants me to report on Thorne. Could he have set me up?)"
    mc "(Did he know whose car he sent me to steal? But why would he get me out of jail then, just to feed me to the Russians?)"
    mc "(I don't know, but now I have to act like nothing happened or Tanya will serve my balls on a silver platter...)"
    mc "(And judging by that maniac laugh, she wasn't kidding.)"
    mc "(Just what the fuck have I gotten myself into...)"

    play music "audio/music/soul.mp3" loop fadeout 3.0 fadein 2.0
    scene black with slowfade

    return






label eliana_2_talkplan_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    scene eliana breakin 2 with slowfade
    mc "(This situation requires some help.)"
    mc "(Maybe only in a form of a bit of talking with a friend, but Tanya wanting me to play double agent and the possibility of Thorne leading me to a trap is a bit unnerving.)"

    scene eliana breakin 1 with dissolve
    mc "(I'll text Eliana...)"
    mc "(Maybe if I can have a conversation about this with someone, that would help setting things straight in my head.)"
    mc "(Awesome, she'll be over soon.)"
    mc "(Reliable girl. Now I'll just wait.)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}Some time later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene eliana breakin 3 with slowfade
    mc "Thank you for coming on such a short notice."
    e "Oh, no worries. I wasn't doing much anyways."
    e "Is this your 'new' room?"
    mc "Ah, yes..."
    mc "It's a bit messy but- {w} Who am I kidding?"
    mc "It's a shithole."
    mc "Please, take a seat."
    e "...{w} Sure."

    scene eliana breakin 5 with fade
    e "So, what was that important thing you wanted to talk about?"
    mc "Alright... {w} So, you know how I told you about the Russians, Thorne, and the Halo I acquired?"
    mc "After giving one of the pills to Thorne, he had another assignment for me."
    mc "Stealing a car."
    e "Tell me you didn't do it..."
    mc "He paid twenty grand!"
    e "Ugh, [mc_name]..."
    mc "Anyways, turns it was the Russians' car."
    mc "Now of course Tanya sent her fucking lapdog after me..."
    mc "In the end, I managed to avoid uh...{w} well, probably being killed, by handing over the other pill."
    e "Jesus Christ, [mc_name]! What is wrong with you?!"
    mc "What? You think handing it over was a mistake?"
    e "No! Getting into that situation was a mistake in the first place! A big one!"
    mc "Fine, I know that now. It's not like I knew at the time."
    mc "Anyway, then Tanya asked me to work for her. Well, she basically just told me I work for her now. "
    mc "And she wants me to report on Thorne."

    scene eliana breakin 6 with dissolve
    mc "Now... if Thorne knew it was the Russians' car, then that fucker set me up."
    mc "But if I go to him to smash his face in, he will know that I met with Tanya."
    mc "And then Tanya will cut my ballsack loose. Personally."
    mc "But if Thorne didn't know, I'm basically betraying him if I report on him to Tanya."
    mc "I also doubt he's powerful enough to shut down the Russians if I decide to tell him about the meeting and what Tanya wants."
    mc "So I'm basically-"

    scene eliana breakin 7 with dissolve
    e "Fucked..."
    e "You thought this through, didn't you?"
    mc "I had some time to think about it, yeah."
    e "Who do you want to side with?"

    scene eliana breakin 5 with dissolve
    mc "Tanya seems like a cold blooded killer and a fuckin lunatic on top of that."
    mc "Thorne is a slimeball but seems like a genuine white collar criminal. On the other hand, if he set me up..."
    e "If both options are wrong, why don't you create a third option?"
    mc "..."
    mc "Wait... {w} That's genius!"
    mc "I've got a plan! Are you free tonight?"
    e "I-I guess. Why?"
    mc "Meet me tonight in the city, I'll text you the address!"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label eliana_4_lead_dialogue:

    stop music fadeout 2.0
    scene black with slowfade
    show text "{size=72}{color=#dc38bf}At dawn...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve


    play sound "audio/sfx/birds.ogg" loop fadein 1.0
    scene eliana lead 1 with slowfade
    mc "Are you sure this is it?"
    e "This is what the GPS shows, yeah."
    mc "How the hell did Thorne's guy find this place anyway?"
    e "In the e-mail he said the city has detected increased levels of chemicals in the sewage water in this area."
    e "He analyzed the pill and it was a match. Looks like somebody has been dumping that precious Halo of yours into the sewers."

    scene eliana lead 2 with dissolve
    mc "Fuck, why does it always have to be the sewers?"
    e "What do you mean?"
    mc "Nothing..."
    mc "Alright, let's get this over with."

    scene eliana lead 3 with dissolve
    mc "The sun is already rising. Thorne could get into his office anytime and he will figure out the location too."
    mc "We have to hurry."

    scene eliana lead 4 with dissolve
    e "{size=-5}Why don't I just find a normal guy who doesn't do crazy shit...{/size}"
    mc "Did you say something?"
    e "Nothing, I'm coming!"

    scene eliana lead 5 with fade
    mc "In there?"
    e "Sadly..."
    mc "Fuck..."

    stop sound fadeout 2.0
    scene eliana lead 6 with slowfade
    play music "audio/music/menacingstalker.mp3" loop fadein 2.5
    e "This is getting creepier by the minute."
    e "There's no way I'm climbing down that hellhole!"
    mc "Oh come on, you wanna wait here alone in the sewers instead?"
    mc "There might be rats..."
    e "[mc_name]!!"
    e "Fine...{w} Let's go."

    scene eliana lead 7 with Fade(1.0, 1.5, 1.0)
    mc "I swear to God if this door is locked..."

    scene eliana lead 8 with fade
    mc "Of course it fucking is!"
    mc "Now we came all the way here for nothing!"

    scene eliana lead 9 with dissolve
    mc "Wait..."
    mc "Did that thing just move?"
    e "I think it's looking at you..."
    fvoice "So you have found this place. Impressive."
    e "It has a speaker!"
    mc "Can it hear us?"
    fvoice "I can.{w} I assume you came here hoping to find...what exactly?"
    mc "For Halo. You know, the new miracle drug! Do you have it?"
    fvoice "Ahah, they usually just get rid of people who wander down here..."
    fvoice "You're lucky I'm here now."
    e "I don't like this, [mc_name]... {w} Let's get out of here."
    fvoice "You will get what you want. I'll make sure of that."
    fvoice "I'll be in touch."
    mc "Well, that went better than expected."
    mc "Let's get out of here now."
    e "That was it? Isn't it weird that it was this simple?"
    mc "The voice said she will be in touch. {w} It was a female voice, right?"
    e "Let's just leave... I need a shower after this."

    scene black with slowfade

    scene eliana lead 10 with Dissolve(1.0):
        subpixel True
        align (0.5, 0.5)
        pause 2.0
        linear 6.0 zoom 1.08
    pause 1.0
    "Mahahah~"

    play music "audio/music/soul.mp3" loop fadeout 3.5 fadein 3.0
    scene black with slowfade
    scene home_livingroom__day with Dissolve(1.0)

    return






label mom_8_morningjerkoff_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
        scene mom morning jerkoff intro 6
    else:
        scene black
        show home_basement__night
        pause 0.3
        play sound "audio/sfx/ringtone.ogg"
        pause 0.5
        scene mom morning jerkoff intro 1 with Fade(0.5, 0.5, 1.0)
        mc "Yo Pete, whatup you dirty fucker!"
        pete "Sup homie!"
        pete "I'm visiting Midnight City for a couple of days!"
        mc "No way!"
        pete "Yeeah man! You know what time it is!"
        mc "Let's get fucked up! I'll meet you at the club!"


        scene black with Fade(1.0, 0.5, 0.0)
        show text "{size=72}{color=#dc38bf}Later that night...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve


        scene mom morning jerkoff intro 2 with Fade(0.0, 0.5, 1.0)
        mc "(Oh fuck...)"
        mc "(That was probably a bit too much to drink.)"

        scene mom morning jerkoff intro 3 with dissolve
        mc "(But I don't give a fuck!)"
        mc "(My life is stressful... I deserve a night out...)"
        mc "(Fuck... the room is spinning...)"
        mc "(I need some sleep.)"

        scene mom morning jerkoff intro 4 with fade
        mc "(I don't think I can get down to the basement so..)"

        scene mom morning jerkoff intro 5 with dissolve
        mc "(The fucken sofa will have to do!)"
        mc "(Argh... I'm out...)"

        scene black with slowfade
        show text "{size=72}{color=#dc38bf}The next morning...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve

        scene mom morning jerkoff intro 6 with Fade(0.0, 0.5, 1.0)
    mom "(Hm, I didn't sleep well last night...)"
    mom "(I think one of th-)"

    scene mom morning jerkoff intro 7 with dissolve
    mom "(Oh!)"

    scene mom morning jerkoff intro 8 with dissolve
    mom "(What's [mc_name] doing in the living room?)"
    mom "(Oh I remember, he did go out last night...)"
    mc "*Heavy snoring*"
    mom "(He's out cold...)"
    mom "(He's gonna have a serious headache when he wakes up.)"
    mom "(Oh... Wait...{w} Is that...?)"

    scene mom morning jerkoff 1 with fade
    mom "(Oh God!)"
    mom "(There it is again...)"

    scene mom morning jerkoff 2 with dissolve
    mom "(His morning wood...)"
    mom "(Last time I...)"

    scene mom morning jerkoff 3 with dissolve
    mom "(Oh, that's too embarrassing to think about...)"
    mom "(Cumming with my son's penis in my mouth...)"
    mom "(It was an accident of course, but only the 'in my mouth' part...)"
    mom "(I'm never doing that again.)"

    scene mom morning jerkoff 4 with dissolve
    mom "........{w}................"
    mom "(It's so big.)"
    mom "(How big is it exactly?)"
    mom "(Maybe I should take a look. A little peek doesn't hurt anyone, right?)"

    scene mom morning jerkoff 5 with dissolve
    mom "[mc_name], wake up!"
    mc "..............."
    mc "*Snoring noises*"
    mom "(He's sleeping like a rock.)"
    mom "(....)"
    mom "(Fine, just a quick peek, then I'll have my morning coffee and pretend nothing ever happened. Yeah.)"

    scene mom morning jerkoff 6 with dissolve
    mom "(Let's get this down a little bit...)"
    mom "(Carefully... I can't afford anyone to see this.)"
    mom "(I might be able to talk my way out of this with [mc_name], but anyone else...)"
    mom "(Okay, I shouldn't hesitate.)"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene mom morning jerkoff 7 with fade
    mom "(Why am I trembling like a little girl?)"
    mom "(Like I've never seen a co-)"

    scene mom morning jerkoff 8 with Dissolve(0.3)
    scene mom morning jerkoff 8 with vpunch
    mom "(Holy!)"
    mom "(I guess I've never seen a cock {i}that big{/i} before...)"
    mom "(I just...)"

    scene mom morning jerkoff 9 with dissolve
    pause 0.8
    mom "(It feels so good in my hand.)"
    mom "(It's as hard as a metal rod! It looks like a perfect fit in my...)"
    mom "(Oh Joyce, stop!)"
    mom "(This probably can't be too comfortable.)"
    mom "(I should release this tension... Yeah... {w} Ah...{w} Who am I kidding with this...?)"
    mom "(I'll do it anyway. Because I want to do it. Yes.)"
    mom "(Oh God help me, I'm a sick mother...)"

    scene MomMorningJerkoff1 with dissolve
    pause
    mom "(Slowly...)"
    mom "(With a firm grip, but not too tight.)"
    mom "(It looks so beautiful! It's a great cock.)"
    mom "(Ah...)"
    mom "(I can't believe I'm actually doing this.)"
    mom "(Jerking off my son in the living room. And he's asleep! I'm a terrible mother...)"
    mom "(But I can't stop. I want this... {w} I came with it in my mouth, now I wanna see it cum for me too.)"

    scene MomMorningJerkoff2 with dissolve
    pause
    mom "(But I can't go too fast or he'll wake up...)"
    mom "(Slow and steady wins the race.)"
    mom "(Oh [mc_name], I hope you'll forgive me for this.)"
    mom "(I'll try to make it up to you somehow...)"
    mom "(Oh!{w} I can feel it tightening up.)"
    mc "Mhmm..."
    pause
    mom "(Is he about to-)"

    scene mom morning jerkoff 10 with vpunch
    pause 0.3

    scene mom morning jerkoff 10 with vpunch
    pause 0.5
    mom "(Oh!!)"

    scene mom morning jerkoff 11 with dissolve
    pause 1.0
    mom "(He came!)"
    mom "(He came all over my hand...)"
    mom "(This is making me so wet!)"
    mom "(His sperm is so hot. I wish I could tas-)"
    mom "(Stop!)"

    scene mom morning jerkoff 12 with dissolve
    mom "(I'm so lucky he didn't wake up!)"
    mom "(I have to clean this up fast!)"
    mom "(Nobody can know about this!)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label isabel_8_relationshiptalk_dialogue:

    scene isa talk basement 1 with slowfade
    mc "(So the plan is to be able to distribute the Halo supply.)"
    mc "(Or at least store it, for now.)"
    mc "(I'll probably need a warehouse for that. The one Thorne showed me is not gonna be suitable, obviously.)"
    mc "(I'll have to work on this part.)"
    mc "(Then I have to go to the dropsite, and-)"

    play sound "audio/sfx/knock.ogg"
    pause 0.2
    "*Knock knock*"
    play sound "audio/sfx/door_open.ogg"
    pause 0.2

    scene isa talk basement 2 with dissolve
    isa "Hey, can we talk for a minute?"
    mc "Uh, sure. What's up?"

    scene isa talk basement 3 with dissolve
    isa "It's about us..."
    isa "I've been thinking and..."
    mc "(These situations usually don't end well...)"
    isa "I know it's not just on any one of us."

    scene isa talk basement 4 with dissolve
    isa "And I don't want to blame either of us."
    isa "What happened, happened. It can't be changed."
    isa "But that doesn't change the fact that things did happen between us."
    isa "Things that shouldn't have..."
    isa "But I...{w} I just can't help but feel that it wasn't wrong."
    isa "Was it?"

    scene isa talk basement 5 with dissolve
    mc "It wasn't. I mean, no one forced anyone to do anything."
    mc "There is attraction and sometimes, these things happen."
    mc "Now that you brought it up, I don't want anything to ruin our good relationship, so we should decide on what to do next."
    mc "I don't think we should feel bad about what happened."

    scene isa talk basement 6 with dissolve
    isa "Right?"
    isa "I feel the same way!"
    isa "It's just that ever since you came back you're so caring."

    scene isa talk basement 7 with dissolve
    isa "You're there when I need you and I...{w} I don't know. I guess I missed intimacy with someone who truly cares for me."
    isa "So you're not against our...{w} thing?"
    mc "Not at all."

    scene isa talk basement 8 with Dissolve(0.3)
    scene isa talk basement 8 with hpunch
    mc "Whoa!"
    isa "I'm so glad!"
    isa "I don't wanna ruin our relationship over something like this."

    scene isa talk basement 9 with dissolve
    mc "You don't have to worry about that."
    isa "I know... How about we set up some boundaries?"
    mc "What do you mean?"
    isa "I mean that we could continue...{w} And fool around a little bit sometimes. {w} But won't go over a certain point."
    isa "You know what I mean."

    scene isa talk basement 10 with dissolve
    mc "Uhm, yeah. Totally."
    isa "[mc_name]!"
    mc "Haha, sure. I'm fine with that."
    isa "I'm so happy I could talk to you about this so openly, without the awkwardness."

    scene isa talk basement 11 with dissolve
    isa "I'm happy we both came back home and that I can have you in my life again."
    mc "I'm happy I have you, too."
    pause 0.3

    scene black with slowfade

    return






label jane_13_textmessage_dialogue:

    scene nightclub intro 0 with slowfade
    play sound "audio/sfx/sms.ogg"
    mc "(It says I've got a message from... {w} Ms Jane!)"
    mc "(She wants to see me in her office this afternoon.)"
    mc "(She wasn't too happy the last time she saw me, so I wonder what this is about.)"

    scene home_basement__day with fade

    return






label eliana_5_pooltalk_dialogue:


    scene eliana pool talk 1 with slowfade
    mc "(Last time I talked to Eliana was when we went to the sewers in search of the Halo and found that weird room with the door.)"
    mc "(She was freaked out by what happened there, I could tell.)"
    mc "(I guess I would have been too if I didn't feel I'm getting so close to victory here.)"
    mc "(After we left the sewers I received a message from an anonymous number. The message was just numbers.)"
    mc "(I looked them up. They are coordinates. I'm pretty sure when I get there I'll get the first batch of this Halo thing.)"
    mc "(I still wonder who I was talking to in those sewers...)"
    mc "(Alright, I messaged Eliana to come over. We actually have some things to talk about.)"
    mc "(In the meantime, I think I'll get some air.)"

    scene eliana pool talk 2 with slowfade
    mc "(Things have moved quicker than I anticipated. Now I need a place to store the drugs once I get them.)"
    mc "(And of course I need to find a way to transport them safely.)"
    mc "(Then selling it. All this while avoiding any unwanted attention. If I can do this, I'll be swimming in dough!)"
    mc "(With that, I can do whatever legit business I want. With the backing of all that drug money, I can easily beat Logan in this stupid game.)"
    mc "(Then I'll get father's respect.{w} And of course, I'll be the new CEO.)"

    scene eliana pool talk 3 with dissolve
    e "Hey, I was looking for you!"

    scene eliana pool talk 4 with dissolve
    e "You didn't tell me you were going to be out here by the pool."
    e "I would have brought my swimsuit."

    scene eliana pool talk 6 with dissolve
    mc "Hey! {w} Yeah, sorry. I didn't want to have a pool party, just came out here to get some air."
    mc "Being locked up in a basement gets old..."

    scene eliana pool talk 5 with dissolve
    e "I bet."
    e "Uhm...{w} Seems like you've been working out lately?"
    mc "Not that much to be honest. I haven't had a good workout since I came back. Why?"
    e "I mean it's just uhm...{w} You know, I haven't seen you shirtless in a while, that's all."
    mc "Oh, that. I can put on something if it's bothering y-"
    e "No, no. I like it."
    e "I mean, it's fine."
    e "Wanna get inside? You said you wanted to talk about something important."
    mc "Yes! {w} Back to the basement..."

    scene eliana pool talk 7 with fade
    mc "(I told Eliana what I've been thinking about, and now we can discuss my options.)"
    mc "(Two heads are better than one afterall.)"
    mc "(She's also the only person I fully trust.)"
    e "Okay, so miraculously, the biggest problem has been dealt with, according to you."
    e "That's getting the product."
    e "I'm still not sure about that weird thing that happened down in the sewers."
    e "It was too easy.{w} Whatever you do, please, be careful!"

    scene eliana pool talk 8 with dissolve
    mc "Oh you know me, my middle name is careful!"
    e "That was really lame..."
    mc "Don't worry, I'll be fine!"
    e "Famous last words?"
    mc "Dude!"
    e "Haha, just kidding of course. But seriously."
    mc "Fine, fine. I'll be cautious. Really."

    scene eliana pool talk 7 with dissolve
    e "The ideal thing for transporting would be..."
    e "Well, something that's used for that anyway. So a truck."
    e "Don't try to put everything into your shi- uhm...{w} car."
    mc "I know my car is shitty. But where the hell do I get a truck?"
    e "You're probably going to have to buy one I guess?"
    mc "Buy one? It costs-"
    mc "Wait a second...{w} My aunt has a construction company. I'm sure she has a truck or two!"
    mc "She dropped by recently anyway, I could just borrow one!"

    scene eliana pool talk 7 with dissolve
    e "Hmm... Yeah, that works for a while."
    e "Just come up with an excuse about for why you need it, other than transporting drugs."
    mc "What's the problem with transporting drugs? I'm sure she'll understand."
    e "You're an ass!"

    scene eliana pool talk 9 with dissolve
    e "Ahahah~"
    mc "Thanks for helping me out with this."
    mc "I don't know who else I could talk about, well, everything."

    scene eliana pool talk 10 with dissolve
    e "Oh [mc_name]..."
    e "I'm always here for y-"
    play sound "audio/sfx/ringtone.ogg"
    "*Ring Ring*"

    scene eliana pool talk 11 with dissolve
    mc "Oh, who's calling me now?"
    mc "I'm even surprised I got reception down here..."

    scene eliana pool talk 12 with dissolve
    mc "Melissa?"
    mc "How did she get my number...?"

    scene eliana pool talk 13 with dissolve
    mc "(I wonder what she wants...)"
    mc "Anyways, I probably shouldn't take it."

    scene eliana pool talk 14 with dissolve
    e "Are you talking to her again?"
    mc "We ran into each other a couple of times since I came back."
    e "After all the things she did to you?!"

    scene eliana pool talk 15 with dissolve
    mc "Wha-"
    e "I think I saw enough of what happened last time."
    e "I don't want to watch that slut drag you down again."
    mc "But-"
    e "I... I remembered I need to do something... I'll find my way out."


    scene eliana pool talk 16 with fade
    mc "(Ah for fucks sake...)"
    mc "(I forgot she hates Melissa. Or rather, I thought she forgot about those things already.)"
    mc "(Melissa and I have history. She was my girlfriend before I left.)"
    mc "(Back then I loved her, but I was probably blinded by her cocksucking skills and her pussy in my face.)"
    mc "(But how could you fault a man for that?)"
    mc "(Anyways, in hindsight I can see she's fuckin coo coo bananas batshit crazy. Eliana was telling me that the whole time.)"
    mc "(And when shit hit the fan, she was the shoulder for me to cry on. No wonder she doesn't want to see me talking to her again.)"
    mc "(The tension between them is something I have to deal with sooner or later.)"
    mc "(But for now, I know what to do. I need to get a truck from my aunt.)"
    mc "(We'll see how charming I can be, I guess...)"

    scene black with slowfade
    return






label natsuko_1_nightkitchen_dialogue:

    stop music fadeout 3.0

    if _in_replay:
        call setup_gallery
        scene natsuko night kitchen intro 1
    else:
        scene natsuko night kitchen intro 1 with slowfade
    mc "(Ugh...)"
    mc "(It's the middle of the night.)"
    mc "(I don't usually just wake up after a long day like this.)"
    mc "(Oh well, I'll get myself a glass of water then.)"

    scene natsuko night kitchen intro 2 with fade
    mc "(Hopefully I can get back to sleep soon.)"
    mc "(I have a competition to win. And an idiot brother to beat.)"
    mc "(I think I'm getting close with this new idea and the Halo.)"

    scene natsuko night kitchen intro 3 with dissolve
    mc "(And of course, I need to satisfy my growing appetite for women.)"
    mc "(I had always been a womanizer, so to speak... Hehe. {w} But I feel like I'm getting more and more engulfed in hunting them.)"
    mc "(Even here in the house...{w} Now that I think about it...)"
    mc "(Isn't it weird that my family turns me on?)"
    nat "Konbanwa."

    scene natsuko night kitchen intro 4 with vpunch
    mc "What?!"
    mc "Holy fuck!"
    mc "What the hell are you doing here?"
    nat "I came to talk to you."

    play music "audio/music/red.mp3" loop fadein 2.0
    scene natsuko night kitchen 1 with dissolve
    mc "You could have just texted, you know, instead of breaking into my house."
    nat "The door was open."
    mc "What?"

    scene natsuko night kitchen 3 with dissolve
    nat "I came to talk about your mission, [mc_name]."
    mc "Mission?"
    nat "You are on the right track. But they keep distracting you."
    nat "They want you running around in circles."
    mc "(Here we go with the deranged rambling again...)"
    nat "I know you've made contact with her. Be careful."
    nat "I'm not quite sure about her yet. She's probably watching right now. She's probably watching your every move."
    mc "What the hell are you talking about?{w} Tanya?"
    mc "Is she spying on me?"
    nat "No.{w} The thing on the other side of the intercom."
    mc "Wait, how do you know about that?"

    scene natsuko night kitchen 2 with dissolve
    mc "And 'thing'? It's called a person, Nat."
    mc "(Why am I talking to someone who's crouching on the kitchen counter after breaking into my house in the middle of the night anyway?)"
    nat "Just be careful with her, for now."
    nat "I need you to focus, [mc_name]."
    mc "Oh, I think I liked this part the last time we met!"
    nat "I don't have much time here. Do you want a visual aid or a physical? Choose!"


    menu:
        "Footjob":
            mc "Let's go with the physical! I wasn't disappointed last time, so-"

            scene black with fade
            scene NatsukoNightFootjob1 with dissolve
            pause
            mc "Oh shit!"
            nat "Stay still so I can work it properly."
            nat "It's not too easy with you. You're big."
            mc "(Oh wow, I wasn't expecting this!)"
            if not lain_mod:
                mc "(It's definitely not her first rodeo. Her toes are wrapping around my cock skillfully and efficiently.)"
            else:
                mc "(Her toes are wrapping around my cock skillfully and efficiently.)"
            mc "(She's working on my cock with intent to milk it as fast as possible.)"
            mc "(It's not about passion or desire, it's technique on a high level, designed to make cocks burst a fat load fast!)"
            mc "(And it's my turn for that I guess...)"

            scene NatsukoNightFootjob2 with dissolve
            pause
            mc "(She's quietly stroking my cock with her small feet.)"
            mc "(Her dark red nail polish and the contrast between my cock and her fair skin makes it much more visually exciting.)"
            nat "I'll let you cum on my foot this time."
            nat "But you have to be quick. Give me your sperm now. Empty your load over my little foot!"
            mc "(Oh I didn't expect dirty talk, the sensation was hard to hold back against as it was.)"
            nat "Cum on my toes, [mc_name]!"
            mc "Ah fuck! I'm cumming!"
            pause

            scene natsuko night kitchen footjob cum 1 with hpunch
        "Pussy Display":


            mc "Despite you being weird, I have to say you're hot as hell!"
            mc "I'll go with the visuals, hehe."

            scene natsuko night kitchen pussy 1 with dissolve
            nat "I hope this will be satisfactory for you."
            mc "Oh, no panties?! Keep that habit. I love that!"

            scene natsuko night kitchen pussy 2 with dissolve
            pause
            nat "I don't like panties."
            nat "But I'm doing this so you can focus. Clear your head, [mc_name]."
            mc "You want me to clear my head like-"
            nat "Milk your manhood for me!"

            scene natsuko night kitchen pussy 3 with dissolve
            pause
            mc "(Oh shit, alright!)"
            mc "My 'manhood' is ready."
            mc "I hope nobody else wakes up in the middle of the night."

            scene NatsukoNightJerkoff1 with dissolve
            pause
            mc "I don't think I could explain this."
            nat "You have a strong manhood..."
            nat "I touched it last time."
            mc "Yes, I remember..."
            mc "(Fuck she's weird.)"
            mc "(Weird and hot and crazy, and she's got an awesome pussy!)"
            mc "(Her breathing is getting faster. Is she enjoying this?)"
            mc "(I can see her eyes are fixed on my cock.)"
            mc "(Hmm, she probably isn't really into me exactly, but she's probably into cocks.)"
            nat "Give me your seed, [mc_name]. Look at my body when you cum!"
            mc "(Oh yeah, her gorgeous little body... I'll ravage it one day...)"
            nat "Cum for me..."
            mc "Ah fuck, I'm cumming!"
            pause

            scene natsuko night kitchen jerkoff cum 1 with hpunch
            mc "Ahh!!"
            scene natsuko night kitchen jerkoff cum 1 with hpunch
            mc "Yeah!"

            scene natsuko night kitchen jerkoff cum 2 with dissolve


    nat "Good. Now that it's done, you can stay focused again."
    nat "Keep going [mc_name]. Complete the task."
    nat "I have to go."

    $ renpy.end_replay()

    mc "What, you always leave so abruptly after I-"

    scene natsuko night kitchen gone 1 with fade
    mc "-cum..."
    mc "(Fuck. And now she said a whole lot of other lunatic shit....)"
    mc "(The voice? How the hell does she know I was down there with Eliana.)"
    mc "(Hmm... Eliana was kind of nervous about the mysterious female voice as well.)"
    mc "(Now that I think about it, it is suspicious as fuck. And she's just giving me what I want?)"
    mc "(Why didn't I doubt this before...)"
    mc "(Shit, now I have a headache. I better go back to bed...)"

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 4.0 fadein 5.0

    return






label lain_mod_laptop_jerkoff:

    scene mc laptop 2 with slowfade
    mc "(Well well well, it's time for some me time!)"
    mc "(Now that everyone is sleeping I won't be disturbed and I can get some sweet relief.)"
    mc "(Let's see what's new on Cornhub!)"

    scene home laptop jerkoff 2 with fade
    mc "(Same old boring stuff... I wish they were making some more innovative stuff from time to time...)"


    if temp_1 == 1:

        scene home laptop jerkoff mom 1 with fade
        mom "Hey [mc_name], have you-"
        pause
        mc "Shit!" with hpunch

        scene home laptop jerkoff mom 2 with dissolve
        mom "Oh my god!"
        mom "I uhm, sorry [mc_name], keep going!"
        mom "I mean, after I leave of course... I-"
        mc "Mom!"
        mom "Yes, yes, I'm leaving, sorry!"


    if temp_1 == 2:

        scene home laptop jerkoff isa 1 with fade
        isa "Sorry for coming in such a late-"
        pause
        isa "Oh wow!" with hpunch

        scene home laptop jerkoff isa 2 with dissolve
        mc "Excuse me?!"
        isa "I just wasn't expecting... That!"
        mc "I wasn't expecting you either... Maybe knock next time?"
        isa "Right, sorry!"
        isa "I'll be leaving now..."


    if temp_1 == 3:

        scene home laptop jerkoff ruby 1 with fade
        ruby "Hey [mc_name], can you lend me some-"
        pause
        ruby "Eww, what the fuck!" with hpunch
        mc "I think I could say the same!"
        mc "Why don't you fucking knock, sis?!"

        scene home laptop jerkoff ruby 2 with dissolve
        ruby "I wasn't expecting this, maybe you should lock your door before doing things to your big-"
        ruby "Shit!"
        mc "If you haven't noticed, I'm living in a fucking basement!"
        mc "There's no lock on the door!"
        ruby "Fine! I'm leaving!"
        mc "Finally!"


    pause 1.0
    scene home laptop jerkoff 2 with dissolve
    mc "(Well... That killed my vibe...)"

    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
