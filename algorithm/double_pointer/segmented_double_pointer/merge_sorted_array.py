"""
   给定两个有序整数数组nums1 和 nums2，将 nums2 合并到nums1中，使 nums1成为一个有序数组。
   初始化nums1 和 nums2 的元素数量分别为m 和 n
   可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素
   example 1:
     输入: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
     输出: [1,2,2,3,5,6]
   example 2:
     输入: nums1 = [1], m = 1, nums2 = [], n = 0
     输出: [1]
"""
from typing import List


# 分段指针的基本应用，比较得到两个数组最大的元素，作为最大值放在最后
# 只需要注意一下m == 0 后，n > 0 的情况
def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
    while m != 0:
        if n > 0 and nums1[m - 1] < nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m = m - 1
    while n != 0:
        nums1[m + n - 1] = nums2[n - 1]
        n = n - 1
    return nums1


if __name__ == '__main__':
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m_1 = 3
    nums2_1 = [2, 5, 6]
    n_1 = 3
    print(merge_sorted_array(nums1_1, m_1, nums2_1, n_1))
    nums1_2 = [1]
    m_2 = 1
    nums2_2 = []
    n_2 = 0
    print(merge_sorted_array(nums1_2, m_2, nums2_2, n_2))