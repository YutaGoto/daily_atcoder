x = int(input())

for a in range(10001):
    for b in range(-10000, 10001):
        if a**5 - b**5 == x:
            print(a, b)
            exit()
