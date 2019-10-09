#intro message
print("")
print("What phrase do you see?")

#user input
phrase = str(input())
#the below variable is added to store the letters while the for letter loop goes through each of them
count = ""
print("")
print("Reversing...")
print("")

#"for letter" loop explained
#"for letter" reads the letters one at time starting from the first
#it then stores it in the variable COUNT
#then the loop goes over again
#and it adds the second letter to the count (this is how it's done backwards)
#it ADDS the LETTER TO the COUNT and not the count to the letter.

for letter in phrase:
    count= letter + count

print("The phrase is: ", count)
print("")