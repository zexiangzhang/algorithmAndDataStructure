"""
    峰值元素是指其值大于左右相邻值的元素
    给你一个输入数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可
    example 1:
     输入: nums = [1,2,3,1]
     输出: 2
     解释：3是峰值元素，你的函数应该返回其索引2
    example 2:
     输入: nums = [1,2,1,3,5,6,4]
     输出: 1 或 5
     解释：你的函数可以返回索引1，其峰值元素为2；或者返回索引5，其峰值元素为6
"""
from typing import List


# 初试化左指针left=0，右指针right=n-1
# 循环条件left < right，进入循环：
#       1、mid = (left + right) // 2
#       2、若nums[mid]>nums[mid+1]，说明左侧的值更大，则nums[mid]或者左侧一定存在峰值,令right = mid，因为mid自身也可能是峰值
#       3、否则，说明右侧的值更大，则右侧一定存在一个峰值,令left = mid+1
# 返回left
def find_peak_element(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(find_peak_element([1, 2, 3, 1]))
    print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))