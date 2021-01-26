"""
    编写一个高效的算法来判断矩阵中，是否存在一个目标值。该矩阵具有如下特性：
        1、每行中的整数从左到右按升序排列
        2、每行的第一个整数大于前一行的最后一个整数
    example 1:
     输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
     输出: True
    example 2:
     输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
     输出: false
"""
from typing import List


# 先逐行查找，如果某一行的尾数小于等于target，返回行坐标，然后对该行进行二分查找
def search_a_2d_matrix_01(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return False
    index = -1
    for i in range(len(matrix)):
        if target <= matrix[i][-1]:
            index = i
            break

    if index == -1:
        return False
    else:
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[index][mid] > target:
                right = mid - 1
            elif matrix[index][mid] < target:
                left = mid + 1
            else:
                return True
        return False


def search_a_2d_matrix_02(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0: return False
    n, m = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid // m][mid % m] == target:
            return True
        if matrix[mid // m][mid % m] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    print(search_a_2d_matrix_01([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(search_a_2d_matrix_01([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

    print(search_a_2d_matrix_02([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(search_a_2d_matrix_02([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))