x = str(input('введите строку'))
d = len(x)
p = x[0:(d+1)//2]
v = x[(d+1)//2:d]
print(v+p)