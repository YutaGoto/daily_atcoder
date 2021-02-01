s = input()

l = s.split('+')
c = 0

for e in l:
    if '0' not in e:
        c += 1

print(c)
