# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    return [line for line in puzzle_input.split()]

def find_dup_char(left,right):
    x = []
    for i in left:
        if i not in x and right.count(i)>0:
           return i
    return ''

def find_dup_char_3(first,second,third):
    x = []
    for i in first:
        if i not in x and second.count(i)>0 and third.count(i)>0:
            return i
    return ''

def priority(c):
    ordinal = ord(c)
    if ordinal >= 65 and ordinal <= 90: #A-Z
        return ord(c)-38
    elif ordinal >= 97 and ordinal <= 122: #a-z
        return ord(c)-96
    return(0)

def part1(data):
    """Solve part 1."""
    sum = 0
    for d in data:
        m = round(len(d)/2)
        comp1 = d[:m]
        comp2 = d[m:]
        dup = find_dup_char(comp1,comp2)
        sum += priority(dup)

    return sum
    

def part2(data):
    """Solve part 2."""
    sum = 0
    counter = 0
    group = []
    for d in data:
        counter += 1
        group.append(d)
        if (counter % 3 == 0):
            dup = find_dup_char_3(group[0],group[1],group[2])
            sum += priority(dup)
            group = []
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

