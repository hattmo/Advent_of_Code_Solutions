import os


with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    total = 0
    for line in infile:
        [l,w,h]  = [int(x) for x in line.split("x")]
        sides =  [l*w,w*h,h*l]
        extra = min(sides)
        sides = [2*x for x in sides]
        sides.append(extra)
        total += sum(sides)
    print(f"solution: {total}")