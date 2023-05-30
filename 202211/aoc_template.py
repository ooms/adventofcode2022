# aoc_template.py

import pathlib
import sys
import re
import math

class Monkey:
    def __init__(self,items,operation,test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def getMonkey(self):
        monkey = {}
        monkey['items'] = self.items
        monkey['operation'] = self.operation
        monkey['test'] = self.test
        monkey['inspected'] = 0
        return monkey

    def getItems(self):
        return self['items']

    def getInspected(self):
        return self['inpsected']
        
def str_to_int(lst):
    ret_lst = []
    for l in lst:
        ret_lst.append(int(l))
    return ret_lst

def parse(puzzle_input):
    """Parse input. """
    monkeys = {}
    items_row = 1
    operation_row = 2
    test_row1 = 3
    test_row2 = 4
    test_row3 = 5
    row_count = 0
    monkey_count = 0
    readingMonkey = False
    line = puzzle_input.split("\n")
    while row_count < len(line): 
        startMonkey = re.search(r"Monkey\s*",line[row_count])
        if startMonkey:
            readingMonkey = True            
        elif readingMonkey:
            if row_count%7 == items_row:
                items = str_to_int(re.findall(r"(\d+)",line[row_count]))
            elif row_count%7 == operation_row:
                operation = ((line[row_count]).split("=")[1]).strip()
            elif row_count%7 == test_row1:
                test = []
                test.append(int(re.findall(r"(\d+)",line[row_count])[0]))
            elif row_count%7 == test_row2:
                test.append(int(re.findall(r"(\d+)",line[row_count])[0]))
            elif row_count%7 == test_row3:
                test.append(int(re.findall(r"(\d+)",line[row_count])[0]))
                monk = Monkey(items,operation,test)
                monkeys[monkey_count] = monk.getMonkey()
                monkey_count += 1
            else:
                readingMonkey == False
        row_count += 1
    return monkeys

def doOperation(inp,cmd):
    old,op,val = cmd.split(" ")
    if op == '+':
        return inp + int(val)
    elif val.isdigit():
        return inp*int(val)
    else:
        return inp*inp

def doTest(inp,lst):
    tst = lst[0]
    if inp%tst == 0:
        return float(lst[1])
    else: 
        return float(lst[2])
    
def getMonkeyBusiness(data):
    inspectedlst = []
    for monkey in data:
        inspectedlst.append(data[monkey]['inspected'])
    inspectedlst.sort(reverse=True)
    return inspectedlst[0]*inspectedlst[1]

def part1(data):
    """Solve part 1."""
    total_rounds = 20
    rnd = 0
    while rnd < total_rounds:
        for monkey in data:
            items = data[monkey]['items']
            #add length of items to inspected of new monkey
            data[monkey]['inspected'] += len(items)
            #clear out the items for this monkey
            data[monkey]['items'] = []
            for itm in items:
                #evaluation the operation
                worry = doOperation(itm,data[monkey]['operation'])
                #divide result by 3 and round
                worry = worry//3
                #evaluate test and assign to new monkey
                monkey_idx = doTest(worry,data[monkey]['test'])
                data[monkey_idx]['items'].append(worry)

        rnd += 1

    print("part1 round: ",rnd,data)
    return getMonkeyBusiness(data)

def getModForAll(data):
    total = 1
    for monkey in data:
        tests = data[monkey]['test']
        total = total*tests[0]


    return total


def part2(data):
    """Solve part 2."""
    total_rounds = 10000
    rnd = 0
    mod_total = getModForAll(data)

    while rnd < total_rounds:
        for monkey in data:
            items = data[monkey]['items']
            #add length of items to inspected of new monkey
            data[monkey]['inspected'] += len(items)
            #clear out the items for this monkey
            data[monkey]['items'] = []
            for itm in items:
                #evaluation the operation
                worry = doOperation(itm,data[monkey]['operation'])
                #evaluate test
                monkey_idx = doTest(worry,data[monkey]['test'])

                #making the numbers smaller by doing a mod of all total tests 
                worry = worry%mod_total
                #assign to new monkey
                data[monkey_idx]['items'].append(worry)

        rnd += 1

    print("part2 round ", rnd, data)

    return getMonkeyBusiness(data)
    

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

