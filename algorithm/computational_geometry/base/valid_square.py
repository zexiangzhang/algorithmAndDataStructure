"""
    给定二维空间中四点的坐标，返回四点是否可以构造一个正方形
    一个点的坐标（x，y）由一个有两个整数的整数数组表示
    example 1:
     输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
     输出: True
"""
from typing import List


# 正方形的定义是，四边相等，对角线相等
def valid_square(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    pl = [p1, p2, p3, p4]
    dist = []
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            item = (pl[i][1] - pl[j][1]) ** 2 + (pl[i][0] - pl[j][0]) ** 2
            dist.append(item)
    dist.sort()
    return True if dist[0] == dist[3] != 0 and dist[4] == dist[5] else False


if __name__ == '__main__':
    print(valid_square(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))

