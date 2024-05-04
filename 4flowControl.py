# Function to check if it's raining and wear a raincoat if it is
def wear_raincoat(weather):
    """Wear a raincoat if it's raining."""
    if weather == "rainy":
        print("It's raining. Wear a raincoat!")
    else:
        print("It's not raining. No need for a raincoat.")

# Function to calculate movie ticket price based on age
def calculate_ticket_price(age):
    """Calculate movie ticket price based on age."""
    if age < 5:
        print(f"Your age was {age}. Children under 5 years old watch for free!")
    elif age >= 5 and age < 18:
        print(f"Your age is {age}. Youth ticket price: $10")
    elif age >= 65:
        print(f"Your age is {age}. Senior ticket price: $8")
    else:
        print(f"Your age is {age}. Adult ticket price: $15")

# Function to check if someone is tall enough to ride the rides
def check_height(height):
    """Check if someone is tall enough to ride the rides."""
    if height >= 120:
        print(f"Your height is {height}cm. You are tall enough to ride the rides!")
    else:
        print(f"Your height is {height}cm. Sorry, you are not tall enough to ride the rides.")

# Function to check if a number is positive, negative, or zero
def check_number(number):
    """Check if a number is positive, negative, or zero."""
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")

def main():
    # Example 1: Checking for rainy weather
    print("Example 1: Checking for rainy weather")
    wear_raincoat("sunny")
    wear_raincoat("rainy")

    # Example 2: Calculating movie ticket prices
    print("\nExample 2: Calculating movie ticket prices")
    calculate_ticket_price(10)
    calculate_ticket_price(55)
    calculate_ticket_price(67)
    calculate_ticket_price(3)

    # Example 3: Checking height for rides
    print("\nExample 3: Checking height for rides")
    check_height(110)
    check_height(130)

    # Example 4: Checking if a number is positive, negative, or zero
    print("\nExample 4: Checking if a number is positive, negative, or zero")
    check_number(-5)
    check_number(0)
    check_number(10)

if __name__ == "__main__":
    main()
