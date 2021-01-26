"""
 对链表进行插入排序
 从第一个元素开始，该链表可以被认为已经部分排序
 每次迭代时，从输入数据中移除一个元素，并原地将其插入到已排好序的链表中
 插入排序算法：
    1、插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    2、每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    3、重复直到所有输入数据插入完为止
 example 1:
     输入: 4->2->1->3
     输出: 1->2->3->4

 example 2:
     输入: -1->5->3->4->0
     输出: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这个道题就像排队,先找个排头start,然后依次从head节点放入start,只需要依次start现有节点比较,插入其中
# 因为我们每次都要从头比较,但是测试集很多都是顺序排列的,没必要从头开始,我们直接比较最后一个tail,放在后面
def insertion_sort_list(head: ListNode) -> ListNode:
    start = ListNode(float("-inf"))
    pre, tail = start
    cur = head
    while cur:
        if tail.val < cur.val:
            tail.next = cur
            tail = cur
            cur = cur.next
        else:
            tmp = cur.next
            tail.next = tmp
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = start
            cur = tmp
    return start.next