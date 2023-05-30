# aoc_template.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input. """
    grid = []
    for line in puzzle_input.split():
        row = []
        i = 0
        while i < len(line):
            row.append(int(line[i]))
            i += 1
        grid.append(row)
    return grid 

def reverse_range(start,end):
    lst = []
    for i in range(start,end):
        lst.append(i)
    revlst = list(reversed(lst))
    return revlst

def checkVisible(a,x,y):

    rows = a.shape[0]
    cols = a.shape[1]
    height = a[x,y]

    leftrev = reverse_range(0,x)
    rghtrev = reverse_range(0,y)
    
    visible = False

    if x == 1:
        visible = a[0,y] < height
    for i in leftrev:
        if a[i,y] < height:
            visible = True
        else:
            visible = False
            break

    if visible:
        return visible

    if x == rows -2 :
        visible = a[rows-1,y] < height
    for i in range(x+1,rows,1):
        if a[i,y] < height:
            visible = True
        else:
            visible = False
            break

    if visible:
        return visible
           
            
    if y == 1:
        visible = a[x,0] < height
    for i in rghtrev:
        if a[x,i] < height:
            visible = True
        else:
            visible = False
            break

    if visible:
        return visible

    if y == cols-2:
        visible = a[x,cols-1] < height
    for i in range(y+1,cols,1):
        if a[x,i] < height:
            visible = True
        else:
            visible = False
            break

    if visible:
        return visible

    return False 

def part1(data):
    """Solve part 1."""
    #size input is 99x99
    arr = np.array(data)
    rows = arr.shape[0]
    cols = arr.shape[1]
    #outer trees are always visible
    number_of_trees = rows*2+cols*2 - 4
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            visible = checkVisible(arr,x,y)
            if visible:
                number_of_trees += 1
    return number_of_trees
    
def calc_scenicscore(lst):
    score = 1
    for l in lst:
        score *= l
    return score
    
def countTrees(a,x,y):
    lst = []
    rows = a.shape[0]
    cols = a.shape[1]
    height = a[x,y]

    leftrev = reverse_range(0,x)
    rghtrev = reverse_range(0,y)

    printit = False
    if x == 2 and y == 1:
        printit = True
    count = 0

    for i in leftrev:
        count += 1
        if a[i,y] >= height:
            break
    lst.append(count)

    count = 0
    for i in range(x+1,rows,1):
        count += 1
        if a[i,y] >= height:
            break
    lst.append(count)

    count = 0
    for i in range(y+1,cols,1):
        count += 1
        if a[x,i] >= height:
            break
    lst.append(count)

    count = 0
    for i in rghtrev:
        count += 1
        if a[x,i] >= height:
            break
    lst.append(count)
        
    return lst

def part2(data):
    """Solve part 2."""
    arr = np.array(data)
    rows = arr.shape[0]
    cols = arr.shape[1]
    treescores = []
    

    for x in range(1,rows-1):
        for y in range(1, cols-1):
            lst = countTrees(arr,x,y)
            print(x,y,arr[x,y],lst)
            treescores.append(calc_scenicscore(lst))


    if len(treescores)>0:
        return max(treescores)
    return 0

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

