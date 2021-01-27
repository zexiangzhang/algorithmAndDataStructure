"""
    给定一个按照升序排列的整数数组nums，和一个目标值target。找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target，返回[-1, -1]
    example 1:
     输入: nums = [5,7,7,8,8,10], target = 8
     输出: [3,4]
    example 2:
     输入: nums = [5,7,7,8,8,10], target = 6
     输出: [-1,-1]
    example 3:
     输入: nums = [], target = 0
     输出: [-1,-1]
"""
from typing import List


# 直观的思路肯定是从前往后遍历一遍，用两个变量记录第一次和最后一次遇见target 的下标，但这个方法的时间复杂度为O(n)，没有利用到数组升序排列的条件
# 由于数组已经排序，因此整个数组是单调递增的，我们可以利用二分法来加速查找的过程
# 考虑target开始和结束位置，其实我们要找的就是数组中[第一个等于target的位置](left_index)和[第一个大于target的位置减一](right_index)
# 二分查找中，left_index即为在数组中寻找第一个大于等于target的下标，right_index即为在数组中寻找第一个大于target的下标，然后将下标减一
# 两者的判断条件不同，为了代码的复用，我们定义search_target(nums, target)表示在nums数组中二分查找target的位置
# 在search_target方法中，二分后，nums[mid] >= target时查找right_index,反之查找left_index
# 因为target可能不存在数组中，因此我们需要重新校验我们得到的两个下标left_index和right_index，看是否符合条件
# 如果符合条件就返回[left_index,right_index]，不符合就返回 [-1,-1]
def search(nums: List[int], target: int) -> List[int]:
    left_index = search_target(nums, target)
    right_index = search_target(nums, target + 1)
    if left_index == len(nums) or nums[left_index] != target:
        return [-1, -1]
    else:
        return [left_index, right_index - 1]


def search_target(nums, target):
    left_index, right_index = 0, len(nums) -1
    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        if nums[mid] >= target:
            right_index = mid - 1
        else:
            left_index = mid + 1
    return left_index


if __name__ == '__main__':
    print(search(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(search(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(search(nums=[], target=0))