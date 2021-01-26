"""
    给定一个矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素
    请注意，它是排序后的第k小元素，而不是第k个不同的元素
    example 1:
     输入: matrix = [[1, 5, 9],[10, 11, 13],[12, 13, 15]],k = 8
     输出: 13
"""
from typing import List


# 根据矩阵性质，最小值为 matrix[0][0]，最大值为 matrix[-1][-1]
# mid 初始化取最大最小值的平均值
#
# count 函数：记录矩阵中小于等于 mid 的元素个数
#       1、从矩阵左下角开始移动，记当前元素为 matrix[i][j]
#       2、若当前元素小于等于 mid，则该列以上元素（包括当前元素）均小于等于 mid，有 i+1 个，然后继续向右移动
#       3、若当前元素大于 mid，则向上移动
# 二分查找思想
#       常见的二分查找是对数组下标（位置）进行二分。
#       这里的二分查找是对值域进行二分。
#           1、如果小于等于 mid 的元素个数大于等于 k，说明矩阵中第 k 小的元素小于等于 mid，更新右边界为 mid
#           2、否则，说明第 k 小的元素大于 mid，更新左边界为 mid+1
#           3、不断更新 mid，直到左右边界相遇，此时 mid 值即为矩阵中第 k 小的元素
def kth_smallest(matrix: List[List[int]], k: int) -> int:
    def count(mid_value):
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid_value:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt >= k

    n = len(matrix)
    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        if count(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(kth_smallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))