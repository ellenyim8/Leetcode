# 9) Palindrome number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10 and x > -1:          # single digit number r not palindrome
            return True
        if x < 0:       # negative numbers are not palindrome
            return False
        
        # if divisible by 10 then not palindrome
        if x % 10 == 0:
            return False 
        
        palin = 0
        while (x > palin):
            n = x % 10
            x = x / 10
            palin = (palin * 10) + n
            
        if x == palin or x == palin / 10:
            return True
        else:
            return False
