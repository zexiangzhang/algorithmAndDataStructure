# 两个字符串
# 找出公共最长的子序列。 顺序一致， 不一定连续。
str1 = 'asdafasdfasf'
str2 = 'affsfffsagfdtjfds'

nums = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

nums[0][0] = int(str1[0] == str2[0])

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        nums[i][j] = max(nums[i - 1][j], nums[i][j - 1]) + \
            int(str1[i] == str2[j])

print(nums[len(str1) - 1][len(str2) - 1])
