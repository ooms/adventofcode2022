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
    assert example1 == {'root': ['pppw','+','sjmn'],
                        'dbpl': 5,
                        'cczh': ['sllz','+','lgvd'],
                        'zczc': 2,
                        'ptdq': ['humn','-','dvpt'],
                        'dvpt': 3,
                        'lfqf': 4,
                        'humn': 5,
                        'ljgn': 2,
                        'sjmn': ['drzm','*','dbpl'],
                        'sllz': 4,
                        'pppw': ['cczh','/','lfqf'],
                        'lgvd': ['ljgn','*','ptdq'],
                        'drzm': ['hmdt','-','zczc'],
                        'hmdt': 32}

@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ...
    
def test_part1_example1(example1):
    """Test part1 on example1 input."""
    assert aoc.part1(example1) == 152
    
def test_part2_example1(example1):
    """Test part2 on example1 input."""
    assert aoc.part2(example1) == 301

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part2 on example2 input."""
    assert aoc.part2(example2) == ...
