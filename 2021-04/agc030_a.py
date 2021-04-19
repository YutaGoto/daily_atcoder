a, b, c = map(int, input().split())

if a+b >= c:
    print(c+b)
else:
    print(a+b+1+b)
