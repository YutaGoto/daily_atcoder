n, m = map(int, input().split())
a = [ int(x) for x in input().split() ]
a.sort()

q = []

for i in range(m):
    b, c = map(int, input().split())
    q.append([c,b])

q.sort(reverse=True)
i = 0
j = 0

while True:
    if i >= m:
        break
    if q[i][0] <= a[j]:
        break
    else:
        a[j] = q[i][0]
        j += 1
        q[i][1] -= 1
        if j >= n:
            break
        if q[i][1] == 0:
            i += 1

print(sum(a))
