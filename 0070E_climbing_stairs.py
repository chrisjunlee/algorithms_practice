class Solution:
    def climbStairs(self, n: int) -> int:
	dp = [0 for x in range(n + 1)]
	dp[0], dp[1] = 1, 1

	for step in range(2, n + 1):
	 dp[step] = dp[step - 1] + dp[step - 2]

	return dp[n]
