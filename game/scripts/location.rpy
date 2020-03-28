init -100 python:

    class MoveTo(Action):
        def __init__(self, location):
            self.location = location
        
        def __call__(self):
            store.current_room = self.location.name
            renpy.jump(store.current_room)


init -1 python:

    class Location():
        def __init__(self, display_name, name, unlocked=True, toolbar_enabled=True, can_leave=True, first_visit=True):
            self.display_name = display_name
            self.name = name
            self.unlocked = unlocked
            self.toolbar_enabled = toolbar_enabled
            self.can_leave = can_leave
            self.first_visit = first_visit


    def go_to(location):
        store.current_room = location.name
        renpy.jump(store.current_room)











default L_home_basement = Location("Basement", "home_basement")
default L_home_bathroom = Location("Bathroom", "home_bathroom")
default L_home_hall = Location("Hall", "home_hall")
default L_home_hall2 = Location("Hall #2", "home_hall2")
default L_home_isabelroom = Location("Isabel's room", "home_isabelroom")
default L_home_kitchen = Location("Kitchen", "home_kitchen")
default L_home_livingroom = Location("Living room", "home_livingroom")
default L_home_loganroom = Location("Logan's room", "home_loganroom", unlocked=False)
default L_home_momroom = Location("Joyce's room", "home_momroom")
default L_home_pool = Location("Pool", "home_pool", unlocked=False)
default L_home_rubyroom = Location("Ruby's room", "home_rubyroom")
default L_home_study = Location("Study", "home_study", unlocked=False)


default L_school_entrance = Location("School Entrance", "school_entrance")
default L_school_hall = Location("School Hall", "school_hall")
default L_school_janeoffice = Location("Ms. Jane's Office", "school_janeoffice")
default L_school_lecturehall = Location("Lecture Hall", "school_lecturehall")
default L_school_library = Location("School Library", "school_library")


default L_thorneoffice_office = Location("Thorne's Office", "thorneoffice_office")


default L_streets_street = Location("Streets", "streets_street")


default L_boutique_store = Location("Boutique", "boutique_store")


default L_nightclub_bar = Location("Nightclub Bar", "nightclub_bar", toolbar_enabled=False, can_leave=False)
default L_nightclub_dancefloor = Location("Nightclub Dancefloor", "nightclub_dancefloor")
default L_nightclub_lounge = Location("Nightclub Lounge", "nightclub_lounge")
default L_nightclub_restroom = Location("Nightclub Bathroom", "nightclub_restroom")


default L_janehome_porch = Location("Ms. Jane's Home", "janehome_porch", toolbar_enabled=False, can_leave=False)
default L_janehome_side = Location("Ms. Jane's Home", "janehome_side")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
