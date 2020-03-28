label isabel_3_crying_dialogue:

    play music "audio/music/soulhotvintage.mp3" loop fadeout 2.0 fadein 2.0
    scene home isa crying 1 with slowfade
    mc "(What? Isabel's Crying?)"
    mc "(I should probably check up on her to see what's the matter.)"
    mc "Hey?"
    mc "What's the matter Isabel?"

    scene home isa crying 2 with dissolve
    isa "Nothing..."
    mc "(Here we go... typical woman.)"
    mc "You're crying just for fun then?"
    isa "I'm not crying!"
    isa "Leave me alone..."

    scene home isa crying 3 with dissolve
    mc "My sister is crying, so I'm not leaving until I find out what happened."
    mc "Did someone hurt you?"
    isa "No..."
    isa "It's Josh..."
    mc "And Josh is...?"
    isa "You can be such an ass at time, [mc_name]. {w} He's my boyfriend!"
    mc "(Now I'm the ass because she never bothered to tell me about her boyfriend?)"
    mc "Right, right, he is. Sorry, I'm not good with names you know, hehe."
    mc "So what's the matter?"
    mc "Did you two have a fight?"

    scene home isa crying 4 with dissolve
    isa "Yeah..."
    isa "He told me he would change, and it looked like me moving here made him get his shit together but..."
    mc "But?"

    scene home isa crying 5 with dissolve
    isa "He was using again!"
    mc "Using? You mean drugs? Did he tell you?"
    isa "His colleague told me..."
    mc "(I'm trying to untangle this but it's getting more tangled by the minute. Isa's boyfriend is a druggie?)"
    mc "I thought this guy is from a respectable family and has had a nice education and stuff like that."

    scene home isa crying 6 with dissolve
    isa "It's all true, but the pressure his family is putting on him and the amount of work he has to do..."
    isa "It's getting to him. There's a shortage of medical personnel in the city and he has to work very long hours."
    isa "He told me that's why he takes drugs, to be able to handle to load."
    isa "But he's been taking it on his off days too, when he was with me or when we travelled together."
    isa "He did it cleverly, until I found out."
    isa "He's trying to come back to me but I don't know what to do..."
    mc "(Damn... I can't say I know exactly how the dude feels, but it sure is easy to get hooked on blow.)"

    scene home isa crying 7 with dissolve
    mc "Well, if he's addicted he should go to rehab, or at least get some help from somewhere."
    mc "You know, friends and loved ones. It sounds like he got a little hooked but maybe it's not all that bad."
    mc "Not that I know too much about your situation together, but you should encourage him to get some help."

    scene home isa crying 8 with dissolve
    mc "Being on that shit and being alone on top of it makes it a lot harder to stop."

    scene home isa crying 9 with dissolve
    isa "[mc_name], you're such a kind guy."
    isa "Really."

    scene home isa crying 10 with dissolve
    mc "Wha-"
    isa "I'm happy I have a brother like you!"

    if not lain_mod:
        mc "(It's not like I want them to make up or anything, I'm just being objective here. I think she should stay away until he comes clean and-)"

        scene home isa crying 11 with dissolve
        isa "You're right, I'm going to make up with him. {w} I'll help him get through this. Together."
        isa "I'm going to call him right now! {w} Thank you [mc_name]!"

        scene home isa crying 12 with dissolve
        mc "(Well... {w} That could have gone better.)"
        mc "(She's doing the exact opposite of what I wanted to suggest her.)"
        mc "(It's always difficult talking to women about emotions and stuff.)"
        mc "(We'll see what comes out of this then...)"

    scene black with slowfade
    play music "audio/music/soul.mp3" loop fadeout 2.0 fadein 2.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
