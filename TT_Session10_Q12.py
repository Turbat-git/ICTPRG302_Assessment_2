# Assessment 2 Question 12 Calculate McMolands Profit:
# TURBAT TURKHUU 20136824

# Display menu options
def print_options():
    print("(1) McMeal, (2) McShmeal, (R) Report")
    return

# Ask for user input until input is input
def validate_user_input():
    response = []
    while True:
        user_input = input("Please enter your response: ").strip().upper()
        if user_input == "R":
            return response
        elif user_input == "1":
            response.append("1")
        elif user_input == "2":
            response.append("2")
        else:
            print("You have entered an invalid option. Please try again.")

# Update the file with the product sold
def update_file(file_handle, response):
    file = open(file_handle, "w")
    for res in response:
        (file.write(res))  # Write each response on a new line

# Display the daily profit
def display_daily_profit(FILE_NAME, MC_MEAL_COST, MC_MEAL_PRICE, MC_SHMEAL_COST, MC_SHMEAL_PRICE):
    file_handle = open(FILE_NAME, "r")
    quicktext = file_handle.read()

    MC_MEAL_PROFIT = MC_MEAL_PRICE - MC_MEAL_COST
    MC_SHMEAL_PROFIT = MC_SHMEAL_PRICE - MC_SHMEAL_COST

    # Removes blank
    numberlist = quicktext.strip()

    meal_count = numberlist.count("1")
    shmeal_count = numberlist.count("2")

    total_meal_profit = meal_count * MC_MEAL_PROFIT
    total_shmeal_profit = shmeal_count * MC_SHMEAL_PROFIT

    meal_sales = meal_count * MC_MEAL_PRICE
    shmeal_sales = shmeal_count * MC_SHMEAL_PRICE

    total_sales = meal_sales + shmeal_sales

    print(f"You made ${total_sales:.2f}, you profited ${total_meal_profit + total_shmeal_profit:.2f}")
    return total_meal_profit, total_shmeal_profit

# Main
MC_MEAL_COST = 4.00
MC_MEAL_PRICE = 10.00
MC_SHMEAL_COST = 6.50
MC_SHMEAL_PRICE = 13.00

FILE_NAME = "TT_mcmolands.txt"

print_options()
user_input = validate_user_input()
update_file(FILE_NAME, user_input)
display_daily_profit(FILE_NAME, MC_MEAL_COST, MC_MEAL_PRICE, MC_SHMEAL_COST, MC_SHMEAL_PRICE)
