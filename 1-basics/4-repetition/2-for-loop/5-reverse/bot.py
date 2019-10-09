#Intro message
print("")
print("What do you see?")

#User input
sight = str(input())

print("")
print("Reversing...")
print("")

print ("The phrase is: ", end="")

#for loop in reverse explained
#Starts with last letter (-1) and works backwards by
#subtracting 1 at time

for position in range (len(sight)-1, -1, -1):   
    print (sight[position], end="") 

print("")
print("")