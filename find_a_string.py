from pip._vendor.distlib.compat import raw_input


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            length_of_substring = len(sub_string)
            string_sub = string[i:i+length_of_substring]
            if sub_string == string_sub:
                count += 1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print(count)