"""
 给定一个整数数组，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素
 example :
    输入: [1,2,1,3,2,5]
    输出: [3,5]
"""
from typing import List
from collections import Counter


def single_number_03_01(numbers: List[int]) -> List[int]:
    return [key for key, value in dict(Counter(numbers)).items() if value == 1]


def single_number_03_02(numbers: List[int]) -> List[int]:
    number_dict = {}
    for i in numbers:
        number_dict[i] = number_dict.get(i, 0) + 1
    result = []
    for i in numbers:
        if number_dict[i] == 1:
            result.append(i)
    return result


def single_number_03_03(numbers: List[int]) -> List[int]:
    bit_mask = 0
    for number in numbers:
        bit_mask ^= number
    diff = bit_mask & (-bit_mask)
    x = 0
    for number in numbers:
        if number & diff:
            x ^= number
    return [x, bit_mask ^ x]


if __name__ == '__main__':
    input_arr = [1, 2, 1, 3, 2, 5]
    print(single_number_03_01(input_arr))
    print(single_number_03_02(input_arr))
    print(single_number_03_03(input_arr))
