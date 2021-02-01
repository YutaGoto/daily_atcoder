n = int(input())
s = list(input())

rnum = s.count('R')
cwnum = 0

cmin = max(rnum, cwnum)

for i in range(n):
    if s[i] == 'W':
        cwnum += 1
    else:
        rnum -= 1

    tmax = max(cwnum, rnum)

    if tmax < cmin:
        cmin = tmax

print(cmin)
