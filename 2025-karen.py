(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""
from karel.stanfordkarel import *

def main():
    for i in range(2):
        move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    turn_left()
    turn_left()
    for i in range(2):
        move()
    turn_right()
    for i in range(3):
        move()
    turn_left()
    turn_left()
    

# custom funtion

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
