from crypto_price_analysis import *

def main_menu():
    
    while True:
        print("\nWelcome to the Data Analysis Tool")
        print("Please select an option:")
        print("1. Product Price Tracker")
        print("2. Job Listing Analysis")
        print("3. Weather Pattern Analysis")
        print("4. Cryptocurrency Price Analysis")
        print("5. Exit")

        option_input = input("Select an option: ")

        if option_input == "1":
            product_price_tracker()
        elif option_input == "2":
            job_listing_analysis()
        elif option_input == "3":
            weather_pattern_analysis()
        elif option_input == "4":
            cryptocurrency_price_analysis()
        elif option_input == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

def product_price_tracker():
    # Code to track and analyze product prices
    print("Running Product Price Tracker...")
    # Add scraping, cleaning, analyzing, and visualizing here
    pass

def job_listing_analysis():
    # Code to analyze job listings
    print("Running Job Listing Analysis...")
    # Add scraping, cleaning, analyzing, and visualizing here
    pass

def weather_pattern_analysis():
    # Code to analyze weather patterns
    print("Running Weather Pattern Analysis...")
    # Add API calls, data processing, and visualization here
    pass



# Start the program by calling the main menu
main_menu()
