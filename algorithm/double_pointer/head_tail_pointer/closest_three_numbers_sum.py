"""
    给定一个包括n个整数的数组nums和一个目标值target
    找出nums中的三个整数，使得它们的和与target最接近
    返回这三个数的和
    example 1:
     输入: nums = [-1,2,1,-4], target = 1
     输出: 2
"""

from typing import List, Union


# 首先进行初步判断，对于数组长度n，如果数组为空或者数组长度小于3，返回空值
# 然后对数组进行排序，声明result为最接近target的值
# 遍历排序后的数组：
#       1、对于重复元素，跳过，避免重复计算
#       2、令左指针left = i + 1,右指针right = n - 1,当left < right时，执行循环：
#           a、定义sum值，sum = nums[i] + nums[left] + nums[right]，如果sum = target，则直接返回target
#           b、如果sum - target的绝对值 < result - target的绝对值，说明sum更接近目标值，更新result
#           c、若sum-target大于0，说明nums[right]太大，right左移
#           d、若sum-target小于0，说明nums[left]太小，left右移
def closest_three_numbers_sum(nums: List[int], target: int) -> Union[None, int, float]:
    length = len(nums)
    if not nums or length < 3:
        return None
    result = float('inf')
    nums.sort()
    for i in range(length):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == target:
                return target
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum - target < 0:
                left += 1
            else:
                right -= 1
    return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(closest_three_numbers_sum(nums=nums, target=target))