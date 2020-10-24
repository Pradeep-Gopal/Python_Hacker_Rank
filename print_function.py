from __future__ import print_function

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    a = '1'
    for i in range(1, n+1):
        a = a + str(i)
    a = a[1:]
    print(a)
