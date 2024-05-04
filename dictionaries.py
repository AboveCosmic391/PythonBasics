def main():
    # Creating a dictionary of students and their ages
    student_ages = {
        "Alice": 20,
        "Bob": 22,
        "Charlie": 21,
        "David": 23,
        "Emma": 20
    }
    print("Original Dictionary:", student_ages)

    # Accessing values using keys
    print("Age of Alice:", student_ages["Alice"])

    # Modifying a value
    student_ages["Alice"] = 21
    print("Modified Dictionary:", student_ages)

    # Adding a new key-value pair
    student_ages["Frank"] = 25
    print("Dictionary after adding Frank:", student_ages)

    # Removing a key-value pair
    del student_ages["David"]
    print("Dictionary after removing David:", student_ages)

    # Checking if a key exists
    if "Charlie" in student_ages:
        print("Charlie's age is", student_ages["Charlie"])

    # Length of a dictionary
    print("Number of students in the dictionary:", len(student_ages))

    # Getting all keys
    print("Keys in the dictionary:", student_ages.keys())

    # Getting all values
    print("Values in the dictionary:", student_ages.values())

    # Getting all key-value pairs
    print("Key-Value pairs in the dictionary:", student_ages.items())

if __name__ == "__main__":
    main()
