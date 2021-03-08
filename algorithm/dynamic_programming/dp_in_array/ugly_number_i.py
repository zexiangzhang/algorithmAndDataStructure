"""
   编写一个程序判断给定的数是否为丑数(丑数就是只包含质因数 2, 3, 5 的正整数)
    example 1:
     输入: 6
     输出: True（6 = 2 * 3）
    example 2:
     输入: 8
     输出: True（8 = 2 * 2 * 2）
    example 3:
     输入: 14
     输出: False（包含质因数7）
"""


# 丑数的质因数只包含[2,3,5]
# 因此如果该数是丑数，让这个数不断除以[2,3,5],最终结果肯定为1，否则就不是丑数
# 对于负数及0自然就不是丑数
def ugly_number(n: int) -> bool:
    if n <= 0:
        return False
    nums = [2, 3, 5]
    for i in nums:
        while n % i == 0:
            n //= i
    return n == 1


if __name__ == '__main__':
    print(ugly_number(6))
    print(ugly_number(8))
    print(ugly_number(14))
