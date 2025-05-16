# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    ask_age = float(input("Enter an age in calendar years: "))
    equate_age = ask_age * DOG_YEARS_MULTIPLIER

    print(f"That's {equate_age} in dog years!")

if __name__ == '__main__':
    main()
