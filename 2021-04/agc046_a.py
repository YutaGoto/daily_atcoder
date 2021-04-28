x = int(input())

c = 0

while True:
    c += 1
    if x*c % 360 == 0:
        print(c)
        exit()
