# Assessment 2 Q1 Enhanced guess the magic number
# 20136824

MAGIC_NUMBER = 42


# a function to check whether an integer was entered or not
def validate(number):
    try:
        number = int(number)
        return number
    except:
        print("Please enter a number only.")
        return "No"


def determine_clue(number_entered, MAGIC_NUMBER):
    if number_entered == MAGIC_NUMBER:
        print("CONGRATULATIONS! You have guessed correctly")
    elif number_entered < MAGIC_NUMBER:
        print("The number is too small")
    elif number_entered > MAGIC_NUMBER:
        print("The number is too large")
    else:
        print("Please enter a number within 1-100 range")
    return number_entered


number = input("Please input a number between 1-100 to guess the magic number ")
number_entered = number

validate(number)
determine_clue(number_entered, MAGIC_NUMBER)
print("The end")
