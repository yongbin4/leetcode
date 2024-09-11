class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_words = ""
        if (len(word1) > len(word2)):
            for i in range(len(word1)):
                merged_words += word1[i]
                try:
                    merged_words += word2[i]
                except:
                    pass
        else:
            for i in range(len(word2)):
                try:
                    merged_words += word1[i]
                except:
                    pass
                merged_words += word2[i]
        return merged_words