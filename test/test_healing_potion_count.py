import pytest

from src.combat_creatures import count_potions_needed

test_cases: list[tuple[str, int, str]] = [
    ("", 0, "No enemies should require no potions"),
    ("Ax", 0, "1 Ancient Ant requires no potions"),
    ("Bx", 1, "1 Badass Beetle should require 1 potion"),
    ("Cx", 3, "1 Creepy cockroach should require 3 potions"),
    ("Dx", 5, "1 Diablolical Dragonfly should require 5 potions"),
    ("AC", 5, "Should require 5 potions"),
    ("BC", 6, "Should return 6 potions needed"),
    ("AABBCC", 14, "Should require 14 potions"),
    ("AxBCDDCAxD", 28, "Should require 28 potions")
]


@pytest.mark.parametrize("enemies,expected_potions_needed,desc", test_cases)
def test_count_potions_needed(
    enemies: str,
    expected_potions_needed: int,
    desc: str
) -> None:
    result: int = count_potions_needed(enemies)
    assert result == expected_potions_needed, desc
