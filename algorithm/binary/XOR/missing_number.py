"""
 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数
 example 1:
    输入：nums = [3,0,1]
    输出：2
    解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
 example 2:
    输入：nums = [0,1]
    输出：2
    解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中
 example 3:
    输入：nums = [9,6,4,2,3,5,7,0,1]
    输出：8
    解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中
 example 4:
    输入：nums = [0]
    输出：1
    解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中
 提示：
    n == nums.length
    1 <= n <= 10的四次方
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二
"""
from typing import List


# 首先我们对数组进行排序
# 随后我们可以在常数时间内判断两种特殊情况：0 没有出现在数组的首位，以及 nn 没有出现在数组的末位
# 如果这两种特殊情况都不满足，那么缺失的数字一定在0和n之间(不包括两者)。
# 此时我们可以扫描这个数组，如果某一个数比它前面的那个数大了超过1，那么这两个数之间的那个数即为缺失的数字
def mussing_number_sort(numbers: List[int]) -> int:
    numbers.sort()
    if numbers[-1] != len(numbers):
        return len(numbers)
    elif numbers[0] != 0:
        return 0
    for i in range(1, len(numbers)):
        expected_num = numbers[i - 1] + 1
        if numbers[i] != expected_num:
            return expected_num


# 可以直接查询每个数是否在数组中出现过来找出缺失的数字
def mussing_number_hash(numbers: List[int]) -> int:
    num_set = set(numbers)
    n = len(numbers) + 1
    for number in range(n):
        if number not in num_set:
            return number


# 数组中有n个数，并且缺失的数在[0..n][0..n]中
# 因此我们可以先得到[0..n][0..n]的异或值，再将结果对数组中的每一个数进行一次异或运算
# 未缺失的数在[0..n][0..n]和数组中各出现一次，因此异或后得到0
# 而缺失的数字只在[0..n][0..n]中出现了一次，在数组中没有出现，因此最终的异或结果即为这个缺失的数字
def mussing_number_xor(numbers: List[int]) -> int:
    mussing_number = len(numbers)
    for index, number in enumerate(numbers):
        mussing_number ^= index ^ number
    return mussing_number


# 可以用高斯求和公式求出 [0..n][0..n] 的和，减去数组中所有数的和，就得到了缺失的数字
# 这种方法有内存溢出的异常
def mussing_number_math(numbers: List[int]) -> int:
    expected_sum = len(numbers) * (len(numbers)+1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


if __name__ == '__main__':
    input_01 = [3, 0, 1]
    input_02 = [0, 1]
    input_03 = [9, 6, 4, 2, 3,  5,  7, 0, 1]
    input_04 = [0]
    print(mussing_number_sort(input_01))
    print(mussing_number_hash(input_02))
    print(mussing_number_xor(input_03))
    print(mussing_number_math(input_04))