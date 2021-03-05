"""
    给定一个包含n个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0
    请找出所有和为0且不重复的三元组
    example 1:
     输入: nums = [-1,0,1,2,-1,-4]
     输出: [[-1,-1,2],[-1,0,1]]
    example 2:
     输入: nums = []
     输出: []
    example 3:
     输入: nums = [0]
     输出: []
"""

from typing import List


# 首先进行初步判断，对于数组长度n，如果数组为空或者数组长度小于3，返回[]
# 然后对数组进行排序，排序的目的是对于排好序的数组，如果第一个元素大于零，则后面不可能有三个数加和等于0，直接返回[]
# 如果元素重复的话则直接跳过
# 令左指针left = i + 1，右指针right = n - 1，left < right时，执行循环：
#       1、当nums[i] + nums[left] + nums[right] = 0，执行循环
#          判断左界和右界是否和下一位置重复，去除重复解并同时将left, right移到下一位置，寻找新的解
#       2、若和大于0，说明 nums[right]太大，right左移
#       3、若和小于0，说明 nums[left]太小，left右移
def three_numbers_sum(nums: List[int]) -> List[List[int]]:
    answer = []
    length = len(nums)
    if not nums or length < 3:
        return answer
    nums.sort()
    for i in range(length):
        if nums[i] > 0:
            return answer
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left = left + 1
                while left < right and nums[right] == nums[right - 1]:
                    right = right - 1
                left = left + 1
                right = right - 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right = right - 1
            else:
                left = left + 1
    return answer


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = []
    nums3 = [0]
    print(three_numbers_sum(nums1))
    print(three_numbers_sum(nums2))
    print(three_numbers_sum(nums3))