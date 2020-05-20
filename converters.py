

def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / .45

users_numbers = [1, 2, 4, 5, 7]

max = users_numbers[0]
for number in users_numbers:
    if number > max:
        max = number

