"""
 给定一个字符串数组words，找到length(word[i]) * length(word[j])的最大值，并且这两个单词不含有公共字母
 可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0
 example 1:
     输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
     输出: 16
     解释：这两个单词为 "abcw", "xtfn"

 example 2:
     输入: ["a","ab","abc","d","cd","bcd","abcd"]
     输出: 4
     解释：这两个单词为 "ab", "cd"

 example 3:
     输入: ["a","aa","aaa","aaaa"]
     输出: 0
     解释：不存在这样的两个单词
"""
from typing import List


# 把所有的单词变成字符set，同时记录下单词的原始长度
# 然后两两组合对集合求并，并为空的就是符合条件的
def max_product(words: List[str]) -> int:
    set_and_length = [(set(w), len(w)) for w in words]
    result, length = 0, len(words)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if not set_and_length[i][0].intersection(set_and_length[j][0]):
                result = max(result, set_and_length[i][1] * set_and_length[j][1])
    return result


if __name__ == '__main__':
    input_arr_01 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    input_arr_02 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    input_arr_03 = ["a", "aa", "aaa", "aaaa"]
    print(max_product(input_arr_01))
    print(max_product(input_arr_02))
    print(max_product(input_arr_03))