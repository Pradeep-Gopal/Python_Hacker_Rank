from __future__ import division
from pip._vendor.distlib.compat import raw_input



if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print int(int(a)/int(b))
    print(float(a)/float(b))