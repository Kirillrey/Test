label thorne_2_lawyer_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0

    scene thorneoffice_office_door_day with fade
    mc "(Why the fuck am I even here...)"
    mc "(OK, I guess I know why.)"
    mc "(I need the money, and working with this dude is probably better than getting snatched up by the cops because of fuckin Kyle.)"

    scene lawyer 2 with dissolve
    thorne "Oh, it's you!"
    mc "Yeah, it's [mc_name]."
    thorne "Hah, I know."

    scene lawyer 3 with dissolve
    thorne "So you came."
    thorne "Why is that?"
    mc "Well, I wanna know why you got me out of jail."
    thorne "Ah, that."

    scene lawyer 4 with dissolve
    thorne "Well isn't it obvious?"
    thorne "Nobody does anything if it doesn't serve them in some way."

    scene lawyer 5 with dissolve
    thorne "You have something I need."
    mc "Like what?"
    thorne "Information, kid!"
    thorne "Where did you get those envelopes?"

    scene lawyer 6 with dissolve
    thorne "And don't you fucking lie to me, alright?"
    thorne "I can get your ass back to jail faster than you'd think."

    scene lawyer 7 with dissolve
    mc "That's just fucking great, I came here so you could threaten me?"
    thorne "You came here because you're curious and you need money."
    thorne "Now, answer my question. The envelopes."
    mc "That fucker Kyle gave them to me, said it's good business to deliver them."
    mc "He didn't say anything about trouble with the cops though."
    thorne "Kyle? Kyle who?"
    mc "...Kyle Parker."
    thorne "So your friend Kyle. Alright."
    thorne "I have to make some arrangements, then we can talk about business."
    thorne "Watch the office 'til I get back, will ya? It won't take long."
    thorne "And don't touch anything."
    mc "Right..."

    scene lawyer 8 with slowfade
    mc "(What a cocksucker...)"
    mc "(Throw me back to jail my ass.)"
    mc "(Maybe I should look around here a little bit...)"

    scene lawyer 10 with dissolve
    mc "(Dude must be hiding something, I need some leverage if he tries to threaten me again.)"

    scene lawyer 11 with dissolve
    mc "(What should I do?)"


    python:
        temp_1 = True
        temp_2 = True
        temp_3 = True

    menu lawyermenu:

        "Check PC" if temp_1:
            mc "(The PC seems to be a good place to start.)"

            scene lawyer 12 with dissolve
            mc "(What the hell?)"
            mc "(Where is the mouse and keyboard?)"

            scene lawyer 13 with dissolve
            mc "(Oh it's touch screen?)"
            mc "(Seems weirdly different than the rest of this crappy retro design in here.)"
            "\"Enter Password\""
            mc "(Fuck... I should have known.)"

            $ temp_1 = False
            jump lawyermenu


        "Check Paper Stack" if temp_2:
            scene lawyer 14 with dissolve
            mc "(Just ordinary papers and contract forms...)"

            $ temp_2 = False
            jump lawyermenu


        "Check Drawers" if temp_3:
            scene lawyer 15 with dissolve
            mc "(Locked.)"
            mc "(Really?)"
            mc "(I can't find anything in here!)"

            $ temp_3 = False
            jump lawyermenu


    play sound "audio/sfx/ringtone.ogg"
    "*phone ringing*"

    scene lawyer 16 with dissolve
    mc "(Should I pick that up?)"
    mc "(Nah... I'll let it go. I don't think that old piece of crap has voicemail either. Probably-)"
    "Isaac. Got the results back."
    "It wasn't the real deal. It's a better replica but still a million miles away from the original."
    "Let me know if you need anything else."
    "*beep*"
    mc "(Well that was interesting...)"

    scene lawyer 17 with slowfade
    thorne "Anything happen while I was away?"
    mc "Nope. You just have a boring ass office, that's all."
    thorne "Hah, alright."
    thorne "Listen up kid. Let me show you that I operate in good faith by giving you a little present."
    mc "Present?"

    scene lawyer 18 with dissolve
    thorne "Call it an advance, if you will."
    thorne "Do you have a laptop?"
    mc "Not right now."
    thorne "Buy one. You'll need it later."

    scene lawyer 19 with dissolve
    thorne "This should be enough."
    mc "(Now we're talking!)"
    mc "Thanks, old man!"

    scene lawyer 20 with dissolve
    thorne "It's Thorne for you, and don't spend it on hookers and dumb shit."
    thorne "I'll call you when I need you. It will be soon enough."
    mc "You know my number?"
    thorne "I know a lot of things about you, and your family, [mc_name]."
    thorne "Now get out of here."
    pause 0.8
    thorne "Oh and..."

    scene lawyer 6 with dissolve
    thorne "Do not mention our meeting, me, or anything about our work to anyone."
    mc "Of course."
    thorne "Good."



    stop music fadeout 2.0
    scene black with slowfade
    show text "{size=72}{color=#dc38bf}1 year later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve
    $ renpy.pause(1.0, hard=True)


    $ renpy.movie_cutscene("videos/cutscene_1.webm")


    scene black with fade
    show text "{size=72}{color=#dc38bf}Present time...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve



    play music "audio/music/funkysoul25.mp3" loop fadein 2.5
    scene mc laptop 1 with fade
    mc "Fuck yes!"
    mc "(I finally have a laptop!)"

    scene mc laptop 2 with dissolve
    mc "(I barely have any money left over from what Thorne gave me, but this will make some stuff much easier.)"
    mc "(And I hate browsing porn on my phone so it's a godsend!)"

    play music "audio/music/soulhotvintage-45.mp3" loop fadeout 2.0 fadein 2.0
    scene black
    show home_basement__night
    with fade

    return






