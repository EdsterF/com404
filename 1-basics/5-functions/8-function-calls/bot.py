#Functions
def display_box(word):
    print("@" * (len(word) + 10))
    print("@ ", word, " @")
    print("@" * (len(word) + 10))
    return word


#def display_lower_case():


#def display_upper_case():


#def display_mirrored():


#def repeat():


def run():
    print("Plase enter a cryptic word")
    word = input()
    print("")
    print("Please choose one of the following options:")
    print("1) Display in a Box – display the word in an ascii art box")
    print("2) Display Lower-case – display the word in lower-case e.g. hello")
    print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
    print("")
    user_choice = (int(input())
    print("")

    if (user_choice == 1):
        display_box(word)



#Run Program
run()
