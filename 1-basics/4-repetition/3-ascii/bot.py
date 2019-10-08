#Intro
print("How many bars should be charged?")
max_charge = int(input())

#Control Variable
base_charge = 0

#Condition
while (base_charge < max_charge):
    base_charge = base_charge + 1
    print("Charging:", base_charge * "█")

#Final Statement
print("The battery is fully charged.")