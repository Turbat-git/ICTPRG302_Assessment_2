# Assessment 2 Question 13 ICT hours
# TURBAT TURKHUU 20136824



# Read through the text file
def read_text(FILE_NAME):
    total_records = 0
    agreed_hours_dict= {}

    quicktext = open(FILE_NAME, "r")
    for line in quicktext:
        split_quicktext = line.strip().split("\t")
        if split_quicktext[0].startswith("ICT") and len(split_quicktext) > 2 and split_quicktext[2].isdigit():
            agreed_hours = int(split_quicktext[2])
            total_records += 1
            if agreed_hours in agreed_hours_dict:
                agreed_hours_dict[agreed_hours] += 1
            else:
                agreed_hours_dict[agreed_hours] = 1

    sorted_agreed_hours_dict = sorted(agreed_hours_dict.items())
    for count, hours in sorted_agreed_hours_dict:
        print(f"Hours: {hours} " + f"  Frequency: {count}")

    print(f"Total number of records: {total_records}")

#main
filename = "agreed-hours.txt"
read_text(filename)