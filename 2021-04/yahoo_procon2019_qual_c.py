k, a, b = map(int, input().split())

if a+1 >= b:
    print(k+1)
    exit()

if k < a:
    print(k+1)
    exit()

ab = b-a
k = k - a + 1
q = k // 2 - 1
r = k % 2

print(q*ab+b+r)
