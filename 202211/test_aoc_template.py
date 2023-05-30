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
    assert example1 == { 0: {'items':[79,98],
                             'operation': 'old * 19',
                             'test': [23,2,3],
                             'inspected': 0},
                         1: {'items':[54,65,75,74],
                             'operation': 'old + 6',
                             'test': [19,2,0],
                             'inspected': 0},
                         2: {'items':[79,60,97],
                             'operation': 'old * old',
                             'test': [13,1,3],
                             'inspected': 0},
                         3: {'items':[74],
                             'operation': 'old + 3',
                             'test': [17,0,1],
                             'inspected': 0}}

@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ...
    
def test_part1_example1(example1):
    """Test part1 on example1 input."""
    assert aoc.part1(example1) == 10605
    
def test_part2_example1(example1):
    """Test part2 on example1 input."""
    assert aoc.part2(example1) == 2713310158

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part2 on example2 input."""
    assert aoc.part2(example2) == ...
