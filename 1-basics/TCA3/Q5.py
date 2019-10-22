#Intro
print("Welcome to the Planet of the Apes...")

#Loop constants
LOOP_MAX=7
LOOP_MIN=0

#Variable
human_encounters=0
ape_encounters=0

#Nested Decisions
while LOOP_MAX > LOOP_MIN:
    print("...be ye human or be ye ape?")
    usr_rply = input()
    if (usr_rply == "Human"):
        human_encounters = human_encounters+1
        print("I did not start this war. But I will finish it.")
        print("")
    elif (usr_rply == "Ape"):
        ape_encounters=ape_encounters+1
        print("Apes together strong!")
        print("")
    else:
        print("This is not your fight.")
        print("")
    
    LOOP_MAX = LOOP_MAX-1

#End statement
print("Total human encountered: ", human_encounters)
print("Total apes encountered: ", ape_encounters)