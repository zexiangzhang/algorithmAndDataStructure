"""
 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素
 example 1:
    输入: [2,2,3,2]
    输出: 3
 example 2:
    输入: [0,1,0,1,0,1,99]
    输出: 99
"""
from collections import Counter
from typing import List


# 数学方法
# 数组1：[a, a, a, b, c, c, c], 数组2：[a, a, a, b, b, b, c, c, c]
# 能看出： 数组2的和 - 数组1的和 = 2b
# 也就是：2b = 3 * (a + b + c) - (a + a + a + b + c + c + c)
# 翻译一下就是： 把原数组去重后的值 * 3 再减去 原数组的和  = 要找的元素 * 2
def single_number_method_02_math(numbers: List[int]) -> int:
    return (sum(set(numbers)) * 3 - sum(numbers)) // 2


# 用Counter统计每个元素出现的次数，出现次数为1的就是要找的元素
def single_number_method_02_hashmap(numbers: List[int]) -> int:
    hash_map = Counter(numbers)
    for key in hash_map.keys():
        if hash_map[key] == 1:
            return key


if __name__ == '__main__':
    first_input = [2, 2, 3, 2]
    second_input = [0, 1, 0, 1, 0, 1, 99]

    print(single_number_method_02_math(first_input))
    print(single_number_method_02_math(second_input))

    print(single_number_method_02_hashmap(first_input))
    print(single_number_method_02_hashmap(second_input))