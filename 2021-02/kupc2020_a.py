n = int(input())

if n == 1:
    print(0)
    exit()


d = 0
cx, cy = map(int, input().split())

for _ in range(n-1):
    x, y = map(int, input().split())
    d += abs(cx - x) + abs(cy - y)
    cx, cy = x, y

print(d)
