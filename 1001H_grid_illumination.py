class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        lamps_set = {(row, col) for [row, col] in lamps}

        for query in queries:
            res.append(light_check(lamps_set, *query))
            splash_off(lamps_set, *query)

        return res

def light_check(lamps, row, col):
    for (i, j) in lamps:
        if i == row or j == col:
            return 1

        if abs(i - row) == abs(j - col):
            return 1

    return 0

def splash_off(lamps, row, col):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            lamps.discard((i,j))
    return
