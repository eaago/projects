class Card:
    def __init__(self, id, name, cost, card_type, description, effect):
        self.id = id
        self.name = name
        self.cost = cost
        self.card_type = card_type
        self.description = description
        self.effect = effect

class Character:
    def __init__(self, name, health, energy, block, status, draw, hand, discard, exhaust, draw_size):
        self.name = name
        self.health = health
        self.energy = energy
        self.block = block
        self.status = status
        self.draw = draw
        self.hand = hand
        self.discard = discard
        self.exhaust = exhaust
        self.draw_size = draw_size

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
    def __init__(self, id, name, health, block, status, moveset):
        self.id = id
        self.name = name
        self.health = health
        self.block = block
        self.status = status
        self.moveset = moveset

class Moves:
    def __init__(self, id, name, type, damage, block, status):
        self.id = id
        self.name = name,
        self.type = type,
        self.damage = damage,
        self.block = block,
        self.status = status

class Event:
    def __init__(self, id, name, choices):
        self.id = id
        self.name = name
        self.choices = choices

class RestSite:
    def __init__(self):
        self.choices = ["Rest", "Upgrade"]






