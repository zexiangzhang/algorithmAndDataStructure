"""
   假设你正在爬楼梯,需要n阶你才能到达楼顶,每次你可以爬1或2个台阶
   你有多少种不同的方法可以爬到楼顶呢？
    example 1:
     输入: 2
     输出: 2
    example 2:
     输入: 3
     输出: 3
"""


# 当n = 1时，有1种方法爬到楼顶
# 当n = 2时，爬到楼顶有2种方法
# 爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
# 因为爬到n-1楼后，再爬1楼就能到达n楼
# 爬到n-2楼同理
# 因此只需初始化爬到1楼和爬到2楼分别有多少种方法，便可以推导出爬到n楼的方法
# 爬到n-1楼，再爬一楼就是n楼，换言之：爬到n-1楼到达n楼只有一种选择
# 而爬到n-2楼到达n楼有两种方法可以选择，但是，其中一种方法和前面的所述n-1楼重复，所以实际上，也是只有一种选择
# 因此爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
def climbing_stairs(n: int) -> int:
    if n < 3:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(climbing_stairs(2))
    print(climbing_stairs(3))