label thorne_3_gettingcar_dialogue:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene getting car 1 with slowfade
    t "Hey, kid!"
    t "About time you showed up. Where the hell have you been?"
    mc "I have a life, you know..."
    t "Yeah, yeah, whatever."
    t "I got a surprise for you."
    t "Come with me, you're going to like this!"

    scene getting car 2 with slowfade
    mc "So, an old warehouse, a shady old man and a surprise."
    mc "Doesn't sound too good... {w} Should I be concerned?"
    t "Watch your tongue kid. I'm not that old."

    scene getting car 3 with dissolve
    t "There!"
    mc "You're giving me a car?"
    t "How do you like it?"
    mc "How do I like it?"

    scene getting car 4 with dissolve
    mc "Hmm, I guess it's a lot like you."
    mc "It has definitely seen better days."

    scene getting car 5 with dissolve
    t "As far as I know you don't have a car-"
    mc "I {i}have{/i} a car, but my dad-"
    t "Right, so as far as everyon else is concerned you're broke as hell and you don't have a car. Period."
    t "Now if you want to be an ungrateful little shit you can have Herbie The Love Bug over there."
    mc "Fine... I get it."
    mc "I guess I'll check it out..."

    scene getting car 6 with dissolve
    mc "Meh..."
    mc "It's better than nothing I guess."

    scene getting car 7 with dissolve
    mc "Definitely won't be picking up girls with this one though..."
    mc "But why are you giving me this car?"
    mc "I hope you don't expect me to pay for this piece of junk!"

    scene getting car 8 with dissolve
    t "It's not like you could pay for it..."
    t "You don't have dime, Harding boy."
    mc "..."
    mc "(Damn, he's actually right. Dad froze my credit cards - well, technically his credit cards, but still - and even took all the cash I had.)"
    mc "(It's been so long since I was home I don't even have a cash-stash here...)"
    mc "(Speaking of stash... Maybe I could retrieve the other one I left back at college.)"
    mc "(Although a road trip in this piece of junk is a gamble I don't really want to take...)"
    t "I got you this car because you'll need it soon."
    t "You work for me now, remember?"
    t "Maybe you should try to keep that in mind, kid."
    t "Now get out of here. I'll call when I need you."
    t "And one more thing... {w} Don't mention this warehouse to anyone. {w} Clear?"
    mc "Right."
    mc "Does the company has some kind of fuel benefit program by any chance?"
    t "You're testing my patience..."
    mc "Alright, alright, I'm going!"
    mc "And uh... {w}thanks."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return







