# This version times out. Runtime 306ms vs next iteration's 108ms

class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        # longest contiguous subarray composed of 2 unique elements
        left, right = 0, 0
        tree_count = dict()
        unique_count = 0
        length, max_length = 0, 0
        
        if tree:
            tree_count[tree[0]] = 1
            length += 1
            
        if len(tree) <= 2:
            return len(tree)
        
        # sliding window
        while left <= right:
            unique_count = [v > 0 for k, v in tree_count.items()].count(True)
            
            if unique_count <= 2:
                length = right - left + 1
                max_length = max(max_length, length)
                
                if right == len(tree) - 1:
                    break;
                    
                right += 1
                tree_count[tree[right]] = tree_count.get(tree[right], 0) + 1
            else:                
                tree_count[tree[left]] = tree_count.get(tree[left], 0) - 1
                left += 1
                length -= 1
        return max_length
