"""
 给定一个大小为n的整数数组，找出其中所有出现超过[n/3]次的元素
 example 1:
     输入: [3,2,3]
     输出: [3]
 example 2:
     输入: [1]
     输出: [1]
example 2:
     输入: [1,1,1,3,3,2,2,2]
     输出: [1,2]
"""
from typing import List


# 需要返回出现次数超过n/3次的元素，可知最多有两个这样的元素
# 假设这两个元素分别为a和b，会出现以下三种情况：
# 1): a,b均超过1/3
# 2): a,b中有一个超过
# 3): a,b中没有一个超过
def majority_element(nums: List[int]) -> List[int]:
    a, b, count_a, count_b = 0, 0, 0, 0
    res = []
    for i in nums:
        if a == i:
            count_a += 1
            continue
        if b == i:
            count_b += 1
            continue
        if count_a == 0:
            a = i
            count_a = 1
            continue
        if count_b == 0:
            b = i
            count_b = 1
            continue
        count_a -= 1
        count_b -= 1
    count_a, count_b = 0, 0
    for j in nums:
        if j == a:
            count_a += 1
        elif j == b:
            count_b += 1
    if count_a > len(nums) / 3:
        res.append(a)
    if count_b > len(nums) / 3:
        res.append(b)
    return res


if __name__ == '__main__':
    print(majority_element([3, 2, 3]))
    print(majority_element([1]))
    print(majority_element([1, 1, 1, 3, 3, 2, 2, 2]))