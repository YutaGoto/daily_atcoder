import sys

n, y = map(int, input().split())

for a in range(0,n+1):
    for b in range(0,n-a+1):
        c = n - a - b
        if a*10000 + b*5000 + c*1000 == y:
            if c >= 0:
                print("{} {} {}".format(a, b, c))
                sys.exit()

print('-1 -1 -1')
