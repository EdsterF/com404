from bot import Bot

class SuperBot(Bot):

    #constructor
    def __init__(self, name, age=0, super_power_level=100):
        super().__init__(name, age)
        self.super_power_level = super_power_level
    
    #methods
    def super_power_level(self):
        super_power_level = (int)

    def get_super_power_level(self):
        return self.super_power_level

    def set_super_power_level(self, power_level):
        self.super_power_level = power_level