from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = raw_input()
    scores = student_marks[query_name]
    sum = 0

    total = 0
    for ele in range(0, len(scores)):
        total = total + scores[ele]

    print("{0:.2f}".format(total/3.00))