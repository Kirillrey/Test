label ruby_3_storejob_dialogue:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene boutique_store__day_manager with slowfade
    mc "(This is as good a shop as any. Let's see if I can score this bet on the first try.)"

    scene ruby store 5 with dissolve
    clerk "Can I help you with something, young man?"
    mc "Yeah, actually."
    mc "My sister is looking for a job and I decided to help her out by asking around in the boutiques around town if they need a hand somewhere."
    clerk "How nice of you to do that!"

    scene ruby store 6 with dissolve
    clerk "We are actually hiring!"
    clerk "I'm the manager, but I'm starting to get a bit too old for the long shifts."
    clerk "We'd need someone in the store from time to time. The pay isn't that great, but it's fair money for a young lady."
    mc "Sounds perfect, old man!"
    if not lain_mod:
        clerk "Tell me, is she pretty?"
        mc "You bet!"
        clerk "Good, good..."
        clerk "Pretty employees attract more customers, I mean."
        mc "Sure..."
        mc "(The old fart seems weird enough, but I guess he just wants to creep a bit.)"
        mc "(Well, can't fault him for that, at that age that's probably all you get.)"
        mc "(That will maybe help with Ruby's fuckin attitude a bit.)"
    else:
        mc "(This will maybe help with Ruby's fuckin attitude a bit.)"
    mc "We got ourselves a deal then. I'll send her to the store."

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return






label ruby_6_workshift_dialogue:

    scene store mc 1 with fade
    mc "(Fuckin Ruby, making me cover for her in this shitty store...)"
    mc "(At least now I know working in retail isn't my true calling in life, that's for sure.)"
    mc "(The dress up show Ruby gave me was definitely worth it though.)"

    scene black with slowfade

    return






