#Function
def escape_by(plan):
    if (plan== "Jumping over"):
        print("We cannot excape that way! The boulder is too big!")
    elif (plan== "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (plan== "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

#Calls to function
escape_by("Jumping over")
escape_by("running around")
escape_by("going deeper")
        
