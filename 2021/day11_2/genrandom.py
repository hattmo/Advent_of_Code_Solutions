import random

with open("./crazy.txt","w") as out_file:
    for _ in range(80):
        for _ in range(80):
            out_file.write(str(random.randrange(0,9)))
        out_file.write("\n")
