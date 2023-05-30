# aoc_template.py

import pathlib
import sys
import numpy as np

def splitline(line):
    return [c for c in line]

def parse(puzzle_input):
    """Parse input. """
    return [splitline(line) for line in puzzle_input.split()]

ELF = '#'
DIRS = ['N','S','W','E']

N = (-1, 0)
S = ( 1, 0)
W = ( 0,-1)
E = ( 0, 1)
NE= (-1, 1)
NW= (-1,-1)
SE= ( 1, 1)
SW= ( 1,-1)


DIRECTIONS = [N,S,W,E,NE,NW,SE,SW]

SCANS = {'N': [N,NE,NW],
         'S': [S,SE,SW],
         'W': [W,NW,SW],
         'E': [E,NE,SE]}

def get_surroundings(ar,i,j):
    if ((i>0) & (i<ar.shape[0])) & ((j>0) & (j<ar.shape[1])):
        temp = np.array([[ar[i-1][j-1],ar[i-1][j],ar[i-1][j+1]],[ar[i][j-1],ar[i][j],ar[i][j+1]],[ar[i+1][j-1],ar[i+1][j],ar[i+1][j-1]]])
    return temp

def get_surroundingsNorth(ar,i,j):
    if ((i>0) & (i<ar.shape[0])) & ((j>0) & (j<ar.shape[1])):
        temp = np.array([[ar[i-1][j-1],ar[i-1][j],ar[i-1][j+1]])
    return temp

def get_surroundingsSouth(ar,i,j):
    if ((i>0) & (i<ar.shape[0])) & ((j>0) & (j<ar.shape[1])):
        temp = np.array([[ar[i+1][j-1],ar[i+1][j],ar[i+1][j+1]])
    return temp

def get_surroundingsWest(ar,i,j):
    if ((i>0) & (i<ar.shape[0])) & ((j>0) & (j<ar.shape[1])):
        temp = np.array([ar[i][j-1],ar[i-1][j-1],ar[i+1][j-1]])
    return temp

def get_surroundingsEast(ar,i,j):
    if ((i>0) & (i<ar.shape[0])) & ((j>0) & (j<ar.shape[1])):
        temp = np.array([ar[i][j+1],ar[i-1][j+1],ar[i+1][j+1]])
    return temp

def no_elves(lf,ar):
    (x,y) = lf
    for n in get_surroundings(ar,x,y):
        if n[0] == x and n[1] == y: 
            continue
        if ar[n[0],n[1]] == ELF:
            return False
    return True

def check_moves(lf,ar,scan):
    (x,y) = lf
    found = False
    for s in scan:
        if s == 'N':
            for n in get_surroundingsNorth(ar,x,y):
                if ar[n[0],n[1]] == ELF:
                    found = True
                    continue
        

                    

    return lf

def part1(data):
    """Solve part 1."""
    arr = np.array(data)    
    rows,cols = arr.shape
    #display = np.full((rows+1,cols+1),'.',dtype='U1')
    #print(display)
    # put a border around the original array with np.pad 

    elves = set()
    for i in range(rows):
        for j in range(cols):
            if arr[i,j] == ELF:
                elves.add((i,j))

    potential_moves = set()
    scan_start = 0
    round_count = 0
    dirs = DIRS
    while round_count <= 1:
        for elf in elves:
            if not no_elves(elf,arr):
                new_elf = check_moves(elf,arr,dirs)
                if new_elf != elf:
                    potential_moves.add(new_elf)

        #first elem goes to end of dirs list
        elem = dirs.pop(0)
        dirs.append(elem)
        print(dirs)
        round_count += 1

    print(potential_moves)





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

