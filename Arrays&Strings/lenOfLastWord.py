# 58) Length of last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list() 
        a = 0
        l = s.strip()
        for i in range(len(l)):
            if l[i] == " ":
                a = 0 
            else:
                a += 1 

        return a 
    