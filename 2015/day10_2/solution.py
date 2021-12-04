def main():
    data = "1321131112"
    for _ in range(50):
        count = 0
        on = data[0]
        next = ""
        for c in data:
            if c == on:
                count+=1
            else:
                next += str(count) + on
                on = c
                count = 1
        next += str(count) + on
        data = next
    print(f"solution: {len(data)}")
            
if __name__ == "__main__":
    main()