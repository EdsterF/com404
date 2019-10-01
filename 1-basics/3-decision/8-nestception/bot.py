#Question 1
print("Where should I look?")
location = input()

if (location == "in the bedroom"):
    print("where in the bedroom should I look?")
    bedroom_location = input()

    if (bedroom_location == "under the bed"):
        print("Found some shoes but no battery")
    
    else:
        print("Found some mess but no battery")

elif (location == "in the bathroom"):
    print("where in the bathroom should I look?")
    bathroom_location = input()

    if(bathroom_location == "bathtub"):
        print("Found a rubber duck but not battery")

    else:
        print("It is wet but I found no battery")

elif (location == "in the lab"):
    print("Where in the lab should I look?")
    lab_location = input()

    if(lab_location == "on the table"):
        print("Yes! I found my battery!")

    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking")

