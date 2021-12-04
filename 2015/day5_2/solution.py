import os

def has_pairs(test:str)->bool:
    for i in range(len(test)-3):
        index = test[i:i+2]
        for j in range(i+2,len(test)-1):
            target = test[j:j+2]
            if index == target:
                return True
    return False


def has_repeat(test:str)->bool:
    for i in range(len(test)-2):
        if test[i] == test[i+2]:
            return True
    return False


def is_nice(test:str) -> bool:
    if not has_pairs(test):
        return False
    if not has_repeat(test):
        return False
    return True

def main():
    with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
        count = 0
        for line in infile:
            if is_nice(line.strip()):
                count += 1
        print(f"solution: {count}")

if __name__ == "__main__":
    main()