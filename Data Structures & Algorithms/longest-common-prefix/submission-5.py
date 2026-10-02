class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        j = 0

        while True:
            if j >= len(strs[0]):
                return out
            for i in range(1, len(strs)):
                if j >= len(strs[i]):
                    return out
                if strs[i][j] != strs[0][j]:
                    return out
            out = out + strs[0][j]
            j = j + 1
