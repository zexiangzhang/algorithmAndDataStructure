"""
    编写一个高效的算法来判断矩阵中，是否存在一个目标值。该矩阵具有如下特性：
      1、每行中的整数从左到右按升序排列
      2、每列的元素从上到下升序排列
    example 1:
     输入: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
     输出: True
    example 2:
     输入: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
     输出: false
"""
from typing import List


# 使用二分法的话就是逐行查找
# 思路详见（https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dichotomy/dichotomy_and_matrix/search_a_2d_matrix_i.py）
# 本题是从右上角开始寻找，如果当前值比目标值大，则 raw += 1，如果当前值比目标值小，则 col -= 1
def search_a_2d_matrix_ii(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    raws = len(matrix)
    cols = len(matrix[0])
    raw = 0
    col = cols - 1
    while 0 <= raw < raws and 0 <= col < cols:
        if matrix[raw][col] < target:
            raw += 1
        elif matrix[raw][col] > target:
            col -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(search_a_2d_matrix_ii(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=5))
    print(search_a_2d_matrix_ii(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20))