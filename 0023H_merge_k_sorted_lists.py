# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # k-list comparison: 4204ms!
    def mergeKLists_v1(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return []

        res = ListNode(0)
        res_head = res

        lists = [node for node in lists if node != None]

        while lists:
            min_val, min_index = lists[0].val, 0

            # finding minimum
            for i, nodelist in enumerate(lists):
                if nodelist.val <= min_val:
                    min_val = nodelist.val
                    min_index = i
            res.next = lists[min_index]
            res = res.next

            lists[min_index] = lists[min_index].next

            if lists[min_index] is None:
                del lists[min_index] 

        return res_head.next

    # with k-heap: 
    #   76ms with reference counting
    #   104ms with any() while condition
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = ListNode(0)
        res_head = res

        if lists == []:
            return []

        # input rinsing 
        lists = [x for x in lists if x is not None]

        minheap = []
        for i, node in enumerate(lists):
            heapq.heappush(minheap, (node.val, i))

        # tricky. Was going with "while lists:" but modifying lists results in index invalidation!

        # method 1: while any(n is not None for n in lists):
        # method 2: faster, but tricky: ref counter. We make sure to only have one item from each list in heap.
        # count = len(lists)
        # while count > 0:
        while any(n is not None for n in lists):  
            min_val, ind = heapq.heappop(minheap)
            res.next = lists[ind]
            res = res.next

            lists[ind] = lists[ind].next
            if lists[ind]:
                heapq.heappush(minheap, (lists[ind].val, ind))

        return res_head.next
