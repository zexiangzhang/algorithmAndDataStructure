"""
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素
    example 1:
     输入: [1,3,5,6], 5
     输出: 2
    example 2:
     输入: [1,3,5,6], 2
     输出: 1
    example 3:
     输入: [1,3,5,6], 7
     输出: 4
    example 4:
     输入: [1,3,5,6], 0
     输出: 0
"""
from typing import List


# 首先设置两个变量left,right分别记录列表两边的索引
# 然后判断左边的索引是否小于等于右边的索引，如果是的话就先计算出中间索引midpoint，中间索引由左右两边的索引整除2计算。
# 然后有三种情况：
#   第一种情况如果target小于中间索引在nums中的数的话，表明target在中间索引的左边，所以将右边索引值设置为中间索引-1。
#   第二种情况，如果target大于中间索引在nums中的数的话，表面target在中间索引的右边，那么左边索引设置为中间索引+1.
#   第三种情况就是target等于中间索引在nums中的值，自然返回中间索引
# 那么如果nums中没有找到target的话，就返回左边索引
def search_insert_position(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target < nums[midpoint]:
            right = midpoint - 1
        elif target > nums[midpoint]:
            left = midpoint + 1
        else:
            return midpoint
    return left


# 暴力解决问题
# 不管这个数在不在数组里面，直接append
# 然后再排序
# 最后返回查找的index（index方法默认返回的是该元素第一次出现的index）
def search_insert_position_by_violence(nums: List[int], target: int) -> int:
    nums.append(target)
    nums.sort()
    return nums.index(target)


if __name__ == '__main__':
    print(search_insert_position([1, 3, 5, 6], 5))
    print(search_insert_position([1, 3, 5, 6], 2))
    print(search_insert_position([1, 3, 5, 6], 7))
    print(search_insert_position([1, 3, 5, 6], 0))

    print(search_insert_position_by_violence([1, 3, 5, 6], 5))
    print(search_insert_position_by_violence([1, 3, 5, 6], 2))
    print(search_insert_position_by_violence([1, 3, 5, 6], 7))
    print(search_insert_position_by_violence([1, 3, 5, 6], 0))