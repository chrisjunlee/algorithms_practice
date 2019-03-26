class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        M, N = len(grid), len(grid[0])

        # max height = min(max_col, max_row)

        # max_col
        max_col = [0 for col in range(N)]
        for col in range(N):
            max_col[col] = max([grid[row][col] for row in range(M)])

        # max_row
        max_row = [0 for row in range(M)]
        for row in range(M):
            max_row[row] = max([grid[row][col] for col in range(N)])

        max_sum = 0

        for row in range(M):
            for col in range(N):
                pot_height = min(max_col[col], max_row[row])
                max_sum += max(pot_height - grid[row][col], 0)

        return max_sum
