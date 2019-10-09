#Intro message
print("How far are we from the cave?")

#User input
cave_distance = int(input())
print("")

#for loop
for count in range (cave_distance, 0, -1):
    #Range explained, based on a count-down
    #cave_distance = where the count starts (based on user input)
    #0 = where the count ends
    #1 = step or difference between each number

    print(str(count) + " steps remaining")
    #count explained
    #count is a variable inside the loop:
    #this contains the "total" for every time the loop goes around
    #in this case 1 is subtracted from the total every time

#Final message
print("")
print("We have reached the cave!")