# Guess the magic number
# Turbat Turkhuu, 20136824

# Constant
MAGIC_NUMBER = 42
MIN_RANGE = 0
MAX_RANGE = 100


# Variables

# Function to validate number
def validate_number(number_to_validate):
    try:
        number_to_validate = int(number_to_validate)
        return number_to_validate
    except:
        print("Your input has not been accepted, please enter a valid input. ")
        return 'No'


# Determine the message based on the number entered
def determine_clue(number_guessed, secret_number):
    message = 'Yes, 42 is the magic number'
    if number_guessed > secret_number:
        message = 'Number is too large'
    elif number_guessed == 'No':
        message = 'Please enter a number'
    elif number_guessed < secret_number:
        message = 'Number is too small'
    elif number_guessed > MAX_RANGE or number_guessed < MIN_RANGE:
        message = 'Number out of boundary'
    return message


number = 0
# Main program
while number != MAGIC_NUMBER:
    number = input("Guess the magic number : (1-99) ")
    number = number.lower()
    if number == 'quit':
        print('Sad to see that you have given up')
        quit()
    number = validate_number(number)
    clue = determine_clue(number, MAGIC_NUMBER)
    print(clue)

# Input from the user

# validate_number(number)
# print(determine_clue(0,42))
# print("The end")
