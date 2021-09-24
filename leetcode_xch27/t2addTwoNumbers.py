"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag=0
        res=ListNode(0)
        iterres=res
        while(l1 or l2):
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            s=val1+val2+flag
            flag=s//10
            val=s%10
            iterres.next=ListNode(val)
            iterres=iterres.next
            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0
        if flag!=0:
            iterres.next=ListNode(1)
        s=res.next
        while(s):
            print(s.val)
            s=s.next

if __name__ == '__main__':
    a=ListNode(2)
    a.next=ListNode(4)
    a.next.next=ListNode(3)
    a.next.next.next = ListNode(1)
    b=ListNode(5)
    b.next=ListNode(6)
    b.next.next=ListNode(4)
    Solution().addTwoNumbers(a,b)