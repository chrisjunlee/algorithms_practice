# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        res = ListNode(0)
        dummy = res
        
        while l1 and l2:        
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
                
            res = res.next
            
        # only one or none can be non-empty
        res.next = l1 if l1 else l2
        
        return dummy.next
