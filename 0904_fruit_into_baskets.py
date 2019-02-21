from collections import defaultdict
class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        length, max_length = 0, 0
        tree_count = defaultdict(lambda: 0)
        uniq_count = 0
        left = 0
        
        for right, fruit in enumerate(tree):
            tree_count[fruit] += 1
            uniq_count = len([v for v in tree_count.values() if v > 0])
            
            if uniq_count <= 2:
                length += 1
                max_length = max(max_length, length)
            else:
                tree_count[tree[left]] -= 1
                left += 1
        
        return max_length
