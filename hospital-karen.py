from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    move()
    move()
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()
    move_block()
    move_beeper()
    for i in range(4):
        move()
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()




#  costom functions 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_block():
    for i in range(5):
        move()

def move_beeper():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()

if __name__ == '__main__':
    main()
