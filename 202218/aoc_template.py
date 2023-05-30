# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    return [tuple(map(int,line.split(','))) for line in puzzle_input.split()]

def rest_list(data,elem):
    x = data[:]
    x.remove(elem)
    return x

def getMinMax(data):
    xMin,yMin,zMin = 1e7,1e7,1e7
    xMax,yMax,zMax = 0,0,0
    for d in data:
        if d[0] > xMax:
            xMax = d[0]
        if d[1] > yMax:
            yMax = d[1]
        if d[2] > zMax:
            zMax = d[2]
        if d[0] < xMin:
            xMin = d[0]
        if d[1] < yMin:
            yMin = d[1]
        if d[2] < zMin:
            zMin = d[2]
    return max(0,xMin),max(0,yMin),max(0,zMin),xMax,yMax,zMax

def part1(data):
    """Solve part 1."""
    #first find limits of x,y,z
    xMin,yMin,zMin,xMax,yMax,zMax = getMinMax(data)

    #how many faces do we have in total?  (example = 78)
    max_faces = len(data)*6

    #now we loop over the list for each coordinate to see if it has adjacent cubes
    count = 0
    for d in data:
        x = d[0]
        y = d[1]
        z = d[2]
        compareList = rest_list(data,d)
        if x-1 >= xMin:
            if ((x-1,y,z) in compareList):
                count += 1
        if x+1 <= xMax:
            if ((x+1,y,z) in compareList):
                count += 1
        if y-1 >= yMin:
            if ((x,y-1,z) in compareList):
                count += 1
        if y+1 <= yMax:
            if ((x,y+1,z) in compareList):
                count += 1
        if z-1 >= zMin:
            if ((x,y,z-1) in compareList):
                count += 1
        if z+1 <= zMax:
            if ((x,y,z+1) in compareList):
                count += 1
        

    return max_faces - count

def is_connected(p_a,p_b):
    diff = [abs(x_a - x_b) for x_a,x_b in zip(p_a,p_b)]
    return sum(diff) == 1

def count_connection(data):
    connections = 0
    for i, d in enumerate(data):
        for other in data[i+1:]:
            if is_connected(d, other):
                connections += 2

    return connections
    
def neighbors(c):
    return ((c[0] + 1, c[1], c[2]),
            (c[0] - 1, c[1], c[2]),
            (c[0], c[1] + 1, c[2]),
            (c[0], c[1] - 1, c[2]),
            (c[0], c[1], c[2] + 1),
            (c[0], c[1], c[2] - 1))

def visit(start,marked,data):
    stack = [start]
    xMin,yMin,zMin,xMax,yMax,zMax = getMinMax(data)
    while len(stack) >0:
        c = stack.pop()
        invalid = False
        if c[0] < 0 or c[0] > xMax or c[1] < 0 or c[1] > yMax or c[2] < 0 or c[2] > zMax:
            invalid = True
        if invalid or c in data or c in marked:
            continue
        marked.add(c)
        stack.extend(neighbors(c))
            
    
def part2(data):
    """Solve part 2."""
    #first find limits of x,y,z
    xMin,yMin,zMin,xMax,yMax,zMax = getMinMax(data)
    #how many faces do we have in total?  (example = 78)
    max_faces = len(data)*6
    print("Min ",xMin,yMin,zMin)
    print("Max ",xMax,yMax,zMax)

    marked = set()
    visit((0,0,0), marked, data)
    result = []
    for z in range(zMax+1):
        for y in range(yMax+1):
            for x in range(xMax+1):
                p = (x,y,z)
                if p in marked or p in data:
                    continue
                result.append(p)

    print("Result = ",result)


    return 6*len(result) - count_connection(result)


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

