"""
 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
 example 1:
    输入: [2,2,1]
    输出: 1
 example 2:
    输入: [4,1,2,1,2]
    输出: 4
"""
from typing import List


def single_number_01(numbers: List[int]) -> int:
    result = 0
    for number in numbers:
        result ^= number
    return result


if __name__ == '__main__':
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))