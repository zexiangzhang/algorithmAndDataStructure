# 题目： 青蛙穿越稻田。 每只青蛙每次跳的步长相同， 不同青蛙步长不一定相等，跳的方向不一定相同，跳的总距离也就不一定相同。 寻找危害最大的青蛙。
#       稻田是一个长方形栅格，每个点上有一束稻子。
#       青蛙每次从一遍进入， 沿着直线从另一边跳出。
#       每次踩到的稻子必须大于3才算是完整路径。
#       假设稻田的面积是 6 x 7 的栅格。 输入踩倒图， 输出踩倒最多的路线于踩倒个数。
#       【1, 1， 1， 1， 1， 1， 1】
#       【0, 1， 0， 1， 0， 0， 0】
#       【1, 1， 1， 0， 1， 1， 1】
#       【1, 0， 1， 1， 1， 1， 1】
#       【1, 1， 1， 1， 1， 1， 1】
#       【0, 0， 0， 0， 0， 0， 0】
#        0表示踩倒。

# 思路： 任意选取两个作为开始跳的点。 求出步长
# 判断：
#     保证前一步长在稻田外。
#     能够算出不少于三个在稻田里面的点
#     最后一跳能够跳出稻田范围
# 排序后再枚举
a = [
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

# xy坐标， 列为x, 行为y
def get_all_points(lists, max_x, max_y):
    all_points = []
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            if lists[y][x]:
                all_points.append((x, y))
    return all_points


def sort_points(point, points):
    sortpoints = sorted(points, key=lambda p: (
        p[0] - point[0])**2 + (p[1] - point[1])**2)
    return sortpoints


def get_line_points(prevpoint, diff_x, diff_y, allpoints, results):
    nextpoint = (prevpoint[0] + diff_x, prevpoint[1] + diff_y)
    if nextpoint not in allpoints:
        if nextpoint[0] < 0 or nextpoint[0] > max_x or nextpoint[1] < 0 or nextpoint[1] > max_y:
            return results
        else:
            return
    results.append(nextpoint)
    return get_line_points(nextpoint, diff_x, diff_y, allpoints, results)


max_x = 6
max_y = 5
minstep = 3

allpoints = get_all_points(a, max_x, max_y)
allresults = []

for key, point1 in enumerate(allpoints[0:-1]):
    sortpoints = sort_points(point1, allpoints[key + 1:])
    for point2 in sortpoints:
        diff_x = point2[0] - point1[0]
        diff_y = point2[1] - point1[1]
        if 0 < point1[0] - diff_x < max_x and 0 < point1[1] - diff_y < max_y:
            continue

        minsteppoints_x = (minstep - 2) * diff_x + point2[0]
        minsteppoints_y = (minstep - 2) * diff_y + point2[1]
        if minsteppoints_x < 0 or minsteppoints_x > max_x or minsteppoints_y < 0 or minsteppoints_y > max_y:
            break
        results = get_line_points(
            point2, diff_x, diff_y, sortpoints, [point1, point2])
        if results:
            allresults.append(results)

max_num = 0
max_lines = []
for result in allresults:
    if len(result) > max_num:
        max_lines = [result]
        max_num = len(result)
    elif result[1] == max_num:
        max_lines.append(result)

print(max_num)
print(max_lines)
