from carddb import *
from characterdb import *
from functionlist import *
from encounterdb import *

clear_screen()

print("\nChoose your character: \n1. Ironclad\nOther characters coming soon.")

player = None

while True:
    try:
        choice = int(input("\n> Choose your character: "))
        if(choice == 1):
            player = character_list[0]
            break
        else:
            print("Selected character not in list. Try again.")
            continue
    except:
        print("Invalid input. Try again.")
        continue
    
if(choice == 1):
    player = character_list[0]
else:
     print("Selected character not in list. Try again.")

clear_screen()

print("\n\nYou are now playing as the", player.name, "\n\nYour starting deck contains:\n")
for card in player.draw:
    print(f"{card.name} - {card.card_type} - Costs {card.cost} energy - {card.description}")

input("\nPress Enter to continue... ")
clear_screen()

# ENCOUNTER 1: SLIME
print("\nAcid Slime Encounter")
enemy_encounter(player, encounter_list[0])


