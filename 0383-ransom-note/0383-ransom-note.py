class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        for letter in ransomNote:
            if letter in magazine:
                result = True
                magazine = magazine.replace(letter, "", 1)
            else:
                result = False
                return result
        return result
