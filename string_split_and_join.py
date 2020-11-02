def split_and_join(line):
    list_of_string = line.split(" ")
    line = "-".join(list_of_string)
    return line

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result