"""
   编写一个程序，找到两个单链表相交的起始节点
   example 1:
     输入: head = [1,4,3,2,5,2], x = 3
     输出: [1,2,2,4,3,5]
   example 2:
     输入: head = [2,1], x = 2
     输出: [1,2]
"""
from algorithm.common_skills.skills.insertion_sort_list import ListNode


# 假设两条链表的第一个公共节点为common_node，链表A的长度为length_a,链表B的长度为length_b,公共节点的长度为length_c，则：
# 头节点headA到common_node前，共有length_a - length_c个节点
# 头节点headB到common_node前，共有length_b - length_c个节点
# 此时构建两个指针，分别遍历两条链表，遍历链表A的指针为point_A,遍历链表B的指针为point_B,初始值分别在两条链表的头节点位置，则：
# 指针point_a先遍历完链表A，再遍历链表B，当走到common_node时，共走步数为：length_a + (length_b − length_c)
# 指针point_b先遍历完链表B，再遍历链表A，当走到common_node时，共走步数为：length_b + (length_a − length_c)
# 如果指针point_a与指针point_b重合，有两种情况：
#       1、若两链表有公共节点 (即 length_c > 0) ：指针point_a, point_b同时指向common_node
#       2、若两链表无公共节点 (即 length_c = 0) ：指针point_a, point_b同时指向None
def intersection_of_two_linked_lists(headA: ListNode, headB: ListNode) -> ListNode:
    point_a, point_b = headA, headB
    while point_a != point_b:
        point_a = point_a.next if point_a else headB
        point_b = point_b.next if point_b else headA
    return point_a
