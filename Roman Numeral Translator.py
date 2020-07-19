import time
while True:

    try:
        users_number = input("Enter your number: ")
        list_of_roman_numerals = ["I", "V", "X", "L", "C", "D", "M",]
        above_1000 = False
        is_zero = False
        def filter_index_place(index):
            if users_number[index] == '0':
                roman_numeral = ""
            elif users_number[index] == '1':
                roman_numeral = list_of_roman_numerals[0]
            elif users_number[index] == '2':
                roman_numeral = list_of_roman_numerals[0] + list_of_roman_numerals[0]
            elif users_number[index] == '3':
                roman_numeral = list_of_roman_numerals[0] + list_of_roman_numerals[0] + list_of_roman_numerals[0]
            elif users_number[index] == '4':
                roman_numeral = list_of_roman_numerals[0] + list_of_roman_numerals[1]
            elif users_number[index] == '5':
                roman_numeral = list_of_roman_numerals[1]
            elif users_number[index] == '6':
                roman_numeral = list_of_roman_numerals[1] + list_of_roman_numerals[0]
            elif users_number[index] == '7':
                roman_numeral = list_of_roman_numerals[1] + list_of_roman_numerals[0] + list_of_roman_numerals[0]
            elif users_number[index] == '8':
                roman_numeral = list_of_roman_numerals[1] + list_of_roman_numerals[0] + list_of_roman_numerals[0] + list_of_roman_numerals[0]
            elif users_number[index] == '9':
                roman_numeral = list_of_roman_numerals[0] + list_of_roman_numerals[2]
            return roman_numeral

        if users_number == "0":
            is_zero = True

        elif len(users_number) == 1:
            roman_numeral = filter_index_place(-1)

        elif len(users_number) == 2:
            ones_place_numeral = filter_index_place(-1)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            tens_place_numeral = filter_index_place(-2)
            roman_numeral = tens_place_numeral + ones_place_numeral

        elif len(users_number) == 3:
            ones_place_numeral = filter_index_place(-1)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            tens_place_numeral = filter_index_place(-2)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            hundreds_place_numeral = filter_index_place(-3)
            roman_numeral = hundreds_place_numeral + tens_place_numeral + ones_place_numeral

        elif len(users_number) == 4:
            ones_place_numeral = filter_index_place(-1)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            tens_place_numeral = filter_index_place(-2)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            hundreds_place_numeral = filter_index_place(-3)
            del list_of_roman_numerals[0]
            del list_of_roman_numerals[0]
            thousands_place_numeral = filter_index_place(-4)
            roman_numeral = thousands_place_numeral + hundreds_place_numeral + tens_place_numeral + ones_place_numeral


        elif len(users_number) >= 4:
            print("Cannot got above 1000...")
            above_1000 = True

        elif users_number == '0':
            print("Zero is not valid...")
            is_zero = True

        if not above_1000 and not is_zero:
            print("Your roman numeral is "+roman_numeral+".")
            time.sleep(10)
            break

    except UnboundLocalError:
        print("Invalid input...")
    except:
        print("Unknown error...")
        
time.sleep(10)
