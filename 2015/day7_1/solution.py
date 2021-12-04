import os
from typing import List



class Node:
    def __init__(self, left, right, target, func):
        self.left = left
        self.right = right
        self.target = target
        self.func = func
        self.complete = False

    def resolve(self):
        if self.complete:
            return
        if self.func(self.left, self.right, self.target):
            self.complete = True

wires = dict()
nodes:List[Node] = []

def assign(left, _, target):
    try:
        if type(left) != int:
            left = wires[left]
        wires[target] = left
        return True
    except KeyError:
        return False

def and_gate(left,right,target):
    try:
        if type(left) != int:
            left = wires[left]
        if type(right) != int:
            right = wires[right]
        wires[target] = left & right
        return True
    except KeyError:
        return False

def or_gate(left,right,target):
    try:
        if type(left) != int:
            left = wires[left]
        if type(right) != int:
            right = wires[right]
        wires[target] = left | right
        return True
    except KeyError:
        return False

def lshift_gate(left,right,target):
    try:
        if type(left) != int:
            left = wires[left]
        if type(right) != int:
            right = wires[right]
        wires[target] = left << right
        return True
    except KeyError:
        return False

def rshift_gate(left,right,target):
    try:
        if type(left) != int:
            left = wires[left]
        if type(right) != int:
            right = wires[right]
        wires[target] = left >> right
        return True
    except KeyError:
        return False

def not_gate(_,right,target):
    try:
        if type(right) != int:
            right = wires[right]
        wires[target] = ~right
        return True
    except KeyError:
        return False

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt", "r") as in_file:
        for line in in_file:
            left = None
            right = None
            func = None
            [operation, target] = [x.strip() for x in line.split("->")]
            operators = [x.strip() for x in operation.split(" ")]
            if len(operators) == 1:
                left = operators[0]
                if left.isdecimal():
                    left = int(left)
                right = None
                func = assign
            elif len(operators) == 2:
                right = operators[1]
                if right.isdecimal():
                    right = int(right)
                if operators[0] == "NOT":
                    func = not_gate
            elif len(operators) == 3:
                left = operators[0]
                if left.isdecimal():
                    left = int(left)
                right = operators[2]
                if right.isdecimal():
                    right = int(right)
                if operators[1] == "AND":
                    func = and_gate
                if operators[1] == "OR":
                    func = or_gate
                if operators[1] == "LSHIFT":
                    func = lshift_gate
                if operators[1] == "RSHIFT":
                    func = rshift_gate
            nodes.append(Node(left,right,target,func))
    resolved = False
    while not resolved:
        resolved = True
        for node in nodes:
            node.resolve()
            if not node.complete:
                resolved = False
    print(f"solution: {wires['a']}")



if __name__ == "__main__":
    main()
