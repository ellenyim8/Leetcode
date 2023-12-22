# 66) Plus one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        d = '' 
        for x in digits:
            d += str(x) 

        d = int(d) 
        d += 1 
        d = str(d) 
        res = []

        for c in range(len(d)):
            res.append(int(d[c]))
        return res
