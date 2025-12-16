import os
import encounterdb
import random
import keyboard

def enemy_encounter(player, encounter):

    shuffle_deck(player.draw)
    message = ""

    # Player Turn Start
    while True:
        player.energy = player.max_energy
        choice = ""

        draw_cards(player, player.draw_size)

        # Player Turn Card Selection
        while(choice != "end"):
            clear_screen()
            print(message)

            print("\n============================\n")
            # Player Information Panel
            print(f"The {player.name}:")
            print(f"\nHP:\t\t{player.health} / {player.max_health}")
            print(f"Block:\t\t{player.block}")
            print(f"Energy:\t\t{player.energy} / {player.max_energy}")
            print(f"\nStatus Effects:")
            if len(player.status) == 0:
                print("No status effects")
            else:
                for stat_effect in player.status:
                    print(stat_effect)

            print("\n============================\n\nThe Enemy:")
            for i, e in enumerate(encounter.enemy):
                print(e.name)
                print(f"\nHP:\t\t{e.health} / {e.max_health}")
                print(f"Block:\t\t{e.block}")
                print(f"\nStatus Effects:")
                if len(e.status) == 0:
                    print("No status effects")
                else:
                    for stat_effect in e.status:
                        print(stat_effect)

            print("\n============================")
            print("\nYour Hand:\n")
            for i, card in enumerate(player.hand):
                print(f"[{i}]. {card.cost} energy - {card.name} - {card.description}")
        
            while True:
                try:
                    choice = input("\nType the card number to play card, \"draw\" to view draw pile, or \"discard\" to view discard pile.\n> What card would you like to play: ")
                    if choice == "end":
                        message = "\nEnded your turn."
                        break
                    elif choice == "draw":
                        print("\nYour Draw Pile:\n")
                        if len(player.draw) == 0:    
                            print("Your draw pile is empty.")  
                        else:                
                            for i, card in enumerate(player.draw):
                                print(f"[{i}]. {card.cost} energy - {card.name} - {card.description}")
                        input("\nPress Enter to return...")
                        break
                    elif choice == "discard":
                        print("\nYour Discard Pile:\n")
                        if len(player.discard) == 0:
                            print("Your discard pile is empty.")
                        else:
                            for i, card in enumerate(player.discard):
                                print(f"[{i}]. {card.cost} energy - {card.name} - {card.description}")
                        input("\nPress Enter to return... ")
                        break
                    elif int(choice) < 0 or int(choice) >= len(player.hand):
                        print("Invalid card number. Try again.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Try again.")
                    continue

            if choice == "end":
                while player.hand:
                    unplayed = player.hand.pop(0)
                    player.discard.append(unplayed)
                break
            elif choice == "draw" or choice == "discard":
                continue
            elif player.energy >= player.hand[int(choice)].cost:
                message = f"\nYou played {player.hand[int(choice)].name}"
                player.energy -= player.hand[int(choice)].cost
                played = player.hand.pop(int(choice))
                player.discard.append(played)
            else:
                message = "\nNot enough energy."

        


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def draw_cards(player, amount):
    if len(player.draw) < amount:
        shuffle_deck(player.discard)
        while player.discard:
            card = player.discard.pop(0)
            player.draw.append(card)

    for i in range(amount):
        card = player.draw.pop(0)
        player.hand.append(card)
        print(f"drew {card.name}")


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=     SLAY THE SPIRE CLONE CONSOLE BASED PROJECT     =")
        print("=                                                    =")
        print("======================================================")