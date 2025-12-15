from carddb import *
from characterdb import *
from functionlist import *

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

print("You are now playing as ", player.name, "\nYour starting deck contains ")
for card in player.deck:
    print(f"{card.name} - {card.card_type} - Costs {card.cost} energy - {card.description}")


