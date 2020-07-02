# This code will fail.
n = int(input())
d = {'0': 0}

for i in range(n):
    tp = ''.join(sorted(input()))
    if tp in d:
        d[tp] = sum(list(range(d[tp] + 2)))
    else:
        d.update({tp: 0})

print(sum(d.values()))
