#User Question
print("How many mountains should I display?")

#User input
mountains = int(input())

#Intro message (outside of loop)
print("Displaying...")

#For loop function based on user input
for count in range(mountains):
    print("")
    print("       __")
    print("      /  \\_")
    print("     /^    \\")
    print("    /  ^    \\_")
    print("  _/ ^ ^     ^\\")
    print(" /  ^     ^    \\")
    print("")

#End message (outside of loop)
print("Done!")