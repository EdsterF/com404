#User question 1
print("")
print("How many rows should I have?")

#User Input 1
rows = int(input())

#User question 2
print("")
print("How many columns should I have?")

#User input 2
columns = int(input())

print("")
print("Here I go:")

#for Nested loop explained
#first loop references to the variable ROWS
#so the nested loop will be re-run based on the ROWS vaule
for count_rows in range (0, rows, 1):
    #the nested loop below (indented)
    #will run against the COLUMNS variable
    #so it'll print a :-) on the same line (thanks to the use of end="")
    #for each time it goes through the loop
    #up to the maximum amout specified by the COLUMNS variable
    #when this ends it will start a new line because
    #of the print("") that's non indented in line with the nest
    #then look in the COUNT_ROWS built in variable
    #and run the nested look again based on the given ROWS vailue
    for count_columns in range (0, columns, 1):
        print (":-)", end="")
    print("")

#End message
print("")
print("Done")