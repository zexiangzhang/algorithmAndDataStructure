"""
    给定两棵二叉树的根节点p和q，编写一个函数来检验这两棵树是否相同
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的
    example 1:
     输入: p = [1,2,3], q = [1,2,3]
     输出: true
    example 2:
     输入: p = [1,2], q = [1,None,2]
     输出: false
    example 3:
     输入: p = [1,2,1], q = [1,1,2]
     输出: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return same_tree(p.left, q.left) and same_tree(p.right, q.right)


# 以example 2中的输入示例
if __name__ == '__main__':
    p = TreeNode()
    p.val = 1
    p_left = TreeNode()
    p_left.val = 2
    p.left = p_left
    p.right = None

    q = TreeNode()
    q.val = 1
    q_right = TreeNode()
    q_right.val = 2
    q.right = q_right
    q.left = None

    print(same_tree(p, q))