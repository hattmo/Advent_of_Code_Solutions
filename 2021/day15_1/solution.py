from collections import defaultdict
import os
from typing import DefaultDict, List, Set, Tuple


class Path:
    def __init__(self, route: Set[Tuple[int, int]],last:Tuple[int,int], distance: int):
        self.last = last
        self.route = route
        self.distance = distance


def main():
    with open(f"{os.path.dirname(__file__)}/input.txt", "r") as in_file:
        cost_data = dict()
        calc_distance: DefaultDict[Tuple[int, int], int] = defaultdict(lambda: -1)
        calc_distance[(0,0)] = 0
        y = 0
        for line in in_file:
            line = line.strip()
            x = 0
            for c in line:
                cost_data[(x, y)] = int(c)
                x += 1
            y += 1

        paths:List[Path] = [Path({(0, 0)},(0,0), 0)]
        while len(paths) > 0:
            tainted_coords:Set[Tuple[int,int]] = set()
            new_paths:List[Path] = list()
            for path in paths:
                if len(path.route.intersection(tainted_coords)) > 0:
                    continue
                coord = path.last
                for x_off,y_off,x_limit,y_limit in [(-1,0,0,-1),(0,-1,-1,0),(1,0,x-1,-1),(0,1,-1,y-1)]:
                    if coord[0] != x_limit and coord[1] != y_limit:
                        target_coord = (coord[0]+x_off,coord[1]+y_off)
                        target_cost = calc_distance[target_coord]
                        potential_cost = path.distance + cost_data[target_coord]
                        if target_cost == -1 or target_cost > potential_cost:
                            tainted_coords.add(target_coord)
                            calc_distance[target_coord] = potential_cost
                            new_paths = [x for x in new_paths if target_coord not in x.route]
                            new_paths.append(Path(path.route.union({target_coord}),target_coord,potential_cost))
            paths = new_paths
        print(f"solution: {calc_distance[(x-1,y-1)]}")
                
 


if __name__ == "__main__":
    main()
