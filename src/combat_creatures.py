ANCIENT_ANT: str = "A"
BADASS_BEETLE: str = "B"
CREEPY_COCKROACH: str = "C"


def count_potions_needed(enemies: str) -> int:
    return enemies.count(BADASS_BEETLE) + enemies.count(CREEPY_COCKROACH)*3


if __name__ == "__main__":
    with open("data/everybody_codes_e2024_q01_p1.txt", "r") as f:
        enemies: str = f.readline()

    potions_needed: int = count_potions_needed(enemies)

    print("Potions needed:", potions_needed)
