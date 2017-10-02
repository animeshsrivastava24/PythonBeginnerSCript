"""Dice roller for any number of dice and sides"""
# random int generator
from random import randint

def main():
    """main function"""
    pass

if __name__ == "__main__":
    main()

def dice_input():
    """Get the number of dice."""
    global dice
    # input for dice number variable
    dice = int(raw_input('How many dice would you like to roll? '))
    # Validate for positive integers
    dice_int = False
    while not dice_int:
        if dice <= 0:
            print "Error! Please enter a positive number of dice."
            dice_input()
        else:
            dice_int = True
            print "Ok, I will roll %s dice." % (dice)
    return


def sides_input():
    """Get the number of sides"""
    global sides
    sides = int(raw_input('How many sides does each dice have? '))
    # Validate for positive integers
    sides_int = False
    while not sides_int:
        if sides <= 0:
            print "Error! Please enter a positive number of sides."
            sides_input()
        else:
            sides_int = True
    return


def roll_dice():
    """Loop through number of dice, randomly generate numbers"""
    print "Ok, rolling %s dice with %s sides." % (dice, sides)
    roll = 0
    for roll in range(0, dice):
        print "[%s]" % (randint(1, sides))

    again = raw_input('Would you like to roll, make a change, or end r/c/e? ')
    
    if again == 'r':
        roll_dice()
    elif again == 'e':
        print "Ok, thanks!"
        return
    elif again == 'c':
        change()
    else:
        print "Please respond with r, c, or e"
        roll_dice()


def change():
    """Change number of dice or sides"""
    which = raw_input('Change dice or sides d/s? ')
    if which == 'd':
        dice_input()
        roll_dice()
    else:
        if which == 's':
            sides_input()
            roll_dice()
        else:
            print 'Please input only d or s'
            change()


dice_input()
sides_input()
roll_dice()
