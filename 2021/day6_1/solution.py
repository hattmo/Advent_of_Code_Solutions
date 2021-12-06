import os
from collections import defaultdict


def main():
    days = 80
    fish = defaultdict(int)
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = [int(x.strip()) for x in in_file.read().strip().split(",")]
        for item in data:
            fish[item] += 1
        for _ in range(days):
            ready_fish = fish[0]
            for index in range(1,9):
                fish[index-1] = fish[index]
            fish[8] = ready_fish
            fish[6] += ready_fish
        total = 0
        for i in fish.values():
            total += i
        print(f"solution: {total}")


if __name__ == "__main__":
    main()