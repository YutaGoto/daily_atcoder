s = list(input())
k = int(input())

if k == 1:
    print(s[0])
else:
    for i, e in enumerate(s):
        if i == k-1:
            print(e)
            exit()
        elif e != '1':
            print(e)
            exit()
