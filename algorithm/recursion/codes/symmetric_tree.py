"""
    给定一个二叉树，检查它是否是镜像对称的
    example 1:
             1                              1
          /    \                          /   \
         2      2                        2     2
       /  \   /   \                       \      \
      3   4  4    3                        3      3
            true                            false
"""
from algorithm.recursion.TreeNode import TreeNode


# 如果左子树空 右子树不空 肯定不对称
# 如果左子树不空，右子树空，肯定也不对称
# 如果都空，对称
# 如果都有左右子树，首先判断值是否相等，再递归下去
def symmetric_tree(top: TreeNode) -> bool:
    def fun(left, right):
        if left and not right:
            return False
        elif not left and right:
            return False
        elif not left and not right:
            return True
        else:
            return left.val == right.val and fun(left.left, right.right) and fun(left.right, right.left)
    if not top:
        return True
    flag = fun(top.left, top.right)
    return flag


if __name__ == '__main__':
    # 用例 2
    top_1 = TreeNode()
    top_1.val = 1
    children_left_1 = TreeNode()
    children_left_1.val = 2
    children_right_1 = TreeNode()
    children_right_1.val = 2
    children_left_children_left_1 = TreeNode()
    children_left_children_left_1.val = 3
    children_left_children_right_1 = TreeNode()
    children_left_children_right_1.val = 4
    children_right_children_left_1 = TreeNode()
    children_right_children_left_1.val = 4
    children_right_children_right_1 = TreeNode()
    children_right_children_right_1.val = 3
    top_1.left = children_left_1
    top_1.right = children_right_1
    children_left_1.left = children_left_children_left_1
    children_left_1.right = children_left_children_right_1
    children_right_1.left = children_right_children_left_1
    children_right_1.right = children_right_children_right_1
    print(symmetric_tree(top_1))
    # 用例 2
    top_2 = TreeNode()
    top_2.val = 1
    children_left_2 = TreeNode()
    children_left_2.val = 2
    children_right_2 = TreeNode()
    children_right_2.val = 2
    children_left_children_right_2 = TreeNode()
    children_left_children_right_2.val = 3
    children_right_children_right_2 = TreeNode()
    children_right_children_right_2.val = 3
    top_2.left = children_left_2
    top_2.right = children_right_2
    children_left_2.left = None
    children_left_2.right = children_left_children_right_2
    children_right_2.left = None
    children_right_2.right = children_right_children_right_2
    print(symmetric_tree(top_2))