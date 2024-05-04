# Importing necessary modules
from datetime import date
import math

# Function to print today's date
def print_todays_date():
    """Prints today's date."""
    today = date.today()
    print("Today's date:", today)

# Function to store a value in a variable (calculate pi)
def calculate_pi():
    """Stores the value of pi."""
    pi = math.pi
    return pi

# Function to calculate rectangle area based on input
def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

# Function to print a value based on an input
def print_name(name):
    """Prints the provided name."""
    print("Name:", name)

# Function to perform a generic demonstration calculation for aircraft location
def fly(lat, long, speed, heading, windspeed, winddirection):
    """Performs a generic demonstration calculation to determine the next location of aircraft."""
    # Assuming a simple calculation for demonstration purposes
    next_lat = lat + (speed * math.cos(math.radians(heading)))
    next_long = long + (speed * math.sin(math.radians(heading)))
    return next_lat, next_long

def main():
    # Demonstrate functions
    print("Demonstrating Basic Functions:")
    
    # Print today's date
    print("\n1. Today's Date:")
    print_todays_date()
    
    # Calculate and print pi
    print("\n2. Value of Pi:")
    pi_value = calculate_pi()
    print("Value of Pi:", pi_value)
    
    # Calculate rectangle area
    print("\n3. Rectangle Area Calculation:")
    length = 5
    width = 3
    area = calculate_rectangle_area(length, width)
    print("Area of Rectangle with length {} and width {}: {}".format(length, width, area))
    
    # Print name
    print("\n4. Printing Name:")
    print_name("Adam")
    
    # Demonstrate aircraft location calculation
    print("\n5. Aircraft Location Calculation:")
    next_lat, next_long = fly(35.0, -100.0, 500, 45, 50, 180)
    print("Next Location of Aircraft - Latitude: {}, Longitude: {}".format(next_lat, next_long))

if __name__ == "__main__":
    main()
