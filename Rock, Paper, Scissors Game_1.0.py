import random
import time
game_is_playing = True

print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'Help' for help")

while True:
    number_of_rounds = input("How many rounds would you like to play?")
    try:
        int(number_of_rounds)
        break
    except ValueError:
        str(number_of_rounds)
        if number_of_rounds == "help":
            print("Here are your list of choices, 'Rock', 'Paper', 'Scissors', and 'Exit' to leave")
            print("You can also type the first letter of any of these words and it will work as a valid command")
        elif number_of_rounds == int:
            break
        elif number_of_rounds == "rock":
            print("You need to start the game first...")
        elif number_of_rounds == "paper":
            print("You need to start the game first...")
        elif number_of_rounds == "scissors":
            print("You need to start the game first...")
        elif number_of_rounds == "exit":
            print("You haven't even started the game, but okay...")
            exit()
        else:
            print("Invalid command, try again")
    except NameError:
        print("Unknown error...")

users_score = 0
bots_score = 0
users_choice = None
while game_is_playing:

    number_of_rounds = int(number_of_rounds)

    number_to_choice = {
        1: "paper",
        2: "rock",
        3: "scissors"
    }

    bots_number = random.randint(1, 3)

    bots_choice = number_to_choice[bots_number]

    users_choice = (input("Enter you choice: ")).lower()
    statement = "The robot has chose " + bots_choice + ". "


    def win_statement():
        print(statement + "You have won this round!")
        print(" ")


    def help_statement():
        print("Here are your list of choices, 'Rock', 'Paper', 'Scissors', and 'Exit' to leave")
        print("You can also type the first letter of any of these words and it will work as a valid command")


    def loss_statement():
        print(statement + "You have lost this round.")
        print(" ")

    if users_choice == bots_choice:
        print("You both have picked " + users_choice + ", try again")
        print(" ")
        number_of_rounds += 1

    elif users_choice == "rock":
        if bots_choice == "paper":
            loss_statement()
            bots_score = bots_score + 1
        elif bots_choice == "scissors":
            win_statement()
            users_score = users_score + 1

    elif users_choice == "paper":
        if bots_choice == "rock":
            win_statement()
            users_score = users_score + 1
        elif bots_choice == "scissors":
            loss_statement()
            bots_score = bots_score + 1

    elif users_choice == "scissors":
        if bots_choice == "rock":
            loss_statement()
            bots_score = bots_score + 1
        elif bots_choice == "paper":
            win_statement()
            users_score = users_score + 1

    elif users_choice == "help":
        help_statement()
        number_of_rounds += 1

    elif users_choice == "exit":
        game_is_playing = False

    else:
        print("Unknown command, try again...")
        number_of_rounds = number_of_rounds + 1

    number_of_rounds -= 1

    if number_of_rounds == 0:
        game_is_playing = False

print("You have scored " + str(users_score) + ". The robot has scored " + str(bots_score) + ".")
if users_score > bots_score:
    print("You have beat the robot!")
elif users_score < bots_score:
    print("You have lost to the robot.")
else:
    print("You have tied with the robot.")

time.sleep(10)

