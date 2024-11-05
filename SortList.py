# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head
        while temp != None:
            res.append(temp.val)
            temp = temp.next

        res.sort()
        temp = head
        for i in range(len(res)):
            temp.val = res[i]
            temp = temp.next
        return head