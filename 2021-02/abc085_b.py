n = int(input())

mochi = []

for _ in range(n):
    d = int(input())
    mochi.append(d)

mochi_set = set(mochi)

print(len(mochi_set))
