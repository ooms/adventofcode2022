# aoc_template.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input. """
    lst = []
    for line in puzzle_input.split("\n"):
        subLst = []
        for coord in line.split(" -> "):
            x,y = coord.split(",")
            subLst.append((int(x),int(y)))
        lst.append(subLst)

    return lst

def setRocks(start,end,gr):
    new_grid = np.copy(gr)
    if start[0] == end[0]:
        if start[1] > end[1]:
            for y in range(end[1],start[1]):
                new_grid[(start[0]),y] = '#'
        else:
            for y in range(start[1],end[1]):
                new_grid[(start[0]),y] = '#'

    else:
        if start[0] > end[0]:
            for x in range(end[0],start[0]):
                new_grid[(x,start[1])] = '#'
        else:
            for x in range(start[0],end[0]):
                new_grid[(x,start[1])] = '#'
    
    return new_grid

def keepFalling(pos,gr):
    (x,y) = pos
    below = gr[(x-1,y)] == '#' or gr[(x-1,y)] == 'o' 
    left_below = gr[(x-1,y-1)] == '#' or gr[(x-1,y-1)] == 'o' 
    right_below = gr[(x-1,y+1)] == '#' or gr[(x-1,y+1)] == 'o' 
    return not below and not left_below and not right_below

def drawSand(start,gr):
    new_grid = np.copy(gr)
    shapeX = np.shape(new_grid)[0]
    shapeY = np.shape(new_grid)[1]
    done = False
    found = False

    for r in range(0,shapeY):
        #if not keepFalling((r,start[1]),new_grid):
        if True:
            if new_grid[r,start[1]] == '#':
                new_grid[r-1,start[1]] = 'o'
                found = True
                break
            elif new_grid[r,start[1]] == 'o':
                if new_grid[r,start[1]-1] == '.':
                    new_grid[r,start[1]-1] = 'o'
                    found = True
                    break
                elif new_grid[r,start[1]+1] == '.':
                    new_grid[r,start[1]+1] = 'o'
                    found = True
                    break
                elif new_grid[r-1,start[1]] == '.':
                    new_grid[r-1,start[1]] = 'o'
                    found = True
                    break


    done = not found 

    return new_grid,done

def part1(data):
    """Solve part 1."""
    # get dimensions of grid: max x, max y
    # create a grid with dimension and set everything to .
    # put the rocks in as # according to the input
    # start flowing the sand at (500,0) until sand drops below max y 
    xMin, xMax = 1e7,0
    yMin, yMax = 1e7,0
    for d in data:
        print("The list is: " + str(d))
        res1 = list(map(max,zip(*d)))
        res2 = list(map(min,zip(*d)))
        if xMin > res2[0]:
            xMin = res2[0]
        if xMax < res1[0]:
            xMax = res1[0]
        if yMin > res2[1]:
            yMin = res2[1]
        if yMax < res1[1]:
            yMax = res1[1]

        print(xMin,xMax,yMin,yMax)
        rows = yMax+1 # [0:yMax]
        cols = xMax - xMin + 1 # [xMin:xMax] don't forget the offset, which is to add xMin to a column

    sandStart = (0,500-xMin)
    g_shape = (rows,cols)
    fill_value = '.'
    grid = np.full(g_shape,fill_value)
    for d in data:
        print(d)
        start = (d[0][1],d[0][0]-xMin)
        grid[start] = '#'
        i = 1
        while i < len(d):
            nextLoc = (d[i][1],d[i][0]-xMin)
            print(nextLoc)
            grid[nextLoc] = '#'
            grid = setRocks(start,nextLoc,grid)
            start = nextLoc
            i += 1
    grid[sandStart] = '+'

    done = False
    while not done:
        grid,done = drawSand(sandStart,grid)
        print(grid)

    print(grid)
            
    

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

