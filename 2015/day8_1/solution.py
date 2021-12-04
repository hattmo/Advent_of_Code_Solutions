import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        added = 0
        for line in in_file:
            line = line.strip()
            added += 2
            index = 1
            while index < len(line)-1:
                c = line[index]
                if c == "\\":
                    if line[index+1] == "x":
                        added += 3
                        index += 3
                    else:
                        added += 1
                        index += 1
                index += 1
        print(f"solution: {added}") 
                


if __name__ == "__main__":
    main()