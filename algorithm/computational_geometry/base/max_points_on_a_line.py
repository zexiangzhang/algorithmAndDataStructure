"""
 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上
 example 1:
     输入: [[1,1],[2,2],[3,3]]
     输出: 3
     解释：
     ^
     |           o
     |       o
     |   o
     o-———————————————>

 example 2:
     输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
     输出: 4
     解释：
     ^  o
     |     o      o
     |        o
     |   o       o
     o-———————————————-->
"""
from typing import List
from collections import *


# 一条直线可以用y=kx+b来表示，如果点(x,y)满足上式则表明(x,y)在直线y=kx+by上
# 这样的话，对于points中的每个点，可以分别计算其和其它每个点形成的直线，而这些直线重复数量的最大值就是经过该点的直线所能经过的最大点数
# 可以用kk作为键值的hashmap来记录这些数据出现的次数
# 最后在hashmap中取最大的值加一就是就是经过该点的直线所能经过的最大点数
# 如果存在重复点的情况，比如[[0,0],[0,0]]，代码中需要判断两点坐标是否相同，如果相同那么结果直接+1就不需要更新hashmap了
# 如果两点可能在一条竖线上，这样就无法计算出kk，因为a[1]-b[1]=0a[1]−b[1]=0，数不能被0除，要特殊处理
def max_points(points: List[List[int]]) -> int:
    def calc(point, i):
        hashmap = defaultdict(int)
        same = 0
        for j in range(len(point)):
            if j != i:
                if point[i] == point[j]:
                    same += 1
                    continue
                if point[i][1] - point[j][1] == 0:
                    k = float('Inf')
                else:
                    k = (point[i][0] - point[j][0]) / (point[i][1] - point[j][1])
                hashmap[k] += 1
        return 1 + same + (max(hashmap.values()) if hashmap else 0)

    res = 0
    if len(points) == 1:
        return 1
    for i in range(len(points)):
        res = max(res, calc(points, i))
    return res


if __name__ == '__main__':
    print(max_points([[1, 1], [2, 2], [3, 3]]))
    print(max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))