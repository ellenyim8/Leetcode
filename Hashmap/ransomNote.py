# 383) Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}

        for letter in magazine:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        print(letters)

        for letter in ransomNote:
            if letter in letters:
                letters[letter] -= 1
                if letters[letter] < 0:
                    return False
            elif letter not in letters:
                return False

        return True
        
