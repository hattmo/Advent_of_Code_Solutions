import os
def to_cord(x,y):
    return str(x) + "-" + str(y)

with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    data = infile.read()
    x = 0
    y = 0
    visited = dict()
    visited[to_cord(x,y)] = True
    for c in data:
        if c == "<":
            x-=1
        elif c == ">":
            x+=1
        elif c == "v":
            y-=1
        elif c == '^':
            y+=1
        else:
            print("invalid char")
        visited[to_cord(x,y)] = True
    print(f"solution: {len(visited)}")