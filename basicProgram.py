# Function to calculate total cost of items in the cart
def calculate_total(cart, prices):
    total_cost = 0
    for item in cart:
        if item in prices:
            total_cost += prices[item]
    return total_cost

# Function to display the items in the cart and their prices
def display_cart(cart, prices):
    print("Items in the cart:")
    for item in cart:
        if item in prices:
            print(f"- {item}: ${prices[item]}")
        else:
            print(f"- {item}: Price not available")

# Main function
def main():
    # Prices of items
    prices = {"apple": 1.0, "banana": 0.5, "orange": 1.5, "grape": 2.0}

    # Shopping cart
    cart = ["apple", "banana", "orange", "grape", "pear"]

    # Display items in the cart
    display_cart(cart, prices)

    # Calculate and display total cost
    total_cost = calculate_total(cart, prices)
    print("\nTotal cost:", total_cost)

if __name__ == "__main__":
    main()
