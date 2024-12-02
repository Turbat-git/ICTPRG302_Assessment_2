# Assessment 2 Q9 Baby Shark
# TURBAT TURKHUU 20136824
# variable to be used in the future
i = 0

user_input = input("Give the name of all the sharks: ")

# Splitting the user input by the comma so that it
# will turn out to be different strings within the list
sharklist = user_input.split(',')

# Header
print("\nBaby Shark Lyrics \n")

# A function that had been used to print and multiplicate the verses in the song
def print_shark(i):
        the_doo = ", doo-doo" * 3
        print((f"{sharklist[i].strip()}, {the_doo}, \n") *3)
        print(sharklist[i].strip() + "\n")
list_length = len(sharklist)

# while loop so that the function can call back to the length of the list and get every string
while i < list_length:
        print_shark(i)
        i = i + 1
