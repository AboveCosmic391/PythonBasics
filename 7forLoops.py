def count_to_100():
    """Counting to 100 and printing the i value."""
    print("Counting to 100:")
    for i in range(1, 101):
        print(i)

def count_to_100_odd_even():
    """Counting to 100 and printing the i value along with 'odd' or 'even'."""
    print("Counting to 100 with odd/even check:")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, "even")
        else:
            print(i, "odd")

def count_down_from_100():
    """Counting down from 100 (decrementing value)."""
    print("Counting down from 100:")
    for i in range(100, 0, -1):
        print(i)

def main():
    # Call each function
    count_to_100()
    print("\n")
    count_to_100_odd_even()
    print("\n")
    count_down_from_100()

if __name__ == "__main__":
    main()
