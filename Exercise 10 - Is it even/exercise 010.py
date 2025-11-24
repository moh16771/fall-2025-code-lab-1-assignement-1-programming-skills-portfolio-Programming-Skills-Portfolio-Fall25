def check_even_odd(number):
    """
    Function that determines if a number is even or odd
    Returns a message indicating the result
    """
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

def main():
    """
    Main function that gets user input and displays the result
    """
    # Ask the user for a number
    try:
        user_number = int(input("Enter a number: "))
        
        # Pass the number to the function and get the result
        result_message = check_even_odd(user_number)
        
        # Print the message returned by the function
        print(result_message)
        
    except ValueError:
        print("Please enter a valid integer!")

# Run the program
if __name__ == "__main__":
    main()
