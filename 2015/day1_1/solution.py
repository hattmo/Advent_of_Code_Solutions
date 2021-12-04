import os


with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
    in_string = infile.read()
    floor = 0
    for c in in_string:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    print(f"solution: {floor}")