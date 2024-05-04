def main():
    # Addition
    result_addition = add(5, 3)
    print("Addition:", result_addition)

    # Subtraction
    result_subtraction = subtract(10, 4)
    print("Subtraction:", result_subtraction)

    # Multiplication
    result_multiplication = multiply(7, 6)
    print("Multiplication:", result_multiplication)

    # Division
    result_division = divide(20, 5)
    print("Division:", result_division)

    # Exponents
    result_exponents = power(2, 3)
    print("Exponents:", result_exponents)

    # Less than
    result_less_than = less_than(5, 10)
    print("Less than:", result_less_than)

    # Equal to
    result_equal_to = equal_to(7, 7)
    print("Equal to:", result_equal_to)

    # Greater than
    result_greater_than = greater_than(15, 10)
    print("Greater than:", result_greater_than)

    # Less than or equal to
    result_less_than_equal = less_than_equal(5, 5)
    print("Less than or equal to:", result_less_than_equal)

    # Greater than or equal to
    result_greater_than_equal = greater_than_equal(10, 10)
    print("Greater than or equal to:", result_greater_than_equal)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(base, exponent):
    return base ** exponent

def less_than(a, b):
    return a < b

def equal_to(a, b):
    return a == b

def greater_than(a, b):
    return a > b

def less_than_equal(a, b):
    return a <= b

def greater_than_equal(a, b):
    return a >= b

if __name__ == "__main__":
    main()