label ruby_11_changingroom_dialogue:

    play music "audio/music/playtime.mp3" loop fadeout 2.0 fadein 2.0
    if _in_replay:
        call setup_gallery
        scene ruby changing booth intro 3
    else:
        scene ruby changing booth intro 1 with slowfade
        ruby "(This is the most boring job ever.)"
        ruby "(Nobody comes in here and even if they do it's annoying.)"
        ruby "(Putting a mannequin here would do the trick just as well as me standing here.)"

        scene ruby changing booth intro 2 with dissolve
        mc "So, I see you actually can come into work."

        scene ruby changing booth intro 3 with dissolve
    ruby "[mc_name]!"
    ruby "It's so great to see you!"

    scene ruby changing booth intro 4 with dissolve
    mc "You being that happy to see me? That's suspicious..."
    ruby "I'll just let that slide, because I know you're such a good brother and you'll do me a favor, right?"
    mc "I knew it!"
    ruby "Pretty please?"
    mc "Alright, what do you want?"
    ruby "There are some clothes I wanna buy but I have to try them on first. Can you watch the store until I'm done?"
    mc "Fine! Just don't take hours!"


    stop music fadeout 10.0
    scene black with fade
    show text "{size=72}{color=#dc38bf}A very long time later...{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(2.5, hard=True)
    hide text with dissolve


    scene ruby changing booth intro 5 with fade
    mc "Done yet?"
    ruby "No! I only came in here like 2 minutes ago!"
    mc "...."
    mc "(2 minutes my ass.)"
    mc "(Taking advantage of my good will?)"

    scene ruby changing booth intro 6 with dissolve
    mc "(I'll have some fun as well, then.)"
    mc "I'm coming in!"

    play music "audio/music/soulhotvintage.mp3" loop fadein 2.0
    scene ruby changing booth intro 7 with fade
    mc "Oh, looking good sis!"
    ruby "What the hell [mc_name]?"
    ruby "What are you doing in here?"

    scene ruby changing booth intro 8 with dissolve
    mc "Right now?"
    mc "Admiring my beautiful sister's choice of clothing for today."
    mc "Showing off some skin I have to admit, but I'm all for that!"

    scene ruby changing booth intro 8 with dissolve
    ruby "And who's watching the store?"
    mc "Ah whatever, nobody comes in here ever anyways."

    scene ruby changing booth intro 9 with dissolve
    clerk "Ruby? Are you in the changing room?"
    ruby "Yeah, uhm, I'm here!"

    scene ruby changing booth intro 10 with dissolve
    ruby "Great, it's the manager!"
    ruby "You are an idiot!"
    ruby "It's already bad that I'm in here in my underwear, but if he finds you in here with me we're so done!"
    ruby "Now hide you idiot! Quick!"

    scene ruby changing booth 1 with fade
    clerk "Are you cleaning up in there?"
    ruby "Y-yeah! Exactly!"
    mc "(Not the best hiding spot, but there aren't too many hiding spots in a changing room.)"
    mc "(It has a nice 'vantage point' however, hehe.)"
    mc "(I think I'll teach her a lesson...)"

    scene ruby changing booth 3 with dissolve
    ruby "Oh!"
    clerk "Are you alright? Do you need any help?"
    ruby "Yeah, it's just that when I was cleaning uhm..."

    scene ruby changing booth 2 with dissolve
    ruby "I spilled some water over my clothes so I uh.. I think I probably need to change."
    mc "(Mhmm, such a nice little butt, I love it!)"
    mc "(She's probably staring right at his face while I'm groping her ass right now, haha.)"

    scene ruby changing booth 4 with dissolve
    clerk "Oh, okay."
    clerk "I wanted to talk to you about the new inventory."
    ruby "S-sure! Can you wa-"
    clerk "I think the new clothes will be fabulous!"

    scene ruby changing booth 2 with dissolve
    mc "(Oh, he's staying!)"
    mc "(I think I can make this conversation more 'enjoyable' for Ruby!)"


    menu:
        "Go for tits":

            scene ruby changing booth tits 1 with dissolve
            mc "(Alright, this is going to be a lot of fun, haha!)"

            scene ruby changing booth tits 2 with dissolve
            mc "(Now just the right amount of force...)"

            scene ruby changing booth tits 3 with fade
            mc "(And it's done!)"
            clerk "Next week, when everything arrives I'll need you at the store for a bit longer, and-"

            scene ruby changing booth tits 4 with dissolve
            mc "(Just a little pinch...)"
            scene ruby changing booth tits 4 with vpunch
            ruby "Ah!"
            clerk "Are you sure you're okay in there?"

            scene RubyChangingroomTits1 with dissolve
            pause
            ruby "Yeah, it's uhm... Ah~"
            ruby "I'm fine!"
            ruby "I'm just kind of in a {b}pinch{/b} right now."
            ruby "With the clothes and everything, you know? Ah ahah"
            mc "(Oh, that nervous laughter...)"
            mc "(Her nipples are hard as stone!)"
            mc "(I'm pretty sure she's aroused by this. Tsk tsk tsk... {w} Ruby, you little perv!)"

            scene ruby changing booth 4 with dissolve
            clerk "Hahaha! Luckily, it's a clothes store!"
            clerk "You're not in a real pinch!"

            scene RubyChangingroomTits2 with dissolve
            pause
            ruby "Oh, it definitely feels - Ah! - Real!"
            mc "(This is amazing!)"
            clerk "Alright, I'll wait outside until you change, then I have to leave for the day."
            ruby "Oh, that would be great!"
            ruby "I mean, thanks for waiting until I get dressed! I mean, change!"
            clerk "I'll be just outside!"
            pause 1.0

            scene ruby changing booth outro tits 1 with vpunch
            ruby "Are you completely out of your mind?!"
            mc "Ouch!"
            mc "You hit me on the head!"

            scene ruby changing booth outro tits 3 with dissolve
            ruby "And be glad you get away with only that!"
            ruby "I should kick you in the balls for this!"
            mc "(She's really mad this time.)"
            mc "(I should just shut up.)"
            mc "You're cute when you're angry."

            scene ruby changing booth outro tits 2 with dissolve
            mc "Especially when you're topless and in those tiny little thongs."
            mc "You really look like a fiery little waifu!"

            scene ruby changing booth outro tits 4 with dissolve
        "Go for panties":



            scene ruby changing booth ass 1 with dissolve
            mc "(Alright, this is going to be a lot of fun!)"

            scene ruby changing booth ass 2 with dissolve
            mc "(I have to do it quick, before she can wiggle that fine piece of ass out of my hands...)"

            scene ruby changing booth ass 3 with vpunch
            pause 1.0
            ruby "Hah!"
            mc "(And done!)"
            mc "(And what a view!)"
            clerk "Next week, when everything arrives I'll need you at the store for a bit longer, and-"

            scene RubyChangingroomPussy1 with dissolve
            pause
            ruby "Oh God!"
            clerk "Are you sure you're okay in there?"

            scene ruby changing booth ass 4 with dissolve
            ruby "Yeah, it's uhm... Ah~"
            ruby "I'm fine!"
            ruby "I'm just a bit sore I think."
            clerk "Oh, I think a good back rub would help."

            scene RubyChangingroomPussy1 with dissolve
            pause
            ruby "Oh, I'm surely getting a good rubbing alright! Ahah ah!"
            mc "(Oh, that nervous laughter...)"
            mc "(She's getting wetter by the minute!)"
            mc "(Getting aroused by this? Tsk tsk tsk... {w} Ruby, you little perv!)"

            clerk "Alright, I'll wait outside until you change, then I have to leave for the day."
            ruby "Oh, that would be great!"
            ruby "I mean, thanks for waiting until I get dressed! I mean, change!"
            clerk "I'll be just outside!"
            ruby "Ahh~"
            ruby "I'll be coming soon, too!"
            mc "(Oh I'm sure you will...)"
            pause 1.0

            scene ruby changing booth outro ass 1 with vpunch
            ruby "Are you completely out of your mind?!"
            mc "Ouch!"
            mc "You hit me on the head!"

            scene ruby changing booth outro ass 3 with dissolve
            ruby "And be glad you get away with only that!"
            ruby "I should kick you in the balls for this!"
            mc "(She's really mad this time.)"
            mc "(I should just shut up.)"
            mc "You're cute when you're angry."

            scene ruby changing booth outro ass 2 with dissolve
            mc "Especially when you're dripping wet from that!"
            mc "You really look like a fiery little waifu!"

            scene ruby changing booth outro ass 4 with dissolve


    ruby "Get.{w} The.{w} FUCK.{w} OUT!"
    mc "Geez, fine!"
    mc "(I'm sure she'll calm down.)"

    $ renpy.end_replay()

    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0
    scene black with slowfade

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
