import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        score = 0
        for line in in_file:
            stack = list()
            for c in line:
                if c in ['(','[',"{","<"]:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if top != "(" and c == ")":
                        score += 3
                        break
                    if top != "[" and c == "]":
                        score += 57
                        break
                    if top != "{" and c == "}":
                        score += 1197
                        break
                    if top != "<" and c == ">":
                        score += 25137
                        break
        print(f"solution: {score}")

if __name__ == "__main__":
    main()