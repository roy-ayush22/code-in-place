:# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

from karel.stanfordkarel import *

def main():
    move()
    for i in range(3):
        while beepers_present():
            pick_beeper()
        move()
        if front_is_clear():
            move()
        
            
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
