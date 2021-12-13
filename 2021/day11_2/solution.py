import os
from typing import Dict, List
from collections import defaultdict


def increase_light(data: Dict[str, int]):
    for key in data.keys():
        data[key] += 1

def try_recurse(col, row, data, popped):
    try:
        data[(col,row)] += 1
        pop_recurse(col, row, data, popped)
    except KeyError:
        pass

def pop_recurse(col, row, data, popped):
    if data[(col,row)] > 9 and not popped[(col,row)]:
        popped[(col,row)] = True
        try_recurse(col+1,row+1,data,popped)
        try_recurse(col+1,row,data,popped)
        try_recurse(col+1,row-1,data,popped)
        try_recurse(col-1,row+1,data,popped)
        try_recurse(col-1,row,data,popped)
        try_recurse(col-1,row-1,data,popped)
        try_recurse(col,row+1,data,popped)
        try_recurse(col,row-1,data,popped)


def pop_light(data: Dict[str, int]):
    popped = defaultdict(lambda: False)
    for key in data.keys():
        if data[key] > 9 and not popped[key]:
            col,row = key
            pop_recurse(col,row,data,popped)




def reset_light(data: Dict[str, int]):
    done = True
    for key in data.keys():
        if data[key] > 9:
            data[key] = 0
        else:
            done = False
    return done


def main():
    with open(f"{os.path.dirname(__file__)}/input.txt", "r") as in_file:
        data = dict()
        row = 0
        for line in in_file:
            line = line.strip()
            col = 0
            for c in line:
                data[(col,row)] = int(c)
                col += 1
            row += 1
        for i in range(1000):
            increase_light(data)
            pop_light(data)
            if reset_light(data):
                print(f"solution: {i+1}")
                exit()



if __name__ == "__main__":
    main()
