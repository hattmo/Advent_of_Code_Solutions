import hashlib
import itertools

def is_valid(in_bytes:bytes):
    return in_bytes[0] == 0x00 and in_bytes[1] == 0x00 and in_bytes[2] < 0x10

input_key = "ckczppom"

for i in itertools.count():
    test = input_key + str(i)
    if is_valid(hashlib.md5(test.encode("utf8")).digest()):
        print(f"solution {i}")
        exit()