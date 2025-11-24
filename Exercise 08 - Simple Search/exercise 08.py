def search_names():
    # Initialize the list of names
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    print("Available names:", names)
    print()
    
    # Basic requirement: Search for "Sam"
    print("=== Basic Search (Predefined: 'Sam') ===")
    search_term = "Sam"
    
    if search_term in names:
        print(f"✓ '{search_term}' was found in the list!")
    else:
        print(f"✗ '{search_term}' was not found in the list.")
    print()
    
    # Optional requirement: User input search
    print("=== Optional: User Input Search ===")
    user_search = input("Enter a name to search for: ")
    
    # Search for user input
    if user_search in names:
        print(f"✓ '{user_search}' was found in the list!")
    else:
        print(f"✗ '{user_search}' was not found in the list.")

# Run the program
search_names()
