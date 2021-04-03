from random import randint

def guess():
        nbre = randint(1, 99)
        attempts = 0
        welcome="This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\n"
        print(welcome)
        while (1):
                x=input("What's your guess between 1 and 99?\n")
                try:
                        x = int(x)
                except ValueError:
                        if (x == "exit"):
                                print("Goodbye!")
                                exit()
                        else:
                                print("That's not a number.")
                                continue
                if int(x) == 42:
                        print("The answer to the ultimate question of life, "
                                + "the universe and everything is 42.")
                        print("Congratulations! You got it on your first try!")
                        exit()
                elif int(x) == nbre:
                        print("Congratulations, you've got it!")
                        print("You won in", attempts, "attempts!")
                        exit()
                elif int(x) < nbre:
                        print("Too low!")
                else:
                        print("Too high!")

guess()
