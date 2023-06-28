def Hangman():
    print("---------------------------Welcome to the hangman Game-----------------------------------")
    word = "Hello"
    #user_word = input("Guess the Word: ")



    count = 7
    new_string = " "



    while True:
        letter = input("Guess the Letter: ")
        if letter in word:
            print("Good Guess")
            new_string = new_string + letter
            #print(new_string)
        else:
            print("Oop! That letter is not in the word.")
            count -= 1
            if count == 6:
                hanger()
                print("|                |")
                print("|                 O")
            elif count == 5:
                print("|                |")
                print("|                 O")
                print("|                 |")
            elif count == 4:
                print("|                |")
                print("|                 O")
                print("|                /|")
            elif count == 3:
                print("|                |")
                print("|                 O")
                print("|                /|\\")
            elif count == 2:
                print("|                |")
                print("|                 O")
                print("|                /|\\")
                print("|                /")
            elif count == 1:
                print("|                |")
                print("|                 O")
                print("|                /|\\")
                print("|                / \\")
            print("Tries left:", count)



        if new_string.strip() == word:
            print("Congratulations, YOU WIN!")
            break



        if count == 0:
            print("Out of tries. Game over!")
            break




def hanger():
    print("-----------------")
    print("|                |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("___")




Hangman()