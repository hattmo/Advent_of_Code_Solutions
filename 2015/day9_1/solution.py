import os
from collections import defaultdict
from itertools import permutations

distances = defaultdict(dict)

def calc_distance(test_case, best):
    d = 0
    i = 0
    while i < len(test_case) -1:
        d+= distances[test_case[i]][test_case[i+1]]
        if d > best:
            return best
        i+=1
    return d
    

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        for line in in_file:
            [from_loc,_,to_loc,_,distance] = [x.strip() for x in line.split(" ")]
            distances[from_loc][to_loc] = int(distance)
            distances[to_loc][from_loc] = int(distance)
        locs = distances.keys()
        best = 300000
        for attempt in permutations(locs,len(locs)):
            best = calc_distance(attempt,best)
        print(f"solution: {best}")

if __name__ == "__main__":
    main()