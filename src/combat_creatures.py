ANCIENT_ANT: str = "A"
BADASS_BEETLE: str = "B"
CREEPY_COCKROACH: str = "C"
DIABOLICAL_DRAGONFLY: str = "D"

ENEMY_POTIONS_REQUIRED: dict = {
    ANCIENT_ANT: 0,
    BADASS_BEETLE: 1,
    CREEPY_COCKROACH: 3,
    DIABOLICAL_DRAGONFLY: 5
}


def count_potions_needed(enemies: str) -> int:
    potion_count: int = 0
    for index in range(0, len(enemies), 2):
        battle = enemies[index:index+2]
        battle = battle.replace("x", "")
        match len(battle):
            case 1:
                potion_count += ENEMY_POTIONS_REQUIRED.get(battle[0], 0)
            case 2:
                potion_count += ENEMY_POTIONS_REQUIRED.get(battle[0], 0)
                potion_count += ENEMY_POTIONS_REQUIRED.get(battle[1], 0)
                potion_count += 2
    return potion_count


if __name__ == "__main__":
    # TODO: Use argparser to read in file name
    with open("data/everybody_codes_e2024_q01_p2.txt", "r") as f:
        enemies: str = f.readline()

    potions_needed: int = count_potions_needed(enemies)

    print("Potions needed:", potions_needed)
