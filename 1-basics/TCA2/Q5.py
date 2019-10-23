#Variable


#message
print("your health is 100%. Escape is in progress...")
  
#loop

MAX_LOOP=5
MIN_LOOP=0
health = 100

while MAX_LOOP>MIN_LOOP:
    
    print("...Oh dear, who is that?")
    answer = input()
    MAX_LOOP=MAX_LOOP-1

    if (answer == "Smiler's Bot"):
        health = health - 20
        print("Time to jam out of here!")
        print("")

    elif (answer == "Hacker"):
        health = health + 20
        print("Yay! Better follow this one!")
        print("")
    
    else:
        print("Phew, just another emoji!")
        print("")
    

#Final message
print("Escaped! Health is", health, "%")