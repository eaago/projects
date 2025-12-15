class Card:
    def __init__(self, id, name, cost, card_type, description, effect):
        self.id = id
        self.name = name
        self.cost = cost
        self.card_type = card_type
        self.description = description
        self.effect = effect

class Character:
    def __init__(self, name, health, energy, block, status, deck):
        self.name = name
        self.health = health
        self.energy = energy
        self.block = block
        self.status = status
        self.deck = deck

    def deal_damage():
        print()

    def receive_block():
        print()

    def receive_damage():
        print()

    def receive_status():
        print()

class EnemyEncounter:
    def __init__(self, id, name, type, enemy):
        self.id = id
        self.name = name
        self.type = type
        self.enemy = enemy # List of enemies

class Enemy:
    def __init__(self, id, name, health, block, status, intent, moveset):
        self.id = id
        self.name = name
        self.health = health
        self.block = block
        self.status = status
        self.intent = intent
        self.moveset = moveset

class Event:
    def __init__(self, id, name, choices):
        self.id = id
        self.name = name
        self.choices = choices

# class Shop:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class RestSite:
    def __init__(self):
        self.choices = ["Rest", "Upgrade"]






