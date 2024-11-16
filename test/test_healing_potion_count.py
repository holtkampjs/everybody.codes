import pytest

from src.combat_creatures import count_potions_needed

test_cases: list[tuple[str, int, str]] = [
    ("", 0, "No enemies should require no potions"),
    ("Axx", 0, "1 Ancient Ant requires no potions"),
    ("Bxx", 1, "1 Badass Beetle should require 1 potion"),
    ("Cxx", 3, "1 Creepy cockroach should require 3 potions"),
    ("Dxx", 5, "1 Diablolical Dragonfly should require 5 potions"),
    ("ACx", 5, "Should require 5 potions"),
    ("BCx", 6, "Should return 6 potions needed"),
    ("AAA", 6, "Should return 6 potions needed"),
    ("AABBCC", 20, "Should require 20 potions"),
    ("xBxAAABCDxCC", 30, "Should require 30 potions")
]


@pytest.mark.parametrize("enemies,expected_potions_needed,desc", test_cases)
def test_count_potions_needed(
    enemies: str,
    expected_potions_needed: int,
    desc: str
) -> None:
    result: int = count_potions_needed(enemies)
    assert result == expected_potions_needed, desc
