# Counter activity

#Question 1
print("Please enter the first whole number")

#Answer 1
number_1 = int(input())

#Question 2
print("Please enter the first whole number")

#Answer 2
number_2 = int(input())

#Question 3
print("Please enter the first whole number")

#Answer 3
number_3 = int(input())

even_counter = 0
odd_counter = 0

if (number_1 % 2 == 0):
    even_counter = even_counter + 1
else:
    odd_counter = odd_counter + 1

if (number_2 % 2 == 0):
    even_counter = even_counter + 1
else:
    odd_counter = odd_counter + 1

if (number_3 % 2 == 0):
    even_counter = even_counter + 1
else:
    odd_counter = odd_counter + 1

print("There were ", even_counter,"even and", odd_counter,"odd numbers.")
#even_numbers = sum(number_1 % 2, number_2 % 2, number_3 % 2)
#odd_numbers = sum(number_1 / 2, number_2 % 2, number_3 % 2)

#if (number_1 % 2):

#elif (number_1 / 2):


    
#elif (number / 2):
#    print("the number", number,"is an even number")