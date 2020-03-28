label mom_2_sleepingpillsfood_dialogue:

    play music "audio/music/funnysneaky.mp3" loop fadeout 2.0 fadein 2.0
    mc "(Yeah, this is it!)"
    mc "(Now's a good time to use the pills.)"

    scene sleeping pill dinner 1 with dissolve
    mc "Hey mom!"
    mom "Oh hi [mc_name], dinner is ready soon."
    mc "Awesome!"
    mc "Why don't you let me help with setting the table?"
    mom "Trying to get on my good side, huh?"
    mc "(Well, that's not entirely untrue.)"
    mc "Just trying to be a good son."
    mom "Well, thank you for the help then."

    scene sleeping pill dinner 2 with dissolve
    mc "(I'll just disassemble the capsule and dissolve the contents in the water.)"
    mc "(Should work like a charm.)"
    mc "(Was thinking about putting in a beer and offering it to him directly, but that's a stupid idea.)"
    mc "(If he was to get suspicious, he'd definitely know it was me.)"
    mc "(This way nobody will suspect anything.)"

    scene sleeping pill dinner 3 with dissolve
    mc "(Now I just need to wait until it's night then sneak to their room.)"
    mc "(Hehe, I'm a cunning motherfucker!)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with fade

    return






label mom_3_isabel_1_homedrinking_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    if mom_level == 3 and isabel_level == 1:
        scene home drinking 1 with fade
        isa "Yeah, most of them are total jerks."
        mom "Most of them?"
        isa "Really? Even dad?"
        mom "He's the biggest one!"

        scene home drinking 2 with dissolve
        isa "Oh Mom! Hahah!"
        isa "Getting tipsy from the wine to say things like that?"
        mom "It's fine, dear, haha!"

        scene home drinking 3 with dissolve
        isa "What do you think of [mc_name]'s return?"
        mom "I was disappointed at first..."
        mom "But then I realized that I can see my boy again, so I'm glad."
        mom "And I think it's probably my fault that he ended up away from home and failed."
        isa "Well from what I've heard he had an interesting life over there."

        scene home drinking 4 with dissolve
        mom "Oh? What did you hear?"
        mom "Let me hear those juicy details! You know I love a good gossip!"

        scene home drinking 5 with dissolve
        isa "I heard that our little [mc_name] was banging chicks left and right."
        isa "And the real reason that he failed was because he nailed a professor's daughter!"
        mom "What?! Oh my god!"

        scene home drinking 6 with dissolve
        isa "Yeah, that's pretty shitty."
        isa "But to be honest he should have thought of that before putting... his thing into every hole!"
        isa "I get that he's a handsome guy with a big mouth and those cheap girls really like that but-"

        scene home drinking 7 with dissolve
        mc "Did I hear someone talk about cheap girls?"
        mom "Speak of the devil..."
        mc "What, you're having a little private booze party and didn't even invite me?"
        isa "That's why it's private, little brother!"

        scene home drinking 8 with dissolve
        mc "Private or not, no party is good without papa [mc_name]'s special vodka!"
        mc "I'm bringing some merchandise to the table so, can I join?"
        isa "What do you say mom, should we let him?"
        mom "I'd say let's give it a shot."

        scene home drinking 9 with dissolve
        mc "Speaking of shots, time for the first round!"
        mc "Cheers!"

        scene home drinking 10 with dissolve
        mc "*Gulp*"

        scene home drinking 11 with dissolve
        mc "Damn!"
        mc "You don't mess around!"
        isa "You got a big mouth little brother, but can you handle two women of this caliber?"
        mc "I'd be happy to try, sis!"


        scene black with fade
        show text "{size=72}{color=#dc38bf}Some time later...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve


        scene home drinking 11 with fade
        mom "Isabel.. I don't think I can take another one..."
        isa "Right..."
        isa "Fine, [mc_name]. You win. Not that it's much of a win though is it?"
        mc "I'll take what I can get."
        mom "I think it's time for bed for me..."
        mom "Ah, damn you [mc_name]! The headache I'll have tomorrow..."
        isa "I think I-"
        isa "I think I have a little more in me. Wanna keep going [mc_name]?"
    else:

        scene home drinking 5 with fade
        mom "Don't you think we are doing this a bit too often?"
        isa "Not at all!"
        isa "We deserve to relax! It just so happens to be that we find the best way to relax is with a bottle of fine wine!"

        scene home drinking 8 with fade
        mc "Did someone say booze?"
        mom "Oh, not again, [mc_name]!"
        isa "I was so hungover after last time!"
        mc "Oh come on, we deserve a little fun!"

        scene home drinking 9 with fade
        isa "...{w} Maybe one shot."
        mom "And that's it!"
        mc "Yeah, just one and that's all!"

        scene black with fade
        show text "{size=72}{color=#dc38bf}1 hour later...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve

        scene home drinking 11 with dissolve
        mom "Isabel.. I don't think I can take one more..."
        isa "Right..."
        isa "We got a little carried away..."
        mom "I think it's time for bed for me..."
        mom "Ah, damn you [mc_name]! The headache I'll have tomorrow...{w} Again!"
        isa "I might take that bottle with me..."

    return






