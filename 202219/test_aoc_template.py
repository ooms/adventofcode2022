#test aoc_template.py

import pathlib
import pytest
# change the aoc_template to import your solution file
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# remove the skip mark lines below when you are ready to start testing
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {0: {ore_cost_ore: 4,
                            clay_cost_ore: 2,
                            obsidian_cost_ore: 3,
                            obsidian_cost_clay: 14,
                            geode_cost_ore: 2,
                            geode_cost_obsidian: 7,
                            ore_robot: 1,
                            clay_robot: 0,
                            obsidian_robot: 0,
                            geode_robot: 0,
                            ore: 0,
                            clay: 0,
                            obsidian: 0,
                            geode: 0},
                        1: {ore_cost_ore: 2,
                            clay_cost_ore: 3,
                            obsidian_cost_ore: 3,
                            obsidian_cost_clay: 8,
                            geode_cost_ore: 3,
                            geode_cost_obsidian: 12,
                            ore_robot: 1,
                            clay_robot: 0,
                            obsidian_robot: 0,
                            geode_robot: 0,
                            ore: 0,
                            clay: 0,
                            obsidian: 0,
                            geode: 0}}

@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ...
    
@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part1 on example1 input."""
    assert aoc.part1(example1) == 33
    
@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part2 on example1 input."""
    assert aoc.part2(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part2 on example2 input."""
    assert aoc.part2(example2) == ...
