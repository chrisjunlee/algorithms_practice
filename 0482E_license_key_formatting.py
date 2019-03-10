class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S:
            return S

        S = S.replace("-", "").upper()[::-1]
        res = []

        for i in range(0, len(S), K):
            res.append(S[i : i+K])

        return "-".join(res)[::-1]
