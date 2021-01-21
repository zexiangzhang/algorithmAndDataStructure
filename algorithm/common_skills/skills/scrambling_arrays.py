"""
 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
 实现 Solution class:
    Solution(int[] nums) 使用整数数组 nums 初始化对象
    int[] reset() 重设数组到它的初始状态并返回
    int[] shuffle() 返回数组随机打乱后的结果
 example 1:
     输入: ["Solution", "shuffle", "reset", "shuffle"]
          [[[1, 2, 3]], [], [], []]
     输出: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
     解释：
        Solution solution = new Solution([1, 2, 3]);
        solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
        solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
        solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
"""
from typing import List
import random


class Solution:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def reset(self) -> List[int]:
        return self.numbers

    # 洗牌算法
    # 假设数组中有n个数，nums[0, 1, ..., n-1]
    # 从nums[1, ..., n-1]中随机选一个数nums[i]，交换nums[0]和nums[i]
    # 从nums[2, ..., n-1]中随机选一个数nums[j]，交换nums[1]和nums[j]
    # 重复上面的步骤，直至所有数都被交换过
    def shuffle(self) -> List[int]:
        nums_copy = self.numbers[::1]
        for index in range(len(nums_copy))[::-1]:
            swap_index = random.randint(0, index)
            nums_copy[swap_index], nums_copy[index] = nums_copy[index], nums_copy[swap_index]
        return nums_copy


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution(nums)
    print(solution.reset())
    print(solution.shuffle())
