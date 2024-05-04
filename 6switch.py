def get_day_of_week(number):
    """Returns the day of the week corresponding to the given number."""
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    # Retrieve the day name from the dictionary using the number
    day = days.get(number, "Invalid day")
    
    return day

def main():
    # Get the day of the week for number 3
    day_of_week = get_day_of_week(7)
    
    # Print the day of the week
    print("Day of the week:", day_of_week)

if __name__ == "__main__":
    main()
