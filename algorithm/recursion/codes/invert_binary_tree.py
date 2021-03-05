"""
    翻转一棵二叉树
            4                               4
          /   \           翻转后           /   \
         2     7          ====>          7     2
        / \   / \                       / \   / \
       1   3  6  9                     9   6 3   1
    即：4 => 2 => 7 => 1 => 3 => 6 => 9  变成  4 => 7 => 2 => 9 => 6 => 3 => 1
"""
from typing import Optional
from algorithm.recursion.TreeNode import TreeNode, print_tree


# top节点的新的左子树：是翻转了的top.right => 即 top.left = invert_binary_tree(top.right);
# top节点的新的右子树：是翻转了的top.left => 即 top.right = invert_binary_tree(top.left)
# 踩坑的地方：
#   不能这么写：
#       top.left = invert_binary_tree(top.right)
#       top.right = invert_binary_tree(top.left)
#   这是因为第一行修改了top.left，会影响了第二行
#   在Python中，正确的写法是把两行写在同一行，就能保证top.left和top.right的修改是同时进行的
def invert_binary_tree(top: TreeNode) -> Optional[TreeNode]:
    if not top:
        return
    top.left, top.right = invert_binary_tree(top.right), invert_binary_tree(top.left)
    return top


if __name__ == '__main__':
    top = TreeNode()
    top.val = 4
    children_left = TreeNode()
    children_left.val = 2
    children_right = TreeNode()
    children_right.val = 7
    children_left_children_left = TreeNode()
    children_left_children_left.val = 1
    children_left_children_right = TreeNode()
    children_left_children_right.val = 3
    children_right_children_left = TreeNode()
    children_right_children_left.val = 6
    children_right_children_right = TreeNode()
    children_right_children_right.val = 9
    top.left = children_left
    top.right = children_right
    children_left.left = children_left_children_left
    children_left.right = children_left_children_right
    children_right.left = children_right_children_left
    children_right.right = children_right_children_right
    print_tree(top)
    invert_top = invert_binary_tree(top)
    print_tree(invert_top)

