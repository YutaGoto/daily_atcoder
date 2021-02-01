def minmin(t, new):
    mm = sorted(new.values())
    return mm[t]

base = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

new = {}

n, m = map(int, input().split())
a = [ int(x) for x in input().split() ]

c = ""

for e in a:
    new[e] = base[e]

while n > 0:
    t = 0
    f = True

    while f:
        mi = minmin(t, new)

        if n - mi >= min(new.values()) or n - mi == 0:
            n -= mi
            c += str([k for k, v in new.items() if v == mi][0])
            f = False
        else:
            t += 1

print("".join(sorted(c, reverse=True)))
