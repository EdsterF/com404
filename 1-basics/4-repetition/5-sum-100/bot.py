#Intro
print("Calculating the sum of the first 100 numbers...")


max_variable = 100

current_total = 0
number = 1

#condition less or equal to 100 (this lets add 100 at the end as well)
#while the variable NUMBER is less or equal to 100
while (number <= max_variable):
    #add the value of NUMBER to the CURRENT TOTAL
    current_total = current_total + number
    #now we increase the value of NUMBER by 1 (+1)
    number = number + 1

    #this loop goes around again, and this time it adds the new NUMBER to
    #the CURRENT TOTAL

#at the end print statment to show the value of CURRENT TOTAL (to include the final number 100)
print("...Done! The answer is ", current_total)
