class Card:
    def __init__(self, deck, name, cost, card_type, description, effect):
        self.deck = deck
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
