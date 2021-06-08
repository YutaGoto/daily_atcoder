a, b, c = map(int,input().split())
t = a


while t < 10000:
    if t % b == c:
        print("YES")
        exit()


    t += a


print("NO")
