#Intro message
print("What strange markings do you see?")

#User input
markings = str(input())

print("")
print("Identifying...")
print("")

#for loop
for position in range (0, len(markings), 1):
    print ("index ", position, ": ", markings[position])

#end message
print("")
print("Done!")