"""
   给定一个数组 nums和一个值val，需要原地移除所有数值等于val的元素，并返回移除后数组的新长度
    example 1:
     输入: nums = [3,2,2,3], val = 3
     输出: 2
    example 2:
     输入: nums = [0,1,2,2,3,0,4,2], val = 2
     输出: 5
"""
from typing import List


# 思路简单描述如下：
#       定义双指针fast_pointer和slow_pointer
#       让快指针先走，当且仅当nums[fast_pointer] != val的时候，将慢指针所在位置的值用快指针所在位置的值覆盖，慢指针往前移动一位
# 最终0 -> slower_pointer区间的值就是目标集合，slow_pointer即为目标值
def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0
    fast_pointer, slow_pointer = 0, 0
    while fast_pointer < len(nums):
        if nums[fast_pointer] != val:
            nums[slow_pointer] = nums[fast_pointer]
            slow_pointer += 1
        fast_pointer += 1
    return slow_pointer


if __name__ == '__main__':
    nums1 = [3, 2, 2, 3]
    val1 = 3
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(remove_element(nums=nums1, val=val1))
    print(remove_element(nums=nums2, val=val2))