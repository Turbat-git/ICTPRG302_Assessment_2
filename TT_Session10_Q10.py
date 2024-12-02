# Assessment 2 Q11 Dictionaries Destination
# TURBAT TURKHUU 20136824

# Function to record destinations
def record_destinations():
    destination = {}
    while True:
        try:
            place_to_visit = input("Destination (or type 'DONE' to finish): ").upper()
            if place_to_visit == "DONE":
                break

            # Check for invalid input length or spaces
            if len(place_to_visit) < 5 or place_to_visit == " ":
                print("Wrong input! Please make sure you use the full name of the country!")
                continue

            # Record the destination
            if place_to_visit not in destination:
                destination[place_to_visit] = 1  # Initialize the count to 1
            else:
                destination[place_to_visit] += 1  # Increment the count

        except:
            print("An error occurred:")

    return destination

# Function to print the favorite destination
def print_favorite_destination(destination_dictionary):
    if len(destination_dictionary) == 0:
        print("No destinations were entered.")
        return

    #https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    Values = list(destination_dictionary.values())
    List = list(destination_dictionary.keys())
    popular_country = List[Values.index(max(Values))]

    count = max(destination_dictionary.values())
    print(count, "people suggested", popular_country)
# Main Program
# Call the appropriate functions
result = record_destinations()
print_favorite_destination(result)