n = int(input())

# 5**25 < 1000000000000000000 < 5**26
# 3**37 < 1000000000000000000 < 5**38

for b in range(1, 26):
    for a in range(1, 38):
        if 5**b + 3**a == n:
            print("{} {}".format(a, b))
            exit()

print(-1)
