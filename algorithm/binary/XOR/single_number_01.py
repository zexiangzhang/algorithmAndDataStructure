"""
 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
 example 1:
    输入: [2,2,1]
    输出: 1
 example 2:
    输入: [4,1,2,1,2]
    输出: 4
"""
from functools import reduce
from typing import List


# 0和任何数异或的结果都是这个数本身。
# 相同的数异或的结果为0。
# 这个数列里面除了一个数只出现了一次，其他数都出现了两次。
# 异或运算满足交换律和结合律。
# 因此从前往后依次异或即可。最终结果就是那个只出现一次的数。
# 比如 1 xor 1 xor 2 xor 3 xor 2 = (1 xor 1) xor (2 xor 2) xor 3 = 0 xor 0 xor 3 = 0 xor 3 = 3
def single_number_01_xor(numbers: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, numbers)


# 因为目标数只出现一次，其余数出现两次，所以列表的每一个数删除两次，报错的就是要找的数
def single_number_01_try_exception(numbers: List[int]) -> int:
    while True:
        target_number = numbers[0]
        numbers.remove(target_number)
        try:
            numbers.remove(target_number)
        except ValueError:
            return target_number


if __name__ == '__main__':
    print(single_number_01_xor([2, 2, 1]))
    print(single_number_01_xor([4, 1, 2, 1, 2]))

    print(single_number_01_try_exception([2, 2, 1]))
    print(single_number_01_try_exception([4, 1, 2, 1, 2]))