label mom_3_homedrinkingmom_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
        scene home drinking 11
    mc "Let me at least walk you to your room, Mom."
    mom "Alright, thanks."

    scene home drinking mom 2 with fade
    mom "Okay, now turn around, I'll change into my sleepwear."
    mc "Uhm, sure thing mom."

    scene home drinking mom 3 with dissolve
    mom "I really enjoyed our time today."
    mc "Yeah, me too."
    mc "We won't be so happy about it tomorrow when the hangover hits, though!"

    scene black with dissolve
    mom "Alright, you can turn back now."

    scene home drinking mom 4 with dissolve
    mc "Mom, I-"
    mom "Shhh..."
    mom "Let me show you something..."

    scene home drinking mom 6 with dissolve
    mc "!!"
    mom "Mhmm~"

    scene home drinking mom 7 with dissolve
    mom "Mhmmmm..."
    mc "(What the hell?!)"
    mc "(Was there something in the booze?)"

    scene home drinking mom 8 with dissolve
    mc "(Mom is kissing me!)"
    mc "(And her lips are so big and soft, pushing against mine...)"
    mc "(I feel like-)"

    scene home drinking mom 5 with dissolve
    mom "Now [mc_name]..."
    mc "(Oh, that was over as fast as it began.)"
    mom "This will be our little secret."
    mom "Promise me."
    mc "I promise."
    mc "But I-"
    mom "Sssh..."
    mom "Let's both go to sleep now."
    mom "Good night, [mc_name]!"

    $ renpy.end_replay()

    scene black with slowfade
    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0

    return






