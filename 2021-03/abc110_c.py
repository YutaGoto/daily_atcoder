from collections import Counter

s = list(input())
t = list(input())

su = Counter(s).values()
tu = Counter(t).values()

if sorted(su) == sorted(tu):
    print("Yes")
else:
    print("No")
