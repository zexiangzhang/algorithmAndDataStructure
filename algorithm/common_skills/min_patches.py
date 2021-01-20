"""
 给定一个已排序的正整数数组 nums，和一个正整数n
 从[1, n]区间内选取任意个数字补充到nums中，使得[1,n]区间内的任何数字都可以用nums中某几个数字的和来表示
 请输出满足上述要求的最少需要补充的数字个数
 example 1:
     输入: nums = [1,3], n = 6
     输出: 1

 example 2:
     输入: nums = [1,5,10], n = 20
     输出: 2

 example 3:
     输入: nums = [1,2,2], n = 5
     输出: 0
"""
from typing import List


# 贪心算法
# 补齐数组特点：假设数组arr添加一个元素即可覆盖[1, n)内所有数字，那么添加的数字m一定满足m <= n
# 假设数组arr可以覆盖[1, n)[1,n)的所有数字，则给arr内加元素m：若m <= n，新数组可以覆盖[1, m + n) = [1, n) ∪ [m, m + n)内所有数字
# 贪心法则： 对于一个覆盖[1,n)的数组arr来说，添加数字n连续扩容范围最大（扩容至[1, 2n)）
# 思路： 设置一个初始范围[1,1，通过不断确认并扩大数组可以覆盖的范围，最终计算出最少需要加入的数字。
# 当i < len(nums)且nums[i] <= add时：
#       不需要加入新数字，循环确认并更新数组可以覆盖的范围[1, add + nums[i])，直到找到大于确认范围add的nums[i]或索引越界。
# 否则：无法根据现有数字构建更大的连续范围，
#       因此需要使用贪心策略向数组加入数字add，将数组从覆盖[1,add)扩容至可覆盖[1,2add)
# 直到确认的范围add > n，说明此时已经覆盖 [1, n]，退出迭代并返回。
def min_patches(nums: List[int], n: int) -> int:
    add = index = count = 0
    while add < n:
        if index < len(nums) and nums[index] <= add + 1:
            add += nums[index]
            index += 1
        else:
            add = 2 * add + 1
            count += 1
    return count


if __name__ == '__main__':
    print(min_patches([1, 3], 6))
    print(min_patches([1, 5, 10], 20))
    print(min_patches([1, 2, 2], 5))