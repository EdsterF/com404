from Bot import Bot
from FlyingBot import FlyingBot
from SuperBot import SuperBot

bop = Bot("bop")

bop.display_name()
bop.display_age()
bop.display_energy()
bop.display_shield()
print()

ed = SuperBot("ed")

print("The {}'s power level is: {}".format(ed.get_name(), ed.get_super_power_level()))
print()

beep = FlyingBot("Beep Bop")

print("{}'s hover distance is: {}".format(beep.get_name(), beep.get_hover_distance()))
print()