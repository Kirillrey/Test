init -2 python:

    def increase_time(num=1):
        if store.time_of_day < 4:
            store.time_of_day += num
            
            if store.time_of_day > 4:
                store.time_of_day = 4
            store.time_of_day_name = store.time_of_day_names[store.time_of_day]



    def set_time(num):
        store.time_of_day = num
        store.time_of_day_name = store.time_of_day_names[store.time_of_day]



    class time:
        
        @staticmethod
        def is_morning():
            return store.time_of_day == 1
        
        @staticmethod
        def is_afternoon():
            return store.time_of_day == 2
        
        @staticmethod
        def is_evening():
            return store.time_of_day == 3
        
        @staticmethod
        def is_night():
            return store.time_of_day == 4
        
        
        @staticmethod
        def is_daytime():
            return store.time_of_day == 1 or store.time_of_day == 2
        
        @staticmethod
        def is_nightime():
            return store.time_of_day == 3 or store.time_of_day == 4
        
        
        @staticmethod
        def is_time(*time_periods):
            return store.time_of_day in time_periods
        
        
        
        @staticmethod
        def day_count():
            return store.day_count
        
        
        
        @staticmethod
        def is_dayofweek(*days):
            return store.day_of_week in days
        
        @staticmethod
        def is_weekday():
            return time.is_dayofweek(1, 2, 3, 4, 5)
        
        @staticmethod
        def is_weekend():
            return time.is_dayofweek(0, 6)



    class SkipTime(Action):
        def __call__(self):
            increase_time()
            renpy.jump(store.current_room)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
