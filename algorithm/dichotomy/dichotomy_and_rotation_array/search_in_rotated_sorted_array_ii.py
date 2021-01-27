"""
    假设按照升序排序的数组在预先未知的某个点上进行了旋转,(例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )
    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false
    nums可能包含重复元素
    example 1:
     输入: nums = [2,5,6,0,0,1,2], target = 0
     输出: true
    example 2:
     输入: nums = [2,5,6,0,0,1,2], target = 3
     输出: false
"""
from typing import List


# 这个问题和前一个搜索旋转排序数组（https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dichotomy/
# dichotomy_and_rotation_array/search_in_rotated_sorted_array_i.py）的区别在于如何处理重复元素
# 旋转排序数组的特性是：排序旋转数组是由两段有序的子序列构成，分为左子列和右子列
# 所以思路是：
#   1、初始化左l=0l=0和右指针r=n-1r=n−1。
#   2、 循环条件l <= r：
#       a. mid=(l+r)//2，若nums[mid]==target，返回True
#       b.若nums[mid]==nums[l]==nums[r]，将左右指针同时向里移一位，l+=1,r-=1
#       c.若nums[mid]>=nums[l]，说明此时mid在左子列中：
#           1):若此时nums[l]<=target<nums[mid]，说明target在左子列中，则此时r=mid-1
#           2):否则，l=mid+1
#       d.否则，说明mid在右子列中：
#           1):若nums[mid]<target<=nums[r]，说明target在右子列中，则此时l=mid+1
#           2):否则r=mid-1
#   3、返回False
def search(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


if __name__ == '__main__':
    print(search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
    print(search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))