import os
from collections import defaultdict

def main():
    coords = defaultdict(lambda:int(0))
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        for line in in_file:
            [from_coord,to_coord] = [x.strip() for x in line.split("->")]
            [x1,y1] = [int(x.strip()) for x in from_coord.split(",")]
            [x2,y2] = [int(x.strip()) for x in to_coord.split(",")]
            if x1 == x2:
                if y2 < y1:
                    y1,y2=y2,y1
                for i in range(y1,y2+1):
                    coords[f'{x1}-{i}'] += 1
            elif y1==y2:
                if x2 < x1:
                    x1,x2=x2,x1
                for i in range(x1,x2+1):
                    coords[f'{i}-{y1}'] += 1
            else:
                if x2 < x1:
                    x1,x2=x2,x1
                    y1,y2=y2,y1
                step = 1
                if y2 < y1:
                    step = -1
                for x,y in zip(range(x1,x2+1),range(y1,y2+step,step)):
                    coords[f'{x}-{y}'] += 1
        count = 0
        for coord in coords:
            if coords[coord] > 1:
                count += 1
        print(f"solution: {count}")


if __name__ == "__main__":
    main()