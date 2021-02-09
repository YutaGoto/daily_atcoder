s, t = sorted(input().split())

if 'B' in s and 'B' in t:
    print(int(t[1]) - int(s[1]))
elif 'F' in s and 'B' in t:
    print(int(s[0]) + int(t[1]) - 1)
else:
    print(int(t[0]) - int(s[0]))
