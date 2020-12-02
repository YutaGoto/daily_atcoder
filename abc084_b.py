a, b = map(int, input().split())
s = input()

if s[0:a].isnumeric() and s[a] == "-" and s[a+1:].isnumeric():
    print("Yes")
else:
    print("No")
