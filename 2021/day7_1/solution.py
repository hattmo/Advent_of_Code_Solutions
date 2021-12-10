import os


def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        positions = [int(x) for x in in_file.read().strip().split(",")]
        max_pos = max(positions)
        min_pos = min(positions)
        best = 0
        for col in range(min_pos,max_pos+1):
            curr = 0
            for pos in positions:
                curr += abs(col-pos)
                if curr > best and best > 0:
                    break
            else:
                if curr < best or best == 0:
                    best = curr

        print(f"solution: {best}")
if __name__ == "__main__":
    main()