"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # asks to enter a weight on earth
    weight_on_earth = float(input("Enter a weight on Earth: "))

    """Calculates the equivalent weight on Mars,
     by multiplying the Earth weight by the gravitational ratio (0.378),
     and rounding to two decimal places"""
    mars_weight = round((weight_on_earth * 0.378), 2)

    # Prints the calculated weight on Mars
    print_mars_weight = print(f"The equivalent weight on Mars: {mars_weight}")



if __name__ == "__main__":
    main()
