n = input()
l = [int(char) for char in n]

if int(n) % sum(l) == 0:
    print('Yes')
else:
    print('No')
