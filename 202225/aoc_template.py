# aoc_template.py

import pathlib
import sys
from itertools import cycle

def parse(puzzle_input):
    """Parse input. """
    return [line for line in puzzle_input.split()]

SN_dict = {'2': 2, '1': 1, '0': 0, '-': -1,'=': -2}
def strconv(inp):
    val = inp 
    return val - 5

def convert(inp):
    if inp == 0:
        return '0'
    elif inp == 1:
        return '1'
    elif inp == 2: 
        return '2'
    elif inp == -1:
        return '-'
    elif inp == -2:
        return '='
    return ''

def reVal(inp,indx):
    retLst = []
    for i in range(indx):
        retLst.append(0)
    if inp < 3:
        retLst.append(inp)
        return retLst
    if inp == 3:
        retLst.append(-2)
        retLst.append(1)
        return retLst
    elif inp == 4:
        retLst.append(-1)
        retLst.append(1)
        return retLst
    elif inp == 5:
        retLst.append(0)
        retLst.append(1)
        return retLst
    else:
        return reVal(inp%5)

def addAll(lst):
    new_lst = lst[0]
    for i in range(len(lst)):
        if i > 0:
            if len(lst[i]) <= len(new_lst):
                for j in range(len(lst[i])):
                        new_lst[j] = new_lst[j] + lst[i][j]
#            new_lst = [x + y for x,y in  zip(cycle(lst[i]),new_lst)]
    return new_lst
    
def decimaltoSNAFU(inp,snafu):
    snaf_val =[]
    index = 0

    while (inp > 0):
        snaf_val.append(reVal(inp%5,index))
        inp = inp // 5
        index += 1


    snaf_val = snaf_val[::-1]

    new_lst = addAll(snaf_val)    



    return snaf_val 

def SNAFUtoDecimal(inp):
    dec_value = 0

    # Initialize base
    # value to 1 => 5^0
    base = 1
    temp = inp
    
    while(temp):
        val = SN_dict[temp[-1]]
        temp = temp[:len(temp)-1]

        dec_value += val * base
        base = base * 5

    return dec_value

def part1(data):
    """Solve part 1."""
    total = 0
    for d in data:
        total += SNAFUtoDecimal(d)

    result = decimaltoSNAFU(total,'')[0]
    
    index = 0
    res = [] 
    for i in result:
        if int(i) > 2:
            res.append(reVal(i,index))
            result[result.index(i)] = 0
        index += 1

    res.append(result)
    res = res[::-1]
    output = addAll(res)

    output = output[::-1]

    out = []
    for c in output:
        out.append(convert(c))

    return ''.join(out)
    
def part2(data):
    """Solve part 2."""

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

