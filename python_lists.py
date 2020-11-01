from pip._vendor.distlib.compat import raw_input

n = int(input())
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]

    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l." + cmd)
    else:
        print(l)
