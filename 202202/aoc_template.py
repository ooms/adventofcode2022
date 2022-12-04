# aoc_template.py

import pathlib
import sys
LOST = [['A', 'Z'],['B', 'X'],['C', 'Y']]
DRAW = [['A', 'X'],['B', 'Y'],['C', 'Z']]
WIN  = [['A', 'Y'],['B', 'Z'],['C', 'X']]

def checkSubset(list1,list2):
#    return all(x in list1 for x in list2)
    for elem in list1:
        if list2 == elem:
            return True

    return False

def parse(puzzle_input):
    """Parse input. """
    ret = []
    for line in puzzle_input.split("\n"):
        sub = []
        for l in line.split():
            sub.append(l)
        ret.append(sub)
    return ret

def part1(data):
    """Solve part 1."""
    score = 0
    for d in data:
        if d[1] == 'X':
            score += 1
        elif d[1] == 'Y':
            score += 2
        elif d[1] == 'Z':
            score += 3
        if checkSubset(DRAW,d) == True:
            score += 3
        elif checkSubset(WIN,d) == True:
            score += 6
            
    return score
    
def win(left):
    if left == 'A':
        return 2
    elif left == 'B':
        return 3
    elif left == 'C':
        return 1

def draw(left):
    if left == 'A':
        return 1
    elif left == 'B':
        return 2
    elif left == 'C':
        return 3

def lose(left):
    if left == 'A':
        return 3
    elif left == 'B':
        return 1
    elif left == 'C':
        return 2
    
def part2(data):
    """Solve part 2."""
    score = 0
    for d in data:
        if d[1] == 'X': #you need to lose
            score += 0 + lose(d[0])
        elif d[1] == 'Y': #you need to end in a draw
            score += 3 + draw(d[0])
        elif d[1] == 'Z': #you need to win
            score += 6 + win(d[0])
    return score

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

