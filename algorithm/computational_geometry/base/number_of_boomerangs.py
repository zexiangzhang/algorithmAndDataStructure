"""
    给定平面上n对互不相同的点points，其中points[i] = [xi, yi]
    回旋镖是由点(i, j, k)表示的元组，其中i和j之间的距离和i和k之间的距离相等
    返回平面上所有回旋镖的数量
    example 1:
     输入: points = [[0,0],[1,0],[2,0]]
     输出: 2
     解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

    example 2:
     输入: points = [[1,1],[2,2],[3,3]]
     输出: 2

    example 3:
     输入: points = [[1,1]]
     输出: 0
"""
from typing import List


# 组成回旋镖的条件是这样：
#   1、先找到一个点
#   2、如果对这个点来说，存在两个点，它们到回旋镖的距离一样，那么这三个点组成一个回旋镖
#   3、这两个点交换位置也算另一种回旋镖
# 每次固定一个点，使用哈希表存储其他点到这个点的距离，如果存在记录次数，回旋镖的数量应为次数*（次数-1）
def number_of_boomerangs(points: [List[List[int]]]) -> int:
    res = 0
    for point in points:
        dicts = {}
        for j in points:
            if point == j:
                continue
            dicts[(point[0] - j[0]) ** 2 + (point[1] - j[1]) ** 2] \
                = dicts.get((point[0] - j[0]) ** 2 + (point[1] - j[1]) ** 2, 0) + 1
        for i in dicts.values():
            res += i * (i - 1)
    return res


if __name__ == '__main__':
    print(number_of_boomerangs([[0, 0], [1, 0], [2, 0]]))
    print(number_of_boomerangs([[1, 1], [2, 2], [3, 3]]))
    print(number_of_boomerangs([[1, 1]]))