# 151) Reverse words in a string

class Solution:
    def reverseWords(self, s: str) -> str:
        rev = " ".join(s.split()[::-1])
        return rev
    