#User's input
print("Please enter a number:")
number = int(input())

base_number = 0
total = 1

while (base_number < number):
    base_number = base_number+1
    total = total * base_number

print("The factorial is", total, ".")

