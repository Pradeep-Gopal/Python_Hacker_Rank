from pip._vendor.distlib.compat import raw_input

a = list(map(int, raw_input().split()))
b = int(a[0] / 2) + 1
h = b - 1
c = 'WELCOME'
d = '.|.'
l = []
p = -1
for i in range(1, a[0]*2 , 2):
    if i == b + h:
        print(c.center(a[1], '-'))
    elif i < b + h:
        print((d*i).center(a[1], '-'))
        l.append(i)
    else:
        print((d * l[p]).center(a[1], '-'))
        p = p - 1



