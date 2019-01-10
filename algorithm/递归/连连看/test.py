def action(point1, point2, allpoints):
    if line(point1, point2, allpoints):
        print('ok find')
    else:
        print('no find')


def line(point1, point2, allpoints):
    if (touch_other_point(point1, point2)):
        return True
    x = point1[0]
    y = point1[1]
    for p in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if (0 <= p[0] <= 9) and (0 <= p[1] <= 8) and not allpoints[p[0]][p[1]]:
            allpoints[p[0]][p[1]] = 1
            if line(p, point2, allpoints):
                return True
    return False


def touch_other_point(point1, point2):
    if (point1[0], point1[1] - 1) == point2:
        return True
    if (point1[0], point1[1] + 1) == point2:
        return True
    if (point1[0] - 1, point1[1]) == point2:
        return True
    if (point1[0] + 1, point1[1]) == point2:
        return True
    return False


# 假设输入 8 x 7 的矩形 min(0, 0) max(8, 7)
test = [
    (1, 1, 1, 1, 1, 0, 0),  # 1
    (1, 0, 0, 1, 0, 0, 0),  # 2
    (1, 0, 1, 0, 1, 1, 1),  # 3
    (0, 0, 1, 0, 1, 1, 1),  # 4
    (1, 0, 0, 0, 0, 0, 1),  # 5
    (1, 1, 1, 0, 1, 0, 1),  # 6
    (1, 0, 0, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1)  # 8
]

# 假想四周有一圈全为空的框
test1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # *0

    [0,  1, 1, 1, 1, 1, 0, 0,  0],  # 1
    [0,  1, 0, 0, 1, 0, 0, 0,  0],  # 2
    [0,  1, 0, 1, 0, 1, 1, 1,  0],  # 3
    [0,  0, 0, 1, 0, 1, 1, 1,  0],  # 4
    [0,  1, 0, 0, 0, 0, 0, 1,  0],  # 5
    [0,  1, 1, 1, 0, 1, 0, 1,  0],  # 6
    [0,  1, 0, 0, 0, 0, 0, 0,  0],  # 7
    [0,  1, 1, 1, 1, 1, 1, 1,  0],  # 8

    [0, 0, 0, 0, 0, 0, 0, 0, 0]  # *9
]

input1 = ((2, 4), (5, 7))
input2 = ((1, 3), (8, 6))
input3 = ((3, 7), (6, 5))

action(input1[0], input1[1], test1)
action(input2[0], input2[1], test1)
action(input3[0], input3[1], test1)
