s = list(input())

while len(s) > 0:
    s.pop()
    ln = len(s)
    if ln % 2 == 0:
        if s[0:(ln//2)] == s[(ln//2):(ln+1)]:
            print(ln)
            exit()

print(0)
