#Variable
health = 100


#Function
def question(answer):
   
    print("...Oh dear, who is that?")
    answer = input()

#loop
    while (answer == "Smiler's Bot"):
        health = health - 20
        print("Time to jam out of here!")
        print("")

    if (answer == "Hacker"):
        health = health + 20
        print("Yay! Better follow this one!")
        print("")
    
    else:
        print("Phew, just another emoji!")
        print("")
    

#Call to function
question(answer)
question(answer)
question(answer)
question(answer)
question(answer)

#Final message
print("Escaped! Health is", health, "%")