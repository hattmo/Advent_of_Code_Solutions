import os

with open(f"{os.path.dirname(__file__)}\input.txt","r") as file:
    tot_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    count = 0
    for line in file:
        count+=1
        for i,c in enumerate(line.strip()):
            tot_list[i] += int(c)
    print(tot_list)
    multi = 1
    a = 0
    b = 0
    for i in reversed(tot_list):
        if i > (count // 2):
            a += multi
        else:
            b += multi
        multi *= 2
    print(a*b)

