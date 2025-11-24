def password_checker():
    correct_password = "secret123"  # Define the correct password
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        # Get password from user
        user_input = input("Enter password: ")
        
        # Check if password is correct
        if user_input == correct_password:
            print("Access granted! Welcome.")
            return  # Exit the function when correct password is entered
        
        # If wrong password
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        if remaining_attempts > 0:
            print(f"Wrong password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted!")
            return

# Run the password checker
password_checker()