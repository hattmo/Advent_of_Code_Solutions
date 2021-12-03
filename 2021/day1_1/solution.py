import os

count = 0
with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    depth = 99999
    for line in infile:
        new_depth = int(line)
        if new_depth > depth:
            count +=1
        depth = new_depth
print(count)