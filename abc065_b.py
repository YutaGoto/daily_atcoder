n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))

c = 0
t = 1

while c < n:
    t = l[t-1]
    c += 1
    if t == 2:
        print(c)
        exit()

print(-1)
