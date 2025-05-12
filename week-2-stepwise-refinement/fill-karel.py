from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while facing_east():
        fill_row()
        turn_180_degrees()
        return_back()
        turn_right()
        next_row()
        
    # initial_position()

def turn_180_degrees():
    turn_left()
    turn_left()

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def return_back():
    while front_is_clear():
        move()
def turn_right():
    for i in range(3):
        turn_left()

def next_row():
    move()
    turn_right()

def initial_position():
    for i in range(4):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
