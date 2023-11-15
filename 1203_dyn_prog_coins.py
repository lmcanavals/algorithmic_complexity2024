# Recursive naive Divide and conquer O(d^n)
def coins(n, d):
    if n == 0:
        return 0
    temp = []
    for di in d:
        if di <= n:
            resp = coins(n - di, d)
            temp.append(resp)
    return min(temp) + 1


# Top down dynamic programmin solution
def dpcoins(n, d):
    c = [0] * (n + 1)
    s = [-1] * (n + 1)
    for i in range(1, n + 1):
        bestc = float('inf')
        si = -1
        for di in d:
            if di > i:
                continue

            if c[i - di] < bestc:
                bestc = c[i - di]
                si = di
        c[i] = bestc + 1
        s[i] = si

    selection = []
    temp = n
    while temp > 0:
        selection.append(s[temp])
        temp -= s[temp]
    return c[n], selection


d = [50, 20, 10, 5, 1]
n = 40

print(coins(n, d))
print(dpcoins(n, d))

d = [50, 25, 20, 10, 5, 1]
n = 40

print(coins(n, d))
print(dpcoins(n, d))


d = [50, 25, 20, 10, 5, 1]
n = 87

# print(coins(n, d))
print(dpcoins(n, d))

