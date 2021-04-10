n, m = map(int, input().split())

wa = [0]*(n+1)
ac = set()

wa_c = 0

for i in range(m):
    p, s = input().split()
    if s == 'AC':
        ac.add(p)
    else:
        if p not in ac:
            wa[int(p)] += 1

for e in ac:
    wa_c += wa[int(e)]

print(len(ac), wa_c)
