import time
import matplotlib.pyplot as plt
from numpy import mean


def timeit(func, args, n=100):
    times = []
    for arg in args:
        start = time.time()
        for _ in range(n):
            func(arg)
        end = time.time()
        times.append((end - start) / n)
    print(f"Elapsed time: {mean(times)} seconds")
    return times

# Best implementation O(n)


def bestfibo(n):
    t1, t2 = 0, 1
    for _ in range(n):
        t1, t2 = t2, t1 + t2

    return t1


print(bestfibo(20))

# Bad implementation of fibonacci O(2^n)


def badfibo(n):
    if n < 2:
        return n
    return badfibo(n - 1) + badfibo(n - 2)


print(badfibo(20))

# Dynamic programming fibonacci O(n)
# top down


def dptdfibo(n):
    t = [0] * (n + 1)
    t[0] = 0
    t[1] = 1
    for i in range(2, n + 1):
        t[i] = t[i - 1] + t[i - 2]

    return t[n]


print(dptdfibo(20))

# bottom up


def dpbufibo(n):
    t = [0] * (n + 1)
    t[0] = 0
    t[1] = 1

    def f(i):
        if i < 2:
            return
        f(i - 1)
        t[i] = t[i - 1] + t[i - 2]

    f(n)
    return t[n]


print(dpbufibo(20))


def dpbu2fibo(n):
    t = [-1] * (n + 1)
    t[0] = 0
    t[1] = 1

    def f(i):
        if i < 2:
            return
        if t[i - 1] == -1:
            f(i - 1)
        if t[i - 2] == -1:
            f(i - 2)

        t[i] = t[i - 1] + t[i - 2]

    f(n)
    return t[n]


print(dpbu2fibo(20))


plt.subplots(figsize=(15, 3))
m = 25
args = list(range(1, 30))
data = timeit(bestfibo, args, m)
plt.subplot(1, 5, 1)
plt.plot(args, data)
data = timeit(badfibo, args, m)
plt.subplot(1, 5, 2)
plt.plot(args, data)
data = timeit(dptdfibo, args, m)
plt.subplot(1, 5, 3)
plt.plot(args, data)
data = timeit(dpbufibo, args, m)
plt.subplot(1, 5, 4)
plt.plot(args, data)
data = timeit(dpbu2fibo, args, m)
plt.subplot(1, 5, 5)
plt.plot(args, data)

plt.savefig('fibo.png')

