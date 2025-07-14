class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # position = set()
        # len_ransom = len(ransomNote)

        # for char in ransomNote:
        #     for j in range(len(magazine)):
        #         if char == magazine[j] and (j not in position):
        #             print(char, magazine[j])
        #             position.add(j)
        #             if len(position) == len_ransom:
        #                 return True
        #             else:
        #                 break

        # return True if len(position) == len(ransomNote) else False

        counter = {}

        for c in magazine:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1

        for c in ransomNote:
            if c in counter and counter[c] == 1:
                del counter[c]
            elif c in counter:
                counter[c] -= 1
            else:
                return False
        
        return True
                    

        