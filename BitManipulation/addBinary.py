# 67) Add Binary 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        m = len(a) - 1
        n = len(b) - 1 
        while m >= 0 or n >= 0 or carry:
            if m >= 0:
                carry += int(a[m])
                m -= 1
            if n >= 0:
                carry += int(b[n])
                n -= 1 

            res.append(str(carry % 2)) 
            carry //= 2 
        
        return ''.join(res[::-1])
    
