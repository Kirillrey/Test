init -1 python:

    class ShopItem:
        def __init__(self, price, purchased=False, own_item=False, used=False):
            self.price = price
            self.purchased = purchased
            self.own_item = own_item
            self.used = used
            self.delivery_delay = 0
        
        def buy(self):
            store.money -= self.price
            self.purchased = True
            
            if time.is_time(1, 2, 3):
                self.delivery_delay = 1
            else:
                self.delivery_delay = 2
        
        def calc_delivery(self):
            if not self.own_item and self.purchased and self.delivery_delay > 0:
                self.delivery_delay -= 1
        
        def check_morning_event(self):
            if not self.own_item and self.purchased and self.delivery_delay == 0:
                return True
            else:
                return False



default sleeping_pills = ShopItem(10)
default isabel_sunscreen = ShopItem(5)
default jane_vibrator = ShopItem(100)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
