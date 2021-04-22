n = int(input())
l = [1]
i = 2

while True:
    j = 2
    while True:
        if i**j <= n:
            l.append(i**j)
            j += 1
        else:
            break
    i += 1

    if i > 32:
        break

print(max(l))
