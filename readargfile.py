import sys

with open(sys.argv[1]) as f:
    n = int(f.readline())

    arr = []
    for i in range(n):
        x, y = map(int, f.readline().strip().split())
        arr.append((x, y))

    print(arr)
