"""
 给定一个整数数组，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素
 example :
    输入: [1,2,1,3,2,5]
    输出: [3,5]
"""
from collections import Counter
from typing import List


# 定义一个数组，遍历列表，如果数组中存在该元素就remove，否则append,最后得到的数组就是出现次数为1的元素数组
def single_number_03_arr(numbers: List[int]) -> List[int]:
    result = []
    for number in numbers:
        if number in result:
            result.remove(number)
        else:
            result.append(number)
    return result


# 用Counter统计每个元素出现的次数，然后收集出现次数为1的元素
def single_number_03_counter(numbers: List[int]) -> List[int]:
    return [key for key, value in dict(Counter(numbers)).items() if value == 1]


# 用哈希表记录元素的出现次数，然后收集出现次数为1的元素
def single_number_03_hashmap(numbers: List[int]) -> List[int]:
    hash_map = {}
    for i in numbers:
        hash_map[i] = hash_map.get(i, 0) + 1
    result = []
    for i in numbers:
        if hash_map[i] == 1:
            result.append(i)
    return result


if __name__ == '__main__':
    input_arr = [1, 2, 1, 3, 2, 5]
    print(single_number_03_arr(input_arr))
    print(single_number_03_counter(input_arr))
    print(single_number_03_hashmap(input_arr))
