
#Intro message
print("What level of brightness is required?")

#User input
brightness = int(input())
print("")

#for loop
for count in range (2, brightness + 1, 2):
    #range explained:
    #This range generates even numbers
    #it does so by starting at 2
    #it ends at the user's input +1 (this rounds it up to an even number)
    #the step is also set at 2, to only display even numbers
    #in between the start and the end of the range

    print("Beep's brightness level: " + "*" * count)
    print("Bop's brightness level: " + "*" * count)
    print("")

#Final message
print("Adjustment complete!")