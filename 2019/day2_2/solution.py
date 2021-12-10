import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = [x.strip() for x in in_file.read().split(",")]
        pc = 0
        data[1] = "64"
        data[2] = "21"
        while True:
            ins = data[pc]
            if ins == '1':
                a = int(data[int(data[pc+1])])
                b = int(data[int(data[pc+2])])
                data[int(data[pc+3])] = a + b
                pc += 4
            if ins == '2':
                a = int(data[int(data[pc+1])])
                b = int(data[int(data[pc+2])])
                data[int(data[pc+3])] = a * b
                pc += 4
            if ins == '99':
                print(data[1] + "" + data[2])
                exit()

if __name__ == "__main__":
    main()