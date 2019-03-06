from collections import defaultdict
class Solution:
    # greedy algorithm
    def jump(self, nums: List[int]) -> int:
        N, count = len(nums), 0
        if N <= 1:
            return count

        # find max within jump range
        index = 0
        max_index = 0

        while index < N:
            max_jump = 0
            for i in range(index + 1, index + nums[index] + 1):
                if index + nums[index] >= N - 1:
                    max_index = N
                    break

                # find max. 
                # tricky 1: be sure to check for i + nums[i], not nums[i]! i -> next, not i
                # tricky 2: be sure to be using >=. Otherwise you can be stuck in same position
                if nums[i] + i >= max_jump:
                    max_jump = nums[i] + i
                    max_index = i
            index = max_index
            count += 1

        return count



    # dp solution: TLE, 91/92 test cases
    def dp_jump(self, nums: List[int]) -> int:
        dp = collections.defaultdict(lambda: float("inf"))
        dp[0] = 0

        N = len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if j - i <= nums[i]:
                    dp[j] = min(dp[j], 1 + dp[i])
                else:
                    # distance from here one will be too far
                    break

        return dp[N - 1]

