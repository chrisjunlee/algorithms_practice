class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        res = ""

        for char in S:
            if char == "(":
                if count > 0:
                    res += char
                count += 1
            else:
                if count > 1:
                    res += char
                count -= 1
        return res
