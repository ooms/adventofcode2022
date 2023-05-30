# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    return [line for line in puzzle_input.split()]

def has_dup_char(lst):
    for i in lst:
        if lst.count(i)>1:
            return True
    return False

def part1(data):
    """Solve part 1."""
    ret = []
    for d in data:
        i = 0
        while i < len(d):
            if not has_dup_char(d[i:i+4]):
                ret.append(i+4)
                break
            i += 1
    return ret
    

def part2(data):
    """Solve part 2."""
    ret = []
    for d in data:
        i = 0
        while i < len(d):
            if not has_dup_char(d[i:i+14]):
                ret.append(i+14)
                break
            i += 1
    return ret
def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