label isabel_1_homedrinkingisabel_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
        scene home drinking isa 6
    else:
        scene home drinking isa 1 with fade
        mc "Okay, let's get you back to your room..."
        isa "I'm fine!"
        mc "Sure, sure..."

        scene home drinking isa 2 with fade
        isa "Are you really unphased by all this booze?"
        mc "Practice makes perfect, I guess."

        scene home drinking isa 3 with dissolve
        isa "Damn, I wonder just what kind of life you led in these past 2 years little brother."
        mc "You probably don't wanna know."
        mc "(This might be a good time to ask more personal questions from her.)"
        mc "So, what's up with your boyfriend?"

        scene home drinking isa 4 with dissolve
        isa "He's a dick!"
        isa "Like all of you guys are..."
        mc "I might take offense here!"

        scene home drinking isa 5 with dissolve
        mc "You really are wasted aren't you?"
        isa "Shut it..."
        mc "So why is he a dick? What did he do to you?"
        isa "You know what [mc_name]? I think this booze is a better conversation partner than you are right now."
        isa "So I might as well..."
        mc "(Even now she won't spill the beans...)"
        mc "(It must be more serious than I thought. I have to get to the bottom of this.)"
        mc "(Not today though. Even if I don't show it, I'm drunk as fuck!)"

        scene home drinking isa 6 with dissolve
    isa "*Gulp-gulp*"
    mc "Whoa, easy there!"
    mc "Let me have that..."

    scene home drinking isa 7 with dissolve
    isa "I think I..."
    isa "I'm feeling a little lightheaded..."

    scene home drinking isa 8 with dissolve
    isa "Uhh..."
    isa "[mc_name]... Be a good brother and turn the lights off, will you?"
    mc "Sure."

    scene home drinking isa 9 with dissolve
    isa "Ah.. Much better."
    mc "So I guess it's time for me to leave."
    isa "No!"

    scene home drinking isa 10 with dissolve
    isa "Please don't go yet..."
    isa "Help me get ready for bed..."
    mc "Should I brush your hair or..."
    isa "Just help me get out of my pants!"
    mc "Just what I wanna hear from a hot girl!"

    scene home drinking isa 11 with dissolve
    isa "Hah... very funny."
    isa "You do know I'm your sister, right?"
    mc "Right, right, I was just joking."

    scene home drinking isa 12 with dissolve
    isa "Much better now... thanks!"
    mc "Okay, now I'll get to bed myself."

    scene home drinking isa 13 with dissolve
    isa "Why don't you sleep here with me tonight?"
    isa "Yeah. I want you to. Please?"
    mc "When you say it like that..."
    mc "(Damn that body is hot...)"

    scene home drinking isa 14 with dissolve
    mc "Hey Isa, do you mind if I-"
    mc "Isabel?"
    isa ".........."

    scene home drinking isa 15 with dissolve
    mc "(That's great, she's already asleep...)"
    if not lain_mod:
        mc "(Looks like it doesn't really matter if I'm here or not.)"

    scene home drinking isa 16 with dissolve
    mc "(Jesus... her ass is amazing!)"
    mc "(If I wasn't so sleepy from all this drinking I might even try to grope it a little bit.)"
    mc "(Shit, I really need to find myself a girlfriend to help with these urges...)"


    scene black with slowfade
    show text "{size=72}{color=#dc38bf}The next morning...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve


    scene home drinking isa 17 with slowfade
    isa "Mhmm..."
    isa "....."

    scene IsaMorningAnimated1 with dissolve
    pause
    isa "Mhmm..."
    mc "..."
    isa "Yeah..."

    scene IsaMorningAnimated2 with dissolve
    pause
    isa "Mhmm... Feels good..."
    isa "Yes... Grind on my pussy..."
    isa "....."
    isa "Huh?"

    scene home drinking isa 18 with dissolve
    isa "(Oh my!)"
    isa "(What's happening?)"

    scene home drinking isa 19 with dissolve
    isa "(I swear to god I had a wet dream just now...)"
    isa "(But I didn't get to cum. Typical...)"
    isa "(Wait...)"

    scene home drinking isa 20 with dissolve
    isa "(Oh my god! It's [mc_name]!)"
    isa "(And he has a...)"
    isa "(Wow! Little brother has grown a lot!)"
    isa "(Wait... I was grinding on his cock?)"
    isa "(Oh my god! I'm so lucky he didn't wake up!)"
    isa "(I better get the hell out of here... I'll die of embarrassment any second!)"


    $ renpy.end_replay()


    scene black with fade
    "Some time later..."

    scene home drinking isa 21 with fade
    mc "(Ugh...)"
    mc "(I knew I was gonna feel shit for the rest of today...)"
    mc "(Looks like Isabel already left. It's kind of surprising after all of the booze she had yesterday.)"
    mc "(I better get out of here before Ruby or Logan start asking questions about why I'm sleeping in Isabel's room...)"

    scene black with fade
    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0

    return






