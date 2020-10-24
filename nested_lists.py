from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    records = []
    second_lowest_score = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        records.append([score, name])
    records.sort(reverse=True)
    # print(records)

    for i in range(len(records) - 1, -1, -1):
        if records[i][0] != records[i - 1][0]:
            # print(records[i - 1][0])
            temp = records[i - 1][0]
            break

    for i in records:
        if temp == i[0]:
            second_lowest_score.append(i)

    # print(second_lowest_score)

    second_lowest_score.sort(key=lambda x: x[1])
    for i in second_lowest_score:
        print(i[1])