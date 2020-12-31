h, w = map(int, input().split())

k = []
nw = []

for _ in range(h):
    s = input()
    if s != '.' * w:
        k.append(s)
        index_num = [n for n, v in enumerate(s) if v == "#"]
        nw.extend(index_num)

nw = list(set(nw))

for e in k:
    v = ''
    for i in nw:
        v += e[i]
    
    print(v)
