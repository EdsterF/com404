#Functions
def display_box(word):
    print("@" * (len(word) + 4))
    print("@", word, "@")
    print("@" * (len(word) + 4))
    return word


def display_lower_case(word):
    print (str.lower(word))


def display_upper_case(word):
    print (str.upper(word))


def display_mirrored(word):
    for position in range (len(word)-1, -1, -1):
        print (word[position], end="")
    print("")


def repeat(word):
    print("How many times should I print the word?")
    word_repeat = int(input())
    for number in range (0, word_repeat, 1):
        if (number % 2 == 0):
            print (word.lower())
        else:
            print (word.upper())


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
    user_choice = input()
    print("")

    if (user_choice == "1"):
        display_box(word)

    elif (user_choice == "2"):
        display_lower_case(word)

    elif (user_choice == "3"):
        display_upper_case(word)

    elif (user_choice == "4"):
        display_mirrored(word)

    elif (user_choice == "5"):
        repeat(word)

#Call to Function
run()