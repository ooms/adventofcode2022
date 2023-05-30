# aoc_template.py

import pathlib
import sys

WIDTH = 40
HEIGHT = 6

def parse(puzzle_input):
    """Parse input. """
    lst = []
    for line in puzzle_input.split("\n"):
        lst.append(line)
    return lst

def part1(data):
    """Solve part 1."""
    total = 0
    count = 0
    x = 1
    cycles = [20,60,100,140,180,220]
    for d in data:
        if d == 'noop':
            count += 1
            if count in cycles:
                total += count*x
        else:
            cmd,num = d.split(" ")
            count += 1
            if count in cycles:
                total += count*x
            count += 1
            if count in cycles:
                total += count*x
            x += int(num)

    return total
   
def initRow():
    ch = ''
    i = 0
    while i < WIDTH:
        ch += '.'
        i += 1
    return ch

def initScreen():
    crt = []
    i = 0
    while i < HEIGHT:
        crt.append(initRow())
        i += 1

    return crt 

def printCRT(scr):
    for s in scr:
        print(s)

def moveSprite(scr,pos):
    posLst = list(initRow())
    #print("DEBUG: len(postLst),len(sprtLst),pos", len(posLst),pos)
    spr = '#'
    posLst[pos]   = spr
    if pos > 0:
        posLst[pos-1] = spr

    if pos < WIDTH-1:
        posLst[pos+1] = spr
    
    return "".join(posLst)

def drawPixel(scr,sprite,cycle):
    posLst = list("".join(scr))
    sprtLst = list("".join(sprite))
    if cycle < WIDTH*HEIGHT: 
        if sprtLst[cycle%WIDTH] == '#':
            posLst[cycle] = '#'
        else:
            posLst[cycle] = '.'

    return "".join(posLst)

def part2(data):
    """Solve part 2."""
    screen = initScreen()
    spritePos = initRow()
    #printCRT(screen)
    x = 1
    count = 0
    spritePos = moveSprite(spritePos,x)
    screen = drawPixel(screen,spritePos,count)
    for d in data:
        if d == 'noop':
            count += 1
            screen = drawPixel(screen,spritePos,count)
        else:
            cmd,num = d.split(" ")
            count += 1
            #part 1 cmd
            screen = drawPixel(screen,spritePos,count)
            count += 1
            #part 2 cmd
            x += int(num)
            spritePos = moveSprite(spritePos,x)
            screen = drawPixel(screen,spritePos,count)

    lst = []
    h = 0
    while h < HEIGHT:
        lst.append(screen[h*WIDTH:(h+1)*WIDTH])
        h += 1
    printCRT(lst)
    return screen


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

