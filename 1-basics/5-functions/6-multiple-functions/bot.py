#Functions
def display_ladder(steps):
    for ladder in range(steps):
        print("|  |")
        print("****")
    print("|  |")    

def create_ladder():
    print("How many steps remain?")
    remaining_steps= int(input())
    print("")
    display_ladder(remaining_steps)
 

#Call to Function
create_ladder()