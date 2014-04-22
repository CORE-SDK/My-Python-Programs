# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # converts the name input into a number
    
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print 'Please Input a valid Name ("Rock", "Paper", "Scissors", "Lizard", "Spock")'
        print " R E I N P U T   Y O U R   G U E S S "
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # converts the input number into the corresponding name
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print 'Number out of Range ( An integer from 0 to 4 )'
        print " R E I N P U T   Y O U R   G U E S S "
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    
    # printing player choice
    print "---------------------------------------------------------------------------------"
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    
    # generating and printing computer choice
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    
    # determining the winner
    mod_diff = (player_number - comp_number) % 5
    if mod_diff == 1 or mod_diff == 2:
        print "Player wins!"
    elif mod_diff == 3 or mod_diff == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print " "
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
