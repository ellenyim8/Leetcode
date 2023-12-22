# 290) Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = dict()
        charMatched = set()
        wordMatched = set()
        
        i = 0
        s = s.split(' ')
        
        if len(pattern) != len(s):
            return False
        
        for char in pattern:
            if char not in hashmap:
                if char in charMatched or s[i] in wordMatched:
                    return False
                
                hashmap[char] = s[i]
                charMatched.add(char)
                wordMatched.add(s[i])
            else:
                if hashmap[char] != s[i]:
                    return False
                
            i += 1
        
        return True

