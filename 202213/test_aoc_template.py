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
    assert example1 == [['[1,1,3,1,1]','[1,1,5,1,1]'],
			            ['[[1],[2,3,4]]','[[1],4]'],
			            ['[9]','[[8,7,6]]'],
			            ['[[4,4],4,4]','[[4,4],4,4,4]'],
			            ['[7,7,7,7]','[7,7,7]'],
			            ['[]','[3]'],
			            ['[[[]]]','[[]]'],
			            ['[1,[2,[3,[4,[5,6,7]]]],8,9]','[1,[2,[3,[4,[5,6,0]]]],8,9]']
			            ]

@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ...
    
def test_part1_example1(example1):
    """Test part1 on example1 input."""
    assert aoc.part1(example1) == 13
    
def test_part2_example1(example1):
    """Test part2 on example1 input."""
    assert aoc.part2(example1) == 140

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part2 on example2 input."""
    assert aoc.part2(example2) == ...
