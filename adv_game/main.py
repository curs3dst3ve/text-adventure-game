##############################
# text adventure game
##############################
# variables
boypronouns = "he,him,mr,etc etc etc etc"
girlpronouns = "she her mrs etc etc etc"
theypronouns = "they them etc etc etc"
difficulty = ""
pronouns = ""
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
      ", this Text Adventure Game is open source and open for contribution.\n")
print("If you are playing this game, please support or credit the creator please!\n")
print("If you need help, or you want to contribute, can look at the game source code here: \n                                https://github.com/curs3dst3ve/text-adventure-game \n")
print("Alright then, " + na + " Let's get started! \n ")
na = str(input("To begin, what's your name?\n"))
pronoun = input(
    "Next, what's your pronouns? \n Select From \n He/Him \n She/Her \n or They/Them \n")
if pronoun == "He/Him" or "he/him" or "he/Him" or "He/him":
    pronoun = boypronouns
elif pronoun == "She/Her" or "she/her" or "she/Her" or "She/her":
    pronoun = girlpronouns
elif pronoun == "He/Him" or "he/him" or "he/Him" or "He/him":
    pronoun = theypronouns
else:
    print("Error 1: Pronoun Choosing.")

difficulty = input(
    "Then, please choose a difficulty.\n Easy\n Normal\n Hard\n Expert\n Master\n why the fuck would you choose this difficulty?\n")

print("Starting Game.\n")
print("Hello " + na + "!")
