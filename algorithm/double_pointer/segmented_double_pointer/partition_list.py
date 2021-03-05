"""
   给定一个链表的头节点head和一个特定值x，对链表进行分隔，使得所有小于x的节点都出现在大于或等于x的节点之前
   保留两个分区中每个节点的初始相对位置
   example 1:
     输入: head = [1,4,3,2,5,2], x = 3
     输出: [1,2,2,4,3,5]
   example 2:
     输入: head = [2,1], x = 2
     输出: [1,2]
"""
from algorithm.common_skills.skills.insertion_sort_list import ListNode


# 定义两个指针left_pointer和right_pointer
# 左指针始终指向左边第一个大于等于x节点的前一个位置
# 右指针寻找右边第一个小于x的节点插到left后面
# left_pointer从左到右找到第一个大于等于x的前一个位置
# right_pointer从大于等于x的位置遍历到第一个小于x的位置tmp，即tmp=right_pointer.next
# 原地移动：right_pointer指向tmp的后一位，right_pointer.next=tmp.next
# tmp节点移动到left_pointer的下一个位置left_pointer.next=tmp
# 同时left_pointer移动到tmp,left_pointer.next=tmp
def partition_list(head: ListNode, x: int) -> ListNode:
    if not head:
        return
    dummy = ListNode(0)
    dummy.next = head
    left = dummy
    while left.next and left.next.val < x:
        left = left.next

    right = left.next
    while right:
        while right.next and right.next.val >= x:
            right = right.next
        if not right.next:
            break
        tmp = right.next
        right.next = tmp.next
        tmp.next = left.next
        left.next = tmp
        left = tmp
    return dummy.next


def print_node(node: ListNode):
    print(node.val)
    if node.next is not None:
        temp = node.next
        print_node(temp)


if __name__ == '__main__':
    list = [1, 4, 3, 2, 5, 2]
    head = ListNode(list[0])
    second = ListNode(list[1])
    third = ListNode(list[2])
    forth = ListNode(list[3])
    fifth = ListNode(list[4])
    sixth = ListNode(list[5])
    head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    fifth.next = sixth
    x = 3
    result = partition_list(head=head, x=x)
    print_node(result)