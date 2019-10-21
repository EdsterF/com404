#Intro message
print("How many miles must I travel before I reach the secret base?")

#User input
max_miles = int(input())

#message
print("I will count the miles...")
print("")
print("I have", max_miles, "miles to go before I reach the base")

#loop
lowest_miles = 1
while (max_miles > lowest_miles):
    print("I have ", end="")
    max_miles= max_miles -1 
    print(max_miles, "miles to go before I reach the base")

#End Statement
print("")
print("I have arrived at the secret headquarters of the MIB")
print("It is time to sneak in.")