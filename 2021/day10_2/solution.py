import os

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        scores= []
        for line in in_file:
            line = line.strip()
            stack = list()
            for c in line:
                if c in ['(','[',"{","<"]:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if top != "(" and c == ")":
                        break
                    if top != "[" and c == "]":
                        break
                    if top != "{" and c == "}":
                        break
                    if top != "<" and c == ">":
                        break
            else:
                total = 0
                for i in reversed(stack):
                    total *= 5
                    if i == "(":
                        total += 1
                    if i == "[":
                        total += 2
                    if i == "{":
                        total += 3
                    if i == "<":
                        total += 4
                scores.append(total)
        scores.sort()
        print(f"solution: {scores[len(scores)//2]}")

if __name__ == "__main__":
    main()