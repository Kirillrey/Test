


default morality = 0


default ruby_influence = 0




default isabel_lust = 0




default mom_yoga3_complimented = False




default mikey_threatened = False
default mikey_violence = False




default viktor_threatened = False









default mom_level = 1
default mom_massage_level = 1
default mom_seen_massage_level = 0
default mom_massage_counter = 0
default mom_yoga_level = 1
default mom_seen_yoga_level = 0
default mom_yoga_counter = 0
default mom_tv_level = 1
default mom_seen_tv_level = 0
default mom_tv_counter = 0
default mom_night_counter = 0
default mom_visited_tonight = False
default m_ns_jerkoff = NightScene("Jerk off", 1, unlocked=True)
default m_ns_usefeet = NightScene("Use feet", 1, unlocked=True)
default m_ns_useass = NightScene("Use ass", 2)
default m_ns_titfuck = NightScene("Titfuck", 3)
default mom_delay = 0

default isabel_level = 1
default isabel_massage_level = 1
default isabel_seen_massage_level = 0
default isabel_massage_counter = 0
default isabel_tv_level = 1
default isabel_seen_tv_level = 0
default isabel_tv_counter = 0
default isabel_night_counter = 0
default isabel_visited_tonight = False
default i_ns_touchtits = NightScene("Touch tits", 1, unlocked=True)
default i_ns_jerkoff = NightScene("Jerk off", 1, unlocked=True)
default i_ns_usehand = NightScene("Use hand", 1, unlocked=True)
default i_ns_usefeet = NightScene("Use feet", 2)
default i_ns_rubpussy = NightScene("Rub pussy", 3)
default i_ns_assjob = NightScene("Assjob", 3)
default isabel_delay = 0

default ruby_level = 1
default ruby_massage_level = 1
default ruby_seen_massage_level = 0
default ruby_massage_counter = 0
default ruby_tv_level = 1
default ruby_seen_tv_level = 0
default ruby_tv_counter = 0
default ruby_night_counter = 0
default ruby_visited_tonight = False
default r_ns_gropeass = NightScene("Grope ass", 1, unlocked=True)
default r_ns_jerkoff = NightScene("Jerk off", 1, unlocked=True)
default r_ns_usefeet = NightScene("Use feet", 1, unlocked=True)
default r_ns_assjob = NightScene("Assjob", 2)
default r_ns_fingerpussy = NightScene("Finger pussy", 3)

default jane_level = 1
default jane_tutoring_counter = 0

default aunt_level = 1
default aunt_visited_tonight = False
default aunt_ns_jerkoff = NightScene("Jerk off", 1, unlocked=True)
default aunt_ns_thighjob = NightScene("Thighjob", 1, unlocked=True)

default thorne_level = 1
default eliana_level = 1
default tanya_level = 1
default natsuko_level = 1
default dad_level = 1

default logan_level = 1
default logan_insulted = False

default mc_tv_level = 1
default mc_seen_tv_level = 0
default mc_tv_counter = 0







default laptop_owned = False
default ruby_logan_in_kitchen = False



default jane_on_sick_leave = False
default tutoring4_liftdress_seen = False
default tutoring4_touchbutt_seen = False
default tutoring4_feet_seen = False
default tutoring4_caress_seen = False

default nc1_chair = False
default nc1_bartender = False
default nc1_melissa = False
default nc1_tanya = False
default nc1_natsuko1 = False
default nc1_natsuko2 = False
default nightclub1_complete = False



default isabel_sunscreen_failed = False
default thorne_office_unlocked = False



default aunt_feet = False








default money = 0

default time_of_day = 0
default time_of_day_name = ""
default time_of_day_names = ("", "Morning", "Afternoon", "Evening", "Night")

default day_of_week = 0
default day_of_week_name = ""
default day_of_week_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

default day_count = 0



default days_since_been_to_class = 0
default all_toolbars_enabled = True
default current_room = None











default prologue_mom = 0
default prologue_isabel = 0
default prologue_ruby = 0
default prologue_logan = 0
default seen_hall_wallphoto = False
default seen_hall2_wallphoto = False









init -999 python:
    game_type = "general"
    extras_installed = False
    elite_installed = False




init -1 python:
    config.audio_directory = None


define config.window_auto_hide = [ 'scene', 'call screen', 'menu', 'pause' ]
































init python:

    def theme_path(folder):
        return "gui/themes/" + persistent.current_theme + "/" + folder + "/"

    def name_func(newstring):
        store.save_name = newstring + "::ELT"

    def mp_notify(message):
        if persistent.notify_users:
            renpy.notify(message)

default persistent.font_name = "Louis George Cafe.ttf"
default persistent.font_size = 30

default persistent.notify_users = True
default persistent.current_theme = "default"

init 1 python:
    if renpy.mobile:
        persistent.font_size = 40






init -1 python:

    class NightScene:
        def __init__(self, name, tier, unlocked=False, seen=False):
            self.name = name
            self.tier = tier
            self.unlocked = unlocked
            self.seen = seen
        
        @property
        def text(self):
            if self.seen:
                return ""
            else:
                return " (New)!"





default temp_1 = ""
default temp_2 = ""
default temp_3 = ""
default temp_4 = ""
default temp_5 = ""

init python:
    def mom_massage_text(level):
        if store.mom_seen_massage_level < level:
            return " (New)!"
        else:
            return ""
    def mom_tv_text(level):
        if store.mom_seen_tv_level < level:
            return " (New)!"
        else:
            return ""

    def isabel_massage_text(level):
        if store.isabel_seen_massage_level < level:
            return " (New)!"
        else:
            return ""
    def isabel_tv_text(level):
        if store.isabel_seen_tv_level < level:
            return " (New)!"
        else:
            return ""

    def ruby_massage_text(level):
        if store.ruby_seen_massage_level < level:
            return " (New)!"
        else:
            return ""
    def ruby_tv_text(level):
        if store.ruby_seen_tv_level < level:
            return " (New)!"
        else:
            return ""

    def mc_tv_text(level):
        if store.mc_seen_tv_level < level:
            return " (New)!"
        else:
            return ""




init -999 python:
    lain_mod = False
default lain_mod_saw_laptop_scene = False


default lm_extra_02_isabel_lotion = False
default lm_extra_03_ruby_masturbate = False

default lm_extra_04_mom_jane = False
default lm_extra_05_isabelRuby_pool = False
default lm_elite_05_ruby_dinner3 = False
default lm_extra_06_ruby_shave = False

default lm_elite_06_momAunt_cooking = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
