import random

game_is_playing = True
number_of_rounds_end = int(input("How many rounds would you like to play? "))
users_score = 0
bots_score = 0
number_of_rounds = number_of_rounds_end
while game_is_playing:

    number_to_choice = {
        1: "paper",
        2: "rock",
        3: "scissors"
    }

    bots_number = random.randint(1, 3)

    bots_choice = number_to_choice[bots_number]

    users_choice = (input("Enter you choice: ")).lower()
    statement = "The robot has chose " + bots_choice + ". "

    def add_round():
        number_of_rounds += 1

    def win_statement():
        print(statement + "You have won this round!")
        print(" ")


    def help_statement():
        print("Here are your list of choices, 'Rock', 'Paper', 'Scissors', and 'Exit' to leave")
        print(" ")


    def loss_statement():
        print(statement + "You have lost this round.")
        print(" ")


    if users_choice == bots_choice:
        print("You both have picked " + users_choice + ", try again")
        add_round()

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
        add_round()

    elif users_choice == "exit":
        game_is_playing = False

    else:
        print("Unknown command, try again...")
        add_round()

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




