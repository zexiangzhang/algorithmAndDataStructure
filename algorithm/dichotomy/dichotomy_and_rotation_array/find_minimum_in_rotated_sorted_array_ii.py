"""
    假设按照升序排序的数组在预先未知的某个点上进行了旋转,例如，数组[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2]
    请找出其中最小的元素
    注意数组中可能存在重复的元素
    example 1:
     输入: [1,3,5]
     输出: 1
    example 2:
     输入: [2,2,2,0,1]
     输出: 0
"""
from typing import List


# 旋转排序数组nums可以被拆分为2个排序数组nums1,nums2,并且 nums1任一元素 >= nums2任一元素
# 因此，考虑二分法寻找此两数组的分界点nums[i](即第2个数组的首个元素)
# 设置left, right指针在nums数组两端，mid为每次二分的中点：
#       1、当 nums[mid] > nums[right]时，mid一定在第1个排序数组中，i一定满足 mid < i <= right，因此执行 left = mid + 1
#       2、当 nums[mid] < nums[right] 时，mid一定在第2个排序数组中，i一定满足 left < i <= mid，因此执行 right = mid
#       3、当 nums[mid] == nums[right] 时，由于数组的元素可重复，难以判断分界点i指针区间）
#           a.例如[1, 0, 1, 1, 1][1,0,1,1,1]和[1, 1, 1, 0, 1][1,1,1,0,1]
#             在 left = 0, right = 4, mid = 2 时，无法判断 mid在哪个排序数组中
#           b.我们采用 right = right - 1 解决此问题，证明：
#               1)、此操作不会使数组越界：因为迭代条件保证了 right > left >= 0
#               2)、此操作不会使最小值丢失：假设 nums[right]nums[right] 是最小值，有两种情况：
#                   i).若nums[right]是唯一最小值：那就不可能满足判断条件 nums[mid] == nums[right]
#                     因为 mid < right（left != right 且 mid = (left + right) // 2 向下取整）
#                   ii).若nums[right]不是唯一最小值，由于 mid < right 而 nums[mid] == nums[right]
#                     即还有最小值存在于 [left, right - 1][left,right−1] 区间，因此不会丢失最小值
def search(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right = right - 1
    return nums[left]


if __name__ == '__main__':
    print(search([1, 3, 5]))
    print(search([2, 2, 2, 0, 1]))