# aoc_template.py

import pathlib
import sys
import numpy as np
from collections import deque as queue

def splitline(line):
    return [c for c in line]

def parse(puzzle_input):
    """Parse input. """
    return [splitline(line) for line in puzzle_input.split()]

LEFT = '<'
RIGHT = '>'
UP = '^'
DOWN = 'v'

START = (0,1)
dRow = [-1,0,1,0]
dCol = [0,1,0,-1]

def canMove(vis,pos,right,left,up,down,rows,cols):
    (x,y) = pos
    #cell out of bounds
    if (x < 1 or y < 1 or x > rows - 2 or y > cols - 2):
        return False

    #cell is coincides with the blizard
    if pos in left or pos in right or pos in up or pos in down:
        return False

    #otherwise
    return True


def addCoord(lst,direction,rows,cols):
    new_lst = []
    if direction == 'right':
        for x,y in lst:
            if y >= cols-2:
                new_lst.append((x,1))
            else:
                new_lst.append((x,y+1))
    if direction == 'left':
        for x,y in lst:
            if y <= 1:
                new_lst.append((x,cols-2))
            else:
                new_lst.append((x,y-1))
    if direction == 'up':
        for x,y in lst:
            if x <= 1:
                new_lst.append((rows-2,y))
            else:
                new_lst.append((x-1,y))
    if direction == 'down':
        for x,y in lst:
            if x >= rows-2:
                new_lst.append((1,y))
            else:
                new_lst.append((x+1,y))
    return new_lst

def moveBlizards(right,left,up,down,rows,cols):
    lst_r = addCoord(right[:],'right',rows,cols)
    lst_l = addCoord(left[:],'left',rows,cols)
    lst_u = addCoord(up[:],'up',rows,cols)
    lst_d = addCoord(down[:],'down',rows,cols)

    return lst_r,lst_l,lst_u,lst_d

def moveE(pos,right,left,up,down,rows,cols):
    new_pos = pos
    (x,y) = new_pos
    if x > 0 and x < rows - 1 and y < cols-2:
        new_pos = (x,y+1)
        if not new_pos in right and not new_pos in left and not new_pos in down and not new_pos in up:
            return new_pos
    if y > 0 and y < cols - 1 and x < rows-2:
        new_pos = (x+1,y)
        if not new_pos in right and not new_pos in left and not new_pos in down and not new_pos in up:
            return new_pos
    if y > 0 and y < cols - 1 and x > 1:
        new_pos = (x-1,y)
        if not new_pos in right and not new_pos in left and not new_pos in down and not new_pos in up:
            return new_pos
    if x > 0 and x < rows -1  and y > 1:
        new_pos = (x,y-1)
        if not new_pos in right and not new_pos in left and not new_pos in down and not new_pos in up:
            return new_pos
    return new_pos

moves = [[-1,0],[1,0],[0,-1],[0,1]]

def shortest_dist(grid):
    R = len(grid)
    C = len(grid[0])
    END = (C-2,R-1)

    bl_right = []
    bl_left = []
    bl_up = []
    bl_down = []
    for i in range(1,R-1):
        for j in range(1,C-1):
            if grid[i,j] == RIGHT:
                bl_right.append((i,j))
            elif grid[i,j] == LEFT:
                bl_left.append((i,j))
            elif grid[i,j] == UP:
                bl_up.append((i,j))
            elif grid[i,j] == DOWN:
                bl_down.append((i,j))

    vis = [[False] * R for i in range(C)]
    dist = [[0] * R for i in range(C)]

    q = queue()
    q.append(START)
    vis[START[0]][START[1]] = True
    dist[START[0]][START[1]] = 0 

    while len(q):
        x,y = q.popleft()
        for dx,dy in moves:
            new_x = x + dx
            new_y = y + dy
            bl_right_tmp, bl_left_tmp, bl_up_tmp, bl_down_tmp = moveBlizards(bl_right,bl_left,bl_up, bl_down,R,C)
            available = canMove(vis,(new_x,new_y),bl_right_tmp,bl_left_tmp,bl_up_tmp,bl_down_tmp,R,C)
            #if new_x > 0 and new_x < R - 1 and new_y > 0 and new_y < C - 1 and not vis[new_x][new_y] and grid[new_x][new_y] == '.':
            if new_x > 0 and new_x < R - 1 and new_y > 0 and new_y < C - 1 and not vis[new_x][new_y] and available:
                q.append((new_x,new_y))
                vis[new_x][new_y] = True
                dist[new_x][new_y] = dist[x][y] + 1
            bl_right, bl_left, bl_up, bl_down = moveBlizards(bl_right,bl_left,bl_up, bl_down,R,C)
    if not vis[END[0]][END[1]]:
        print(-1)
    else:
        print(dist[END[0]][END[1]])

def part1(data):
    arr = np.array(data)
    shortest_dist(arr)

def effe_part1(data):
    """Solve part 1."""
    arr = np.array(data) 
    bl_right = []
    bl_left = []
    bl_up = []
    bl_down = []
    rows,cols = arr.shape
    END = (rows-2,cols-2)
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if arr[i,j] == RIGHT:
                bl_right.append((i,j))
            elif arr[i,j] == LEFT:
                bl_left.append((i,j))
            elif arr[i,j] == UP:
                bl_up.append((i,j))
            elif arr[i,j] == DOWN:
                bl_down.append((i,j))

    pos = START
    print('Minute ',0,pos,bl_right,bl_left,bl_up,bl_down)
    minute = 1
    doPrint = False

    #declare the visited array
    vis = [[False for i in range(cols)] for i in range(rows)]
    # stores indices of the matrix cells
    q = queue()

    # mark the starting cell as visited
    # and push it to the queue
    q.append(START)
    vis[START[0]][START[1]] = True

    while len(q) > 0:
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print("Minute ", minute, x,y)

        bl_right_tmp, bl_left_tmp, bl_up_tmp, bl_down_tmp = moveBlizards(bl_right,bl_left,bl_up, bl_down,rows,cols)
        # go to adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            new_pos = (adjx,adjy)
            if canMove(vis,new_pos,bl_right_tmp,bl_left_tmp,bl_up_tmp,bl_down_tmp,rows,cols):
            # check where to move to 
                #pos = moveE(pos,bl_right_tmp, bl_left_tmp,bl_up_tmp, bl_down_tmp,rows,cols)
                q.append(new_pos)
                vis[adjx][adjy] = True
        bl_right, bl_left, bl_up, bl_down = moveBlizards(bl_right,bl_left,bl_up, bl_down,rows,cols)
        #if doPrint: print('Minute ',minute,pos,bl_right,bl_left,bl_up,bl_down)
        minute += 1
        if new_pos == END:
            break
    print(vis)

    return minute 
    

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

