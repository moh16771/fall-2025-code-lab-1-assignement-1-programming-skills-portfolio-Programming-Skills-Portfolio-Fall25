def password_system_basic():
    correct_password = "12345"  # 1. Define the correct password
    
    # 2. Use while loop to repeatedly ask for password
    while True:
        user_input = input("Enter password: ")
        
        if user_input == correct_password:
            # 3. Output appropriate message for correct password
            print("Access granted! Welcome to the system.")
            break
        else:
            print("Wrong password. Please try again.")

# Run the basic version
password_system_basic()
