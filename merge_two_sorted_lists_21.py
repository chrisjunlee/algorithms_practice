# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        res = None
        res_head = res
        
        # pointers to each list element
        min_node = None
        
        while l1 and l2:        
            # compare pointers. take min
            if l1.val < l2.val:
                min_node = ListNode(l1.val)
                l1 = l1.next
            else:
                min_node = ListNode(l2.val)
                l2 = l2.next
        
            # append minimum to res
            if res is None:
                res = min_node
            else:
                res.next = min_node
                res = res.next         
        
        # append remaining list items from list1 or list2
        if l1:
            if res is None:
                res = l1
            else:
                res.next = l1
        
        if l2:
            if res is None:
                res = l2
            else:
                res.next = l2
        
        return res_head
