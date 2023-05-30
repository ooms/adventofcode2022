#aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input. """
    return [int(line) for line in puzzle_input.split()]

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
        NewNode.prevval = laste

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node does not exist")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        
        middle_node.nextval = NewNode
        NewNode.prevval = middle_node

    def findNode(self,index):
        head = self.headval

        while (head.nextval != None):
            if ((head.nextval).dataval[0] == index):
                return head
            head = ((head).nextval)
        return None

    def swapNodes(self, index,forward):
        head = self.headval

        a = None
        b = None

        #Search for x in hhe linked list
        # and store their pointer in a
        curra = self.headval
        while(curra != None):
            if curra.dataval[0] == index:
                a = curra
                break
            curra = curra.nextval
        #while(head.nextval != None):
            #if ((head.nextval).dataval[0] == index):
            #    a = head
            #    break

            #head = ((head).nextval)

        #determine b according to forward or back
        if forward:
            b = a.nextval
        else:
            b = a.prevval
            print("a b dataval",a.dataval,b.dataval)

        #If we have found both a and b
        # in the linked list swap current
        # pointer and next pointer of these
        if (a != None and b != None):
            if forward:
                temp = a.nextval
                a.nextval = b.nextval
                b.nextval = temp
                temp2 = b.prevval
                b.prevval = a.prevval
                a.prevval = temp2
                temp = a.nextval.nextval
                a.nextval.nextval = b.nextval.nextval
                b.nextval.nextval = temp
                temp2= b.prevval.prevval
                b.prevval.prevval= a.prevval.prevval
                a.prevval.prevval= temp2
            else:
                temp = a.prevval
                a.prevval = b.prevval
                b.prevval = temp
                temp2 = a.nextval
                a.nextval = b.nextval
                b.nextval = temp2
                temp = a.prevval.prevval
                a.prevval.prevval= b.prevval.prevval
                b.prevval.prevval= temp
                temp2 = a.nextval.nextval
                a.nextval.nextval = b.nextval.nextval
                b.nextval.nextval = temp2

        return head

    def listprint(self):
        printval = self.headval
        #print(printval.dataval)
        #printval = printval.nextval
        i = 0
        #while printval is not self.headval:
        while i < 7:
            print(printval.dataval)
            printval = printval.nextval
            i += 1

    def first(self):
        printval = self.headval
        return printval

    def last(self):
        printval = self.headval
        retval = None
        while printval is not None:
            retval = printval
            printval = printval.nextval
        return retval

def getIndices(lst):
    return sorted(enumerate(lst), key=lambda i:i[0])

def doStep(steps,indx,lst):
    new_lst = lst[:]
    if steps+indx <= 0:
        new_lst.insert(len(lst)-1-(indx+steps)%len(lst),new_lst.pop(indx))
    elif steps+indx >= len(lst):
        new_lst.insert(indx-(indx+steps)%len(lst),new_lst.pop(indx))
    else:
        new_lst.insert((indx+steps)%len(lst),new_lst.pop(indx)) 
    return new_lst

def getIndex(lst,i):
    indx = 0
    for l in lst:
        if l[0] == i:
            return indx,l[1]
        indx += 1
    return indx,0

def getIndexOfZero(lst):
    indx = 0
    for l in lst:
        if l == 0:
            return indx
        indx += 1
    return indx

def part1(data):
    """Solve part 1."""
    orig_list = getIndices(data)
    zero_index = getIndexOfZero(data)
    list1 = SLinkedList()

    start = None
    rev_list = reversed(orig_list)
    #for d in rev_list:
    for d in orig_list:
        list1.AtEnd(d)

    start = list1.first()
    last = list1.last()
    last.nextval = start
    start.prevval = last

    print("before swap")
    #list1.listprint()
    

    i = 0
    doPrint = False
    while i < len(orig_list):
    #while i < 1:
        doPrint = (orig_list[i][0] == 2)
        index = orig_list[i][0]
        steps = orig_list[i][1]
        if doPrint: print("index, steps", index,steps)
        s = 0
        if doPrint: print("moves ",orig_list[i])
        while s < abs(steps):
            forward = steps >= 0
            if doPrint and s == 0: 
                print("before step: ", s,forward,index)
                list1.listprint()
            
            list1.swapNodes(index,forward)
            if doPrint and s == 0: 
                print("after step: ", s)
                list1.listprint()
            s += 1
        if doPrint and False: 
            print("end result: ")
            list1.listprint()
        i += 1

    print("after swap")
    #list1.listprint()

    print("zero index",zero_index)
    node = list1.findNode(zero_index).nextval
    print("zero node", node.dataval)
    
    one_node = list1.findNode((zero_index+1000)%len(orig_list)).nextval
    print("1000th", one_node.dataval)
    two_node = list1.findNode((zero_index+2000)%len(orig_list)).nextval
    print("2000th", two_node.dataval)
    three_node = list1.findNode((zero_index+2000)%len(orig_list)).nextval
    print("3000th", three_node.dataval)
    #new_zero_index = getIndex(new_list,zero_index)
    #print("new zero index", new_zero_index[0]+1000)
    #print("1000th",new_list[(new_zero_index[0]+1000)%len(new_list)])
    #print("2000th",new_list[(new_zero_index[0]+2000)%len(new_list)])
    #print("3000th",new_list[(new_zero_index[0]+3000)%len(new_list)])

    #one = new_list[(new_zero_index[0]+1000)%len(new_list)][1]
    #two = new_list[(new_zero_index[0]+2000)%len(new_list)][1]
    #three = new_list[(new_zero_index[0]+3000)%len(new_list)][1]
    one = 0
    two = 0
    three = 0

    return one + two + three

def _part1(data):
    """Solve part 1."""
    #new_list = data[:]
    zero_index = getIndexOfZero(data)
    new_list = getIndices(data)
    orig_list = getIndices(data)
    i = 0
    while i < len(orig_list):
        index,steps = getIndex(new_list,i)
        new_list = doStep(steps,index,new_list)
        print(i)
        i += 1
    #print(new_list)
    print("zero index",zero_index)
    new_zero_index = getIndex(new_list,zero_index)
    print("new zero index", new_zero_index[0]+1000)
    print("1000th",new_list[(new_zero_index[0]+1000)%len(new_list)])
    print("2000th",new_list[(new_zero_index[0]+2000)%len(new_list)])
    print("3000th",new_list[(new_zero_index[0]+3000)%len(new_list)])

    one = new_list[(new_zero_index[0]+1000)%len(new_list)][1]
    two = new_list[(new_zero_index[0]+2000)%len(new_list)][1]
    three = new_list[(new_zero_index[0]+3000)%len(new_list)][1]

    return one + two + three
    

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

