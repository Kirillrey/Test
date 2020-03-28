label tutoring1_intro_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene tutoring 1 with fade
    jane "Alright [mc_name], I'm glad you showed up."
    jane "Let's start today's lesson."
    mc "(Man, looking this woman in the eye is the hardest thing I've done in my entire life!)"
    mc "(This is going to be a long tutoring session...)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 1 with dissolve
    jane "Do you understand?"
    mc "I think so..."
    mc "(I don't. Fuck!)"
    jane "So there's you assignment in front of you, let's see if you can solve it."
    jane "I'll be grading some tests in the meantime."
    mc "Alright."

    return



label tutoring1_concentrate_dialogue:

    mc "(I better concentrate on this if I want to graduate at all.)"
    mc "(Oh fuck my life...)"
    mc "(Let's see what I can make out of this...)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 7 with dissolve
    jane "Not bad [mc_name]!"
    mc "Really?"
    jane "No, it's pretty bad."
    mc "Oh..."
    jane "But I see you've got some things right."
    jane "So there's might be hope for you to get your degree!"
    mc "That doesn't sound too good."
    jane "Listen. I'm gonna work you to the very last drop."
    jane "I see you have potential and once I'm set on a target I pounce and I don't let go until I'm satisfied."
    jane "So don't worry, we'll get through this together, just keep it up all the time for me, alright?"
    mc "No problem with keeping it up Ms Jane, sure!"
    jane "Great, see you at the next session!"

    return



label tutoring1_stareathertits_dialogue:

    scene tutoring 4 with dissolve
    mc "(Fuck this bullshit, I have tits to look at!)"
    mc "(I think I can easily take a sneak peak while she's occupied with those tests.)"

    scene tutoring 5 with dissolve
    mc "(Ah yes, those mammaries are the biggest ones I've seen!)"
    mc "(And they look natural too! This woman is gifted, for sure.)"
    mc "(Big brains and big tits! One is enough to get through life, but two! Damn...)"

    scene tutoring 6 with dissolve
    jane "Do you think I'm not used to men staring at me?"
    jane "I offer you help so you can get your degree and you can't even control your urges?"
    mc "I-"
    jane "I'm disappointed in you, [mc_name]!"
    jane "Come back here when you learned some respect!"

    return



label tutoring1_makemistake_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
        scene tutoring 1

    mc "(I think now I understand this subject enough so that I can try something...)"
    mc "(This is a gamble, but maybe it will work out.)"

    scene tutoring 3 with dissolve
    mc "(Worst thing that could happen is she'll think I'm retarded.)"
    mc "(Not the worst thing a woman ever thought of me I guess.)"

    scene black with dissolve
    "30 minutes later..."

    scene tutoring 8 with dissolve
    jane "I see you've made some pretty big mistakes here [mc_name]."
    jane "It's really a shame, you've been doing so nice lately, I could see your improvement."
    jane "Now it's a step back. What happened?"
    mc "Sorry Ms Jane, I couldn't really concentrate."
    jane "Why is that?"
    mc "(Here we go!)"
    mc "I don't know how to say this but..."
    mc "Uhm.."
    jane "Come on [mc_name], you can tell me."

    scene tutoring 9 with dissolve
    mc "It's because you are so beautiful and sexy! It's really hard to concentrate when a hot bombshell is sitting next to me!"
    jane "Hot... Bombsh-"
    jane "I- How can you say-"
    mc "It's not like I want to feel this, but it's really not easy, you know. I respect that you are teaching me but..."

    scene tutoring 8 with dissolve
    jane "I see. Sorry for being rude about it."
    jane "But this is not going to work like this, if we want you to improve."
    mc "I had an idea..."
    mc "(Now the main part.)"
    jane "I'm listening."
    mc "I read about how incentive rewards are the best motivational tools for progression."
    mc "So instead of your beauty being the negative element here, we could turn it into a positive instead, in the form of issuing a reward."
    jane "What kind of reward?"
    mc "If I do good on the assignment, can I look at your breasts for a little bit?"

    scene tutoring 10 with dissolve
    jane "What? My breasts?"
    jane "I..."
    jane "I guess I understand your reasoning..."
    mc "(And now at last, a step back.)"
    mc "Of course I understand this is an unusual thing and you would be in full control of the situation."
    mc "I'm still your student."
    mc "But what am I saying... Let's just forget this conversation."
    mc "I'm sorry I brought this up. I'll make do somehow."

    scene tutoring 11 with dissolve
    jane "No..."
    mc "(Got her!)"
    jane "I mean, I guess I'm okay with it."
    jane "We can try if it really helps with your studies."
    jane "Just looking, right?"
    mc "Of course!"
    jane "That's not too bad then. If it's for a good cause."

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene TutoringBreathingAnimated1 with dissolve
    pause
    jane "Go ahead, take your time."
    mc "Oh wow!"
    mc "Ms Jane... Your breasts are amazing."
    mc "But not just those."
    mc "You are a real beauty!"
    jane "Well uhm, thank you [mc_name], it's nice of you to say that."
    mc "(My god, those melons make my dick jolt with excitement in my pants!)"
    mc "(Who would have thought studying can get you 1st class tits in your face?!)"
    jane "Alright, I think that's enough, right?"
    mc "Yes, I feel much better. I'll do my best to pass the course!"
    jane "Alright then, I hope this really helps. See you at the next session."

    $ renpy.end_replay()

    return






