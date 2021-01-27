"""
    给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的h指数。
    h指数的定义:
        h代表高引用次数，一名科研人员的h指数是指她的(N篇论文中)总共有h篇论文分别被引用了至少h次(其余的N - h篇论文每篇被引用次数不多于h次)
    example 1:
     输入: citations = [0,1,3,5,6]
     输出: 2
     解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
          由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3
"""
from typing import List


# 二分法
# 如：[0,1,4,5,6,7,8],h最大为4，因为在数组中至少可以找到4个大于或等于4的数字
# h+1则不成立，因为数组中不存在5个大于或等于5的数字；h-1一定成立，因为必定存在3个大于或等于3的数字
# 于是h是临界值，表示最大的符合要求的值，[0,h]条件成立，[h+1,n]条件不成立，n表示元素总数
def h_index(nums: List[int]) -> int:
    left = 0
    # 右边界为n
    right = len(nums)
    while left < right:
        mid = left + right + 1 >> 1
        # h = mid 时是否至少存在h个元素大于mid
        if check(nums, mid):
            left = mid
        else:
            right = mid - 1
    return left


def check(nums, h):
    count = 0
    for num in nums:
        if num >= h:
            count += 1
    if count >= h:
        return True
    return False


if __name__ == '__main__':
    print(h_index([0, 1, 3, 5, 6]))