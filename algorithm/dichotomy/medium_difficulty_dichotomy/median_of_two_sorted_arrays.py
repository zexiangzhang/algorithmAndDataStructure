"""
    给定两个大小为m和n的正序（从小到大）数组 nums1和nums2返回这两个正序数组的中位数
    example 1:
     输入: nums1 = [1,3], nums2 = [2]
     输出: 2.00000
     解释：合并数组 = [1,2,3] ，中位数 2
    example 2:
     输入: nums1 = [1,2], nums2 = [3,4]
     输出: 2.50000
     解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
    example 3:
     输入: nums1 = [0,0], nums2 = [0,0]
     输出: 0.00000
    example 4:
     输入: nums1 = [], nums2 = [1]
     输出: 1.00000
    example 5:
     输入: nums1 = [2], nums2 = []
     输出: 2.00000
"""
from typing import List


# 短数组(倒序)           长数组
#
#          样例：
#                 [shorter][::-1] + [longer]
#                 [5,   3 ,   2]     [2, 4, 6, 8, 9]
#          原下标   2     1    0       0  1  2  3  4
#                  |     |
#     下标对应关系 m-0-1 m-i-1        part+i-m-1
#                  |     |
#          新下标   0     1    2       3  4  5  6  7
#                 start   i   end-1
#
# 想像如同有一个长度为（n+m)//2的滑块盖住了这样排列的数组的一半
#                 [5,   *,   *,     *,  * ,6, 8, 9]
#
#     只要左右滑动，找出滑块盖住的部分全部不大于未盖住的部分
#     则盖住部分的边界 就是中位数的临近位置
#     可证  滑动区间最长为短数组的长度
def solution(nums1: List[int], nums2: List[int]) -> float:
    # 分出长短数组
    l, s = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
    n, m = len(l), len(s)
    # 有一个空数组情况处理
    if not m:
        mid_1 = l[n // 2] - 1
        mid_2 = l[n // 2]
        return mid_2 if n % 2 else (mid_2 + mid_1) / 2
    # 前一半最小值的总数
    part = (n + m) // 2
    # 因为都是正序，
    # 故只需将短数组s中第i位的值与长数组l中的第part-i位比较
    #   判断s[i]是否在前一半数的小值部分
    # 只需用二分法查找较短的数组 即折半滑动滑块
    start = 0
    end = m
    while end > start:
        i = (start + end) // 2
        if s[m - i - 1] > l[part + i - m]:  # 滑块右移
            start = i + 1
        else:  # 滑块左移
            end = i
    # 当滑块移动短数组或者start=end 表示滑块盖住部分全部不大于未盖住部分

    # 情况1 所有小值不在短数组中 即滑块不在短数组上
    if start > m - 1:
        mid_1 = l[part - 1]
        mid_2 = min(s[0], l[part]) if part < n else s[0]  # part=n 表示 两数组长度相同
    # 情况2 滑块部分或全部盖住短数组
    else:
        mid_1 = max(s[m - start - 1], l[part + start - m - 1]) if part + start - m > 0 else s[m - start - 1]
        mid_2 = min(s[m - start], l[part + start - m]) if start > 0 else l[part + start - m]
    return mid_2 if (n + m) % 2 else (mid_2 + mid_1) / 2


if __name__ == '__main__':
    print(solution(nums1=[1, 3], nums2=[2]))
    print(solution(nums1=[1, 2], nums2=[3, 4]))
    print(solution(nums1=[0, 0], nums2=[0, 0]))
    print(solution(nums1=[], nums2=[1]))
    print(solution(nums1=[2], nums2=[]))