label mom_4_afterdrink_dialogue:

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene home afterdrink mom 1 with dissolve
    mom "Hey [mc_name]!"
    mc "Hi mom..."

    scene home afterdrink mom 2 with dissolve
    mc "I wanted to talk about the night when we were drinking..."
    mom "Oh..."

    scene home afterdrink mom 3 with dissolve
    mom "That was a fun night, wasn't it?"
    mom "I don't even remember when the last time I drank that much was!"

    scene home afterdrink mom 4 with dissolve
    mc "Yeah but..."
    mc "I wanted to talk about what happened after that..."
    mc "In your bedroom."
    mom "I only remember going to sleep [mc_name], I don't know what else is there to talk about."
    mc "(What?)"
    mc "(Did she really forget? Or...)"

    scene home afterdrink mom 5 with dissolve
    mom "Sorry, but I have to get ready."
    mom "Can't be late for work. See you later!"
    mc "(Did she pretend to not remember kissing me?)"
    mc "(Damn...)"

    scene black with slowfade

    return






label ruby_2_askjob_dialogue:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene ruby kitchen portrait 1 with slowfade:
        subpixel True
        yalign 1.0
    scene ruby kitchen portrait 1:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 7.0 yalign 0.03
    pause
    mc "Hey there Ruby!"

    scene ruby store 1 with dissolve
    ruby "Hey [mc_name]."
    mc "Why the long face?"
    ruby "Nothing..."
    mc "Fine."
    mc "What are you doing by the way?"
    mc "I don't even know what you're up to usually."
    mc "Have you found a job yet?"

    scene ruby store 2 with dissolve
    ruby "Not yet..."
    mc "Why not?"
    ruby "I don't know, okay?"
    ruby "Stop bothering me with this, you're just like dad..."

    scene ruby store 3 with dissolve
    mc "I just wanted to help out..."
    ruby "Sorry..."
    ruby "But you can't help. I can't do what I want without a job, but it's not that easy to find one."
    mc "What kind of jobs were you applying for?"
    ruby "Mostly office stuff. But I get rejected from all the high paying positions."
    if not lain_mod:
        mc "Uhm, you're aware that not so long ago you were celebrating your eighteenth birthday, right?"
    else:
        mc "Uhm, you realize that you're still very young, right?"

    scene ruby store 2 with dissolve
    ruby "What does that have to do with this?"
    mc "(Wow, she's really clueless.)"
    mc "It means that you won't be able to earn a shitton of money right when you get out of school."
    mc "Maybe you should lower your expectations first and try to get a different job until you get experience."
    mc "(Even I know that...)"

    scene ruby store 3 with dissolve
    ruby "Yeah, it's not that easy..."
    mc "I bet I can find you a job in no time."

    scene ruby store 4 with dissolve
    ruby "Seriously?"
    ruby "That would be awesome!"
    mc "Alright then. But you'll owe me one!"
    ruby "Anything you want!"
    mc "(I'd be careful around my pervy ass self with those statements, but I guess she's a bit naive.)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label ruby_7_choresargument_dialogue:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene ruby chores 1 with slowfade
    mom "I've had enough of your excuses young lady!"
    mom "Your room looks like a pigsty!"
    mom "While you're living in my house you'll do as I say and clean that room right now!"

    scene ruby chores 2 with dissolve
    ruby "Your house?"
    ruby "It's not even your house, dad paid for all of this!"
    ruby "You don't get to tell me what to do!"

    scene ruby chores 3 with dissolve
    mom "How dare you, you insolent little-"
    mc "(Oh shit!)"
    mc "(Ruby and mom are having a fight... It doesn't look good.)"
    mc "(And I'm just had to walk in on it... Awkward...)"
    mc "(Maybe if I just leave they won't notice me.)"
    ruby "I can do what I want and whenever I want to!"
    mc "(Oof, what a tantrum!)"

    scene black with fade
    mom "Ruby, get back here!"

    scene ruby chores 4 with fade
    mom "{i}Sigh...{/i}"
    mom "Why is she so stubborn...?"

    scene ruby chores 5 with dissolve
    mc "Everything okay, mom?"
    mom "Yeah it's... {w} You know how she is..."
    mc "Right...{w} Want me to talk to her?"
    mom "Well, she did always listen to you more than anyone in this family..."
    mom "Would you do that for me?"
    mc "Sure, no problem!"
    mom "Thank you [mc_name], I appreciate it."

    scene black with slowfade

    return






