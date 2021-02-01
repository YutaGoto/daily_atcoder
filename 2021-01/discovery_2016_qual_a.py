w = int(input())

s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

c = 0
b = 0

while True:
    k = ''
    b = 0

    while b < w:
        k += s[c]

        c += 1
        b += 1

        if c >= 51:
            break

    print(k)

    if c >= 51:
        exit()
