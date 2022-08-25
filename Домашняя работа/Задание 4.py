x = str(input('введите строку'))
c = x.count('f')
if c == 1:
    print(x.find('f'))
elif c >=2:
    print(x.find('f'),x.rfind('f'),sep=' ')
elif c == 0:
    print()