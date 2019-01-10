import math


def cal_sum(x1, y1, x2, y2):
    return a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]


def cut(n, x1, y1, x2, y2):
    m = 10000000
    if res[n][x1][y1][x2][y2] != -1:
        return res[n][x1][y1][x2][y2]
    if n == 1:
        t = cal_sum(x1, y1, x2, y2)
        res[n][x1][y1][x2][y2] = t * t
        return t * t

    for a in range(x1, x2):
        c = cal_sum(a + 1, y1, x2, y2)
        d = cal_sum(x1, y1, a, y2)
        t = min(cut(n - 1, x1, y1, a, y2) + c * c,
                cut(n - 1, a + 1, y1, x2, y2) + d * d)
        if m > t:
            m = t

    for b in range(y1, y2):
        c = cal_sum(x1, b + 1, x2, y2)
        d = cal_sum(x1, y1, x2, b)
        t = min(cut(n - 1, x1, y1, x2, b) + c * c,
                cut(n - 1, x1, b + 1, x2, y2) + d * d)
        if m > t:
            m = t

    res[n][x1][y1][x2][y2] = m
    return m


a = [
    [1,  2,  3,  4,  5,  6,  7,  8],
    [10, 11, 22, 2,  64, 21, 66, 0],
    [3,  64, 45, 65, 6,  52, 23, 43],
    [3,  23, 64, 43, 0,  12, 5,  0],
    [24, 54, 12, 75, 23, 3,  12, 9],
    [42, 23, 75, 53, 22, 34, 5,  10],
    [54, 33, 34, 33, 0,  75, 0,  0],
    [13, 23, 64, 65, 0,  64, 12, 66]
]

n = 10

resli1 = [-1 for x in range(0, 8)]
resli2 = [resli1 for x in range(0, 8)]
resli3 = [resli2 for x in range(0, 8)]
resli4 = [resli3 for x in range(0, 8)]
res = [resli4 for x in range(0, n + 1)]

result = n * cut(n, 0, 0, 7, 7) - a[7][7]**2
print(math.sqrt(abs(result) / (n * n)))
