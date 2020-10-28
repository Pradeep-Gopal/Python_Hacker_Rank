import numpy

from pip._vendor.distlib.compat import raw_input

row_col = raw_input().split()
row = int(row_col[0])
col = int(row_col[1])

my_array = numpy.zeros([row, col], int)

for i in range(row):
    num = raw_input().split()
    my_array[i] = num

res = numpy.sum(my_array, axis=0)

result = 1
for i in range(len(res)):
    result = int(res[i])*result
print(result)





