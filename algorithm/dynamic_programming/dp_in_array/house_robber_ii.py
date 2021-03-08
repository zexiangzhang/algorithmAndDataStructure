"""
   你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的
   同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
   给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额
    example 1:
     输入: [2,3,2]
     输出: 3
    example 2:
     输入: [1,2,3,1]
     输出: 4
"""
from typing import List


# 环状排列房间意味着第一个房子和最后一个房子中只能选择一个偷窃
# 对于上述情况，它的最大值肯定小于等于只去掉首或者只去掉尾的队列
# 假设队列排列房间问题的结果queue_house_robber(nums)
# 详见：https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_array/house_robber_i.py
# 则：
#       1、在不偷窃第一个房子的情况下，最大金额是queue_house_robber(nums[1:])
#       2、在不偷窃最后一个房子的情况下，最大金额是queue_house_robber(nums[:-1])
# 则环形排列房间的偷窃最大金额为：以上两种情况的较大值
def house_robber(nums: List[int]) -> int:
    if len(nums) != 1:
        def queue_house_robber(nums):
            a, b = 0, 0
            for num in nums:
                a, b = max(b + num, a), a
            return a
        return max(queue_house_robber(nums[1:]), queue_house_robber(nums[:-1]))
    return nums[0]


if __name__ == '__main__':
    print(house_robber([2, 3, 2]))
    print(house_robber([1, 2, 3, 1]))
