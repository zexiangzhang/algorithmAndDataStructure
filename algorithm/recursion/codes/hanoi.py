"""
    有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆：
    每次只能移动一个圆盘；
    大盘不能叠在小盘上面。
    提示：可将圆盘临时置于B杆，也可将从A杆移出的圆盘重新移回A杆，但都必须遵循上述两条规则。
    问：如何移？最少要移动多少次？
    example 1:
     输入: A = [2, 1, 0], B = [], C = []
     输出: C = [2, 1, 0]
    example 2:
     输入: A = [1, 0], B = [], C = []
     输出: C = [1, 0]
"""
from typing import List


def hanoi(A: List[int], B: List[int], C: List[int]):
    move(len(A), A, B, C)
    print(C)


def move(length, A, B, C):
    if length == 1:
        C.append(A[-1])
        A.pop()
        return
    else:
        move(length - 1, A, C, B)
        C.append(A[-1])
        A.pop()
        move(length - 1, B, A, C)


if __name__ == '__main__':
    hanoi([2, 1, 0], [], [])
    hanoi([1, 0], [], [])



