# aoc_template.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input. """
    spaces = []
    for line in puzzle_input.split():
        space = []
        for ln in line.split(","):
            elf = []
            for l in ln.split("-"):
                elf.append(int(l))
            space.append(elf)
        spaces.append(space)
    print(spaces)
    return spaces

def make_array(first,last):
    ar = []
    i = first
    while i <= last:
        ar.append(i)
        i += 1
    return ar

def part1(data):
    """Solve part 1."""
    sum = 0
    for pairs in data:
        left = pairs[0]
        right = pairs[1]
        l_array = make_array(left[0],left[1])
        r_array = make_array(right[0],right[1])
        overlap = np.intersect1d(l_array,r_array)
        if len(overlap) > 0 and (len(overlap) == len(l_array) or len(overlap) == len(r_array)):
            sum += 1
    return sum
    

def part2(data):
    """Solve part 2."""
    sum = 0
    for pairs in data:
        left = pairs[0]
        right = pairs[1]
        l_array = []
        r_array = []
        i = left[0]
        while i <= left[1]:
            l_array.append(i)
            i += 1
        i = right[0]
        while i <= right[1]:
            r_array.append(i)
            i += 1
        overlap = np.intersect1d(l_array,r_array)
        if len(overlap) > 0:
            sum += 1
    return sum

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

