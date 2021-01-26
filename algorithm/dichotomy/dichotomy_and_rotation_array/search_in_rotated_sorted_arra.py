"""
    升序排列的整数数组nums在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为[4,5,6,7,0,1,2] ）。
    请你在数组中搜索target ，如果数组中存在这个目标值，则返回它的索引，否则返回-1
    example 1:
     输入: nums = [4,5,6,7,0,1,2], target = 0
     输出: 4
    example 2:
     输入: nums = [4,5,6,7,0,1,2], target = 3
     输出: -1
    example 3:
     输入: nums = [1], target = 0
     输出: -1
"""
from typing import List


# 数组从任意位置劈开后，至少有一半是有序的
# 基于这个条件，我们可以先找到哪一段是有序的 (只要判断端点即可)
# 然后看 target 在不在这一段里：
#       1、如果在，那么就把另一半丢弃
#       2、如果不在，那么就把这一段丢弃
def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
    print(search([1], 0))