"""
    给定一个排序数组，需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
    example 1:
     输入: nums = [1,1,2]
     输出: 2
    example 2:
     输入: [0,0,1,1,1,2,2,3,3,4]
     输出: 5
"""
from typing import List


# 快慢指针的基本应用
# 数组是有序的，则重复的元素一定是相邻的
# 定义两个指针：fast_pointer和slow_pointer
# 让快指针先走，然后会发生两种情况：
#       1、nums[fast_pointer] == nums[slow_pointer],此时让快指针继续往前移动即可，即fast_pointer += 1
#       2、nums[fast] != nums[slow],此时有两个操作：
#           a、慢指针往前移动，即slow_pointer += 1
#           b、将慢指针所在位置的值用快指针所在位置的值覆盖，即nums[slow_pointer] = nums[fast_pointer]
# 最后0 -> slow_pointer范围内的元素就是原数组内没有重复的元素集
def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    if not nums:
        return 0
    fast_pointer, slow_pointer = 0, 0
    while fast_pointer < len(nums):
        if nums[fast_pointer] == nums[slow_pointer]:
            fast_pointer += 1
        else:
            slow_pointer += 1
            nums[slow_pointer] = nums[fast_pointer]
    return slow_pointer + 1


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates_from_sorted_array(nums1))
    print(remove_duplicates_from_sorted_array(nums2))