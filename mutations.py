from pip._vendor.distlib.compat import raw_input

n = raw_input()
main_set = set()

main_set = set(map(int, raw_input().split()))
m = int(raw_input())

for _ in range(m):
    l = list(raw_input().split())
    operation = l[0]
    set_size = l[1:]

    sub_set = set(map(int, raw_input().split()))
    eval("main_set." + operation + "(sub_set)")
print(sum(main_set))




