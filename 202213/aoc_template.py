# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    ret_lst = []
    lst = []
    for line in puzzle_input.split("\n"):
        if line == "":
            ret_lst.append(lst)
            lst = []
            continue
        lst.append(line)
    ret_lst.append(lst)

    return ret_lst

def compare(left,right):
    if type(left) == type(right) == int:
        if left < right:
            return -1
        elif left > right: 
            return 1
        else:
            return 0
    elif type(left) == type(right) == list:
        n = len(left)
        m = len(right)
        res = 0
        for i in range(min(n,m)):
            res = compare(left[i],right[i])
            if res:
                break
        if res == 0:
            if n < m:
                return -1
            elif n > m:
                return 1
            else: 
                return 0
    elif type(left) == int:
        res = compare([left],right)
    else:
        res = compare(left,[right])
    return res
 
def part1(data):
    """Solve part 1."""
    idx = 1
    correct = []
    for d in data:
        left = eval(d[0])
        right = eval(d[1])
        if compare(left,right) == -1:
            correct.append(idx)

        idx += 1

    total = 0
    for cor in correct:
        total += cor
    print(total,correct)

    return total
    

def part2(data):
    """Solve part 2."""
    div_left = '[[2]]'
    div_right = '[[6]]'
    unsorted = []
    for d in data:
        unsorted.append(eval(d[0]))
        unsorted.append(eval(d[1]))

    unsorted.append(eval(div_left))
    unsorted.append(eval(div_right))

    ordered = []

    i = 0
    lowest = unsorted[0]
    while len(unsorted) > 0:
        cmp = compare(unsorted[i],lowest)
        if cmp <= 0:
            lowest = unsorted[i]
        i += 1
        if i == len(unsorted):
            ordered.append(lowest)
            unsorted.remove(lowest)
            if unsorted:
                lowest = unsorted[0]
            i = 0
    print(ordered)

    n = ordered.index(eval(div_left)) + 1
    m = ordered.index(eval(div_right)) + 1

    return n*m


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

