"""
 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素
 example 1:
    输入: [2,2,3,2]
    输出: 3
 example 2:
    输入: [0,1,0,1,0,1,99]
    输出: 99
"""
from typing import List
from collections import Counter


def single_number_method_02_01(numbers: List[int]) -> int:
    return (3 * sum(set(numbers)) - sum(numbers)) // 2


def single_number_method_02_02(numbers: List[int]) -> int:
    hash_map = Counter(numbers)
    for key in hash_map.keys():
        if hash_map[key] == 1:
            return key


def single_number_method_02_03(numbers: List[int]) -> int:
    seen_once = seen_twice = 0
    for number in numbers:
        seen_once = ~seen_twice & (seen_once ^ number)
        seen_twice = ~seen_once & (seen_twice ^ number)
    return seen_once


if __name__ == '__main__':
    first_input = [2, 2, 3, 2]
    second_input = [0, 1, 0, 1, 0, 1, 99]

    print(single_number_method_02_01(first_input))
    print(single_number_method_02_01(second_input))

    print(single_number_method_02_02(first_input))
    print(single_number_method_02_02(second_input))

    print(single_number_method_02_03(first_input))
    print(single_number_method_02_03(second_input))