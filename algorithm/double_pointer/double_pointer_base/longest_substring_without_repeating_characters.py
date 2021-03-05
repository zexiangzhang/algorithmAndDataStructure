"""
   给定一个字符串，找出其中不含有重复字符的最长子串的长度
    example 1:
     输入: s = "abcabcbb"
     输出: 3
    example 2:
     输入: s = "bbbbb"
     输出: 1
    example 3:
     输入: s = "pwwkew"
     输出: 3
    example 4:
     输入: s = ""
     输出: 0
"""


# 首先做一些简单的过滤，当字符串为空时返回0
# 定义双指针fast_pointer和slow_pointer，且维护最长字串的长度max_length
# 遍历字符串：
#       1、如果字符不在滑动窗口中，则直接扩展窗口，即右指针右移一位
#       2、如果字符在滑动窗口中：
#           a.从窗口中移除重复字符及之前的字符串部分，即：
#           在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1，然后左指针右移，索引X + 1
#           b.扩展窗口, 即右指针右移一位
# 更新最大长度
# 如果最大长度不为零，返回最大长度
# 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本身的长度
def longest_substring_without_repeating_characters(s: str) -> int:
    if not s:
        return 0
    max_length = 0
    left_pointer, right_pointer = 0, 0
    for i, c in enumerate(s):
        if c not in s[left_pointer: right_pointer]:
            right_pointer += 1
        else:
            left_pointer += s[left_pointer: right_pointer].index(c) + 1
            right_pointer += 1
        max_length = max(right_pointer - left_pointer, max_length)
    return max_length if max_length != 0 else len(s)


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = ""
    print(longest_substring_without_repeating_characters(s1))
    print(longest_substring_without_repeating_characters(s2))
    print(longest_substring_without_repeating_characters(s3))
    print(longest_substring_without_repeating_characters(s4))
