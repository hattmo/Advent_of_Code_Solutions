import os
from typing import List


class Board:
    def __init__(self,values:List[int]) -> None:
        self.marked = [False] * 25
        self.values = values

    def mark(self,target:int):
        try:
            self.marked[self.values.index(target)] = True
        except:
            pass

    def won(self):
        for y in range(5):
            for x in range(5):
                if not self.marked[y*5+x]:
                    break
            else:
                return True
        for x in range(5):
            for y in range(5):
                if not self.marked[y*5+x]:
                    break
            else:
                return True
        return False

    def value(self):
        out = 0
        for m,v in zip(self.marked,self.values):
            if not m:
                out += v
        return out
    
    def __str__(self) -> str:
        return self.values.__str__()

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        first = True
        count = 0
        values = []
        boards:List[Board] = []
        for line in in_file:
            line = line.strip()
            if first:
                first = False
                moves = [int(x.strip()) for x in line.split(",") if x.isnumeric()]
                continue
            
            elif len(line) == 0:
                continue
            else:
                values += [int(x.strip()) for x in line.split(" ") if x.isnumeric()]
                count+=1
            if count == 5:
                count = 0
                boards.append(Board(values))
                values = []

        for move in moves:
            for board in boards:
                board.mark(move)
                if board.won():
                    result = move * board.value()
                    print(f"solution: {result}")
                    exit()

if __name__ == "__main__":
    main()