label thorne_4_negotiation_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.0
    scene thorne negotiation 1 with slowfade
    t "Just in time."
    t "Take a seat right there, and shut your mouth."
    t "I want you to listen."
    mc "Hi to you too..."
    mc "(Asshole.)"

    scene black with fade
    show text "{size=72}{color=#dc38bf}A few moments later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve

    scene thorne negotiation 2 with slowfade
    t "Mikey, Mikey!"
    t "Long time no see, huh?"
    mikey "Can't say it's a pleasure, Thorne."

    scene thorne negotiation 3 with dissolve
    mikey "Who's the little pup over there?"
    t "He's [mc_name], a new associate of mine."
    mikey "I didn't know you're operating a kindergarten now..."


    menu:
        "Stay Silent":
            mc "..."
            mc "(This is bullshit...)"
            mikey "Is he a mute or what?"
            t "Alright, alright. Take a seat Mikey."
        "Insult":

            $ morality -= 1

            mc "Is this some kind of meeting for old farts and wannabe standup comedians?"
            t "Alright, alright. Take a seat Mikey, [mc_name] - shut the fuck up."
        "Threaten":

            $ morality -= 3
            $ mikey_threatened = True

            mc "Wanna be funny, huh?"
            mc "Why don't we see how funny you are with a broken nose?"
            t "Alright, alright. Take a seat Mikey, [mc_name] - shut the fuck up."


    scene thorne negotiation 4 with fade
    t "So, what do you have for me, Mikey?"
    mikey "It's getting hotter by the minute, Thorne!"
    mikey "These fuckers are getting serious, they are organizing."
    mikey "They really want to get their hands on the stuff."

    scene thorne negotiation 5 with dissolve
    t "That's not nearly enough. We already know that."
    mikey "That's all I have?"
    t "You're trying to tell me the fucking Russians don't know anything about the stuff?"
    mikey "Nobody knows shit!"
    mikey "It's been popping up here and there and everyone's been trying to replicate it ever since, but no success."

    scene thorne negotiation 6 with dissolve
    t "It's your fucking job to find out where it's popping up and who is the supplier!"
    t "That's why I'm paying you!"
    mikey "You're not paying me enough!"
    mikey "Being a rat in the Russian mob isn't exactly a safe occupation right now!"
    mikey "That's all the info I could get!"
    t "It's not enough!"
    mikey "I'm risking my ass everyday for this shit and this is what I get?"
    mc "(Looks like things are escalating.)"

    menu:
        "Stand up":
            pass

    scene thorne negotiation 7 with dissolve
    mikey "You can go and fuck yourself, Thorne!"
    t "You're forgetting what I've done for your sorry ass, Mikey!"
    t "Who the fuck got you out, huh?"
    t "It's only because of me that you can see your fucking wife!"

    menu:
        "Get closer":
            pass

    scene thorne negotiation 8 with dissolve
    t "You don't want to lose that, right?"
    mikey "Are you threatening me?!"

    scene thorne negotiation 9 with dissolve
    mikey "I told you already, this shit is too dangerous!"
    mikey "What good am I dead for my wife?!"
    mikey "I'm done with your bullshit!"

    menu:
        "Stay silent":

            $ morality += 1

            scene thorne negotiation 23 with dissolve
            mikey "Get yourself someone else to do your spying!"
            mikey "I'm done!"

            scene thorne negotiation 24 with slowfade
            mc "That probably didn't go as planned."
            t "Wow, you're a sharp kid, how did you know?"
            mc "No need for sarcasm, old man."

            scene thorne negotiation 25 with dissolve
            t "Alright, alright..."
            t "Mikey didn't bring us enough information, so we'll have to find some other methods to get to the bottom of this."

            scene thorne negotiation 24 with dissolve
            mc "What kind of info are we looking for anyway?"
            t "The new pills..."
            mc "What kind of pills?"
            mc "Is it that new sex drug thing?"

            scene thorne negotiation 25 with dissolve
            t "Exactly."
            t "People started calling it Halo..."
            mc "Interesting name for a drug."
            t "They say it increases the user's pleasure dramatically, like they are in heaven."
            t "It's also an aphrodisiac, naturally. {w} There are rumours about a powdered form with slightly different effects."
            t "If this thing is real - and it certainly looks like it is - then whoever controls the supply, controls the city."
            mc "And you want to control the supply?"
            t "No, I'm not that kind of guy. But if you're smart you keep your eye on the playing field."
            t "Midnight City has been divided up by gangs and crime families, but aside from small conflicts it's been mostly peaceful."
            t "This new stuff, however... {w} This will stir up the pot, and fast."
            t "Since Mikey here has underperformed, I'll have job for you soon. A real one this time."
            t "Keep your eyes open, you're playing with the big boys now, kid."
            mc "Alright."
            mc "(I hope that includes a fat paycheck as well, I'm getting low on cash here...)"
            t "I'll contact you soon. Now go."
        "Be violent":



            $ mikey_violence = True

            pause 0.2
            scene thorne negotiation 10 with vpunch
            mikey "Ugh!"

            scene thorne negotiation 11
            pause 0.5

            scene thorne negotiation 12 with dissolve
            pause

            scene thorne negotiation 13 with vpunch
            pause 0.6

            scene thorne negotiation 14 with dissolve
            pause 0.3

            scene thorne negotiation 15
            pause 0.3

            scene thorne negotiation 16
            pause 1.0

            scene thorne negotiation 17 with dissolve
            mikey "Ugh!!"
            mikey "What the fuck! You broke my nose!"
            if mikey_threatened:
                mc "Still feeling funny? Huh?"

            scene thorne negotiation 18 with dissolve
            t "Get the fuck out of here Mikey, and bring me more info!"
            t "I wanna know where those fucking pills come from!"
            mikey "Ah fuck... {w} Fuck you Thorne!"
            t "Did you say something?"

            scene thorne negotiation 19 with dissolve
            mc "..."
            t "The fuck was that?"
            t "Didn't I tell you sit down and shut it?"

            scene thorne negotiation 20 with dissolve
            mc "I thought you might need some help!"

            scene thorne negotiation 21 with dissolve
            t "Next time let me know if you're planning to bash the skull of my informant with a damn clock."
            mc "Where's the power of surprise then?"
            t "Alright, alright..."
            t "At least I know you're not afraid to get your hands dirty."
            t "Mikey didn't bring us enough information, so we'll have to find some other methods to get to the bottom of this."

            scene thorne negotiation 20 with dissolve
            mc "What kind of pills are we talking about anyway?"
            mc "Is it that new sex drug thing?"

            scene thorne negotiation 21 with dissolve
            t "Exactly."
            t "People started calling it Halo..."
            mc "Interesting name for a drug."
            t "They say it increases the user's pleasure dramatically, like they are in heaven."
            t "It's also an aphrodisiac, naturally. {w} There are rumours about a powdered form with slightly different effects."
            t "If this thing is real - and it certainly looks like it is - then whoever controls the supply, controls the city."
            mc "And you want to control the supply?"
            t "No, I'm not that kind of guy. But if you're smart you keep your eye on the playing field."
            t "Midnight City has been divided up by gangs and crime families, but aside from small conflicts it's been mostly peaceful."
            t "This new stuff, however... {w} This will stir up the pot, and fast."
            t "Since Mikey here has underperformed, I'll have job for you soon. A real one this time."
            t "Keep your eyes open, you're playing with the big boys now, kid."
            mc "Alright."
            mc "(I hope that includes a fat paycheck as well, I'm getting low on cash here...)"
            t "I'll contact you soon. Now go."

            scene black with fade
            scene thorne negotiation 22 with fade
            t "Haha!"
            t "Youth..."


    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return






