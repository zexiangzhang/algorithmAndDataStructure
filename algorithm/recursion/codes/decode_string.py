"""
   给定一个经过编码的字符串，返回它解码后的字符串
   编码规则为: k[encoded_string]，表示其中方括号内部的encoded_string正好重复k次
   注意 k 保证为正整数
   可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
   可以认为原始数据不包含数字，所有的数字只表示重复的次数k ，例如不会出现像3a或2[4]的输入
    example 1:
     输入: s = "3[a]2[bc]"
     输出: "aaabcbc"
    example 2:
     输入: s = "3[a2[c]]"
     输出: "accaccacc"
    example 3:
     输入: s = "2[abc]3[cd]ef"
     输出: "abcabccdcdcdef"
    example 4:
     输入: s = "abc3[cd]xyz"
     输出: "abccdcdcdxyz"
"""


# 遍历字符串，对每种情况做出相应操作
#   1、如果当前字符为数字，即'0' <= s[i] <= '9'
#       将该数字加到子字符串要重复的次数count中去，因为数字可能有多位，因此注意原count要先乘以10再加上新加入的数字
#   2、如果当前字符为左括号，即s[i] == '['
#       a.进行递归，注意每次递归时的result和count都重新赋值过
#       b.递归的返回值为当前已遍历到的索引i和子字符串tmp
#       c.拿到返回值后将tmp乘以count后加到result中，并重置count
#   3、如果当前字符为右括号，即s[i] == ']'
#       返回当前索引i以及在当前递归层的循环过程中生成的子字符串resultult
#   4、如果当前字符为字母
#       直接加到result中
# 返回最终字符串result
# 递归时：将'['和’]‘分别作为递归开始和终止的条件
#   1、s[i] == '['：开启新一轮递归，记录递归回来的索引值和字符串，res = 当前字符串res + num*递归回的字符串
#   2、s[i] == ']'：返回当前索引值（']'的索引）以及此方括号内的字符串
def decode_string(s: str) -> str:
    def dfs(i):
        result, count = "", 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                count = count * 10 + int(s[i])
            elif s[i] == '[':
                i, tmp = dfs(i + 1)
                result += tmp * count
                count = 0
            elif s[i] == ']':
                return i, result
            else:
                result += s[i]
            i += 1
        return result
    return dfs(0)


if __name__ == '__main__':
    print(decode_string("3[a]2[bc]"))
    print(decode_string("3[a2[c]]"))
    print(decode_string("2[abc]3[cd]ef"))
    print(decode_string("abc3[cd]xyz"))