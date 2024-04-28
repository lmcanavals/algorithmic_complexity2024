n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().strip().split())
    arr.append((x, y))

print(arr)
