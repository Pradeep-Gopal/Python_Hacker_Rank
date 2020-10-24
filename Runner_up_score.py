from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr = list(arr)
    arr.sort()

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != arr[i-1]:
            print(arr[i - 1])
            break


