from Bot import Bot

class Super_Bot (Bot):

    #constructor
    def __init__(self, name, age=0, super_power_level=100):
        super().__init__(name, age)
        self.super_power = super_power
    
    #methods
    def get_super_power(self):
        return self.super_power_level
    
    def set_super_power_level(self, super_power_level):
        self.set_super_power_level = super_power_level