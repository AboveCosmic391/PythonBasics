def main():
    # Creating a tuple
    my_tuple = ("apple", "banana", "cherry", "apple", "banana")
    print("Original Tuple:", my_tuple)

    # Accessing elements of a tuple
    print("First element:", my_tuple[0])  # Indexing starts from 0
    print("Last element:", my_tuple[-1])  # Negative indexing starts from the end

    # Slicing a tuple
    print("Sliced tuple:", my_tuple[1:4])  # Extracts elements 1 to 3

    # Counting occurrences of an element
    count_apple = my_tuple.count("apple")
    print("Count of 'apple':", count_apple)

    # Finding the index of an element
    index_banana = my_tuple.index("banana")
    print("Index of 'banana':", index_banana)

    # Length of a tuple
    print("Length of tuple:", len(my_tuple))

    # Concatenating tuples
    another_tuple = ("orange", "grape")
    concatenated_tuple = my_tuple + another_tuple
    print("Concatenated tuple:", concatenated_tuple)

    # Unpacking tuples
    first, second, *rest = concatenated_tuple
    print("First element after unpacking:", first)
    print("Second element after unpacking:", second)
    print("Rest of the elements after unpacking:", rest)

if __name__ == "__main__":
    main()
