import os
from typing import Dict
from collections import defaultdict
from blessed import Terminal
from time import sleep

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

def draw_data(data:Dict[str,int],term:Terminal):
    out = term.clear
    for col in range(10):
        for row in range(10):
            val = data[(col,row)]
            if val == 0:
                out += 'X'
            else:
                out += " "
        out += "\n"
    print(out)

def main():
    term = Terminal()
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
        while True:
            increase_light(data)
            pop_light(data)
            reset_light(data)
            draw_data(data,term)
            sleep(0.5)



if __name__ == "__main__":
    main()
