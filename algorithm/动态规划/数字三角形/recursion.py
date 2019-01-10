class Test:
    n1 = 0
    n2 = 0

    # 递归思想
    def action(self, nums, n):
        self.nums = nums
        self.n = n
        return self.max_sum(0, 0)

    def max_sum(self, i, j):
        if i == self.n - 1:
            return self.nums[i][j]
        self.n1 += 1
        x = self.max_sum(i + 1, j)
        y = self.max_sum(i + 1, j + 1)
        return max(x, y) + self.nums[i][j]

    # 带记忆的递归
    def action2(self, nums, n, max_nums):
        self.nums = nums
        self.n = n
        self.max_nums = max_nums
        return self.max_sum2(0, 0)

    def max_sum2(self, i, j):
        if self.max_nums[i][j]:
            return self.max_nums[i][j]

        if i == self.n - 1:
            max_num = self.nums[i][j]
        else:
            self.n2 += 1
            x = self.max_sum2(i + 1, j)
            y = self.max_sum2(i + 1, j + 1)
            max_num = max(x, y) + self.nums[i][j]

        self.max_nums[i][j] = max_num
        return max_num


n = 20
nums = [
    [5],
    [1, 6],
    [9, 2, 4],
    [1, 6, 4, 5],
    [6, 4, 6, 3, 4],
    [6, 5, 3, 3, 4, 9],
    [2, 4, 6, 3, 4, 3, 5],
    [2, 2, 5, 3, 4, 3, 5, 3],
    [6, 9, 3, 3, 7, 9, 9, 0, 5],
    [1, 4, 7, 9, 3, 3, 9, 6, 5, 6],
    [4, 2, 3, 3, 2, 4, 3, 6, 5, 6, 2],
    [1, 8, 2, 4, 3, 3, 9, 6, 2, 1, 9, 1],
    [9, 4, 3, 3, 6, 4, 2, 5, 5, 6, 2, 3, 8],
    [1, 3, 8, 6, 3, 3, 9, 2, 7, 7, 4, 5, 7, 1],
    [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4],
    [4, 2, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 5],
    [9, 4, 3, 4, 3, 3, 9, 6, 2, 6, 3, 7, 2, 7, 4, 3, 7],
    [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 1, 7, 2],
    [9, 4, 3, 3, 9, 7, 1, 6, 5, 6, 3, 7, 2, 7, 4, 8, 2, 1, 3],
    [9, 3, 8, 6, 3, 3, 9, 2, 7, 6, 3, 7, 2, 7, 4, 7, 1, 3, 6, 9],
]

max_nums = [[0 for _ in range(0, i)] for i in range(1, n + 1)]
a = Test()
print('action1: ', a.action(nums, n), ' 次数:', a.n1)  # 时间复杂度2的n次方
print('action2: ', a.action2(nums, n, max_nums),
      ' 次数:', a.n2)  # 时间复杂度n(n-1)/2次方
