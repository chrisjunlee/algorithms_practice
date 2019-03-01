import collections
# 100% faster than all submissions!
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        row_count = collections.defaultdict(lambda: 0)
        col_count = collections.defaultdict(lambda: 0)
        x_diff_y = collections.defaultdict(lambda: 0)
        x_plus_y = collections.defaultdict(lambda: 0)

        lamps_set = {(x, y) for [x, y] in lamps}

        for [x, y] in lamps:
            row_count[x] += 1
            col_count[y] += 1
            x_diff_y[x - y] += 1
            x_plus_y[x + y] += 1

        for query in queries:
            res.append(light_check(lamps_set, row_count, col_count, x_diff_y, x_plus_y, *query))
            splash_off(N, lamps_set, row_count, col_count, x_diff_y, x_plus_y, *query)

        return res

def light_check(lamps, row_count, col_count, x_diff_y, x_plus_y, row, col):
    if row in row_count or col in col_count:
        return 1

    if (row + col) in x_plus_y or (row - col) in x_diff_y:
        return 1

    return 0

def splash_off(N, lamps, row_count, col_count, x_diff_y, x_plus_y, row, col):
    row_min = 0 if row == 0 else row - 1
    row_max = N - 1 if row == N - 1 else row + 1
    col_min = 0 if col == 0 else col - 1
    col_max = N - 1 if col == N - 1 else col + 1

    for i in range(row_min, row_max + 1):
        for j in range(col_min, col_max + 1):
            if (i, j) in lamps:
                lamps.discard((i, j))
                _decrement(row_count, i)
                _decrement(col_count, j)
                _decrement(x_diff_y, i - j)
                _decrement(x_plus_y, i + j)

def _decrement(table, index):
    table[index] -= 1

    if table[index] == 0:
        del table[index]
    return
