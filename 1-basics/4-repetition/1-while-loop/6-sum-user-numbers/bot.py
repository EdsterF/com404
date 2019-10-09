#Intro
print("How many numbers should I sum up?")

max_input_numbers = int(input())

inputs_done = 0

total = 0

while (inputs_done < max_input_numbers):

    print("Please enter number", inputs_done + 1, "of", max_input_numbers, ":")
    user_input = int(input())
    total = total + user_input
    inputs_done = inputs_done + 1



print("The answer is", total, ".")












#print("How many live cables must I avoid?")
#max_live_cables = int(input())

#control variable
#cables_avoided = 0

#Condition
#while (cables_avoided < max_live_cables):
 #   print("Avoiding...", end="")
  #  cables_avoided = cables_avoided + 1
   # print("Done!", cables_avoided, "cables avoided.")