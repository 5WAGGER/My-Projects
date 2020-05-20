
users_number = input("Enter your number: ")
try:
    int(users_number)

    if len(users_number) == 1:
        print(" ")
    elif len(users_number) == 2:
        print(" ")

    elif len(users_number) == 3:
        print(" ")
except ValueError:
    print("Invalid Number")



