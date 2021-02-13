h, w = map(int, input().split())

field = []
ans = []

for _ in range(h):
    s = input()
    field.append(s)
    ans.append([0] * w)

for j, row in enumerate(field):
    for i, e in enumerate(list(row)):
        if e == "#":
            ans[j][i] = -9
            ue = True
            shita = True
            migi = True
            hidari = True

            if j == 0:
                ue = False
            if j == h-1:
                shita = False
            if i == 0:
                hidari = False
            if i == w-1:
                migi = False

            if ue:
                ans[j-1][i] += 1
                if hidari:
                    ans[j-1][i-1] += 1
                if migi:
                    ans[j-1][i+1] += 1

            if shita:
                ans[j+1][i] += 1
                if hidari:
                    ans[j+1][i-1] += 1
                if migi:
                    ans[j+1][i+1] += 1

            if hidari:
                ans[j][i-1] += 1
            if migi:
                ans[j][i+1] += 1

for ll in ans:
    sans = ''
    for e in ll:
        if e < 0:
            sans += '#'
        else:
            sans += str(e)

    print(sans)
