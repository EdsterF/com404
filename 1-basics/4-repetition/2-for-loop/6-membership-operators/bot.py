#intro message
print("What phrase do you see?")

#user input
phrase = str(input())
result = ""
#print("The phrase is: ")

for letter in phrase:
    result= letter + result

print("The phrase is: ", result)
