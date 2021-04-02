n = int(input())
base = 2025
l = base - n

for i in range(1, 10):
    if l % i == 0 and l // i < 10:
        print("{} x {}".format(i, l // i))
