import copy

n = int(input())
t = [ int(x) for x in input().split() ]
m = int(input())

for i in range(m):
    tt = copy.copy(t)
    p, x = map(int, input().split())
    tt[p - 1] = x
    print(sum(tt))
