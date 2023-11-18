# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        root = head
        carry = 0

        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0

            if l2:
                v2 = l2.val
            else:
                v2 = 0

            sum = v1+v2+carry
            carry = sum//10
            head.next = ListNode(sum%10)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)   

        return root.next