"""
 给定一个从1到n排序的整数列表。
 首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
 第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
 我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
 返回长度为 n 的列表中，最后剩下的数字。
 example 1:
     输入: 9
     输出: 6
     解释：
        n = 9, 数组为:1 2 3 4 5 6 7 8 9             start_number = 1, remain = 9, diff = 1
        第一次：2 4 6 8                             start_number = 8, remain = 4, diff = 2
        第二次：2 6                                 start_number = 2, remain = 2, diff = 4
        第三次：6
        只剩一个数字，返回：6
 example 2:
     输入: 10
     输出: 8
     解释：
        n = 8, 数组为:1 2 3 4 5 6 7 8 9 10            start_number = 1, remain = 10, diff = 1
        第一次：2 4 6 8 10                            start_number = 10, remain = 5, diff = 2
        第二次：4 8                                   start_number = 4, remain = 2, diff = 4
        第三次：8
        只剩一个数字，返回：8
"""


# 约瑟夫环体，找规律
# 通过观察其实每次消除的是一个等差数列，剩下的也是一个等差数列
# 假设start_number是消除过程中列表的第一个元素,remain是消除后列表的元素个数，diff是等差数列的公差
# diff是上一次diff * 2，即diff <<= 1
# 每轮消除之后，remain是原来的列表长度进行向下取整除以2的结果(9 // 2 = 4), 即remain >>= 1
# 每轮消除之后的start_number跟当前消除的方向以及remain的奇偶性有关:
#       如果从左往右消除，则新列表的start_number就是当前消除列表的第二个元素，即为start_number + diff，其中diff是当前要消除的列表的diff
#       如果是从右往左消除，则新列表的start_number值会受remain的奇偶性所影响
#       举个例子，如果remain是奇数，如[1,2,3,4,5][1,2,3,4,5]，那么从右开始消除，则会消掉1, 3, 51,3,5, 剩下[2, 4][2,4]
#       如果remain是偶数, 如[1,2,3,4][1,2,3,4]，则从右开始消除之后，剩下[1, 3][1,3]
#       可以发现，如果remain是奇数，新列表的start_number即为start_number + diff，否则新列表start_number不变
def elimination_game(n: int) -> int:
    start_number = diff = 1
    remain = n
    from_left = True
    while remain > 1:
        if from_left:
            start_number += diff
        else:
            if remain & 1 == 1:
                start_number += diff
        remain >>= 1
        diff <<= 1
        if from_left:
            from_left = False
        else:
            from_left = True
    return start_number


if __name__ == '__main__':
    print(elimination_game(9))
    print(elimination_game(10))