#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return None
        s=None
        h=head

        ## 链表倒序 实现。
        while h:
            tmp = ListNode(h.val)
            tmp.next=s
            s=tmp
            h=h.next          #每次搞个临时的节点

        x=[]
        i=1
        while s:
            if i!=n:
                x.append(s.val)
            s=s.next
            i+=1
        # print(s.val)
        return x
        # while s:
        #     print(s.val)
        #     s = s.next
    def nixu(self, head):
        Node=ListNode(None)
        Node.next=head
        cur=Node.next
        pre=None
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        s=pre
        while s:
            print(s.val)
            s = s.next

if __name__ == '__main__':
    a=ListNode(1)
    a.next=ListNode(2)
    a.next.next=ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    n=2
    # print(Solution().removeNthFromEnd(a,n))
    print(Solution().nixu(a))