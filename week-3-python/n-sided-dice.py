import random

def main():
    dice_sides = int(input("How many sides does your dice have? "))

    # generates a random number between 1 and number of dice side entered
    dice_roll_result = random.randint(1,dice_sides)


    print(f"Your roll is {dice_roll_result}")

if __name__ == '__main__':
    main()
