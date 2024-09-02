# Guess the magic number
# Turbat Turkhuu, 20136824

# Constant
MAGIC_NUMBER = 42
# Variables

# Function to validate number
def validate_number(number):
    try:
        number = int(number)
        return number
    except:
        print("Your input has not been accepted, please enter a valid input. ")
        return 'No'

# Determine the message based on the number entered
def determine_clue(number_entered, MAGIC_NUMBER):
    if number < MAGIC_NUMBER:
        message = 'Number is too small'
    elif number > MAGIC_NUMBER:
        message = 'Number is too large'
    elif number == MAGIC_NUMBER:
        message = 'Yes, 42 is the magic number'
    elif number == 'No':
        message = 'Please enter a number'
    else:
        message = 'Number out of boundary'
    return message

# Main program
number = input("Guess the magic number : (1-99) ")
if number.islower() == 'quit':
    {
        print('Sad to see that you have given up');
        quit();

    }
else:
    {
    number = validate_number(number);
    clue = determine_clue(number, MAGIC_NUMBER);
    print(clue);

    }


# Input from the user

#validate_number(number)
#print(determine_clue(0,42))
#print("The end")
