import os
from collections import defaultdict
from typing import DefaultDict, Tuple

def print_data(data,from_x,from_y,to_x,to_y):
    out = ""
    for y in range(from_y,to_y):
        for x in range(from_x,to_x):
            out += "#" if data[(x,y)] else "."
        out += "\n"
    print(out)

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        lookup = list()
        for c in in_file.readline():
            if c == "#":
                lookup.append(True)
            else:
                lookup.append(False)
        in_file.readline()
        data:DefaultDict[Tuple[int,int]] = defaultdict(lambda: False)
        for y, line in enumerate(in_file):
            line = line.strip()
            for x,c in enumerate(line):
                if c == "#":
                    data[(x,y)] = True
        first_x = -60
        first_y = -60
        last_x = x + 60
        last_y = y + 60
        defualt_val = True
        for _ in range(2):
            new_data:DefaultDict[Tuple[int,int]] = defaultdict(lambda: defualt_val)
            defualt_val = not defualt_val
            for y in range(first_y,last_y):
                for x in range(first_x,last_x):
                    index = 0
                    index += 1 if data[(x+1,y+1)] else 0
                    index += 2 if data[(x,y+1)] else 0
                    index += 4 if data[(x-1,y+1)] else 0
                    index += 8 if data[(x+1,y)] else 0
                    index += 16 if data[(x,y)] else 0
                    index += 32 if data[(x-1,y)] else 0
                    index += 64 if data[(x+1,y-1)] else 0
                    index += 128 if data[(x,y-1)] else 0
                    index += 256 if data[(x-1,y-1)] else 0
                    new_data[(x,y)] = lookup[index]
            data = new_data
        total = len([x for x in data.values() if x==True])
        print(f"solution: {total}")
if __name__ == "__main__":
    main()