from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(list(map(int, raw_input().split())))
    print(hash(integer_list))