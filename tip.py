# Main function that orchestrates the program
def main():
    # Ask the user how much the meal cost, and convert the input to a float (dollars)
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Ask the user what percentage they want to tip, and convert the input to a float (percentage)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip based on the meal cost and the tip percentage
    tip = dollars * percent
    
    # Output the amount of tip to leave, formatted to two decimal places
    print(f"Leave ${tip:.2f}")
    
    # Output the percentage of the tip, formatted as a whole number percentage (e.g., 15% instead of 0.15%)
    print(f"You tipped {percent * 100:.0f}%")  # Multiplies by 100 to show the percentage in a readable format


# Function that converts the input dollar amount (string) into a float value
def dollars_to_float(d):
    # Strip the "$" symbol and convert the string to a float
    return float(d.strip("$"))

# Function that converts the input percentage (string) into a float value
def percent_to_float(p):
    # Strip the "%" symbol and convert the string to a float, then divide by 100 to get the decimal form of the percentage
    return float(p.strip("%")) / 100


# Call the main function to run the program
main()
