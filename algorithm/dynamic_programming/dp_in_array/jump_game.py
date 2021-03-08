"""
   给定一个非负整数数组 nums,你最初位于数组的第一个下标,数组中的每个元素代表你在该位置可以跳跃的最大长度
   判断你是否能够到达最后一个下标
    example 1:
     输入: nums = [2,3,1,1,4]
     输出: true
    example 2:
     输入: nums = [3,2,1,0,4]
     输出: false
"""
from typing import List


# 如果某一个作为起跳点的格子可以跳跃的距离是3，那么表示后面3个格子都可以作为起跳点
# 可以对每一个能作为起跳点的格子都尝试跳一次，把能跳到最远的距离不断更新
# 在遍历的过程中，如果 最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可以跳到
# 反之，如果在遍历结束后，最后一个位置不能跳到，则返回False
# 简单来说就是初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置
# 最后比较最远位置和数组长度
def jump_game(nums: List[int]) -> bool:
    max_index = 0
    for index, jump in enumerate(nums):
        if index <= max_index < index + jump:
            max_index = index + jump
    return max_index >= index


if __name__ == '__main__':
    print(jump_game([2, 3, 1, 1, 4]))
    print(jump_game([3, 2, 1, 0, 4]))
