class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        words = []
        for character in s:
            if character != " ":
                temp += character
            elif temp != "":
                words.append(temp)
                temp = ""
        if temp != "":
            words.append(temp)
        return " ".join(words[::-1])