import os
from collections import defaultdict
from typing import DefaultDict, Dict, Tuple

def main():

    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        [start,end] = in_file.read().split("\n\n")
        start = start.strip()
        first = start[0]
        last = start[-1]
        pairs:DefaultDict[Tuple[str,str],int] = defaultdict(int)
        for i in range(len(start)-1):
            pairs[(start[i],start[i+1])] += 1

        rules:Dict[Tuple[str,str],Tuple[Tuple[str,str],Tuple[str,str]]] = dict()
        for line in end.strip().split("\n"):
            line = line.strip()
            [left,right] = line.split(" -> ")
            rules[(left[0],left[1])] = ((left[0],right),(right,left[1]))
        for _ in range(40):
            new_pairs:DefaultDict[Tuple[str,str],int] = defaultdict(int)
            for pair in pairs:
                rule_result = rules[pair]
                amount = pairs[pair]
                new_pairs[rule_result[0]] += amount
                new_pairs[rule_result[1]] += amount
            pairs = new_pairs
        
        counts:DefaultDict[str,int] = defaultdict(int)
        for pair in pairs:
            amount = pairs[pair]
            counts[pair[0]] += amount
            counts[pair[1]] += amount
        for i in counts:
            counts[i] //= 2
        counts[first] += 1
        counts[last] += 1
        max_val = max(counts.values())
        min_val = min(counts.values())

        print(f"solution: {max_val-min_val}")


if __name__ == "__main__":
    main()