label tutoring2_intro_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    scene tutoring 1 with fade
    jane "Alright [mc_name], let's start today's lesson."

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 1 with fade
    jane "Do you understand?"
    mc "I think so..."
    jane "So there's you assignment in front of you, let's see if you can solve it."
    jane "I'll be grading some tests in the meantime."
    mc "Alright."

    return



label tutoring2_concentrate_dialogue:

    mc "(I better concentrate so she'll let me have some private time between my eyes and her giant tits!)"

    scene tutoring 3 with dissolve
    mc "(Oh fuck my life...)"
    mc "(Let's see what I can make of this...)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 7 with fade
    jane "Not bad [mc_name]!"
    mc "Really?"
    jane "Actually, yes!"
    mc "Nice!"
    jane "But there's still a long ways to go!"
    jane "Now... I guess you want your reward, right?"
    mc "I hope I deserved it."
    jane "You certainly did, feel free to look."

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene TutoringBreathingAnimated1 with dissolve
    pause
    mc "Oh Ms Jane, I think your breasts are the best in the world!"
    mc "Are they real?"
    jane "Of course they are!"
    mc "I was asking because it's hard to even sculpt something like those!"
    mc "And I see that you don't wear a bra, right?"
    jane "I... What kind of question is that?"
    mc "Oh... Sorry."
    jane "(Ah, what am I saying... He's so enthusiastic and he's actually improving, and here I am killing his mood.)"
    jane "(He's already staring at them like a hungry wolf at its prey... Let him ask some questions then.)"
    jane "No, I'm the one who should apologize."
    jane "It's just that this situation is new to me."
    jane "But you are right, I don't wear a bra."
    mc "Oh wow!"
    mc "I wonder what they look like without that dress!"
    mc "But please, don't misunderstand..."
    jane "It's natural for you to think about that."
    jane "But I think this is enough... I'll see you at the next lesson."

    return



label tutoring2_stareathertits_dialogue:

    scene tutoring 6 with dissolve
    jane "[mc_name], I know you are staring."
    jane "This is not what we agreed on. I'm doing you a big favor so come back when you can keep your end of the bargain."
    mc "(Damn...)"

    return



