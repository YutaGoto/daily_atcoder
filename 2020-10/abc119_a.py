import datetime

s = input()
st = datetime.datetime.strptime(s, '%Y/%m/%d')
heisei = datetime.datetime(2019,4,30)
if st <= heisei:
  print("Heisei")
else:
  print("TBD")
