s = input()

if len(set(list(s))) == 2 and list(s).count(s[0]) == 2:
    print("Yes")
else:
    print("No")
