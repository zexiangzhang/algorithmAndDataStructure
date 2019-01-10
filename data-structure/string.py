# string C 中的string char[] python's list模拟
class String:
    store = []

    def __init__(self, *args):
        self.store = list(args)

    def add(self, char):
        self.store.append(char)

    def __repr__(self):
        for i in self.store:
            print(i, end='', flush=True)
        return ''


s = String('a', 'b')
s.add('c')
s.add('d')
print(s)

# 字符串的模式匹配 m = 原字符串长度， n = 子字符串长度
# 1. 朴素匹配算法 O(m*n)


def match(need_match, match):
    for i in range(len(need_match)):
        for j in range(len(match)):
            if i + j >= len(need_match) or need_match[i + j] != match[j]:
                break
            if j + 1 == len(match):
                return i


str1 = 'agwadsgaghhadfase'
str2 = 'fas'
print(match(str1, str2))

# 2. KMP模式匹配算法 O(m) TODO: more learning
# 移动位数 = 已匹配的字符数 - 对应的部分匹配值

# 部分匹配表, 第一个默认为-1
# a b c d a b e f
# -1 0 0 0 1 2 0 0
#
# 前后缀的最长公共子元素的长度。
# a => 'a' => [], [] => -1
# b => 'ab' => [a] [b] => 0
# c => 'abc' => [a ab] [bc c] => 0
# d => 'abcd' => [a ab abc] [bcd cd d] => 0
# a => 'abcda' => [a ab abc abcd] [bcda cda da a] => 'a' 1
# b => 'abcdab' => [a ab abc abcd abcda] [bcdab cdab dab ab b] => 'ab' => 2
# e => 'abcdabe' => [a ab abc abcd abcda abcdab] [bcdabe cdabe dabe abe be e] => 0
# f => 'abcdabef' => [a ab abc abcd abcda abcdab] [bcdabef cdabef dabef abef bef ef e] => 0


def kmp_table(string):
    if not string:
        return None
    length = len(string)
    table = [-1, 0]
    if length > 1:
        for i in range(1, length):
            p = i
            while p > 0 and string[p] != string[table[p]]:
                p = table[p]
            else:
                table.append(table[p] + 1)

    return table


print(kmp_table('abcdabef'))


def kmp_match(string, pattern):
    if not string or not pattern:
        return None
    table = kmp_table(pattern)
    start, matched = 0, 0
    ls, lp = len(string), len(pattern)
    stop = ls - lp + 1
    res = list()
    while True:
        while matched == lp or string[start + matched] != pattern[matched]:
            if matched == lp:
                res.append(start)
            start += matched - table[matched]
            matched = max(0, table[matched])
            if not start < stop:
                return res
        else:
            matched += 1


print(kmp_match('agwadsgaghhadfase', 'fas'))
