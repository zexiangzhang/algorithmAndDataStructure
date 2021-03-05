"""
   给定n个整数，找出平均数最大且长度为k的连续子数组，并输出该最大平均数
    example 1:
     输入: [1,12,-5,-6,50,3], k = 4
     输出: 12.75(最大平均数 (12-5-6+50)/4 = 51/4 = 12.75)
"""
from typing import List


# 前缀和（preSum）算法
# 由于k是不变的，因此可以先求区间的最大和，然后再除以k
# 数组长度为length，我们定义一个长度为length + 1的preSum数组
# preSum[i]表示该元素左边所有元素之和（不包含当前元素）
# 然后遍历一次数组，累加区间 [0, i) 范围内的元素，可以得到 preSum 数组
# 先遍历一次数组，求数组每个位置的preSum
# 然后再遍历一次，求长度为 k 的每个区间的最大和
# 最终除以 k 得到最大平均数
def maximum_average_subarray_pre_sum(nums: List[int], k: int) -> float:
    length = len(nums)
    pre_sum = list(range(length + 1))
    for i in range(length):
        pre_sum[i + 1] = pre_sum[i] + nums[i]
    largest = float("-inf")
    for i in range(k - 1, length):
        largest = max(pre_sum[i + 1] - pre_sum[i + 1 - k], largest)
    return largest / float(k)


# 滑动窗口（Sliding Window）算法
# 本题可以抽象为一个长度固定为k的滑动窗口
# 当每次窗口右移的时候，需要把右边的新位置加到窗口中的sum中
# 把左边被移除的位置从窗口的sum中减掉
# 这样窗口里面所有元素的sum是准确的
# 我们求出最大的和，最终除以 k 得到最大平均数。
# 需要注意的是，需要根据 i 的位置，计算滑动窗口是否开始、是否要移除最左边元素：
#       1、当 i >= k 时，为了固定窗口的元素是 k 个，每次移动时需要将 i - k 位置的元素移除。
#       2、当 i >= k - 1时，最左边第一个滑动窗口内的元素刚好 k 个，开始计算滑动窗口的最大和
def maximum_average_subarray_sliding_window(nums: List[int], k: int) -> float:
    sums = 0
    largest = float('-inf')
    for i, num in enumerate(nums):
        sums += num
        if i >= k:
            sums -= nums[i - k]
        if i >= k - 1:
            largest = max(sums, largest)
    return largest / float(k)


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(maximum_average_subarray_pre_sum(nums=nums, k=k))
    print(maximum_average_subarray_sliding_window(nums=nums, k=k))