"""
 不使用运算符+和-，计算两整数a、b之和
 example 1:
     输入: a = 1, b = 2
     输出: 3

 example 2:
     输入: a = -2, b = 3
     输出: 1
"""


# a^b异或^运算是没有进位的加，比如 1 0 ^ 0 1 = 1 1
# a&b与&运算后的结果左移一位可以获得进位的值，比如01 & 01 = 01，01 << 1 = 10 与运算后左移一位拿到进位的值10
# 此时 (a^b) + (a&b)<< 1 即累加后的结果,原理即无进位的值+进位的值等于一个数
# 进位为0时，计算结束
# python整数类型为Unifying Long Integers,无限长整数类型
# 因此相较于其他语言的代码,python代码需要一些其他的判断
def get_sum(a: int, b: int) -> int:
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    while b:
        carry = a & b
        a ^= b
        b = (carry << 1) & 0xFFFFFFFF
    return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


if __name__ == '__main__':
    print(get_sum(1, 2))
    print(get_sum(-2, 3))