#Intro question
print("How many zones must I cross?")

#Variables
zones_max = int(input())
zones_min = 0

print("Crossing zones...")

#Decisions
while (zones_max > zones_min):
    print("...crossed zone", zones_max)

    zones_max=zones_max-1

#End message
print("Crossed all zones. Jumanji!")