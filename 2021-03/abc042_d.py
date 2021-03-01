# not completed

from math import factorial
h, w, a, b = map(int, input().split())

kanarazutoru = w-b
c = 0

for i in range(kanarazutoru):
    if i >= 1:
        hh = h-a-1-1
        ww = b+i

        if hh == 0:
            c += 1
            continue
        elif hh < 0:
            continue

        zenhan = factorial(hh+ww) // (factorial(hh)*factorial(ww))
        kouhan = factorial(a+(w-b-i-1)) // (factorial(a)*factorial(w-b-i-1))

        print(zenhan)
        print(kouhan)

        c += zenhan * kouhan
    else:
        hh = h-a-1
        ww = w-b

        zenhan = factorial(hh+ww) // (factorial(hh)*factorial(ww))
        kouhan = factorial((h-a)+(w-b-1)) // (factorial(h-a)*factorial(w-b-1))

        print(zenhan)
        print(kouhan)

        c += zenhan * kouhan

print(c)
