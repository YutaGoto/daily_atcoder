n = int(input())

c = 0
base = 1

while True:
    c += base
    if n == 1:
        print(c)
        exit()
    else:
        n = n // 2 + n % 2
        base *= 2
