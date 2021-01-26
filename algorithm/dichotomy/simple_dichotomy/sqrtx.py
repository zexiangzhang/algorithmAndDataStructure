"""
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去
    example 1:
     输入: 4
     输出: 2
    example 2:
     输入: n = 8
     输出: 2
     说明: 8 的平方根是 2.82842...,由于返回类型是整数，小数部分将被舍去。
"""


# 二分查找
# 使用二分查找，暂时不考虑整数部分，直接带小数部分进行二分查找
# 注意一点，最后判断其整数部分，可以二分到left和right的整数部分一致，这时x的平方根肯定在这两个数之间，这是返回left或者right的整数部分即可
def my_sqrt(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) / 2
        if mid ** 2 == x:
            return int(mid)
        if mid ** 2 > x:
            right = mid
        else:
            left = mid
        if int(left) == int(right):
            return int(left)


if __name__ == '__main__':
    print(my_sqrt(4))
    print(my_sqrt(8))