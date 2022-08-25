x = str(input('введите строку'))
d = len(x)
y = x.find(' ')
p = x[0:y]
v = x[y+1:d]
print(v+' '+p)