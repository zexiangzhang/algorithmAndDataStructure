"""
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串
    example 1:
     输入: "aba"
     输出: True
    example 2:
     输入: "abca"
     输出: True
"""


# 首先考虑是否是回文字符串，可以单独写函数来判断，也可以使用python切片的特性
#       如：str = “abcd”， 则reverse_str = str[::-1] = "dcba",所以如果str = reverse_str,则是回文字符串
# 当左右两个指针遇到不等的元素时,删除左指针指向的字符或者右指针指向的字符，判断剩余的所有字符是否可以构成回文串
# 左右指针从两端同时向中间走，那么有两种情况：
#       1、左右指针遇到的元素相等，继续向中间走
#       2、左右指针遇到的元素不等，则删除其中的一个字符，然后再判断剩余的所有字符是否是回文串
def valid_palindrome(s: str) -> bool:
    is_palindrome_str = lambda s: s == s[::-1]
    str_part = lambda s, x: s[:x] + s[x + 1:]
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_str(str_part(s, left)) or is_palindrome_str(str_part(s, right))
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    str1 = "aba"
    str2 = "abca"
    print(valid_palindrome(s=str1))
    print(valid_palindrome(s=str2))
