s = input()

dif = 1000

for i in range(len(s)-2):
    k = int(s[i:i+3])
    if abs(k - 753) < dif:
        dif = abs(k - 753)

print(dif)
