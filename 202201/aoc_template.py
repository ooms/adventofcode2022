# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    ret = []
    elf = []
    for line in puzzle_input.split("\n"):
        if line == "":
            if len(elf) > 0:
                ret.append(elf)
                elf = []
        else:
            elf.append(int(line))
    ret.append(elf)
    return ret

def part1(data):
    """Solve part 1."""
    calories = []
    for elf in data:
        sum = 0
        for c in elf:
            sum += c
        calories.append(sum)
    return max(calories)
    

def part2(data):
    """Solve part 2."""
    calories = []
    for elf in data:
        sum = 0
        for c in elf:
            sum += c
        calories.append(sum)
    calories.sort(reverse=True)
    print(calories[0],calories[1],calories[2])
    return calories[0]+calories[1]+calories[2]

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

