# Rock-paper-scissors-lizard-Spock template


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
import random

def name_to_number(name):
    dic = {"rock": 0, "Spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
    return dic[name]

def number_to_name(number):
    dic = {0: "rock", 1: "Spock", 2: "paper", 3: "lizard", 4: "scissors"}
    return dic[number]

def rpsls(player_choice):
    player = name_to_number(player_choice)
    computer = random.randrange(0, 5)
    print "Player chooses", player_choice
    print "Computer chooses", number_to_name(computer)
    
    if player == computer:
        print "Player and computer tie!"
    elif (player - computer) % 5 <= 2:
        print "Player wins!"
    else:
        print "Computer wins!"
    
    print ""
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric
