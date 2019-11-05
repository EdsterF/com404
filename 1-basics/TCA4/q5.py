#Variable
Health = 100

print("Your health is 100%. Escape is in progress...")

MAX_LOOP=5
MIN_LOOP=0


while (MAX_LOOP>MIN_LOOP):
    print("...Oh dear, who is that?")
    answer = input()
    if answer == "Smiler's Bot":
        Health = Health-20
        print("Time to jam out of here!")
    elif answer == "Hacker":
        Health = Health+20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji")
    MAX_LOOP=MAX_LOOP-1

#End message
print("Escaped! Health is ", Health)