# aoc_template.py

import pathlib
import sys
import re

def str_to_int(lst):
    ret = []
    for l in lst:
        ret.append(int(l))
    return ret

def parse(puzzle_input):
    """Parse input. """
    height = 0
    nr_of_stacks = 0
    # first scan dimension of the input
    for line in puzzle_input.split("\n"):
        if line.split()[0].isdigit():
            nr_of_stacks = int(line.split()[-1])       
            break;
        height += 1
    start_steps = height + 2 # this is where the instructions start
    #initialize the stacks for the dimensions from the input
    sts = []
    i = 0
    while i < nr_of_stacks:
        sts.append([])
        i += 1
    
    #now we actually start parsing the stacks
    cnt = 0
    for line in puzzle_input.split("\n"):
        i = 0
        while i < nr_of_stacks:
            index = i+1+i*3 # the index of each possible stack
            if (index < len(line)): # make sure the end of the line is not reached
                if (line[index] != " "): # if there is a letter, we put on the correct stack
                    sts[i].append(line[index])
            i += 1
        cnt += 1
        if cnt == height: # end of the stacks is reached, so we are done
            break

    #now we parse the instructions
    i = 0
    for line in puzzle_input.split("\n"):
        if i >= start_steps: 
            lst = re.findall('\\d+',line) # oh boy, regular expression to get the numbers out of the line
            sts.append(str_to_int(lst))
        i += 1

    return sts

def make_stacks(data):
    lst = []
    for d in data:
        try:
            if not isinstance(d[0],int):
                lst.append(d)
        except ValueError:
            continue
    return lst

def part1(data):
    """Solve part 1."""
    stacks1 = []
    stacks1 = make_stacks(data)
    for d in data:
        try: 
            if isinstance(d[0],int):
                amount  = d[0]
                mv_from = d[1]-1
                mv_to   = d[2]-1
                lst = stacks1[mv_from][:amount]
                del stacks1[mv_from][:amount]
                for l in lst:
                    stacks1[mv_to].insert(0,l)
        except ValueError:
            continue

    ret = ""
    for s in stacks1:
        if (len(s)>0):
            ret += s[0]
    return ret
    

def part2(data):
    """Solve part 2."""
    stks = []
    stks = make_stacks(data)
    for d in data:
        try: 
            if isinstance(d[0],int):
                amount  = d[0]
                mv_from = d[1]-1
                mv_to   = d[2]-1
                lst = stks[mv_from][:amount]
                del stks[mv_from][:amount]
                if (len(lst)>0):
                    rev = reversed(lst)
                    for l in rev:
                        stks[mv_to].insert(0,l)
                else:
                    stks[mv_to].insert(0,lst)
        except ValueError:
            continue

    ret = ""
    for s in stks:
        if len(s)>0:
            ret += s[0]
    return ret

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    #somehow I need to parse this again to get the original input
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
#        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

