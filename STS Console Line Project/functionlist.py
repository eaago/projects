import os
import encounterdb
import random

def enemy_encounter(player, encounter):

    shuffle_deck(player.draw)
    message = ""

    while True:
        # Player Turn
        player.energy = player.max_energy
        choice = ""

        draw_cards(player)

        while(choice != "end"):
            clear_screen()
            print(message)
            print(f"\nYour current energy:\n{player.energy}")
            print("\nYour Draw Pile:\n")
            for i, card in enumerate(player.draw):
                print(i, ". ", card.name)

            print("\nYour Current Hand:\n")
            for i, card in enumerate(player.hand):
                print(i, ". ", card.name)

            print("\nYour Discard Pile:\n")
            for i, card in enumerate(player.discard):
                print(i, ". ", card.name)
            
            while True:
                try:
                    choice = input("\n> What card would you like to play: ")
                    if choice == "end":
                        message = "\nEnded your turn."
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

def draw_cards(player):
    if len(player.draw) < player.draw_size:
        print("im here")
        shuffle_deck(player.discard)
        while player.discard:
            card = player.discard.pop(0)
            player.draw.append(card)

    for i in range(player.draw_size):
        card = player.draw.pop(0)
        player.hand.append(card)
        print(f"drew {card.name}")
        print(f"draw size is {player.draw_size}")
    

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=     SLAY THE SPIRE CLONE CONSOLE BASED PROJECT     =")
        print("=                                                    =")
        print("======================================================")