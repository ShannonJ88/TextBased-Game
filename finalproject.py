##########################################################
##                                                      ##
##                  Shannon Julion                      ##
##     Final Project - Text based Adventure Game        ##
##                      Python 2                        ##
##                                                      ##
##########################################################

##########################################################
##########################################################
##					******************					##
##                  *   DOLL FILES   *					##
#                   ******************					 #
#  Help Ava solve the mystery and find her missing doll! #
# Ava's precious baby doll that her grandmother gave to  #
# her before passing away has gone missing. This doll 	 #
# means the world to her and she doesn't know what she 	 #
# will do if she doesn't find it.  Ava lives in Sugar 	 #
# Land which has multiple units. You will play this game # 
# by navigating through the units to find this doll.  	 #
# Each unit has an obstacle that you will to get past to #
# find the doll. If you do not sucessfully complete this #
# obstacle, you will fail this mission and end the game. # 
# If you select the correct unit and pass the obstacle,  #
# you will win!Please solve the mystery and reunite Ava  #
# with her missing doll.								 #
#														 #	
##########################################################
##########################################################

import random
import time


def display_intro():
    print "Welcome to SugarLand!"
    name = raw_input("Please enter your name: ")
    print "Hello", name, "!"
    print "We have a dilemma here..."
    time.sleep(2)
    print "Ava's doll is missing... Oh no!!!"
    time.sleep(2)
    print "Please help her find her precious doll!"
    time.sleep(2)
    print "Navigate through SugarLand and solve this mystery!"
    print " "
    time.sleep(2)
	
#--------------------- Start Game --------------------------------------#
def start_Game():
    choice = raw_input("Enter 1 to enter Sugar Land OR Enter 2 to exit: ")
    
    while True:
        if choice == "1":
            print "Welcome! Let's get started!"
            return sugarLand_entry()
        elif choice == "2":
            print "Winners can't be quitters! Goodbye!"
            exit();
        else:
            print "Please enter a valid command(1 or 2): "
            return start_Game()

def sugarLand_entry():
    print "You are now in SugarLand"
    print "Select which unit you want to search first"
    print "....but I must warn you....."
    time.sleep(4)
    print "pay close attention to the instructions OR ELSE!" 
    print "Select 1 to enter Cotton Candy Cabin"
    print "Select 2 to enter Lollipop Lab"
    print "Select 3 to enter Peppermint Place"
    unit = raw_input("Please Select an option(Select 1, 2, or 3): ")
    while True:
        if unit == "1":
            cottonCandy_Cabin()
        elif unit == "2":
            lollipop_lab()
        elif unit == "3":
            peppermint_Place()
        else:
            exit()

def cottonCandy_Cabin():
    print "You enter Cotton Candy Cabin"
    print "Rainbows are painted on every wall"
    print "The unit is filled with Cotton Candy"
    print "You really want to eat some Cotton candy...."
    print "but you see a clown" 
    print "You need to get past the clown in order to search Cotton Candy Cabin" 
    option = raw_input("Enter(eat, cry, or next): ")
    while True:
        
        if option == "cry":
            print "You walk up to the clown and ask it to help you find the missing doll"
            print "Then you begin to cry"
            print "Clowns hate crying"
            print "The clown zips to the door and exits Cotton Candy Cabin"
            print "You search the area, looking everywhere for the missing doll"
            print "....and you can't find it anywhere"
            time.sleep(3)
            print "Good try! You loose! The missing doll is not located in Cotton Candy Cabin, GOODBYE"
            exit() 
        elif option == "eat":
            print "Who told you to eat that candy! Follow directions and make better decisions! Game Over! GOODBYE"
            exit()
        elif option == "next":
            print "Great choice the missing doll is not located in this room anyway!"
            print "You are now leaving Cotton Candy Cabin...up next...Lollipop Lab"
            peppermint_Place()
        else:
            print "Please enter a valid option next time!"
            exit()

def lollipop_lab():
    print "You have now entered Lollipop Lab"
    print "Search this unit to find it"
    print "You are fighting the temptation to eat the lollipops, but the swirls are making you dizzy"
    print "You head to the kitchen...."
    print "Oh no!....Jolly the joyus Jack Russel is sitting in the kitchen wagging her tail"
    print "Figure out a way to get rid of Jolly so that you can search the Lollipop Lab"
    option_two = raw_input("Enter(whistle, or fetch): ")

    while True:
        if option_two == "whistle":
            print "You whistle really loud and Jolly runs towards you barking. You aren't a dog person so you run as fast as you can to the exit, GOODBYE!"
            display_intro()
        elif option_two == "fetch":
            print "You saw a bone next to the entrance of the doorway, you grab the bone, call Jolly, then throws the bone out the Lollipop Lab" 
            print "Jolly runs after it and you slam the door shut and yell, SUCKER and laugh"
            print "You search for the Ava's doll, you look everywhere....but no luck again!"
            print "You need to leave Lollipop Lab and search another unit! Choose another unit and don't give up! It has to be in Sugarland somewhere!"
            sugarLand_entry()
        else:
            print "Please enter a valid option next time!"
            exit()
	
def peppermint_Place():
    print "You have now entered Peppermint Place"
    print "Maybe the missing doll is located in here, search the unit to solve the mystery!"
    print "You start looking in the living room, nothing there"
    print "You head to the bedroom and on the bed you see Mr. Mint..."
    print "Mr Mint sees you and yells, do not enter the room, Leave PepperMint Place immediately"
    print "The doll has to be in the room, why else is Mr. Mint demanding that you leave? "
    print "....hmmmm how can you get in this room now?"
    option_three = raw_input("Enter(roar, or joke): ")

    while True:
        if option_three == "roar":
            print "You suddenly go ROAAAAAAARRRRRRRRRR really loud"
            print "So loud that everyone in SugarLand hears you"
            print "So loud that you frighten Mr. Mint!"
            print "He gets up off the bed and starts throwing peppermint candycanes at you... He yells get out of here!"
            print "He continues to throw the candycanes until you leave PepperMint Place"
            exit()
        elif option_three == "joke":
            print "You decide to tell Mr. Mint a joke. He loves Jokes"
            print "He laughs hysterically at your joke then asks you what you're doing in Peppermint Place"
            print "You tell them that you are trying to help Ava find her missing doll that disappeared in SugarLand"
            print "Mr Mint thinks that's awfully nice of you and precedes to help you look for the doll"
            print "You both search everywhere for the doll, the bathroom, closets, under the beads, in the cracks of the couches!"
            time.sleep(4)
            print "..................and you find the missing doll HOORAY!!!! YOU WIN the game! Your character is everything! Thank you for finding Ava's precious doll!"
            exit()
            
            
            
            
            
display_intro()
start_Game()