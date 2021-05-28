n = int(input())
a, b = map(int, input().split())
p = [ int(x) for x in input().split() ]

contests = [0] * 3

for e in p:
    if e <= a:
        contests[0] += 1
    elif a < e <= b:
        contests[1] += 1
    else:
        contests[2] += 1

print(min(contests))
