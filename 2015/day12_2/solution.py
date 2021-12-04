import os
import json
 
total = 0

def parse(data):
    global total
    if type(data) == list:
        for item in data:
            parse(item)
    elif type(data) == str:
        return
    elif type(data) == int:
        total += data
    elif type(data) == dict:
        if "red" in data.values():
            return
        else:
            for key in data.keys():
                parse(data[key])
    else:
        print(type(data))
        input()

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        global total
        data = json.load(in_file)
        parse(data)
        print(total)

if __name__ == "__main__":
    main()