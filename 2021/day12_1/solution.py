import os
from collections import defaultdict
from typing import DefaultDict, List
import pprint
pp = pprint.PrettyPrinter(indent=4)

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        connections:DefaultDict[str,List[str]] = defaultdict(list)
        for line in in_file:
            line = line.strip()
            [left,right] = [x.strip() for x in line.split("-")]
            connections[left].append(right)
            connections[right].append(left)
        #print(connections)

        working_paths = [["start"]]
        more = True
        while more:
            more = False
            new_paths = []
            for path in working_paths:
                if path[-1] == "end":
                    new_paths.append(path)
                    continue
                more = True
                next_steps = connections[path[-1]]
                for step in next_steps:
                    if (step.islower()  and step not in path) or step.isupper():
                        new_paths.append(path + [step])
            working_paths = new_paths
        # pp.pprint(working_paths)
        print(f"solution: {len(working_paths)}")
                    



if __name__ == "__main__":
    main()