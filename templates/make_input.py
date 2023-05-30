# make_input.py

import pathlib
import sys
from aocd.models import Puzzle

def write_input(puzzle_input):
    """Write input file"""
    f = open("input.txt","x")
    for i in puzzle_input:
        f.write(i)
    f.close()



if __name__ == "__main__":
    fyear = int(sys.argv[1])
    fday = int(sys.argv[2])
    print(fyear,fday)
    puzzle_input = Puzzle(year=fyear, day=fday)
    write_input(puzzle_input.input_data)

