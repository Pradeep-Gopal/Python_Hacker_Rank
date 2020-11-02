from pip._vendor.distlib.compat import raw_input


def swap_case(s):
    new_string = ""

    for i in range(len(s)):
        if s[i].isupper():
            temp_string = s[i].lower()
        else:
            temp_string = s[i].upper()
        new_string += temp_string
    return new_string

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print(result)