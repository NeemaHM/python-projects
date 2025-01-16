# Import the math module to access mathematical constants and functions like pi
import math

# Function to compute the area of a circle given its radius
def calculate_area(radius):
    # Formula to calculate the area of a circle: area = π * r^2
    area = math.pi * radius ** 2
    # Return the computed area
    return area

# Main function to handle user input and display results
def main():
    # Ask the user to input the radius and convert it to a float
    radius_input = float(input("Enter the radius = "))

    # Call the calculate_area function and store the result
    results = calculate_area(radius_input)

    # Print the area, rounded off to two decimal places using f-string formatting
    print(f"The area is {results:.2f}")

# Call the main function to run the program
main()
