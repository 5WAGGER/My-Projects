import time
def car_game(user_command):
    print("You have started the car game.")
    print("Type 'Help' for help.")
    print(" ")
    user_commands_used = False
    playing_car_game = True
    car_is_running = False
    car_velocity = 0.0
    distance_traveled = 0.0
    in_the_car = False
    car_is_accelerating = False
    car_is_decelerating = False
    terminal_velocity = 180

    while playing_car_game:
        try:
            user_command = input("> ").lower()

            user_commands_used = False


            if user_command == 'debug' and not user_commands_used:
                print("In the car = " + str(in_the_car))
                print("Car is running = " + str(car_is_running))
                print("Car is accelerating = " + str(car_is_accelerating))
                print("Car velocity = " + str(car_velocity))
                print("Car Distance = " + str(distance_traveled))
                print("Terminal velocity of the car = " + str(terminal_velocity))
                user_commands_used = True

            if user_command == "help" and not user_commands_used:
                print("Here is a list of commands you can use."
                      "'Enter', 'Exit', 'Start', 'Gas', 'Stop' 'Brake', 'Debug', 'Odometer' and 'Speedometer'")
                user_commands_used = True

            if car_is_accelerating and not user_commands_used:

                if user_command == "enter":
                    print("You are already in the car")
                    user_commands_used = True

                elif user_command == "exit":
                    in_the_car = False
                    print("You have exited the car while driving")
                    user_commands_used = True


                elif user_command == "start":
                    car_is_running = True
                    print("The car is already started")
                    user_commands_used = True

                elif user_command == "stop":
                    car_is_running = False
                    car_is_accelerating = False
                    print("The car has stopped running")
                    user_commands_used = True

                elif user_command == "gas":
                    print("You are already accelerating")
                    user_commands_used = True

                elif user_command == "brake":
                    car_is_accelerating = False
                    print("You have stopped accelerating")
                    user_commands_used = True

                elif user_command == "speedometer":
                    print(car_velocity)
                    user_commands_used = True

                elif user_command == "odometer":
                    print(distance_traveled)
                    user_commands_used = True

            if car_is_running and not user_commands_used:
                if user_command == "enter":
                    print("You are already in the car")
                    user_commands_used = True

                elif user_command == "exit":
                    in_the_car = False
                    print("You have exited the car")
                    user_commands_used = True

                elif user_command == "start":
                    car_is_running = True
                    print("You have started the car")
                    user_commands_used = True

                elif user_command == "stop":
                    car_is_running = False
                    print("You have turned off the car")
                    user_commands_used = True

                elif user_command == "gas":
                    car_is_accelerating = True
                    print("The car has started accelerating")
                    user_commands_used = True

                elif user_command == "brake":
                    if car_velocity == 0:
                        print("Nothing happened")
                        user_commands_used = True
                    if car_velocity > 0:
                        car_is_decelerating = True
                        print("The car has started decelerating")
                        user_commands_used = True

                elif user_command == "speedometer":
                    print(car_velocity)
                    user_commands_used = True

                elif user_command == "odometer":
                    print(distance_traveled)
                    user_commands_used = True

            if in_the_car and not user_commands_used:
                if user_command == "enter":
                    print("You are already in the car")
                    user_commands_used = True

                elif user_command == "exit":
                    in_the_car = False
                    print("You have exited the car")
                    user_commands_used = True

                elif user_command == "start":
                    car_is_running = True
                    print("You have started the car")
                    user_commands_used = True

                elif user_command == "gas":
                    print("Nothing happened")
                    user_commands_used = True

                elif user_command == "brake":
                    print("Nothing happened")
                    user_commands_used = True

                elif user_command == "speedometer":
                    print(car_velocity)
                    user_commands_used = True

                elif user_command == "odometer":
                    print(distance_traveled)
                    user_commands_used = True

            if not in_the_car and not user_commands_used:
                if user_command == "enter":
                    in_the_car = True
                    print("You have entered the car")
                    user_commands_used = True

                if user_command == "exit":
                    in_the_car = False
                    print("You are already outside of the car")
                    user_commands_used = True

                if user_command == "start":
                    car_is_running = True
                    print("You need to be in the car to start it")
                    user_commands_used = True

                if user_command == "gas":
                    print("You need to be in the car to use the gas pedal")
                    user_commands_used = True

                if user_command == "brake":
                    print("You need to be in the car to use the brake pedal")
                    user_commands_used = True

                if user_command == "speedometer":
                    print(car_velocity)
                    user_commands_used = True

                if user_command == "odometer":
                    print(distance_traveled)
                    user_commands_used = True

            if not user_commands_used:
                print("Invalid Command")

            if car_is_accelerating:
                if terminal_velocity > car_velocity:
                    car_velocity = car_velocity + 15

            if car_is_decelerating:
                if car_velocity != 0:
                    car_velocity = car_velocity - 15

            distance_traveled = distance_traveled + car_velocity

        except:
            print("Unknown Error...")

user_command = input("> ").lower()

car_game(user_command)

time.sleep(10)
