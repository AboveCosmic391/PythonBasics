def main():
    # Call function with concatenated strings inside
    print("Concatenated inside function:", concatenate_inside())

    # Call function with two strings passed in and concatenated inside the function
    print("Concatenated with passed strings:", concatenate_with_args("Hello, ", "world!"))

    # Call function that returns concatenated strings
    print("Concatenated returned from function with no arguments:", concatenate_no_args())

    # Call function that returns concatenated strings using passed strings
    string1 = "Hello, "
    string2 = "world!"
    print("Concatenated returned from function with passed strings:", concatenate_with_return(string1, string2))

    # Example with a variable assigned to a function result
    title = makeTitle()
    print("Title:", title)

def concatenate_inside():
    return "This " + "is " + "a " + "concatenated " + "string."

def concatenate_with_args(str1, str2):
    return str1 + str2

def concatenate_no_args():
    return "Concatenated " + "string " + "with " + "no " + "arguments."

def concatenate_with_return(str1, str2):
    return str1 + str2

def makeTitle():
    return "cat" + " in the hat"

if __name__ == "__main__":
    main()
