from classlist import *
from movesetdb import *

enemy_list = [

    Enemy(
        id = 0,
        name = "Acid Slime (S)",
        health = 25,
        block = 0,
        status = [],
        moveset = acid_slime_s
    )

]

# ============ ENCOUNTERS ===================

encounter_list = [

    EnemyEncounter(
        id = 0,
        name = "Solo Acid Slime (S)",
        type = "Normal",
        enemy = [enemy_list[0]]
    )

]