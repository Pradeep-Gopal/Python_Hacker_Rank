from pip._vendor.distlib.compat import raw_input


def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = character
    string = ''.join(new_list)
    return string


if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)