from pip._vendor.distlib.compat import raw_input


def print_full_name(a, b):
    test = "Hello " + a +" "+ b + "! You just delved into python." 
    print(test)


if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)