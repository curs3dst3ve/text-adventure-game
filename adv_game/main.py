##############################
# text adventure game
##############################
# variables
na = ""
die = False
insane_effect = False
poisoned = False
health = 100
wood = 0
metal = 0
gem = 0
keys = 0
secret_keys = 0
secret_activator = False
secret_activator_2 = False
secret_activator_3 = False
##############################
print("\n")
print("Hello" + na +
      ", this Text Adventure Game is open source and open for contribution.")
print("If you are playing this game, please support or credit the creator please!")
print("If you need help, or you want to contribute, can look at the game source code here: \nhttps://github.com/curs3dst3ve/text-adventure-game ")
print("Alright then, " + na + " Let's get started!")
na = str(input("To begin, what's you name?\n"))
pronoun = input(
    "Next, what's your pronouns? \n Select From \n He/Him \n She/Her \n or They/Them \n")
print("Starting Game.\n")
print("Hello " + na + "!")
