class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0

        nums.sort()

        i, diff = 0, 0
        while i < N - 1:
            diff = max(diff, abs(nums[i] - nums[i+1]))
            i += 1

        return diff


