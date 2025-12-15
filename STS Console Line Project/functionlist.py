import os
import encounterdb
import random

def enemy_encounter(player, encounter):

    shuffle_deck(player.draw)

    while True:
        # Player Turn
        player.hand = draw_cards(player)
        choice = 1

        while(choice != 99):
            clear_screen()
            print(f"\nYour current energy:\n{player.energy}\n")
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
                    choice = int(input("\n> What card would you like to play: "))
                    if choice < 0 or choice >= len(player.hand):
                        print("Invalid card number. Try again.")
                        continue
                    elif(choice == 99):
                        break
                    else:
                        break
                except:
                    print("Invalid input. Try again.")
                    continue

            if choice == 99:
                break
            elif player.energy >= player.hand[choice].cost:
                print(f"You played {player.hand[choice].name}")
                player.energy -= player.hand[choice].cost
                played = player.hand.pop(choice)
                player.discard.append(played)
            else:
                print("Not enough energy.")

        


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def draw_cards(player):
    if len(player.draw) < player.draw_size:
        shuffle_deck(player.discard)
        while player.discard:
            card = player.discard.pop(0)
            player.draw.append(card)

    for i in range(player.draw_size):
        card = player.draw.pop(0)
        player.hand.append(card)
    
    return player.hand


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=     SLAY THE SPIRE CLONE CONSOLE BASED PROJECT     =")
        print("=                                                    =")
        print("======================================================")