"""
    给定一个含有n个正数的数组x
    从点(0,0)开始，先向北移动x[0]米，然后向西移动x[1]米，向南移动x[2]米，向东移动x[3]米，持续移动。也就是说，每次移动后方位会发生逆时针变化
    扫描走过的路劲是否交叉
    example 1:
     输入: [2,1,1,2]
     输出: true
    example 2:
     输入: [1,2,3,4]
     输出: false
    example 3:
     输入: [1,1,1,1]
     输出: true
"""
from typing import List


# 画图分析，当数组长度 < 4时，不可能发生交叉
# 当数组长度 >= 4时，会出现相交：
# 第 4 条线段只可能与第 1 条线段交叉。
# 第 5 条线段只可能与第 2、1 条线段交叉。
# 第 6 条线段只可能与第 3、(2)、1 条线段交叉。
# 第 7 条线段只可能与第 4、(3)、2 条线段交叉（注意，不可能与第 1 条线段交叉，因为路径是逆时针的，此时线段 1 要么被围在内部，要么被抛在外部）
# ......
# 从上面分析可以看出，我们至多需要一个大小为 6 的滑动窗口，即可覆盖所有的交叉情况
# 滑动窗口每移动一步，我们都判断一次新进入窗口的线段与最前面三条线段的交叉关系
# 一个边界情况是，前4条、前5条线段虽不够6个窗格，但却有可能发生交叉，同样需要判断
def self_crossing(x: List[int]) -> bool:
    if len(x) < 4:
        return False
    a, b, c, (d, e, f) = 0, 0, 0, x[:3]
    for i in range(3, len(x)):
        a, b, c, d, e, f = b, c, d, e, f, x[i]
        if e < c - a and f >= d:
            return True
        if c - a <= e <= c and f >= (d if d - b < 0 else d - b):
            return True
    return False


if __name__ == '__main__':
    print(self_crossing([2, 1, 1, 2]))
    print(self_crossing([1, 2, 3, 4]))
    print(self_crossing([1, 1, 1, 1]))