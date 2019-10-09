#Intro message
print("What type of adventure should I have?")

#User input
adventure_type = input()

if ((adventure_type=="scary") or (adventure_type=="short")):
    print("")
    print("Entering the dark forest!")

elif ((adventure_type=="safe") or (adventure_type=="long")):
    print("")
    print("Taking the safe route!")

else: 
    print("")
    print("Not sure what route to take.")