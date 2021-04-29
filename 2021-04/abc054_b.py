n, m = map(int, input().split())

nlist = []
mlist = []

for i in range(n):
    nlist.append(list(input()))

for j in range(m):
    mlist.append(list(input()))

exist = False

for i in range(n):
    for j in range(n):
        if i+m-1 >= n or j+m-1 >= n:
            continue

        match = True
        for k in range(m):
            for l in range(m):
                if nlist[i+k][j+l] != mlist[k][l]:
                    match = False
        if match:
            exist = True
if exist:
    print("Yes")
else:
    print("No")
