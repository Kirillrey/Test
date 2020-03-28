define config.version = "Elite-0.6-Remake"



init python:
    build.archive("audio", "all")
    build.archive("images", "all")
    build.archive("scripts", "all")
    build.archive("videos", "all")




    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("game/**.rpy", None)












    build.classify("game/audio/**", "audio")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.ttf", "images")

    build.classify("game/**.rpyc", "scripts")

    build.classify("game/videos/**", "videos")

    build.classify("game/images/Elite/videos/**", "videos")




























    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
