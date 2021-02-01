n = int(input())

al = []

m1 = -1
m2 = -2

for _ in range(n):
    a = int(input())
    al.append(a) 
    if a > m1:
        m2 = m1
        m1 = a
    elif a > m2:
        m2 = a

for e in al:
    if e == m1:
        print(m2)
    else:
        print(m1)
