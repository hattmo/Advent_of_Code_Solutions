from string import ascii_lowercase


ascii_lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def has_straight(test:list):
    i = 0
    test_len = len(test)
    while i < test_len-2:
        if test[i+2] - test[i+1] == 1 and test[i+1] - test[i] == 1:
            return True
        i+=1
    return False

def has_bad_char(test:list):
    return (8 in test) or (14 in test) or (11 in test)

def has_pairs(test:list):
    first_pair = None
    i = 0
    test_len = len(test)
    while i < test_len-1:
        if test[i] == test[i+1]:
            if first_pair == None:
                first_pair = test[i]
            elif test[i] != first_pair:
                return True
        i+=1
    return False

def encode(source:str):
    out = []
    for c in source:
        out.append(ascii_lowercase.index(c))
    return out

def decode(source:list):
    out = ""
    for c in source:
        out += ascii_lowercase[c]
    return out

def increment(source:list):
    index = len(source) - 1
    source[index] += 1
    while source[index] == 26:
        source[index] = 0
        index -= 1
        source[index] += 1

def good_pass(source:list):
    if has_bad_char(source):
        return False
    if not has_pairs(source):
        return False
    if not has_straight(source):
        return False
    return True

def main():
    data = encode("vzbxxzaa")
    while not good_pass(data):
        increment(data)
    print(decode(data))

if __name__ == "__main__":
    main()
