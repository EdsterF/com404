#Intro message
print("How many zones must I cross?")

#User input
zones_max= int(input())

print("Crossing zones...")

print("...crossed zone", zones_max)

zones_min= 1

while (zones_max > zones_min):
    
    zones_max=zones_max-1
    print("...crossed zone", zones_max)

print("Crossed all zones. Jumanji!")