label tutoring2_makemistake_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
        scene tutoring 3
    else:
        scene tutoring 3 with dissolve
    mc "(Maybe it's time to push things a bit further...)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 8 with dissolve
    jane "[mc_name], what happened?"
    jane "I'm seeing pretty big mistakes here!"
    jane "I thought that reward was helping..."
    mc "Oh, it is!"
    mc "But it's still hard to concentrate sometimes."
    mc "You are so beautiful, it's hard to ignore. It's not your fault though, I should probably control myself more, I'm sorry."
    jane "(He looks genuinely sorry, and I can see he's trying to get better.)"
    jane "(I guess I can give him a bit more encouragement.)"
    jane "What if we increased the reward a bit? Would that help?"
    mc "(Fuck yes!)"
    mc "I think so, yeah."
    jane "So what do you have in mind?"
    mc "(Hmm... I probably shouldn't ask for too much or it will blow the whole operation.)"
    mc "Could you maybe, shake them for me?"
    jane "Shake them? Oh well..."

    scene tutoring 12 with dissolve
    jane "(Jane... What have you gotten yourself into...)"
    jane "I guess I can do that, but you have to promise you'll do better, okay?"
    mc "I promise Ms Jane!"
    jane "Good."

    scene TutoringTitsShakeAnimated1 with dissolve
    pause
    jane "Is it okay like this?"
    mc "Is it okay? It is awesome!"
    mc "You are the best Ms Jane!"
    jane "Thanks! I don't do this often to say the least..."
    mc "Don't you shake your breasts to your boyfriend Ms Jane?"
    jane "I don't-"
    jane "It's complicated..."
    mc "Sorry, I didn't want to be rude."
    jane "Nevermind, just enjoy the sights while you can, I can't do this for long."
    mc "Thank you for helping me, you're truly a great teacher!"
    jane "(He's so sweet when he says that...)"
    jane "(But he's right, I'm his teacher. This shouldn't go any further than this, it's already gone further than it ever should have.)"
    jane "Okay, that's enough [mc_name]. I'll see you at the next lesson."

    $ renpy.end_replay()

    return






label tutoring3_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene tutoring 1
    else:
        scene tutoring 1 with slowfade
    jane "Alright [mc_name], let's start today's lesson."

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 7 with fade
    jane "Do you understand?"
    mc "I think so..."
    jane "Good!"
    jane "Here's an assignment then, let's put your knowledge to the test!"

    scene tutoring 13 with slowfade
    mc "(Shit, this is getting harder.)"
    mc "(It probably doesn't help that it's hard to concentrate with her next to me and-)"

    scene tutoring 14 with dissolve
    pause 0.4

    scene tutoring 15 with dissolve
    mc "Whoops!"

    scene tutoring 16 with dissolve
    jane "Don't worry, I'll pick that up for you, you just concentrate on the assignment!"

    scene tutoring 17 with fade
    jane "It's probably here somewhere..."
    mc "(Oh boy!)"
    mc "(With great melons come a great bottom! Can it get any better?)"

    scene tutoring 18 with dissolve
    mc "(I wish I could see under her dress...)"
    mc "(It's probably too soon for that, if she noticed she'd have me expelled right away.{w} Maybe later...)"
    jane "Ah, I got it!"

    scene tutoring 16 with fade
    jane "There you go, now let's get back to the task at hand."

    scene black with slowfade

    scene tutoring 16 with fade
    jane "Alright, it's looking good. There's still room for improvement, of course."
    mc "Yeah, it's getting a bit harder."
    jane "Let's uhm... {w} Get you your reward then."
    jane "I mean, I assume you want it?"
    mc "Of course Ms Jane, you're the best!"

    scene TutoringTitsShakeAnimated1 with dissolve
    pause
    mc "This is magnificent Ms Jane!"
    jane "Don't forget your promise, Connnor!"
    jane "You have to do better!"
    mc "Not that I mind but why are you so eager to help me out? Most teachers don't care about a single student..."
    jane "Well, it's two things. I'm not like most of the teachers, I actually care."
    jane "You students are the future, and it's our responsibility to give you the best we can, in my opinion."
    jane "And you have kind of a reputation here...{w} If I can make you pass, it'll definitely score a good point at the management."
    mc "Ah, I see. I'll try my best then, so we both end up in a better position!"
    jane "(Just chatting casually while I'm shaking my tits to him...)"
    jane "(But he's so respectful, despite his age...{w=1.2} I like that.)"
    jane "Alright, [mc_name].{w} I hope you had enough, see you at the next lesson!"

    $ renpy.end_replay()

    return






