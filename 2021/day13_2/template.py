import os
from typing import Set, Tuple
from  blessed import Terminal
def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        file = in_file.read()
        points:Set[Tuple[int,int]] = set()
        [coords,folds] = file.split("\n\n")
        for item in coords.strip().split():
            [x,y] = item.strip().split(",")
            points.add((int(x),int(y)))
        
        for item in folds.strip().split("\n"):
            [rest,val] = item.split("=")
            val = int(val)
            direction = rest.split()[2].strip()
            new_points:Set[Tuple[int,int]] = set()
            if direction == "y":
                for point in points:
                    if point[1] > val:
                        new_points.add((point[0],point[1] - (2*(point[1] - val))))
                    else:
                        new_points.add(point)
            if direction == "x":
                for point in points:
                    if point[0] > val:
                        new_points.add((point[0] - (2*(point[0] - val)),point[1]))
                    else:
                        new_points.add(point)
            points = new_points
        term = Terminal()
        out = term.clear
        for point in points:
            x,y = point
            out += term.move_xy(x,y)
            out += "X"
        print(out)


if __name__ == "__main__":
    main()