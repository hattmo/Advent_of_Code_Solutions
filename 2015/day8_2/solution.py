import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        added = 0
        for line in in_file:
            line = line.strip()
            added += 2
            for c in line:
                if c == "\"":
                    added += 1
                if c == "\\":
                    added += 1
        print(f"solution: {added}") 
                


if __name__ == "__main__":
    main()