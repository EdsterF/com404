#This program helps BEEP to paint

#Question
print("Towards which direction should I paint (up, down, left or right)?")

#User input
paint_direction = input()

#conditions
if (paint_direction == "up"):
    print("I am painting in the upward direction!")
elif(paint_direction == "down"):
    print("I am painting in the downward direction!")
elif (paint_direction == "left"):
    print("I am painting in the left direction!")
elif (paint_direction == "right"):
    print("I am painting in the right direction!")
else:
    print("Can't achieve given direction")

#Final Statement
print("Shall we try a different direction now?")

#User input
paint_direction = input()

#conditions
if (paint_direction == "up"):
    print("I am painting in the upward direction now!")
elif(paint_direction == "down"):
    print("I am painting in the downward direction now!")
elif (paint_direction == "left"):
    print("I am painting in the left direction now!")
elif (paint_direction == "right"):
    print("I am painting in the right direction now!")
else:
    print("Can't achieve given direction")

#Final Statement
print("That's enough painting for me now")