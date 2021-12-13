import os
from typing import Dict, List
from collections import defaultdict

popped_total = 0

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
        global popped_total
        popped_total += 1
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
    for key in data.keys():
        if data[key] > 9:
            data[key] = 0


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
        global popped_total
        popped_total = 0
        for _ in range(100):
            increase_light(data)
            pop_light(data)
            reset_light(data)
        print(f"solution: {popped_total}")


if __name__ == "__main__":
    main()
