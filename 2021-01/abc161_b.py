n, m = map(int, input().split())
a = [ int(x) for x in input().split() ]

s = sum(a)

a.sort(reverse=True)

if a[m-1] >= s / (4*m):
    print("Yes")
else:
    print("No")
