from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])

        for word in strs:
            key = ''.join(sorted(list(word)))
            groups[key] += [word]

        return list(groups.values())

