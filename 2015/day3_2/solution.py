import os
def to_cord(x,y):
    return str(x) + "-" + str(y)

with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    data = infile.read()
    x = 0
    y = 0
    xr = 0
    yr = 0
    santa = True
    visited = dict()
    visited[to_cord(x,y)] = True
    for c in data:
        if santa:
            if c == "<":
                x-=1
            elif c == ">":
                x+=1
            elif c == "v":
                y-=1
            else:
                y+=1
            visited[to_cord(x,y)] = True
        else:
            if c == "<":
                xr-=1
            elif c == ">":
                xr+=1
            elif c == "v":
                yr-=1
            else:
                yr+=1
            visited[to_cord(xr,yr)] = True
        santa = not santa
    print(f"solution: {len(visited)}")