label tutoring4_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene tutoring 1
    else:
        scene tutoring 1 with slowfade
    jane "Alright [mc_name], let's start today's lesson."

    scene black with fade
    show text "{size=72}{color=#dc38bf}30 minutes later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene tutoring 7 with fade
    jane "Do you understand?"
    mc "I think so..."
    jane "Good!"
    jane "Here's an assignment then, let's put your knowledge to the test!"

    scene tutoring 13 with slowfade
    mc "(Alright, this is hard, but I think I got it.)"
    mc "(But I can't keep making mistakes on purpose, she might think I'm retarded or something.)"
    mc "(I have a few options on how I want to advance this...)"


    menu:
        "Drop Pen" if not tutoring4_liftdress_seen or not tutoring4_touchbutt_seen:
            mc "(Let's see if she goes for it again...)"

            scene tutoring 14 with dissolve

            scene tutoring 15 with dissolve
            mc "Whoops!"

            scene tutoring 16 with dissolve
            jane "Don't worry, I'll pick that up for you, you just concentrate on the assignment!"

            scene tutoring 17 with slowfade
            jane "It's probably here somewhere..."
            mc "(Aw yes!!)"
            mc "(Okay, okay...)"
            mc "(I can't just do nothing this time...)"
            mc "(Maybe I could...)"


            menu:
                "Lift Dress" if not tutoring4_liftdress_seen:

                    $ tutoring4_liftdress_seen = True

                    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
                    mc "(I could try lifting her dress...)"
                    mc "(Definitely risky, but it might just be doable.)"
                    mc "(Her dress looks very lightweight, she might not notice if I pull carefully.)"
                    mc "(Here we go!)"

                    scene tutoring 19 with slowfade
                    mc "(Mother of God, that ass!)"
                    mc "(I love it! This was a good decision.)"
                    mc "(I was hoping for no panties, but it's awesome nonetheless!)"

                    scene tutoring 20 with dissolve
                    jane "Where is that stupid pen...?"
                    mc "(Thank God for that pen, I can keep ogling for just a bit more!)"
                    mc "(I wonder if I could make her wear no panties in the future...)"
                    jane "Finally, I got it!"

                    scene tutoring 16 with fade
                    jane "There you go, now let's get back to the task at hand."
                    mc "(Whew, she didn't notice it, awesome!)"

                    scene black with slowfade
                    pause 1.0


                "Touch Butt" if not tutoring4_touchbutt_seen:

                    $ tutoring4_touchbutt_seen = True

                    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
                    mc "(I could try touching her butt.)"
                    mc "(Straight up grabbing it won't fly though...)"
                    mc "Let me help you Ms Jane!"

                    scene tutoring 21 with fade
                    mc "Can you see it somewhere?"
                    mc "(Oh man, it's nice, big, firm, round...)"
                    mc "(I could go on all day!)"
                    jane "I uh..."

                    scene tutoring 22 with fade
                    jane "(Did he just touch my butt?)"
                    jane "(I haven't been touched there in...)"

                    scene tutoring 23 with dissolve
                    jane "(He's probably just trying to help.)"
                    jane "(He has respected our boundaries so far, this is probably just something innocent.)"
                    jane "(I don't want to embarrass him by pointing out that his hand is on my bottom.)"
                    jane "I got it, [mc_name], thank you!"

                    scene tutoring 16 with fade
                    jane "There you go, now let's get back to the task at hand."
                    mc "(Whew, finally touching her hot body! It was awesome!)"

                    scene black with slowfade
                    pause 1.0


        "Ask for incentive" if not tutoring4_feet_seen or not tutoring4_caress_seen:

            mc "(I could just ask for some 'incentives' straight up.)"
            mc "(If I ask something small enough she may agree...)"


            menu:
                "Feet" if not tutoring4_feet_seen:

                    $ tutoring4_feet_seen = True

                    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
                    scene tutoring 1 with fade
                    mc "You know Ms Jane, I was wondering if you are open to a little experiment."
                    jane "Experiment?"
                    mc "I read that phisycal contact during intense intellectual workloads increase people's performance by up to fifteen percent."
                    jane "Where did you read that?"
                    mc "Online."
                    jane "Online... {w} Right."
                    jane "Well, that depends... What did you have in mind?"
                    mc "Oh, nothing much, just maybe... I don't know."
                    mc "Rest your feet on my lap? I guess that works. It might be a bit more comfortable to you as well."
                    jane "Hmmm, I don't see any harm in that."
                    jane "Alright, but get to the assignment then."

                    scene tutoring feet 1 with dissolve
                    mc "(It worked!)"
                    mc "(Man, if I do it smart enough, I can have a good time here!)"

                    scene tutoring feet 2 with dissolve
                    jane "Hmm, it's actually not bad."
                    jane "Laying back like this, while grading these papers."
                    jane "Good idea, [mc_name]. I hope this helps you as well!"

                    scene tutoring feet 3 with dissolve
                    mc "Haha, right?"
                    mc "(I know what it doesn't help with.)"
                    mc "(Keeping my blood out of my groin area.)"

                    scene tutoring feet 4 with dissolve
                    mc "(She has beautiful feet, nicely shaped and well kept.)"
                    mc "(I even like the nail polish color.)"

                    scene tutoring feet 5 with dissolve
                    mc "(I have to be careful with having a boner though...)"
                    mc "(She probably wouldn't appreciate it at our current relationship.)"
                    mc "(I'll have to concentrate and do well on this paper to be able to justify this...)"

                    scene black with slowfade
                    pause 1.0


                "Caress" if not tutoring4_caress_seen:

                    $ tutoring4_caress_seen = True

                    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
                    scene tutoring 1 with fade
                    mc "You know Ms Jane, I was wondering if you are open to a little experiment."
                    jane "Experiment?"
                    mc "I read that phisycal contact during intense intellectual workloads increase people's performance by up to fifteen percent."
                    jane "Where did you read that?"
                    mc "Online."
                    jane "Online... {w} Right."
                    jane "Well, that depends... What did you have in mind?"
                    mc "Oh, nothing much, just maybe... I don't know."
                    mc "Put your hand on my thigh while I work?"
                    jane "Don't you think that's a little intimate, [mc_name]?"
                    mc "I don't consider my thighs an intimate region and my arm wouldn't work since I'm using it to write."
                    jane "Hmm... {w} Alright, I'm a bit reluctant, just to let you know."
                    jane "But fifteen percent could be a nice increase, let's see then."

                    scene tutoring caress 1 with dissolve
                    mc "(It worked!)"
                    mc "(Man, if I do it smart enough, I can have a good time here!)"

                    scene tutoring caress 2 with dissolve
                    jane "(It feel awkward just holding my hand there...)"
                    jane "(He didn't ask for it, but I should probably move it a bit, caress his leg.)"
                    jane "(I hope he won't take it the wrong way...)"

                    scene tutoring caress 3 with dissolve
                    mc "(Oh, she started moving her hand up and down!)"
                    mc "(She might not be that reluctant afterall.)"
                    mc "(I shouldn't push my luck though.)"

                    scene tutoring caress 4 with dissolve
                    mc "(If I pop a boner right here, I can say goodbye to my chances with her forever.)"
                    mc "(I can't have a boner {i}this time...{/i})"
                    mc "(Ah... {w} I better concentrate on the paper, I have to do better so she sees that it works!)"

                    scene black with slowfade
                    pause 1.0

    $ renpy.end_replay()

    return



