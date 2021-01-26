"""
 统计所有小于非负整数n的质数的数量
 example 1:
     输入: n = 10
     输出: 4
     解释：小于10的质数一共有4个,它们是2,3,5,7
 example 2:
     输入: n = 0
     输出: 0
  example 3:
     输入: n = 1
     输出: 0
"""


# 假设一个数i为质数，那么此时大于i且是i的倍数的数一定不是质数，例如2i，3i...
# 应该从i * i开始，而不是 2 * i2∗i 开始
# 因为对于每个数i来说，枚举是从小到大的，此时前面数字的倍数都已经进行了标记
# 对于i 而言，2∗i 也肯定会被在枚举数字2时进行标记，[2, i)区间的数同理
def count_primes(n: int) -> int:
    is_prime = [1] * n
    count = 0
    for i in range(2, n):
        if is_prime[i]:
            count += 1
            for j in range(i * i, n, i):
                is_prime[j] = 0

    return count


if __name__ == '__main__':
    print(count_primes(10))
    print(count_primes(0))
    print(count_primes(1))