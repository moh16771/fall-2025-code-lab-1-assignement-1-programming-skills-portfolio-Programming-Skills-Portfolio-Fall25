def days_in_month_enhanced():
    # Create dictionary with month names and days
    months = {
        1: {"name": "January", "days": 31},
        2: {"name": "February", "days": 28},
        3: {"name": "March", "days": 31},
        4: {"name": "April", "days": 30},
        5: {"name": "May", "days": 31},
        6: {"name": "June", "days": 30},
        7: {"name": "July", "days": 31},
        8: {"name": "August", "days": 31},
        9: {"name": "September", "days": 30},
        10: {"name": "October", "days": 31},
        11: {"name": "November", "days": 30},
        12: {"name": "December", "days": 31}
    }
    
    try:
        month = int(input("Enter the month number (1-12): "))
        
        if month not in months:
            print("Invalid input! Please enter a number between 1 and 12.")
            return
        
        month_name = months[month]["name"]
        days = months[month]["days"]
        
        # Leap year adjustment for February
        if month == 2:
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_year in ['yes', 'y']:
                days = 29
        
        print(f"{month_name} (Month {month}) has {days} days.")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the enhanced program
if __name__ == "__main__":
    days_in_month_enhanced()
