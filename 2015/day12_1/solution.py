import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = in_file.read()
        temp = ""
        tot = 0
        for i,c in enumerate(data):
            if c.isdigit():
                if data[i-1] == "-":
                    temp += "-"
                temp += c
            else:
                if len(temp) > 0:
                    tot += int(temp)
                    temp = ""
        print(f"solution: {tot}")

if __name__ == "__main__":
    main()