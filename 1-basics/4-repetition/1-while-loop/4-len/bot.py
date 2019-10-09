#Intro
print("Please enter a phrase")
phrase = input()

#max
phrase_length = len(phrase)

#control variable
num_char = 0

#Condition
while (num_char < phrase_length):
    num_char = num_char + 1

print("Bop " * num_char)
