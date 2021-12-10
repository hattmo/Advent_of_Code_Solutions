import os
from typing import List

def find_zero(data:List[str]):
    for item in data:
        if len(item) == 6:
            data.remove(item)
            return item


def find_one(data:List[str]):
    for item in data:
        if len(item) == 2:
            data.remove(item)
            return item

def find_two(data:List[str],four:str):
    for item in data:
        missing = 0
        for c in four:
            if c not in item:
                missing +=1
        if missing == 2:
            data.remove(item)
            return item

def find_three(data:List[str],one:str):
    five_size = [x for x in data if len(x) == 5]
    for item in five_size:
        for c in one:
            if c not in item:
                break
        else:
            data.remove(item)
            return item

def find_four(data:List[str]):
    for item in data:
        if len(item) == 4:
            data.remove(item)
            return item

def find_five(data:List[str]):
    out = data[0]
    data.remove(data[0])
    return out

def find_six(data:List[str],one:str):
    six_size = [x for x in data if len(x) == 6]
    for item in six_size:
        for c in one:
            if c not in item:
                break
        else:
            continue
        data.remove(item)
        return item

def find_seven(data:List[str]):
    for item in data:
        if len(item) == 3:
            data.remove(item)
            return item

def find_eight(data:List[str]):
    for item in data:
        if len(item) == 7:
            data.remove(item)
            return item

def find_nine(data:List[str], four:str):
    six_size = [x for x in data if len(x) == 6]
    for item in six_size:
        for c in four:
            if c not in item:
                break
        else:
            data.remove(item)
            return item

def get_digit(numbers:List[str], target:str):
    for i,num in enumerate(numbers):
        if len(num) != len(target):
            continue
        for c in num:
            if c not in target:
                break
        else:
            return i

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        total = 0
        for line in in_file:
            [left,right] = [x.strip() for x in line.split("|")]
            data = [x.strip() for x in left.split(" ")]
            one = find_one(data)
            four = find_four(data)
            seven = find_seven(data)
            eight = find_eight(data)
            three = find_three(data,one)
            six = find_six(data,one)
            nine = find_nine(data,four)
            zero = find_zero(data)
            two = find_two(data,four)
            five = find_five(data)
            numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
            targets = [x.strip() for x in right.split(" ")]

            val = 0
            for target in targets:
                val *= 10
                val += get_digit(numbers,target)
            total += val
        print(f"solution: {total}")

if __name__ == "__main__":
    main()