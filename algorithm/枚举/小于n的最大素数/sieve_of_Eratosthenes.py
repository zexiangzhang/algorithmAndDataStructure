# 埃拉托斯特尼筛法
import math

n = 100000

a = {i: True for i in range(1, n + 1)}

for x in range(2, int(math.sqrt(n)) + 1):
    for y in range(2, int(n / x) + 1):
        if x * y <= n:
            a[y * x] = False

last = 2

for key, value in a.items():
    if value:
        last = key

print(last)  # 0.28s user 0.01s system 98% cpu 0.292 total
