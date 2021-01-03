def user_choice():

    # VARIABLES

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0, 11)
    within_range = False

    # TWO CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE == False
    while choice.isdigit() == False or within_range == False:

        choice = input("Pleae enter a number (0 - 10): ")
        # DIGIT Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        # RANGE CHECK
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Sorry you are out of acceptable range")
    return int(choice)


print(user_choice())
