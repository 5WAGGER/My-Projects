import random

user_input = input("Do you want each dice different or the same? (yes/no): ")

if user_input == "yes":
    def dice_roll_once(number_of_sides):

        number_to_word = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve"
        }

        random_number = random.randint(1, number_of_sides)

        translated_word = number_to_word[random_number]

        print("You have rolled a " + translated_word + ".")

        return translated_word


    def dice_roll(times):
        i = 0
        while i != times:
            dice_roll_once(int(input("Enter the number of side on the dice (Min 1, Max 12): ")))
            times += 1

    dice_roll(int(input("Enter how many times you want to roll the dice: ")))

elif user_input == "no":

    number_of_sides = int(input("Enter the number of side on the dice (Min 1, Max 12): "))

    def dice_roll_once(number_of_sides):

        number_to_word = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve"
        }

        random_number = random.randint(1, number_of_sides)

        translated_word = number_to_word[random_number]

        print("You have rolled a " + translated_word + ".")

        return translated_word


    def dice_roll(times):
        i = 0
        for i in range(times):
            dice_roll_once(number_of_sides)
            times += 1


    dice_roll(int(input("Enter how many times you want to roll the dice: ")))


else:
    print("Invalid input")