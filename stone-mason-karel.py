from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    build_temple()              # starts the program


def build_column():             # checks for clear path and put beepers
    while front_is_clear():
        move()
        put_beeper()

def start():                    # this function builds the column
    turn_left()
    put_beeper()
    build_column()

def turn_180_degrees():         # karel moves 180 degrees ( resetting orientation after building a column )
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_bottom():           # moves to the bottom from the top
    while front_is_clear():
        move()
    turn_left()

def move_to_next_column():      # moves to next column 
    for i in range(4):
        if front_is_clear():
            move()

def build_temple():           
    for i in range(4):
        start()    
        build_column()
        turn_180_degrees()
        move_to_bottom()
        move_to_next_column()

if __name__ == '__main__':
    main()
