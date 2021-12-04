import os

vowels = ["a","e","i","o","u"]
bad_sub = ["ab","cd","pq","xy"]


def count_vowels(test:str)->int:
    count = 0
    for c in test:
        if c in vowels:
            count+=1
    return count

def has_repeat(test:str)->bool:
    last = ""
    for c in test:
        if c == last:
            return True
        last = c
    return False

def has_bad_substr(test:str)->bool:
    for bad in bad_sub:
        if bad in test:
            return True
    return False

def is_nice(test:str) -> bool:
    if count_vowels(test) < 3:
        return False
    if not has_repeat(test):
        return False
    if has_bad_substr(test):
        return False
    return True


with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    count = 0
    for line in infile:
        if is_nice(line.strip()):
            count += 1
    print(f"solution: {count}")