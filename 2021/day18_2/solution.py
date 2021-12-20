import os
from typing import List, Tuple, Union
import copy

class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.depth = 0

    def set_left(self, val: Union[int, 'Node']):
        self.left = val
        self.set_depth(self.depth)

    def set_right(self, val: Union[int, 'Node']):
        self.right = val
        self.set_depth(self.depth)

    def set_depth(self,val:int):
        self.depth = val
        if type(self.right) == Node:
            self.right.set_depth(val+1)
        if type(self.left) == Node:
            self.left.set_depth(val+1)

    def get_magnitude(self)->int:
        if type(self.right) == Node:
            right = self.right.get_magnitude()
        else:
            right = self.right
        if type(self.left) == Node:
            left = self.left.get_magnitude()
        else:
            left = self.left
        return 3*left + 2*right

    def explode(self)->Tuple:
        if self.depth >= 3:
            if type(self.left) == Node and type(self.left.left) == int and type(self.left.right) == int:
                if type(self.right) == int:
                    self.right += self.left.right
                else:
                    target = self.right
                    while type(target.left) != int:
                        target = target.left
                    target.left += self.left.right
                result = (self.left.left,0)
                self.left = 0
                return result

        if type(self.left) == Node:
            result = self.left.explode()
            if len(result)>0:
                if result[1] != 0:
                    if type(self.right) == int:
                        self.right+=result[1]
                    else:
                        target = self.right
                        while type(target.left) != int:
                            target = target.left
                        target.left += result[1]
                    return (result[0],0)
                else:
                    return result

        if self.depth >= 3:
            if type(self.right) == Node and type(self.right.left) == int and type(self.right.right) == int:
                if type(self.left) == int:
                    self.left += self.right.left
                else:
                    target = self.left
                    while type(target.right) != int:
                        target = target.right
                    target.right += self.right.left
                result = (0,self.right.right)
                self.right = 0
                return result

        if type(self.right) == Node:
            result = self.right.explode()
            if len(result)>0:
                if result[0] != 0:
                    if type(self.left) == int:
                        self.left+=result[0]
                        
                    else:
                        target = self.left
                        while type(target.right) != int:
                            target = target.right
                        target.right += result[0]
                    return (0,result[1])
                else:
                    return result
 
        return tuple()

    def split(self)->bool:
        if type(self.left) == Node:
            if self.left.split():
                return True
        elif self.left >= 10:
            split_node = Node()
            split_node.set_left(self.left//2)
            split_node.set_right(self.left//2+(self.left%2>0))
            self.set_left(split_node)
            return True

        if type(self.right) == Node:
            if self.right.split():
                return True
        elif self.right >= 10:
            split_node = Node()
            split_node.set_left(self.right//2)
            split_node.set_right(self.right//2+(self.right%2>0))
            self.set_right(split_node)
            return True
        return False

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"

    def __add__(self,target):
        out = Node()
        out.set_left(self)
        out.set_right(target)
        reduce_node(out)
        return out




def parse_line(line:str):
    line = line.strip()
    stack:List[Tuple[Node,bool]] = list()
    cursor = Node()
    on_left = True
    for c in line[1:-1]:
        if c == "[":
            stack_item = (cursor,on_left)
            stack.append(stack_item)
            on_left = True
            cursor = Node()
        elif c == ',':
            on_left = False
            pass
        elif c == "]":
            parent:Tuple[Node,bool] = stack.pop()
            parent_node = parent[0]
            parent_left = parent[1]
            if parent_left:
                parent_node.set_left(cursor)
            else:
                parent_node.set_right(cursor)
            cursor = parent_node
            on_left = False
        else:
            if on_left:
                cursor.set_left(int(c))
            else:
                cursor.set_right(int(c))
    return cursor

def reduce_node(node:Node):
    done = False
    while not done:
        if len(node.explode()) > 0:
            continue
        if node.split():
            continue
        done = True

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt", "r") as in_file:
        nodes:List[Node] = list()
        for line in in_file:
            nodes.append(parse_line(line))

        max_val = 0

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    result = copy.deepcopy(nodes[i]) + copy.deepcopy(nodes[j])
                    if result.get_magnitude() > max_val:
                        max_val = result.get_magnitude()
        

        print(f"solution: {max_val}")







if __name__ == "__main__":
    main()
