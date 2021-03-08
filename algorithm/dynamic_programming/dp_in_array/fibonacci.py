"""
   斐波那契数，通常用F(n) 表示，形成的序列称为斐波那契数列
   该数列由0和1开始，后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0，F(1)= 1
    F(n) = F(n - 1) + F(n - 2)，其中 n > 1
    给定一个n ，请计算 F(n)
    example 1:
     输入: 2
     输出: 1
    example 2:
     输入: 3
     输出: 2
    example 3:
     输入: 4
     输出: 3
"""


# 递归
# 递归结束的地方为：F(0) = 0,F(1) = 1
# 递归关系式：F(n) = F(n-1) + F(n-2)
def fibonacci_recursion(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    # 根据python语法特性可简写成如下代码：
    # return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2) if n < 2 else n


# 动态规划
# 显然递归过程中，有F(n) = F(n-1) + F(n-2),且F(n-1) = F(n-2) + F(n-3),这里F(n-2)属于重复计算的部分
# 根据动态规划的思想，可以将已经出现计算好的结果保存下来，下一次计算之前，先去查一遍就行，不需要再重新计算
# 即：可以用数组记录下来所有小于n的fibonacci_dp(n)，在存储的结果中，只记录前两个结果即可，可以使用两个变量交替
def fibonacci_dp(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fibonacci_recursion(2))
    print(fibonacci_recursion(3))
    print(fibonacci_recursion(4))

    print(fibonacci_dp(2))
    print(fibonacci_dp(3))
    print(fibonacci_dp(4))