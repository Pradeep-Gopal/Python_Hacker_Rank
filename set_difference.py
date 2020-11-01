from pip._vendor.distlib.compat import raw_input

n = raw_input()
a = set(map(int, raw_input().split()))
b = raw_input()
c = set(map(int, raw_input().split()))
print(len(a.difference(c)))
