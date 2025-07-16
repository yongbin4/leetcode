class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # need to process the string into a alphanumeric or if alphanumeric we proceed
        # isalnum()
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
            else:
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
        return True

