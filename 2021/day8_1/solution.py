import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        count = 0
        for line in in_file:
            data = [x.strip() for x in line.split("|")[1].strip().split(" ")]
            for item in data:
                if len(item) in [2,3,4,7]:
                    count+=1
        print(f"solution {count}")



if __name__ == "__main__":
    main()