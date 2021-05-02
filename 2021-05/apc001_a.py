x, y = map(int, input().split())

if x == y:
    print(-1)
    exit()

if x % y == 0:
    print(-1)
    exit()

i = 1
while True:
    if x*i % y != 0:
        print(x*i)
        exit()
    else:
        i += 1
