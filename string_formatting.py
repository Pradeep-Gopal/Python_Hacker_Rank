from pip._vendor.distlib.compat import raw_input
from pip._vendor.msgpack.fallback import xrange


def print_formatted(STDIN):

    w = len(str(bin(STDIN)).replace('0b', ''))
    print(w)

    for i in xrange(1, STDIN + 1):
        b = bin(int(i)).replace('0b', '').rjust(w, ' ')
        o = oct(int(i)).replace('0o', '').rjust(w, ' ')
        h = hex(int(i)).replace('0x', '').upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print(j, o, h, b)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)