label mom_7_movienight_dialogue:

    if _in_replay:
        call setup_gallery
        stop music fadeout 2.0
        scene mom chill night 7
    else:
        play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
        scene mom chill night 1 with slowfade:
            subpixel True
            yalign 1.0
        scene mom chill night 1:
            subpixel True
            yalign 1.0
            pause 1.5
            linear 7.0 yalign 0.06
        pause

        scene mom chill night 2 with dissolve
        mc "(There's mom.)"
        mc "(But what is she doing? She looks sad.)"
        mc "(Maybe I can help?)"

        scene mom chill night 3 with dissolve
        mc "Hey, mom!"
        mc "Why the long face?"

        scene mom chill night 4 with dissolve
        mc "Isn't this supposed to be your day off?"
        mom "It is..."
        mc "What's the issue then?"

        scene mom chill night 5 with dissolve
        mom "Your dad promised me he'd spend the day with me."
        mom "That we would go to the movies tonight."
        mom "But of course, something important came up at work so he's staying in the office late."
        mc "(Damn, if I had a wife like that I sure as hell wouldn't neglect her.)"
        mc "You know how he is..."
        mom "Yeah..."
        mc "Why don't we do our own movie night then?"

        scene mom chill night 6 with dissolve
        mom "Really?"
        mc "Sure, I don't have anything to do tonight, so why not?"
        mom "Wow, [mc_name]! Thank you!"
        mom "I'm feeling much better already. {w} Come to my bedroom tonight, then."


        stop music fadeout 2.0
        scene black with fade
        show text "{size=72}{color=#dc38bf}Later that night...{/color}{/size}" at truecenter with dissolve
        $ renpy.pause(2.5, hard=True)
        hide text with dissolve


        scene mom chill night 7 with dissolve
    mc "(Damn, it's straight up a movie night in her bedroom...)"
    mc "(I thought this would be more of a living room experience, but I can't complain.)"
    mc "(She looked really sad though, so I hope I won't fuck this up and I can make her happy.)"


    scene black with fade
    play music "audio/music/red.mp3" loop fadein 2.5
    scene mom chill night 8 with slowfade:
        subpixel True
        yalign 1.0
    scene mom chill night 8:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.09
    pause
    mc "(Oh,{w} my{w} fucking{w} god!)"


    scene mom chill night 9 with dissolve
    mom "[mc_name]! I've been waiting for you."

    scene mom chill night 10 with dissolve
    mom "I hope you don't mind that I changed into... {w} something more comfortable."
    mc "Oh, not at all!"
    mc "You look amazing, as usual."
    mom "Ahah~"

    scene mom chill night 11 with slowfade
    mom "So?"
    mom "Come on, lie down next to me."
    mc "(Jesus, I'm gonna be lying on the bed next to her...)"
    mc "(She's so damn seductive!)"
    mc "(The way she's laying there, calling me how a lover would call her partner to have some hot, passionate sex.)"
    mc "(Shit, it's just a movie night. Chickflix and chill, and all that.)"

    scene mom chill night 12 with slowfade
    mc "Alright, let's start the movie then!"

    scene black with slowfade
    show text "{size=72}{color=#dc38bf}After the mediocre movie...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene mom chill night 13 with fade
    mom "It wasn't too bad, was it?"
    mc "Meh, kind of."
    mc "I was expecting something more."

    scene mom chill night 14 with dissolve
    mom "To be honest...{w} Me too."
    mom "But I've got an idea."

    scene mom chill night 15 with dissolve
    mc "(She's so gorgeous...)"
    mc "(A true MILF! And when I say MILF, I mean it...)"

    scene mom chill night 14 with dissolve
    mom "Could you stay with me tonight?"
    mom "I'm tired of falling asleep alone, having this huge bed all to myself..."
    mc "Of course, anything for you, mom!"

    scene mom chill night 16 with fade
    mom "You're such a good boy..."
    mom "I'm so glad you're back here."

    scene mom chill night 17 with dissolve
    mc "The basement is kind of shitty, but this makes up for it."
    mom "Awh, I know. I don't want you to feel that your siblings get treated better than you."
    mom "I'll try to make up for it some more...{w} In other ways..."
    mc "(Man, I'm such a fucking pro, having a casual conversation while fighting off the bloodflow that would surely end the movie night with a grand finale...)"
    mc "(I still think about the night she kissed me...)"
    mc "(Was it just in a drunken haze and didn't mean anything?)"

    scene mom chill night 18 with dissolve
    mc "(Or was it some secret desire, repressed deep within her?)"
    mc "(Well, I guess I'll never know...)"

    stop music fadeout 2.0
    scene black with slowfade
    show text "{size=72}{color=#dc38bf}The next morning...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene mom chill night 19 with dissolve
    pause 2.0

    play sound "audio/sfx/birds.ogg" loop fadein 2.0
    scene mom chill night 20 with slowfade
    mom "(Mmm...)"

    scene mom chill night 21 with dissolve
    mom "(Ahh... Looks like I feel asleep on [mc_name] last night...)"

    scene mom chill night 22 with dissolve
    mom "*Gasp!*"
    mom "(Oh my God!)"
    mom "(It's- {w} huge! {w} And staring right at me!)"

    scene mom chill night 23 with dissolve
    mom "(Okay... I should calm down.)"
    mom "(He's asleep. He's having morning wood, perfectly normal.)"
    mom "(But the size of it isn't...)"
    mom "(Mmm... It's been a while since I've seen such a beautiful cock.)"
    mom "(Too bad it's attached to my son...)"
    mom "(But he's asleep so...{w} Maybe I could...)"

    scene mom chill night 24 with dissolve
    mom "(Just a little bit...)"
    mom "(I could...)"

    scene mom chill night 25 with dissolve
    mom "(Enjoy myself.)"
    mom "(Quietly... And quick!)"

    scene mom chill night 26 with dissolve
    mom "(The sight of this beautiful cock has already gotten me wet...)"
    mom "(Oh God, I'm acting like a slut, already gushing just because of seeing a dick!)"
    mom "(I guess that's what happens when you haven't had sex in six months...)"

    scene mom chill night 27 with dissolve
    mom "(Oh my...)"
    mom "(I wish I could feel it in me...)"
    mom "(This is so wrong, having cravings for my son's...{w} big...{w} hard...)"
    mom "(Maybe I could just smell it...)"

    scene mom chill night 28 with dissolve
    mom "(Just a little whiff...)"
    mom "(Ahh~)"
    mom "(It smells so potent, so ready!)"
    mc "Mm...{w}Mhngg..."
    mom "(Oh, I think I disturbed him. Oh no, he's gonna turn and-)"

    scene mom chill night 29 with vpunch
    mom "(Mmnnng!!!)"
    mom "(It's in my mouth!)"
    mom "(It just slid right in there!)"
    mom "(This is so wrong...{w} This is so hot!!!)"
    mom "(I'm gonna cum!)"


    scene mom chill night 30
    with flash
    with vpunch
    mom "(Oh fuck, I'm cumming while my son's dick is in my mouth!)"

    scene mom chill night 30
    with flash
    with vpunch

    scene mom chill night 30
    with flash
    with vpunch
    pause 1.3


    scene mom chill night 31 with dissolve
    mom "(Oh God...)"
    mom "(It felt so good but...)"
    mom "(Oh my God...)"
    mom "(What have I done...)"
    mom "(I have to leave before he wakes up to this.)"
    mom "(I couldn't look him in the eye anyway, not after this...)"

    scene mom chill night 32 with slowfade
    mc "*Zzzzzz...*"

    $ renpy.end_replay()

    stop sound fadeout 1.0
    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadein 2.0

    return






