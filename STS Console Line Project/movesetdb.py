from classlist import Moves
import constants

# Acid Slime (S)
acid_slime_s = [
    Moves(
        id = 0,
        name = "Tackle",
        type = constants.ATTACK,
        damage = 8,
        block = None,
        status = None
    ),
    Moves(
        id = 1,
        name = "Harden",
        type = constants.BLOCK,
        damage = None,
        block = 10,
        status = None
    ),
    Moves(
        id = 2,
        name = "Slime Spray",
        type = constants.STATUS,
        damage = None,
        block = None,
        status = [constants.WEAK]
    ),
]