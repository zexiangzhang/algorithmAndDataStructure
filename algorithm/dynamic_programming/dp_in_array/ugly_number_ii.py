"""
   编写一个程序，找出第n个丑数(丑数就是只包含质因数 2, 3, 5 的正整数)
    example 1:
     输入: 10
     输出: 12（1, 2, 3, 4, 5, 6, 8, 9, 10, 12是前10个丑数）
"""


# 很容易想到的方法是：
#       从1起检验每个数是否为丑数，直到找到n个丑数为止
#       但是随着n的增大，绝大部分数字都不是丑数，枚举的效率非常低
# 因此，换个角度思考，如果我们只生成丑数，且生成n个，这道题就迎刃而解
# 生成丑数的规律：如果已知丑数ugly_number，那么ugly_number * 2，ugly_number * 3和ugly_number * 5也都是丑数
# 用一个有序数组dp记录前n个丑数
# 三个指针pointer_2，pointer_3和pointer_5指向dp中的元素
# 此时最小的丑数只可能出现在dp[pointer_2]的2倍、dp[pointer_3]的3倍和dp[pointer_5]的5倍三者中间
# 通过移动三个指针，就能保证生成的丑数是有序的
# 初始化数组dp和三个指针pointer_2，pointer_3和pointer_5
# dp[0] = 1，表示最小的丑数为1。三个指针都指向dp[0]
# 重复以下步骤n次，dp[i]表示第i + 1小的丑数：
#       比较2 * dp[pointer_2], 3 * dp[pointer_3], 5 * dp[pointer_5]三者大小，令dp[i]为其中的最小值
#       如果dp[i] == 2 * dp[pointer_2]，pointer_2指针后移一位
#       如果dp[i] == 3 * dp[pointer_3]，pointer_3指针后移一位
#       如果dp[i] == 2 * dp[pointer_5]，pointer_5指针后移一位
# dp[n - 1]即为第n小的丑数，返回
def ugly_number(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    pointer_2, pointer_3, pointer_5 = 0, 0, 0
    for i in range(1, n):
        dp[i] = min(2 * dp[pointer_2], 3 * dp[pointer_3], 5 * dp[pointer_5])
        if dp[i] == 2 * dp[pointer_2]:
            pointer_2 += 1
        if dp[i] == 3 * dp[pointer_3]:
            pointer_3 += 1
        if dp[i] == 5 * dp[pointer_5]:
            pointer_5 += 1
    return dp[n - 1]


if __name__ == '__main__':
    print(ugly_number(10))
