#defines classes
from tkinter import E


class player():
    health = 100
    name = ""
    location = "start point"
    def __innit__(self, health, name):
        self.health = health
        self.name = name
        self.location
    
    def do_damage(self):
        pass

class sword():
    damagetype= ""
    type = ""
    colour = ""
    pickedup = False

    def __innit__(self, damagetype, type, colour):
        self.damagetype = damagetype
        self.type = type
        self.colour = colour

#defines function to loop player for incorrect answers
def incorrectAnswerLoop(answers):
    while True:
        user_input=input()

        if user_input in answers:
            return user_input
            break

        else:
            print("incorrect input")
            continue

#defines sequence for players sword creation
def sword_sequence():

    #asks user for input/type of sword. Uses while loop to stop incorrect input breaking program
    print("Type of sword \n katana, claymore, dagger")

    #puts player in loop to collect sword type
    sword.type = incorrectAnswerLoop({"katana", "claymore", "dagger"})

    print("\n Cool your sword type is:", sword.type, "\n")

    #asks user input and stores as variable, lets player use whatever colour.
    print("what colour sword?\n")
    sword.colour=input()
    
    print("\nCool, your sword colour is:", sword.colour, "\n")

    #asks user what damage type they want, using a while loop for accepted input
    print("What damage type?\n holy, blood, fire\n")
    
    #puts player in loop to collect damage type
    sword.damagetype = incorrectAnswerLoop({"holy", "blood", "fire"})

    #prints sword stats to player
    print("\nCool, your  sword type is", sword.type, ", your sword colour is", sword.colour, ", and your swords damage type is", sword.damagetype)

#defines level (unfinished btw)
def forest_sequence():
    #defines commands inorder to print to player
    commands = ["forward", "left", "right",\
        "sword stats", "location", "help", "pick up", "attack"]

    #asks players name to use in later dialogue (which is not yet implemented)
    print("what is your name?")
    player.name = input()

    #outlines area around player and gives help command
    print("You are in a forest and your sword is next to you.\n (type help for list of commands)")

    #starts while loop inorder to "kill" player when health reaches zero (however combat system not yet implemented)
    while player.health > 0:
        #asks for user input
        user_input = input().lower()
        
        #big array of user input possibilities which most are fairly simple
        if user_input == "help":
            print("your commands are:", commands)

        elif user_input == "sword stats":
            print("\nCool, your  sword type is", sword.type, ", your sword colour is", sword.colour, ", and your swords damage type is", sword.damagetype)

        elif user_input == "location":
            print(player.location)

        #prints string 1 if sword is picked up. String 2 if not
        elif user_input == "attack":
            if sword.pickedup == True:
                print("you swing your sword and hack off a branch")
            else:
                print("you dont have your sword")

        #assigns True boolean to sword class if pick up is entered. if already picked up it says you already have your sword
        elif user_input== "pick up":
            if sword.pickedup == False and player.location == "start point":
                print("you pick up your sword")
                sword.pickedup = True
            else:
                print("you already have your sword")

        elif user_input== "forward":
            player.location = 

        #inputs other than defined continues loop
        else:
            print("incorrect input")
            continue
    
    #prints string if player is dead
    if player.health > 0:
        print("You Died")
    
    #pass statement to prevent possible errors
    else:
        pass

#starts sword squence
sword_sequence()

#starts forest sequence
forest_sequence()      



    