label tutoring4_notseenall_dialogue:

    scene tutoring 16 with fade
    jane "Alright, it's looking good. There's still room for improvement, of course."
    mc "Yeah, it's getting a bit harder."
    jane "Let's uhm... {w} Get you your reward then."
    jane "I mean, I assume you want it?"
    mc "Of course Ms Jane, you're the best!"

    scene TutoringTitsShakeAnimated1 with dissolve
    pause
    jane "Is it okay?"
    mc "I can't get enough of it Ms Jane!"
    mc "I love them!"
    jane "Oh..."
    jane "(Am I blushing...?)"
    jane "Alright, [mc_name]. {w} I hope you had enough, see you at the next lesson!"

    return



label tutoring4_gropetits_dialogue:

    if _in_replay:
        call setup_gallery
        play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0
        scene tutoring 16
    else:
        scene tutoring 16 with fade
    jane "Alright, it's looking good. There's still room for improvement, of course."
    mc "Yeah, it's getting a bit harder."
    jane "Let's uhm... {w} Get you your reward then."
    jane "I mean, I assume you want it?"
    mc "About that..."
    mc "I was wondering if I could... {w} No, that would be rude to ask you that, sorry."
    jane "Go on, I want to hear it."
    mc "I mean, your breasts are so wonderful, really I haven't seen anything like it before."
    mc "And I probably never will, so I thought I'd really like to know how they feel..."
    jane "Do you want to touch them?"
    mc "I uhm...{w} Yes."
    jane "I..."
    jane "(Oh God, Jane...)"
    jane "(It's been going so good, it would be a shame to ruin it now, but this...)"
    jane "(Looking is one thing, but touching...)"
    mc "I can promise to be gentle, if that's what's bothering you."
    jane "(He's so cute...)"
    jane "Fine, just this once."
    jane "And promise me not to tell this to anyone! We're both out of here if anyone hears about this!"
    mc "Of course, I'd never risk getting you in trouble!"

    scene TutoringTitsGropeAnimated1 with dissolve
    pause
    mc "Oh, Ms Jane, this is unexpected!"
    mc "I never thought they are this heavy!"
    mc "It must be hard on you..."
    jane "Yeah..."
    mc "But they feel wonderful!"
    jane "I'm glad you like them... {size=-10}Ahh~{/size}"

    scene TutoringTitsGropeAnimated2 with dissolve
    pause
    jane "(What the hell is wrong with you Jane?)"
    jane "(Moaning like a naughty school girl when someone grabs your tits?!)"
    mc "(I hope she enjoys this as much as I do...)"
    jane "(Oh God... This tingling feeling in my body...)"
    jane "(I'm starting to get wet... {w} He does it so good...)"
    jane "(What the hell am I doing?)"
    jane "(This has to stop, this has just become too much!)"
    jane "That's enough [mc_name]..."
    jane "I'll... {w}see you on the next lesson."

    $ renpy.end_replay()

    return






