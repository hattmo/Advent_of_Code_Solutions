import os
from collections import defaultdict
from itertools import permutations

happy_factors = defaultdict(dict)

def calc_happy(test_case:tuple, best):
    d = 0
    i = 1
    while i < len(test_case) -1:
        d += happy_factors[test_case[i]][test_case[i+1]]
        d += happy_factors[test_case[i]][test_case[i-1]]
        i+=1
    d += happy_factors[test_case[0]][test_case[1]]
    d += happy_factors[test_case[0]][test_case[-1]]
    d += happy_factors[test_case[-1]][test_case[0]]
    d += happy_factors[test_case[-1]][test_case[-2]]
    if d > best:
        return d
    else:
        return best
    

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        for line in in_file:
            [from_pers,_,gain_lose,factor,_,_,_,_,_,_,to_pers] = [x.strip() for x in line.split(" ")]
            to_pers = to_pers[:-1]
            factor = int(factor)
            if gain_lose == "lose":
                factor = -factor
            happy_factors[from_pers][to_pers] = factor

        you_dict = dict()
        for item in happy_factors:
            you_dict[item] = 0
            happy_factors[item]["You"] = 0
        happy_factors["You"] = you_dict
        people = happy_factors.keys()
        best = 0
        for attempt in permutations(people,len(people)):
            best = calc_happy(attempt,best)
        print(f"solution: {best}")

if __name__ == "__main__":
    main()