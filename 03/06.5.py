kvals = [i for i in range(-100000, 100001)]
abssum = []
ones = []
for k in kvals:
    x = 103*(14 + 47*k)
    y = 103*(-11 - 37*k)
    one = 37*x + 47*y
    ones.append((one, x, y))
    val = abs(x) + abs(y)
    abssum.append((val, x, y))

wrong = [i for i in ones if i[0] != 103]
print('Incorrect calculations: {0}'.format([i for i in wrong]))
target = min(abssum)
print('Minium: {0}'.format(target))
