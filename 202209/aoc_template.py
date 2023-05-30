# aoc_template.py

import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input. """
    lst = []
    for line in puzzle_input.split("\n"):
        com,steps = line.split(" ")
        lst.append([com,int(steps)])
    return lst

def sameRow(head,tail):
    (xh,yh) = head
    (xt,yt) = tail

    return (yh == yt)

def sameCol(head,tail):
    (xh,yh) = head
    (xt,yt) = tail

    return (xh == xt)

def touching(head,tail):
    (xh,yh) = head
    (xt,yt) = tail

    candidates = [(xh,yh),(xh-1,yh),(xh+1,yh),(xh,yh-1),(xh,yh+1),(xh+1,yh+1),(xh-1,yh+1),(xh-1,yh-1),(xh+1,yh-1)]
    return tail in candidates

def sameRowOrCol(head,tail):
    (xh,yh) = head
    (xt,yt) = tail

    return sameRow(head,tail) or sameCol(head,tail)

def isDiagonal(head,tail):
    (xh,yh) = head
    (xt,yt) = tail

    candidates = [(xh+1,yh+1),(xh-1,yh+1),(xh-1,yh-1),(xh+1,yh-1)]
    return tail in candidates


def move(pos,direction):
    (x,y) = pos
    new_pos = (0,0)
    if direction == 'R':
        new_pos = (x+1,y)
    elif direction == 'L':
        new_pos = (x-1,y)
    elif direction == 'U':
        new_pos = (x,y+1)
    elif direction == 'D':
        new_pos = (x,y-1)

    return new_pos

def follow(prev_head,head,tail):
    ret = prev_head 
    (xh,yh) = head
    (xt,yt) = tail

    if sameRow(head,tail):
        if xh - xt > 1:
            ret = move(tail,'R')
        elif xh - xt < -1:
            ret = move(tail,'L')
    elif sameCol(head,tail):
        if yh - yt > 1:
            ret = move(tail,'U')
        elif yh - yt < -1:
            ret = move(tail,'D')
    else:
        if yh - yt > 0:
            tail = move(tail,'U')
        else:
            tail = move(tail,'D')
        if xh- xt > 0:
            ret = move(tail,'R')
        else:
            ret = move(tail,'L')


    return ret

def part1(data):
    """Solve part 1."""
    head = (0,0)
    tail = (0,0)
    tails = [tail]
    heads = [head]
    
    for cmd,steps in data:
        lst = []
        s = 0
        while s < steps:
            head = move(head,cmd)
            if not touching(head,tail):
                tail = follow(heads[-1],head,tail)

            if tail not in lst:
                lst.append(tail)
            heads.append(head)
            s += 1

            
        for l in lst:
            if l not in tails:
                tails.append(l)
    return len(tails)
    

def part2(data):
    """Solve part 2."""
    head = (0,0)
    tail = (0,0)
    tails = []
    ret_lst = []
    for i in range(9):
        tails.append(tail)
    heads = [head]
    
    for cmd,steps in data:
        lst = []
        s = 0
        while s < steps:
            prev = heads[-1]
            head = move(head,cmd)
            leader = head
            for i in range(9):
                if not touching(leader,tails[i]):
                    tails[i] = follow(prev,leader,tails[i])
                leader = tails[i]
                if i > 0:
                    prev = tails[i-1]

            if tails[8] not in lst:
                lst.append(tails[8])
            heads.append(head)
            s += 1

            
        for l in lst:
            if l not in ret_lst:
                ret_lst.append(l)
    return len(ret_lst)
    

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

