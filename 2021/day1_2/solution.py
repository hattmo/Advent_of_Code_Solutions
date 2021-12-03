import os

count = 0
with open(f"{os.path.dirname(__file__)}\input.txt","r") as inputfile:
    depth_list = []
    for line in inputfile:
        depth_list.append(int(line))
    for index in range(len(depth_list)-3):
        if depth_list[index] < depth_list[index+3]:
            count+=1
print(count)

