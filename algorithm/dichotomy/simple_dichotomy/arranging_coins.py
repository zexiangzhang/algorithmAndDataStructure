"""
    你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
    给定一个数字 n，找出可形成完整阶梯行的总行数
    example 1:
     输入: n = 5
     输出: 2
    example 2:
     输入: n = 8
     输出: 3
"""


# 二分查找
#   1、设立左右边界分别为0和n，每次取中间值mid为行数，将mid行总数和n对比
#   2、和n相等时直接return mid，小于n时，左边界left=mid+1 ，大于n时，右边界right = mid-1
#   3、在不断的判定后如果硬币不能刚好分完，那么left会等于能分的最多行数+1，right会等于总量超出n的最小行数-1，即为能分的最多行数，return right
def arranging_coins(n: int) -> int:
    left, right = 0, n
    while True:
        if left > right:
            return right
        mid = (left + right) // 2
        count = (1 + mid) * mid / 2
        if count == n:
            return mid
        elif count < n:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    print(arranging_coins(5))
    print(arranging_coins(8))