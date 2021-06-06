s = input()

zen = int(s[0:2])
kou = int(s[2:4])

yymm, mmyy = False, False

if 12 >= kou >= 1:
    yymm = True

if 12 >= zen >= 1:
    mmyy = True


if yymm and mmyy:
    print('AMBIGUOUS')
elif yymm and not mmyy:
    print('YYMM')
elif not yymm and mmyy:
    print('MMYY')
else:
    print('NA')
