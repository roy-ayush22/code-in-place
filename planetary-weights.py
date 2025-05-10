"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
Mercury_Ratio = 0.376
Venus_Ratio = 0.889
Mars_Ratio = 0.378
Jupiter_Ratio = 2.36
Saturn_Ratio = 1.081
Uranus_Ratio = 0.815
Neptune_Ratio = 1.14

def main():
    earth_weight = float(input("Enter a weight on Earth: "))

    planet = input("Enter a planet: ")

    if planet == "Mercury":
        planet_weight = earth_weight * Mercury_Ratio
    elif planet == "Venus":
        planet_weight = earth_weight * Venus_Ratio
    elif planet == "Mars":
        planet_weight = earth_weight * Mars_Ratio
    elif planet == "Jupiter":
        planet_weight = earth_weight * Jupiter_Ratio
    elif planet == "Saturn":
        planet_weight = earth_weight * Saturn_Ratio
    elif planet == "Uranus":
        planet_weight = earth_weight * Uranus_Ratio
    else:
        planet_weight = earth_weight * Neptune_Ratio

    equivalent_weight = round(planet_weight, 2)

    print(f"The equivalent weight on {planet}: {equivalent_weight}")

if __name__ == "__main__":
    main()
