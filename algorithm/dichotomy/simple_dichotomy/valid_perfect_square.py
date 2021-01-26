"""
    给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False
    example 1:
     输入: 16
     输出: True
    example 2:
     输入: 14
     输出: false
"""


# 二分法的基本运用
def valid_perfect_square(num: int) -> bool:
    left, right = 1, num
    while left < right:
        mid = (left + right) // 2
        if mid * mid < num:
            left = mid + 1
        else:
            right = mid
    return left * left == num


if __name__ == '__main__':
    print(valid_perfect_square(16))
    print(valid_perfect_square(14))