label thorne_6_clubofficeintro_dialogue:

    play music "audio/music/funkysoul25.mp3" loop fadeout 2.0 fadein 2.0
    scene nightclub intro 1 with slowfade
    thorne "Hey kid."
    thorne "It's time I gave you a real job."
    mc "What is it?"
    thorne "I need you to get some of that Halo."
    mc "The drug that every member of the underworld in this city want their hands on?"
    thorne "You're being overdramatic. It's not a miracle pill, it's just that the quantity is low and the demand is high."

    scene nightclub intro 2 with dissolve
    mc "And why do you need that?"
    thorne "I have a guy who can analyze it. We need to know more about this stuff."
    thorne "Might be a good way to figure out where it's coming from, eh?"
    thorne "Now here's the plan."

    scene nightclub intro 1 with dissolve
    thorne "You'll go to The Tempest Club tonight, I already arranged everything, they'll let you through."
    mc "I'm on the list?"
    thorne "Yeah, yeah..."
    mc "And why do I have to go? Why don't you just go and get it yourself?"
    thorne "You're the rich boy druggie, dipshit. Getting this shit is like second nature for you, right?"
    mc "Fuck you, man..."
    thorne "Don't take it too seriously.{w} Thing is, they don't really appreciate my great self in that club... It's kind of a long story."
    mc "Then why that club?"
    thorne "It's mostly high rollers there. This thing ain't cheap so if anyone wants to sell some, it's a good place to look."
    thorne "Get in, get the stuff and bring it to the office."

    scene nightclub intro 2 with dissolve
    thorne "And of course, tell-"
    mc "Yeah yeah, tell nobody."
    thorne "Do this, and you'll get a nice reward."
    mc "It better be worth it, old man..."
    thorne "And put on a fucking shirt for once!"
    mc "Ugh...."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label thorne_8_givepills_dialogue:

    play music "audio/music/loopster.mp3" loop fadeout 2.0 fadein 2.5
    scene thorne pills 1 with slowfade
    t "Finally!"
    t "Have you got it?"
    mc "Yeah, hello to you too!"
    t "Oh, you wanna have some small talk?"
    t "You might have missed the door then, the manicure salon is two to the left!"
    mc "Jesus, man, calm the fuck down."

    scene thorne pills 2 with fade
    mc "Here's your fuckin pill."
    mc "(I'm not going to give him the second one. It's better if he doesn't know at all.)"
    mc "(If it's as good as they say it is, I think I'll have a use for it myself later.)"

    scene thorne pills 3 with fade
    t "Hmmm..."
    t "Well, well, well!"

    scene thorne pills 4 with dissolve
    t "Looks like I was right when I got you out of the dump."
    t "You're not half bad, kid."
    t "This will get me a lead in no time!"
    mc "Get {i}us{/i} a lead, right?"
    t "Oh, yes of course. Us..."

    scene thorne pills 5 with fade
    t "Now if this turns out to be the real deal, that proves you're not a dimwit."
    t "I got a hunch that it's the right stuff. I got another assignment for you."
    mc "There was supposed to be a reward for getting the pill..."
    t "Until I know for certain this isn't some kind of stupid trick and you're not using a fake to get some easy cash, I can't give you anything, can I?"
    t "You know how it is kid, I trust you but you can never be too careful."
    mc "Uh-huh..."
    t "However, the next job pays upon delivery."
    mc "What do you mean?"
    t "One of my clients crashed their pricey car and the insurance doesn't want to pay."
    t "Now of course he turned to me with his problem because he knows I can take care of everything around here."
    t "So your job is to go to a specific garage, and bring the car inside to the drop-off point."
    mc "I have to drive the crashed car?"
    t "No, of course not! I would never do that to you!"
    t "This is another car. The same model, same color, but a new one. Insurance doesn't want to pay so we'll get him a new one! Easy!"
    mc "Hold up... {w} You want me to steal a car, don't you?"
    mc "I sure as hell won't steal a car for some asshole client of yours!"

    scene thorne pills 6 with dissolve
    t "That's a shame..."
    t "This would have landed you twenty grand, but I guess I'll have to tell my client that my associate is a little pussy and we can't handle his case..."
    mc "(Twenty thousand bucks?! That's enough to start some kind of business to take on Logan!)"
    mc "(I do this job and I'm out! I have to take this chance!)"
    mc "What's the address?"
    t "Attaboy!"
    t "Take this note, the details are written here."
    t "Your payment will be at the drop-off point."
    t "And kid...{w} Don't fuck this up!"
    pause 0.5

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label eliana_3_breakin_dialogue:

    play music "audio/music/funnysneaky.mp3" loop fadeout 2.0 fadein 2.5
    scene eliana breakin 8 with slowfade
    e "So why exactly have you made me meet you in an office building in the middle of the night?"
    mc "I'm choosing the third option."
    e "Which is...?"

    scene eliana breakin 9 with dissolve
    mc "Which is the one where I take control of the situation."
    e "First grand theft auto, and now breaking and entering?"
    e "You're sure adding a lot to your criminal record lately, [mc_name]."
    mc "It's not a crime if you don't get caught, right? Hehe!"
    e "That's not... Ugh, forget it."
    pause 0.7
    mc "Done!"

    scene eliana breakin 10 with dissolve
    e "Wanna tell me the plan now that you have already made me your accomplice?"
    mc "When I handed Thorne the Halo pill, he said he's going to get to the source from that."
    mc "I have no idea how, he seems to have a guy for it."
    mc "In any case, if he has the location, the data on it is probably here in his office."
    e "Why would he keep it here?"
    mc "He has a stupid habit of writing down important information on notes, like the details of a crime."
    mc "But I don't know, it's just a feeling. We have to look."
    mc "Come on."

    scene eliana breakin 11 with fade
    mc "Alright, I think I'll look around over there."
    mc "The PC is password protected so it's going to be a hard one."
    mc "You could just-"

    scene eliana breakin 13 with fade
    e "Hmm, this is interesting..."
    e "I'm checking out his e-mails."
    mc "Wait, what?"
    mc "Did he leave it unlocked?"

    scene eliana breakin 14 with dissolve
    e "You can break physical locks. I can break digital ones."
    mc "Where the hell did you learn that?"

    scene eliana breakin 15 with dissolve
    e "I had a roommate when I was in the exchange program."
    e "She was a computer nerd. I learned a thing or two from her."
    e "She also gifted me with a thumb drive that I can use in situations like these."
    e "Although it was intended more for breaking into a boyfriend's laptop or something. But... it works."

    scene eliana breakin 14 with dissolve
    mc "Damn..."
    mc "Wait, you have a boyfriend?"
    e "{i}A boyfriend{/i}, not my boyfriend, [mc_name]."
    mc "Oh, yeah, got it!"
    e "I got it too, I found the GPS coordinates of the place."
    mc "Fuck yes! You are awesome!"

    scene eliana breakin 16 with dissolve
    e "Haha, I didn't think this would work!"
    e "But you didn't tell me why you needed this?"
    mc "Both Tanya and Thorne want to control me and go for this new miracle drug."
    mc "I want to get to it first. Otherwise I'll just be pushed around and discarded when I'm not needed anymore."
    mc "Fuck if I'll let that happen."
    e "And what happens if you find the source?"
    mc "It's not if, it's when. And when I do find it, I'll have a pretty big bargaining chip."
    mc "And we are going right now!"
    e "{i}*Sigh...*{/i} {w} I knew you were gonna say that."
    e "Let me go back home first... {w} I'll meet you at dawn at the place. I'll text you the GPS location."
    mc "Okay. Now what do you say we get the hell out of here before someone notices us?"
    e "Agreed!"

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
