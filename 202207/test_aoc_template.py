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

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {'root':['root_a',14848514,8504156,'root_d'],'root_a':['root_a_e',29116,2557,62596],'root_a_e':[584],'root_d':[4060174,8033020,5626152,7214296]}

@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == {'root':['a',14848514,8504156,'d'],'a':['e',29116,2557,62596],'e':[584],'d':[4060174,8033020,5626152,7214296]}
    
def test_part1_example1(example1):
    """Test part1 on example1 input."""
    assert aoc.part1(example1) == 95437
    
def test_part2_example1(example1):
    """Test part2 on example1 input."""
    assert aoc.part2(example1) == 24933642

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part2 on example2 input."""
    assert aoc.part2(example2) == ...
