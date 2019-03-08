class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0 for i in range(len(height))]
        rmax = [0 for i in range(len(height))]

        maxh = 0
        for i, h in enumerate(height):
            maxh = max(maxh, h)
            lmax[i] = maxh

        maxh = 0
        for i, h in enumerate(height[::-1]):
            maxh = max(maxh, h)
            rmax[len(height) - 1 - i] = maxh

        res = 0
        for i, curr in enumerate(height):
            vol = min(lmax[i], rmax[i]) - curr

            res += vol if vol >= 0 else 0

        return res
