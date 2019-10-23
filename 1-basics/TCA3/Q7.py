#Intro message
print("Please enter a word")
#User input
word = input()

print("Please choose one of the following options")
print("1) Under")
print("2) Over")
print("3) Both")
print("4) Grid")
option_choice = input()

#Decisions
if(option_choice == "1"):
    print(word)
    word_length= len(word)
    print("*" * word_length)

elif(option_choice == "2"):
    word_length= len(word)
    print("*" * word_length)
    print(word)

elif(option_choice == "3"):
     word_length= len(word)
     print("*" * word_length)
     print(word)
     print("*" * word_length)

elif(option_choice == "4"):
    word_length= len(word)
    print("Please specify the grid size, rows and columns")
    rows = int(input())
    columns = int(input())

    min_rows = 0


    
    print((("*" * word_length)+"   ")*columns)
    #Nested decision
    while rows>min_rows:
        print((word+ "   ") *columns)
        print((("*" * word_length)+"   ")*columns)
        rows = rows-1
    
        







        #word_length= int(len(word))
        #if columns < 0:
        #print((("*" * word_length)+"   ")*grid)
        #print((word+ "   ") *grid)
        #print((("*" * word_length)+"   ")*grid)

