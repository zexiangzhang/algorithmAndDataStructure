# 思路： 按边计算所有可能连接起来大于三的路线， 判断路线上的被踩的个数与相隔距离。
# x 思路错误
import math

a = [
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

# xy坐标， 列为x, 行为y


def get_all_points(lists):
    all_points = []
    for x in range(0, 7):
        for y in range(0, 6):
            if lists[y][x]:
                all_points.append((x, y))
    return all_points

# * 取出两点之间所有正整数点, 必须总个数大于等于三


def get_line_all_points(point1, point2):
    if point1 == point2:
        return
    line = [point1, point2]
    a = (point1[1] - point2[1]) / (point1[0] - point2[0])
    b = (point1[0] * point2[1] - point1[1] *
         point2[0]) / (point1[0] - point2[0])
    for x in range(0, 7):
        if (x != point1[0]) and (x != point2[0]):
            y = a * x + b
            if math.ceil(y) == int(y) and int(y) <= 5:
                line.append((x, int(y)))
    if (len(line) > 2):
        return line
    return

# 取出线路上的点, 必须大于三


def line_points(line, allpoints):
    linepoints = [p for p in line if p in allpoints]

    if len(linepoints) >= 3:
        return linepoints
    return

# * 取出线路上的距离相等的点


def same_length_points(points):
    points.sort(key=lambda p: p[0])
    num = len(points)
    for key, p in enumerate(points):
        s = (p[0] - points[key + 1][0])**2 + (p[1] - points[key + 1][1])**2
        for p2 in range(key + 1, num):
            pass

    if len(samelengthpoints) >= 3:
        return samelengthpoints
    return


# 四条边有六种出入方法
sides = {
    1: ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)),
    2: ((0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)),
    3: ((6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)),
    4: ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0))
}

allpoints = get_all_points(a)
all_results = []
for i, points in sides.items():
    for j in range(i + 1, 5):
        for point1 in points:
            for point2 in sides[j]:
                line = get_line_all_points(point1, point2)
                if line:
                    linepoints = line_points(line, allpoints)
                    if linepoints:
                        samelengthpoints = same_length_points(linepoints)
                        all_results.append(samelengthpoints)

max_num = 0
max_lines = []
for result in all_results:
    if len(result) > max_num:
        max_lines = [result]
        max_num = len(result)
    elif result[1] == max_num:
        max_lines.append(result)

print(max_num)
print(max_lines)
