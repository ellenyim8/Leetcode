# 205 isomorphic strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # len(s) == len(t)

        hashmap = dict()
        mapChars = set()

        for i in range(len(s)):
            if s[i] not in hashmap:
                # check if t[i] is already mapped
                if t[i] in mapChars:
                    return False
                
                hashmap[s[i]] = t[i]
                mapChars.add(t[i]) 
            else:
                # print(hashmap[s[i]])
                # print(t[i])
                if hashmap[s[i]] != t[i]:
                    return False

        return True

