import textwrap

from pip._vendor.distlib.compat import raw_input


def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        s = string[i:i+max_width]
        if(len(s) == max_width):
            print(s)
        else:
            return s

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)