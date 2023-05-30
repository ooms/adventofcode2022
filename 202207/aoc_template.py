# aoc_template.py

import pathlib
import sys
import re

def getPrevDir(current):
    newdir = current
    x = re.split(r"_",current)
    if len(x)> 0:
        newdir = x[0]
        i = 1
        while i < len(x)-1:
            newdir = newdir + '_' + x[i]
            i += 1
    return newdir

def parse(puzzle_input):
    """Parse input. """
    d = {}
    prev_dir = 'root'
    skip = False
    cur_dir = ''
    for line in puzzle_input.split("\n"):
        if skip:
            skip = False
        elif line == '$ cd /': # root
            cur_dir = prev_dir
            d[cur_dir] = []
            skip = True
        elif line == '$ cd ..':
            cur_dir = getPrevDir(cur_dir)
            prev_dir = cur_dir
        elif line[:4] == '$ cd':
            cur_dir = prev_dir + '_' + line[5:]
            prev_dir = cur_dir
            d[cur_dir] = []
            skip = True
        elif line[:3] == 'dir':
            dirline = prev_dir + '_' + line[4:]
            d[cur_dir].append(dirline)
        else:
            lst = re.findall('\\d+',line)
            if len(lst) > 0:
                d[cur_dir].append(int(lst[0]))

    return d

def getSizeOfDir(data,elem):
    size = 0
    if isinstance(elem,int):
        return elem 

    for item in data[elem]:
        try:
            if isinstance(item,int):
                size += item
            else:
                size += getSizeOfDir(data,item)
        except ValueError:
            continue
    return size

def getSizeOfDirs(data):
    dir_list = []
    for d in data:
        dir_sum = 0
        for item in data[d]:
            dir_sum += getSizeOfDir(data,item)
        dir_list.append(dir_sum)
    return dir_list

def part1(data):
    """Solve part 1."""
    lst = getSizeOfDirs(data)
    total_sum = 0
    for l in lst:
        if l <= 100000:
            total_sum += l

    return total_sum
    

def part2(data):
    """Solve part 2."""
    lst = getSizeOfDirs(data)
    unused = 70000000 - lst[0]
    needed = 30000000 - unused
    tmp = []
    for l in lst:
        if l > needed:
            tmp.append(l)
    print(tmp)
    return min(tmp)

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

