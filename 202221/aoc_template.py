# aoc_template.py

import pathlib
import sys
import re
import operator

def parse(puzzle_input):
    """Parse input. """
    d = {}
    for line in puzzle_input.split("\n"):
        monkey,cmds = line.split(':')
        lst = re.findall('\\d+',cmds)
        if len(lst) > 0:
            d[monkey] = float(lst[0])
        else:
            lst = []
            for c in cmds.strip().split(' '):
                if not c == ' ':
                    lst.append(c)
            d[monkey] = lst
    return d

OPERATORS = { '+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.truediv,
              '=': operator.eq}


def eval_operation(left,right,operator):  
    op1, op2 =  float(left),float(right)
    return OPERATORS[operator](op1,op2)

def getValue(data,key,part2,hu):
    if part2 and key == 'humn':
        return hu
    if isinstance(data[key],float):
        return data[key]
    ops = []
    oper = '' 
    for item in data[key]:
        if item in OPERATORS:
            oper = item
        else:
            ops.append(getValue(data,item,part2,hu))
        if len(ops) == 2:
            if part2 and key == 'root': # for part 2
                oper = '=' #number to reach is 90565407195785
                print(ops[1],ops[0],hu)
            return eval_operation(ops[0],ops[1],oper)
    return 0

def part1(data):
    """Solve part 1."""
    return getValue(data,'root',False,0)
        
    

def part2(data):
    """Solve part 2."""
    #starting point example
    hmnu = 310
    #starting point input
    #hmnu =  3219579455941
    found = False
    while not found:
        hmnu -= 1
        found = getValue(data,'root',True,hmnu)
    return hmnu

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

