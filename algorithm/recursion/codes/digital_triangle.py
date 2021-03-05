"""
    一个三角形的数字堆， 找出一条从三角形顶端到底端的路径，使得路径上的各数字之和最大。求最大之和
    要求： 只能向左右下角移动
"""
from typing import List


# 递归
# 深搜到最底层，直接把该值返回
# 否则直接用当前元素加下一行大的深搜值
def digital_triangle_recursion(nums: List[List[int]], x: int, y: int) -> int:
    if x == len(nums) - 1:
        return nums[x][y]
    res = nums[x][y] + max(digital_triangle_recursion(nums, x + 1, y), digital_triangle_recursion(nums, x + 1, y + 1))
    return res


# 动态规划
# 首先创建一个辅助数组，将原三角形的最后一行数字复制到辅助数组的最后一行
# 然后辅助数组从倒数第二行开始，就是将原三角形的倒数第二行原值（li[i][j]）加上辅助数组最后一行的较大值max(rec[i+1][j],rec[i+1][j+1])
# 最后辅助数组的第一个元素就是目标值
def digital_triangle_dp(nums: List[List[int]]) -> int:
    rec = [[0] * len(nums) for _ in range(len(nums))]
    for j in range(len(nums)):
        rec[len(nums) - 1][j] = nums[len(nums) - 1][j]
    for i in range(len(nums) - 2, -1, -1):
        for j in range(len(nums[i])):
            rec[i][j] = max(rec[i + 1][j], rec[i + 1][j + 1]) + nums[i][j]
    return rec[0][0]


if __name__ == '__main__':
    nums = [
        [5],
        [1, 6],
        [9, 2, 4],
        [1, 6, 4, 5],
        [6, 4, 6, 3, 4],
        [6, 5, 3, 3, 4, 9],
        [2, 4, 6, 3, 4, 3, 5],
        [2, 2, 5, 3, 4, 3, 5, 3],
        [6, 9, 3, 3, 7, 9, 9, 0, 5],
        [1, 4, 7, 9, 3, 3, 9, 6, 5, 6],
        [4, 2, 3, 3, 2, 4, 3, 6, 5, 6, 2],
        [1, 8, 2, 4, 3, 3, 9, 6, 2, 1, 9, 1],
        [9, 4, 3, 3, 6, 4, 2, 5, 5, 6, 2, 3, 8],
        [1, 3, 8, 6, 3, 3, 9, 2, 7, 7, 4, 5, 7, 1],
        [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4],
        [4, 2, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 5],
        [9, 4, 3, 4, 3, 3, 9, 6, 2, 6, 3, 7, 2, 7, 4, 3, 7],
        [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 1, 7, 2],
        [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 8, 2, 1, 3],
        [9, 3, 8, 6, 3, 3, 9, 2, 7, 6, 3, 7, 2, 7, 4, 7, 1, 3, 6, 9],
    ]
    print(digital_triangle_recursion(nums, 0, 0))
    print(digital_triangle_dp(nums))

