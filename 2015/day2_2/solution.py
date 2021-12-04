import os
import math

with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    total = 0
    for line in infile:
        sides  = [int(x) for x in line.split("x")]
        [l,w,h] = sides
        perimeter = (sum(sides) - max(sides)) * 2
        volume = math.prod(sides)
        result = perimeter + volume
        total += result
    print(f"solution: {total}")