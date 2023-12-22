# 49) Group Anagrams

from collections import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res = []
        
        def createAnagramKey(s):
            # s: str
            key = ''
            for ch in sorted(s):
                key += ch
            return str(key)
        
        def groupAnagrams(keys):
            group = dict()
            for k in keys:
                if group.get(createAnagramKey(k)) == None:
                    group[createAnagramKey(k)] = [k]
                else:
                    group[createAnagramKey(k)].append(k)

            return group
        
        anagrams = groupAnagrams(strs)
        res = list()
        
        for key, value in anagrams.items():
            res.append(value)
        
        return res

    
