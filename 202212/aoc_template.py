# aoc_template.py

import pathlib
import sys
import numpy as np

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def parse(puzzle_input):
    """Parse input. """
    return [line for line in puzzle_input.split()]

def convertElevation(letter):
    if (letter == 'S' or letter == 'E'):
        return letter
    return ALPHABET.index(letter)+1

def makeArray(data):
    new_array = []
    for d in data:
        ln = [convertElevation(x) for x in d]
        new_array.append(ln)
    return new_array


def part1(data):
    """Solve part 1."""
    a = makeArray(data)
    arrtmp = np.array(a)

    rows = arrtmp.shape[0]
    cols = arrtmp.shape[1]

    startPos = np.where(arrtmp == 'S')
    endPos = np.where(arrtmp == 'E')
    
    arrtmp[startPos[0],startPos[1]] = 1
    arrtmp[endPos[0],endPos[1]] = 26
    #convert to integers
    arr = arrtmp.astype('int')

    distmap = np.ones((rows,cols),dtype=int)*np.Infinity
    distmap[startPos[0],startPos[1]] = 0
    originmap = np.ones((rows,cols),dtype=int)*np.nan
    visited = np.zeros((rows,cols),dtype=bool)
    finished = False

    #define the start position
    x,y= startPos[0],startPos[1]
    count = 0

    #Loop Dijkstra until reaching the target cell
    while not finished:
        #move to x+1,y
        if x < rows-1:
            if arr[x+1,y]<=arr[x,y]+1 and not visited[x+1,y]:
                distmap[x+1,y]=distmap[x,y] + 1
                originmap[x+1,y]=np.ravel_multi_index([x,y], (rows,cols))

        #move to x-1,y
        if x>0:
            if arr[x-1,y]<=arr[x,y]+1 and not visited[x-1,y]:
                distmap[x-1,y]=distmap[x,y] + 1
                originmap[x-1,y]=np.ravel_multi_index([x,y], (rows,cols))

        #move to x,y+1
        if y < cols-1:
            if arr[x,y+1]<=arr[x,y]+1 and not visited[x,y+1]:
                distmap[x,y+1]=distmap[x,y] + 1
                originmap[x,y+1]=np.ravel_multi_index([x,y], (rows,cols))

        #move to x,y-1
        if y>0:
            if arr[x,y-1]<=arr[x,y]+1 and not visited[x,y-1]:
                distmap[x,y-1]=distmap[x,y] + 1
                originmap[x,y-1]=np.ravel_multi_index([x,y], (rows,cols))

        visited[x,y] = True
        distmaptemp = distmap
        distmaptemp[np.where(visited)]=np.Infinity
        #now we find the shortest path so far
        minpost=np.unravel_index(np.argmin(distmaptemp),np.shape(distmaptemp))
        x,y=minpost[0],minpost[1]
        if x==endPos[0] and y==endPos[1]:
            finished = True
        count += 1


    return distmap[endPos[0],endPos[1]]

    

def part2(data):
    """Solve part 2."""
    a = makeArray(data)
    arrtmp = np.array(a)

    rows = arrtmp.shape[0]
    cols = arrtmp.shape[1]

    startPos = np.where(arrtmp == 'S')
    endPos = np.where(arrtmp == 'E')
    aPos = np.where(arrtmp == '1')
    listOfaCoord = list(zip(aPos[0],aPos[1]))
    
    arrtmp[startPos[0],startPos[1]] = 1
    arrtmp[endPos[0],endPos[1]] = 26
    #convert to integers
    arr = arrtmp.astype('int')

    listOfaCoord.append(list(zip(startPos[0],startPos[1]))[0])
    print(len(listOfaCoord))
    
    paths = []
    isPrint = False
    for x,y in listOfaCoord:
        print(x,y)
        if (x == 0 and y == 8): isPrint = True
        distmap = np.ones((rows,cols),dtype=int)*np.Infinity
        distmap[x,y] = 0
        originmap = np.ones((rows,cols),dtype=int)*np.nan
        visited = np.zeros((rows,cols),dtype=bool)
        finished = False
        count = 0
        x_prev = -1
        y_prev = -1

        #Loop Dijkstra until reaching the target cell
        while not finished:
            #move to x+1,y
            if x < rows-1:
                if arr[x+1,y]<=arr[x,y]+1 and not visited[x+1,y]:
                    distmap[x+1,y]=distmap[x,y] + 1
                    originmap[x+1,y]=np.ravel_multi_index([x,y], (rows,cols))

            #move to x-1,y
            if x>0:
                if arr[x-1,y]<=arr[x,y]+1 and not visited[x-1,y]:
                    distmap[x-1,y]=distmap[x,y] + 1
                    originmap[x-1,y]=np.ravel_multi_index([x,y], (rows,cols))

            #move to x,y+1
            if y < cols-1:
                if arr[x,y+1]<=arr[x,y]+1 and not visited[x,y+1]:
                    distmap[x,y+1]=distmap[x,y] + 1
                    originmap[x,y+1]=np.ravel_multi_index([x,y], (rows,cols))

            #move to x,y-1
            if y>0:
                if arr[x,y-1]<=arr[x,y]+1 and not visited[x,y-1]:
                    distmap[x,y-1]=distmap[x,y] + 1
                    originmap[x,y-1]=np.ravel_multi_index([x,y], (rows,cols))

            visited[x,y] = True
            distmaptemp = distmap
            distmaptemp[np.where(visited)]=np.Infinity
            #now we find the shortest path so far
            minpost=np.unravel_index(np.argmin(distmaptemp),np.shape(distmaptemp))
            x_prev = x
            y_prev = y
            x,y=minpost[0],minpost[1]
            if isPrint: print(x,y)
            if x == x_prev and y == y_prev:
                break
            if x==endPos[0] and y==endPos[1]:
                finished = True

            count += 1

        if finished == True:
            paths.append(list(distmap[endPos[0],endPos[1]]))
        print(paths)


    paths.sort()
    return paths[0][0]

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

