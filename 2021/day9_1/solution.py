import os


def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = dict()
        row = 0
        max_col = 0
        max_row = 0
        for line in in_file:
            line = line.strip()
            col = 0
            for c in line:
                data[(col,row)] = int(c)
                col += 1
                if col > max_col:
                    max_col = col
            row+=1
            if row > max_row:
                    max_row = row
        total = 0
        for col,row in data.keys():
            val = data[(col,row)]
            left = 10
            right = 10
            up = 10
            down = 10
            if col > 0:
                left = data[(col-1,row)]
            if col < max_col-1:
                right = data[(col+1,row)]
            if row > 0:
                up = data[(col,row-1)]
            if row < max_row-1:
                down = data[(col,row+1)]
            if val < min([left,right,up,down]):
                total += (val + 1)
        print(f"solution: {total}")



if __name__ == "__main__":
    main()