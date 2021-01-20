"""
 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）
 example 1:
     输入: [5,7]
     输出: 4

 example 2:
     输入: [0,1]
     输出: 0
"""


# 统计两个数二进制表示的公共前缀
# 因为假设两个数在第i位前面都相同,第i位一个为0,一个为1,那么这两个数之间一定存在一个数,这个数得第i位为1,且后面的都是0
# 这样与之后i位以及之后就都是零了,所以求两个数的公共前缀即可，通过两个数不断右移，直到两个数相等，再左移对应的位数
def range_bitwise_and(m: int, n: int) -> int:
    temp = 0
    while m < n:
        m = m >> 1
        n = n >> 1
        temp += 1
    return m << temp


if __name__ == '__main__':
    print(range_bitwise_and(5, 7))
    print(range_bitwise_and(0, 1))