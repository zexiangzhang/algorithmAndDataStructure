"""
    给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i,ai)
    在坐标内画n条垂直线，垂直线i的两个端点分别为(i,ai)和(i,0)
    找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水
    example 1:
     输入: [1,8,6,2,5,4,8,3,7]
     输出: 49
    example 2:
     输入: [1,1]
     输出: 1
    example 3:
     输入: [4,3,2,1,4]
     输出: 16
"""

from typing import List


# 设置双指针left_index,right_index分别位于容器壁两端
# 设每一状态下水槽面积为 S(left_index, right_index),(0 <= left_index < right_index < n)
# 由于水槽的实际高度由两板中的短板决定，所以：
#       S(left_index, right_index) = min(height[left_index], height[right_index]) × (right_index - left_index)
# 在每一个状态下，无论长板或短板收窄1格，都会导致水槽底边宽度-1：
# 若向内移动短板，水槽的短板min(height[left_index], height[right_index])可能变大，因此水槽面积S(left_index, right_index)可能增大
# 若向内移动长板，水槽的短板min(height[left_index], height[right_index])不变或变小，下个水槽的面积一定小于当前水槽面积
# 因此，向内收窄短板可以获取面积最大值


# 可以使用反证法证明一下为什么双指针下移动高度小的指针不会漏掉可能出现的最大值
# 设宽度为w，左指针为left_index，右指针为right_index
# 原来的面积为：s = height(left_index) * w,且面积由两板中的短板决定
# 如果移动right_index,有两种情况：
#   1、移动后right_index - 1的高度比left_index高，s‘ = height(left_index) * (w - 1), 此时s' < s
#   2、移动后right_index - 1的高度比left_index低，s‘ = height(right_index) * (w - 1), 此时s' < s
# 两种情况下移动后的面试s'都比原来的面积s小
def container_with_most_water_double_pointer(height: List[int]) -> int:
    left_index, right_index = 0, len(height) - 1
    answer = 0
    while left_index < right_index:
        area = min(height[left_index], height[right_index]) * (right_index - left_index)
        answer = max(answer, area)
        if height[left_index] <= height[right_index]:
            left_index += 1
        else:
            right_index -= 1
    return answer


if __name__ == '__main__':
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]
    height3 = [4, 3, 2, 1, 4]
    print(container_with_most_water_double_pointer(height=height1))
    print(container_with_most_water_double_pointer(height=height2))
    print(container_with_most_water_double_pointer(height=height3))