class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        b_map = {num: i for i, num in enumerate(B)}
        return [b_map[num] for num in A]
