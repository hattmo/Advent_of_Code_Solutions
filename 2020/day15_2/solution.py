from typing import Collection


from collections import defaultdict

values = [1,12,0,20,8,16] 
target  = 30000000
lookup = defaultdict(list)



for i,start in enumerate(values):
    lookup[start].append(i+1)

last = values[-1]
percent = 0
for i in range(len(values),target):
    if i % 300000 == 0:
        percent += 1
        print(f"%{percent}")
    last_indexes = lookup[last]
    if len(last_indexes) < 2:
        last = 0
    else:
        last =  last_indexes[1] - last_indexes[0]
    new_indexes = lookup[last]
    new_indexes.append(i+1)
    if len(new_indexes) > 2:
        del new_indexes[0]
print(last)