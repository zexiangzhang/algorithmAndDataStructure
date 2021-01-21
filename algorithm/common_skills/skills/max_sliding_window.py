"""
 给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
 返回滑动窗口中的最大值
 example 1:
     输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
     输出: [3,3,5,5,6,7]

 example 2:
     输入: nums = [1], k = 1
     输出: [1]

 example 3:
     输入: nums = [1,-1], k = 1
     输出: [1,-1]
"""
from typing import List


# 将数组nums从左到右按照k个一组进行分组，最后一组中元素的数量可能会不足k个
# 如果我们希望求出nums[i]到nums[i+k−1]的最大值，就会有两种情况：
# 如果i是k的倍数，那么nums[i]到nums[i+k−1] 恰好是一个分组。我们只要预处理出每个分组中的最大值，即可得到答案；
# 如果i不是k的倍数，那么nums[i]到nums[i+k−1] 会跨越两个分组，占有第一个分组的后缀以及第二个分组的前缀
# 假设j是k的倍数，并且满足i<j≤i+k−1，那么nums[i]到nums[j−1] 就是第一个分组的后缀
# nums[j]到nums[i+k−1] 就是第二个分组的前缀
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    prefix_max, suffix_max = [0] * length, [0] * length
    for i in range(length):
        if i % k == 0:
            prefix_max[i] = nums[i]
        else:
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
    for i in range(length - 1, -1, -1):
        if i == length - 1 or (i + 1) % k == 0:
            suffix_max[i] = nums[i]
        else:
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

    return [max(suffix_max[i], prefix_max[i + k - 1]) for i in range(length - k + 1)]


if __name__ == '__main__':
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(max_sliding_window([1], 1))
    print(max_sliding_window([1, -1], 1))
