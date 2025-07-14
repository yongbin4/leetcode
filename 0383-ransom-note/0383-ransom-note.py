class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        position = set()
        len_ransom = len(ransomNote)

        for char in ransomNote:
            for j in range(len(magazine)):
                if char == magazine[j] and (j not in position):
                    print(char, magazine[j])
                    position.add(j)
                    if len(position) == len_ransom:
                        return True
                    else:
                        break

        return True if len(position) == len(ransomNote) else False
                    

        