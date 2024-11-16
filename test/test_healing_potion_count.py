import pytest

from src.combat_creatures import count_potions_needed

test_cases: list[tuple[str, int, str]] = [
    ("", 0, "No enemies should require no potions"),
    ("A", 0, "Ancient ants require no potions"),
    ("B", 1, "1 Badass Beetle should require 1 potion"),
    ("C", 3, "1 Creepy cockroach should require 3 potions"),
    ("AC", 3, "Should return 3 potions needed"),
    ("BC", 4, "Should return 4 potions needed"),
    ("AABBCC", 8, "Should require 8 potions")
]


@pytest.mark.parametrize("enemies,expected_potions_needed,desc", test_cases)
def test_count_potions_needed(
    enemies: str,
    expected_potions_needed: int,
    desc: str
) -> None:
    result: int = count_potions_needed(enemies)
    assert result == expected_potions_needed, desc
