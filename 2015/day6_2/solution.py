import os

lights = list()

def init_lights():
    for i in range(1000*1000):
        lights.append(0)

def adjust_lights(x1,y1,x2,y2,mode):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            index = y * 1000 + x
            if mode == "on":
                lights[index] += 1
            if mode == "off":
                if lights[index] > 0:
                    lights[index] -= 1
            if mode == "toggle":
                lights[index] += 2

def main():
    init_lights()
    with open(f"{os.path.dirname(__file__)}\input.txt","r") as infile:
        for line in infile:
            tokens = line.strip().split(" ")
            if len(tokens) == 4:
                [x1,y1] = tokens[1].split(",")
                [x2,y2] = tokens[3].split(",")
                adjust_lights(int(x1),int(y1),int(x2),int(y2),"toggle")
            else:
                [x1,y1] = tokens[2].split(",")
                [x2,y2] = tokens[4].split(",")
                adjust_lights(int(x1),int(y1),int(x2),int(y2),tokens[1])
        count =0
        for light in lights:
            count += light
        print(f"solution: {count}")

if __name__ == '__main__':
    main()