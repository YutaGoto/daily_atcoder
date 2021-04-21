h, w = map(int, input().split())

hsums = [0]*w
wsums = [0]*h
sf = []

for i in range(h):
    l = [ int(x) for x in input().split() ]
    wsums[i] = sum(l)
    sf.append(l)
    for j in range(w):
        hsums[j] += l[j]

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(str(hsums[j] + wsums[i] - sf[i][j]))

    print(' '.join(ans))
