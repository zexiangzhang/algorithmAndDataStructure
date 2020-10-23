# 小于n的最大素数（质数）

### 常规筛选
n = 100000

prime_numbers = [2]

if n <= 2:
    print(2)
else:
    for x in range(3, n, 2):
        for y in prime_numbers:
            if x % y == 0:
                break
        else:
            prime_numbers.append(x)

print(prime_numbers.pop())  # 5.90s user 0.01s system 99% cpu 5.908 total

# 埃拉托斯特尼筛选
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
