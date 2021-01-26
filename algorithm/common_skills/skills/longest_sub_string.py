"""
 找到给定字符串（由小写字符组成）中的最长子串T，要求T中的每一字符出现次数都不少于k。输出T的长度
 example 1:
     输入: s = "aaabb", k = 3
     输出: 3
     解释：最长子串为"aaa"，其中'a'重复了3次

 example 2:
     输入: s = "ababbc", k = 2
     输出: 5
     解释：最长子串为"ababb"，其中'a'重复了2次，'b'重复了3次
"""


# 题目要求T中的每一个字符出现的次数都不少于k
# 那么如果字符串s中某一个字符c的数量 >= k，则s就是符合要求的最长子串T
# 如果c的数量 < k,那么可以以c为分隔符来分割这个字符串
# 对每一个分割后的子串t递归即可返回返回满足题目要求的最长子串长度T
def longest_sub_string(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    for c in set(s):
        if s.count(c) < k:
            return max(longest_sub_string(t, k) for t in s.split(c))
    return len(s)


if __name__ == '__main__':
    print(longest_sub_string('aaabb', 3))
    print(longest_sub_string('ababbc', 2))