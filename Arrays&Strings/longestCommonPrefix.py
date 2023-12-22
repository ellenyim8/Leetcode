# 14) Longest Common Prefix 

from collections import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0: return ""

        minLen = len(strs[0])

        for s in strs:
            minLen = min(minLen, len(s))

        res = ""
        for i in range(minLen):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur:
                    return res 
            res += cur 

        return res 
    