label dad_1_rent_dialogue:

    stop music fadeout 2.0
    play sound "audio/sfx/birds.ogg" loop fadein 2.0

    scene dad rent 1 with slowfade
    mc "(It's been a while since I've been back.)"
    mc "(It's not as good as I was hoping to be, but it's not tragic either.)"
    mc "(But I feel like I'm behind...)"

    scene dad rent 2 with dissolve
    mc "(I don't really have anything to show for my efforts here, besides that wreck of a car I now have, courtesy of Thorne...)"
    mc "(I have to get something tangible soon to show for dad or otherwise I'm sure I'll lose to that prick Logan.)"

    scene dad rent 3 with dissolve
    dad "Oh, son. You're up early."
    dad "That's good to see."
    mc "(Speak of the devil...)"
    mc "Morning, dad."

    scene dad rent 5 with dissolve
    dad "Actually, it's good you're here, I wanted to talk to you about something."
    dad "It's been a while since you've moved back home."
    dad "I thought I'd give you some leeway while you get back on track but I think enough time has passed."

    scene dad rent 4 with dissolve
    dad "I need you to pay rent from now on."
    dad "I think $1,500 a month is reasonable."

    scene dad rent 6 with dissolve
    mc "All that for a basement?"
    mc "Isn't that a bit much? And I don't know about Logan or the others needing to pay rent."

    scene dad rent 5 with dissolve
    dad "They don't, but they haven't made the same mistakes as you, have they?"
    dad "It's time to take responsibility for your actions, son. I'm not trying to make you feel bad."
    dad "I'm doing this so you get a taste of how life works."
    dad "If I give you everything on a silver platter, what will you do when I'm gone?"
    dad "You might think I'm harsh now, but in due time, you'll thank me, son."
    dad "That day may only come when I'm not around anymore.{w} Or maybe it won't ever come. Then I'll have failed as your father."

    scene dad rent 4 with dissolve
    dad "I'm working to build a foundation that you or Logan will be able to build upon and further our family."
    dad "That will be my legacy, and you will decide what to do with it."
    dad "I'm doing my part, son. Will you do yours?"

    scene dad rent 5 with dissolve
    mc "Fine. I'll get you the money."
    dad "Alright."
    dad "Oh by the way, your mother told me about you trying to get Ruby to do her chores."
    dad "It looks like you haven't had much success there."

    scene dad rent 6 with dissolve
    mc "I tried, but she doesn't want to listen!"

    scene dad rent 7 with dissolve
    dad "At the company, when someone doesn't do their job, there's disciplinary action."
    dad "Trying is not enough anymore, [mc_name]..."

    scene dad rent 8 with dissolve
    mc "(And he just left...)"
    mc "(But he gave me an idea.)"
    mc "(I'll get Ruby to do her chores, no matter what it takes. That might score a good point with the old man.)"

    stop sound fadeout 1.0
    play music "audio/music/soul.mp3" loop fadein 2.5
    scene black with slowfade

    return






