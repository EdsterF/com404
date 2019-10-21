#Intro message
print("I wonder what is in my suitcase...")

#Function
def item_from_suitcase(item):

    #If statement within the function
    if(item == "tootbrush"):
        print("")
        print("A tootbrush. Well, got to have clean teeth!")
        print("")
    
    elif(item == "spidey suit"):
        print("")
        print("My spidey suit! I won't be needing this. I am on holiday.")
        print("")
    
    else:
        print("")
        print("An unexpected item! It could be useful.")
        print("")

#Call to function
item_from_suitcase("tootbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")