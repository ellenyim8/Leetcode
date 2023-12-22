# 125) Valid Palindrome

import re
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        # two pointers
        st = re.compile('[%s]' % re.escape(string.punctuation))
        new_s = st.sub('', s)
        new_s = new_s.split(' ')
        new_s = ''.join(new_s)
        new_s = new_s.lower()
        print(new_s)

        n = len(new_s)
        #n = len(s)
        left = 0
        right = n - 1

        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        return True
    