label jane_7_schoolmissing_dialogue:

    play music "audio/music/comedy.mp3" loop fadeout 2.0 fadein 2.0

    scene jane missing 1 with slowfade
    mc "(Hmmm...)"
    mc "(Ms Jane is not working today.)"
    mc "(This note says she's on sick leave...)"
    mc "(Damn, how am I gonna get my tutoring done?)"
    mc "(Okay, I'm more interested in her, rather than the tutoring part.)"

    scene jane missing 2 with dissolve
    mc "(Hmmm...)"
    mc "(I could go and visit her.)"
    mc "(If she's sick, I'm pretty sure she'd appreciate if I went over and asked if she needed anything.)"
    mc "(Well, it couldn't hurt. Time to get to the school office to find out her address.)"
    mc "(This will probably take a while...)"

    stop music fadeout 2.5
    scene black with fade
    show text "{size=72}{color=#dc38bf}A lot of time later..{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene janehome_porch__night_ground with Fade(0.0, 0.5, 1.0)

    return






label jane_10_stopteaching_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0

    scene tutoring 27 with slowfade
    mc "(Oh, Ms Jane is back to teaching again!)"
    mc "(I guess it's time for an extra tutoring session!)"

    scene tutoring 24 with fade
    jane "Oh [mc_name]..."
    jane "It's good you're here. I wanted to talk to you about... {w} Uhm, you know."
    jane "About our tutoring sessions."

    scene tutoring 25 with dissolve
    jane "I don't think I can continue doing this."
    jane "It was wrong of me to do it in the first place."
    jane "I have had time to think about it while I was at home on sick leave and I realized how terribly immoral it was."
    jane "I shouldn't have used my body or anything sexual as an incentive for you."

    scene tutoring 26 with dissolve
    mc "But it was going great!"
    mc "I mean, I have improved a lot, you said so yourself."
    jane "Right. Which means you are not hopeless and you can improve without any of this...{w} thing that we've been doing."
    mc "Oh come on, Ms Jane. Please! I know you liked it too!"
    mc "I could see you were being turned on by this!"

    scene tutoring 28 with dissolve
    jane "No, [mc_name], you are terribly wrong!"
    jane "And to think it was turning me on is nonsense! Having this conversation in the first place is just proof how messed up all this was!"
    jane "Besides, if anyone found out, I'd be out of a job in no time! I'd probably be all over the news as well! Do you want that?"
    mc "No, I-"

    scene tutoring 29 with dissolve
    jane "Then stop this discussion at once, we're done with it."
    jane "You will improve on your own with the appropriate time investment in your studies and we won't talk about this ever again."
    jane "Now if you'll excuse me, I have a lot of work to do."
    mc "Fine..."

    scene tutoring 30 with dissolve
    mc "(Well, shit!)"
    mc "(What the hell did I do to fuck this up?)"
    mc "(Women are cray...)"
    mc "(Should I just let this go...? {w} Probably not...)"
    mc "(She wasn't turned on? {w} Oh, I'll turn her on alright!)"

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label jane_14_continueteaching_dialogue:

    if _in_replay:
        call setup_gallery
        stop music fadeout 2.0
        scene tutoring 33
    else:
        play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
        scene tutoring 31 with slowfade
        jane "Thank you for coming, [mc_name]."
        jane "I want to talk to you about something."
        mc "If it's about the economics assignment, I'm wor-"
        jane "No, don't worry. Not about that."

        scene tutoring 32 with dissolve
        jane "I...{w} I want to apologize."
        jane "I was being rude the other day."
        jane "Our tutoring sessions have been intteresting, I admit. But they were also upsetting for me."
        jane "I haven't done anything like that before."
        jane "I just don't want to do anything wrong..."
        mc "If we both agree, it's not wrong. I think that, at least."
        mc "(I can see she's nervous about this. A couple kind words could go a long way here.)"
        mc "I think you're a fantastic teacher and I really think I'm improving thanks to you, Ms Jane."
        jane "You're good young man, [mc_name]."

        scene tutoring 33 with dissolve
    jane "So what I was thinking is..."
    jane "I think I'm ready to continue our sessions."
    mc "Really? That's awesome!"
    jane "And as an apology..."

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene tutoring 34 with dissolve
    pause
    jane "I hope you like them."
    jane "(Oh my God... I'm really doing this.)"
    jane "(I'm bearing my breasts to my student...)"
    jane "(I've surely gone insane. {w} But this is the hottest thing I've done.)"

    scene tutoring 35 with dissolve
    mc "Ms Jane I..."
    mc "Oh my God!"
    mc "Your breasts are breathtaking... No- {w} You're breathtaking!"

    scene tutoring 36 with dissolve
    jane "Ah..."
    jane "Uhm, {w} apology accepted, then?"
    mc "A hundred percent!"
    mc "You know how to make a guy like me happy."
    jane "(Am I doing this to make him happy with me? To accept me?)"
    jane "(Oh Jane...)"
    mc "If this is any indication of what's to come, I'll be your best student in no time!"

    scene tutoring 33 with dissolve
    jane "Ahah~"
    jane "Alright then, I'll see you again later."
    mc "Thank you for doing this for me, Ms Jane. I really appreciate your kindness."
    mc "And just so you know, I really think you're beautiful."
    jane "(He's making me blush...)"
    jane "I uh-"
    mc "(I better leave now and give her some time to think about the things I said.)"
    mc "See you at the next tutoring session!"

    $ renpy.end_replay()

    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
