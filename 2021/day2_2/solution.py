import os

with open(f"{os.path.dirname(__file__)}\input.txt","r") as file:
    hor = 0
    depth = 0
    aim = 0
    for line in file:
        parts = line.split(" ")
        if parts[0] == "forward":
            hor += int(parts[1])
            depth += aim * int(parts[1])
        if parts[0] == "down":
            aim += int(parts[1])
        if parts[0] == "up":
            aim -= int(parts[1])
    print(hor*depth)