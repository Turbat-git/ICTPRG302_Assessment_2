# Assessment 2 Q6 Fixing the broken keyboard
# TURBAT TURKHUU 20136824


# Fixing the keyboard
def fix_broken_keyboard(message):
    fixed_keyboard = user_input.replace('##', 'a')
    fixed_keyboard = fixed_keyboard.replace('$$$', 'e')
    fixed_keyboard = fixed_keyboard.replace('$$', 'u')
    return fixed_keyboard


# Replace negativity with positivity (not...bad replaced with good)
def remove_negativity(fixed_keyboard):
    start = user_input.find('not')
    end = user_input.find('bad')
    end = end + 3
    if start != -1 and end != -1 and start < end:
        positive_message = user_input.replace(user_input[start:end],'good')
    else:
        return -1
    return positive_message

# Main Program
# Ask user input and call functions to fix the keyboard and
# change the message to a positive message.
user_input = input("What is the message: ")
user_input = fix_broken_keyboard(user_input)
user_input = remove_negativity(user_input)


# Display result
print(f'When corrected the message is: \n{user_input}')