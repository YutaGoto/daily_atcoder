a, b, c, d, e, f = map(int, input().split())

def wariai(suger, water):
    if suger+water == 0 or suger == 0:
        return 0
    else:
        return suger / (water+suger)

wmax = float(100*a)
smax = 0.0

for i in range(31):
    for j in range(31):
        for k in range(100):
            for l in range(100):
                water = 100*a*i + 100*b*j
                suger = c*k + d*l

                if water == 0:
                    break

                if suger > e * (a*i+b*j):
                    break

                if water + suger > f:
                    break

                if wariai(suger, water) > wariai(smax, wmax):
                    wmax = water
                    smax = suger

print(int(wmax+smax), int(smax))