label logan_insults_kitchen_dialogue:

    scene black
    show home_kitchen__evening_logan_ground

    if temp_1 == 1:
        mc "Hey, banana man."
        logan "Pff - That's all you have?"
        logan "All your blood is apparently routed to your nether region instead of making it up to your brain."
        logan "You've probably created a new strain of STD at this point."

    elif temp_1 == 2:
        mc "How's it feel to be the unattractive brother?"
        logan "But we're twins!"
        mc "Exactly!{w} Wait..."

    elif temp_1 == 3:
        logan "You know, I remember when Dad told me about the day when we got home from the hospital...{w} they had a buy-one-get-one-free deal going on."
        mc "Fuck you..."

    elif temp_1 == 4:
        mc "Oh, a banana?"
        mc "Your finger just doesn't cut it anymore?"
        mc "Or maybe you're preparing for the real deal?"
        logan "Very funny, [mc_name]! Did you read that in a book?"
        logan "Oh, silly me... You can't even read!"

    elif temp_1 == 5:
        mc "The only woman to tell you she loves you is mom."
        mc "She does it out of pity."

    elif temp_1 == 6:
        mc "When anti-vaxxers talk about vaccines causing autism, you're the illustration."

    elif temp_1 == 7:
        mc "Did mom ever tell you that you were raised on toilet water?"
        logan "Very funny. We'll see who gets to laugh when you're begging for a job at MY company."
        logan "There's always a need for janitors, I suppose..."

    elif temp_1 == 8:
        logan "No brain, no personality..."
        logan "Tell me, what's it like now that Dad took back his money, the only attractive thing about you?"
        mc "You prick..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
