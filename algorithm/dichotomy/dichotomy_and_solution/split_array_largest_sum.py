"""
    给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小
    example 1:
     输入: nums = [7,2,5,10,8],m = 2
     输出: 18
     解释：一共有四种方法将nums分割为2个子数组
          其中最好的方式是将其分为[7,2,5] 和 [10,8],因为此时这两个子数组各自的和的最大值为18，在所有情况中最小
"""
from typing import List


# 在这道题里面，假设所需要的值为x
# 对这个数组，如果每个数单独成一数组，那么子数组的各自和的最大值，就是所有数中的最大值
# 如果对这个数组不分组，那么子数组的各自和的最大值就是这个数组的和
# 所以二分查找里面的left应该是max(nums)， right应该是sum(nums)
# 根据二分法的常规代码结构：所以可以写出如下的代码：
#   left, right = max(nums),sum(nums)
#   while left < right:
#       mid = (left + right) // 2
#       if #排除右侧的条件:
#           right = mid
#       else:
#           left = mid + 1
#   return left
# 注释里先写：排除右侧的条件
# 怎样排除左侧的条件呢？即，给定一个左，右，和中间值，如何判断我们需要的最大值在中间和左边围起来的范围内呢？
# 我们假设给定了mid，那么需要判断，如果以mid作为最大值，能形成几组，然后和给定的m值作对比。显然，如果这个mid越大，要分出来的组数越少。
# 如果形成的组数比要求的多，说明这个给定的mid太小了，要扩大，而如果形成的组数太少了，说明给定的mid太大了，要缩小。
# 而如果相等呢？
# 我们假设有这么一个题目，给定列表[5,123]和m = 2来找出最大值，假如在二分中选择了124，这样子只能分成两个组
# 而显然124这个数不是正确答案，正确答案是123，所以相等的时候，我们认为这个查找值mid应该缩小
# 如果设定一个cnt变量记录分组数，即可写成这样的形式：
#   left, right = max(nums),sum(nums)
#   while left < right:
#       mid = (left + right) // 2
#       if cnt <= m:
#           right = mid
#       else:
#           left = mid + 1
#   return left
# 可是分组数怎么计算呢？
# 思路是这样，我们维护一个cnt和一个sums，表示目前的组数和目前的和。
# 初始，自然cnt = 1，sums = 0
# 我遍历这个数组
#       1、让sums加上这个遍历着的数
#       2、如果这个加起来的和比上限要小，那么就遍历下一个
#       3、 如果这个加起来的和比上限大，说明要分组了
#       4、那么cnt += 1，同时这个数作为新组的开头，即sums = 这个遍历的数
# 这样可以写出一个函数
# def group(mid):
#     sums, cnt = 0, 1
#     for i in nums:
#         if sums + i > mid:
#             cnt += 1
#             sums = i
#         else:
#             sums += i
#     return cnt
# 所以最终的代码如下solution_01所示，不想写分函数，也可以参考solution_02
def solution_01(nums: List[int], m: int) -> int:
    def group(mid_value):
        sum_value, cnt = 0, 1
        for i in nums:
            if sum_value + i > mid_value:
                cnt += 1
                sum_value = i
            else:
                sum_value += i
        return cnt
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if group(mid) <= m:
            right = mid
        else:
            left = mid + 1
    return left


def solution_02(nums: List[int], m: int) -> int:
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        sum_value, cnt = 0, 1
        for i in nums:
            if sum_value + i > mid:
                cnt += 1
                sum_value = i
            else:
                sum_value += i
        if cnt <= m:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(solution_01(nums=[7, 2, 5, 10, 8], m=2))
    print(solution_02(nums=[7, 2, 5, 10, 8], m=2))