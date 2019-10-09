#Decisions with if...elif...else statements
#Nested decisions
#Multiple conditions with logical (AND, OR and NOT) operators

#Beep will decide if stop to rest his battery
#or continue to explore

#User question 1
print("What do you think I should do now?")

#User Input 1
action = input()

#User question 2
print("Will I have enough time for a break?")

#User input 2
break_rest = input()

if ((action=="walk") and (break_rest=="no")):
    print ("Should I stop,  as my battery needs recharging")
    stop = input()
    
    if (stop=="yes"):
        print ("About time!")
    
    elif (stop=="no"):
        print("I really need to stop now")

    else:
        print ("I'm getting rather worn out")

elif ((action=="stop") or (break_rest=="yes")):
    print ("That's just what I need!")

else :
    print ("I'd be happy to take a break.")