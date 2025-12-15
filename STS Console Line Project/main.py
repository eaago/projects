from carddb import *
from characterdb import *

print("Slay the Spire Clone Console Based Game\n\nChoose your character: \n1. Ironclad\nOther characters coming soon.")

player = None

while True:
    try:
        choice = int(input("Choose your character: "))
        if(choice == 1):
            player = character_list[0]
    except:
        print("Invalid input. Try again.")
    break

print("You are now playing as ", player.name)
