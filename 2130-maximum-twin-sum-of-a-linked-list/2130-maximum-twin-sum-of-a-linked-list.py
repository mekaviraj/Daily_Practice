# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = l = 0
        p = head
        while p:
            p, l = p.next, l + 1
        p, h, i, stack = head, l // 2, 0, []
        while p:
            if i < h:
                stack.append(p.val)
                i += 1
            else:
                res = max(res, p.val + stack.pop())
            p = p.next
        return res