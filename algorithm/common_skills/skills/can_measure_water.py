"""
 有两个容量分别为x升和y升的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好z升的水？
 如果可以，最后请用以上水壶中的一或两个来盛放取得的z升水。
 你允许：
    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空
 example 1:
     输入: x = 3, y = 5, z = 4
     输出: True

 example 2:
     输入: x = 2, y = 6, z = 5
     输出: False
"""


# 在任意一个时刻，此问题的状态可以由两个数字决定：X 壶中的水量，以及 Y 壶中的水量
# 在任意一个时刻，我们可以且仅可以采取以下几种操作：
#       把 X 壶的水灌进 Y 壶，直至灌满或倒空
#       把 Y 壶的水灌进 X 壶，直至灌满或倒空
#       把 X 壶灌满
#       把 Y 壶灌满
#       把 X 壶倒空
#       把 Y 壶倒空
# 使用深度优先搜索来解决。
# 搜索中的每一步以 remain_x, remain_y 作为状态，即表示 X 壶和 Y 壶中的水量
# 在每一步搜索时，依次尝试所有的操作，递归地搜索下去
# 这可能会导致陷入无止境的递归
# 因此使用一个HashSet存储所有已经搜索过的remain_x, remain_y状态，保证每个状态至多只被搜索一次
def can_measure_water(x: int, y: int, z: int) -> int:
    stack = [(0, 0)]
    seen = set()
    while stack:
        remain_x, remain_y = stack.pop()
        if remain_x == z or remain_y == z or remain_x + remain_y == z:
            return True
        if (remain_x, remain_y) in seen:
            continue
        seen.add((remain_x, remain_y))
        # 把 X 壶灌满
        stack.append((x, remain_y))
        # 把 Y 壶灌满
        stack.append((remain_x, y))
        # 把 X 壶倒空
        stack.append((0, remain_y))
        # 把 Y 壶倒空
        stack.append((remain_x, 0))
        # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
        stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
        # 把 Y 壶的水灌进 X 壶，直至灌满或倒空
        stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
    return False


if __name__ == '__main__':
    print(can_measure_water(3, 5, 4))
    print(can_measure_water(2, 6, 5))