from collections import defaultdict
import os
from typing import DefaultDict, Dict, Tuple

def find_size(point:Tuple[int,int],data:Dict[Tuple[int,int],int],max_col:int,max_row:int,visited:DefaultDict[Tuple[int,int],bool]):
    count = 1
    col, row = point
    visited[(col,row)] = True
    if col > 0 and not visited[(col-1,row)] and data[(col-1,row)]!=9:
            count += find_size((col-1,row),data,max_col,max_row,visited)
    if col < max_col-1 and not visited[(col+1,row)] and data[(col+1,row)]!=9:
            count += find_size((col+1,row),data,max_col,max_row,visited)
    if row > 0 and not visited[(col,row-1)] and data[(col,row-1)]!=9:
           count += find_size((col,row-1),data,max_col,max_row,visited)
    if row < max_row-1 and not visited[(col,row+1)] and data[(col,row+1)]!=9:
                count += find_size((col,row+1),data,max_col,max_row,visited)
    return count

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = dict()
        row = 0
        max_col = 0
        max_row = 0
        for line in in_file:
            line = line.strip()
            col = 0
            for c in line:
                data[(col,row)] = int(c)
                col += 1
                if col > max_col:
                    max_col = col
            row+=1
            if row > max_row:
                    max_row = row
        low_points= []
        for col,row in data.keys():
            val = data[(col,row)]
            left = 10
            right = 10
            up = 10
            down = 10
            if col > 0:
                left = data[(col-1,row)]
            if col < max_col-1:
                right = data[(col+1,row)]
            if row > 0:
                up = data[(col,row-1)]
            if row < max_row-1:
                down = data[(col,row+1)]
            if val < min([left,right,up,down]):
                low_points.append((col,row))
        basin_sizes = []
        for point in low_points:
            visited = defaultdict(lambda:False)
            basin_sizes.append(find_size(point,data,max_col,max_row,visited))

        basin_sizes.sort()
        print(f"solution: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")




if __name__ == "__main__":
    main()