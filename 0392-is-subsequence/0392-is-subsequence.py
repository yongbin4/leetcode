class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # use two pointer: one for s and one for t
        # we compare each index in s and t until we find the same char
        # until length of t
        # if length of s_index is same as length of s, it is true otherwise false

        s_index = 0

        for i in range(len(t)):
            if s_index == len(s):
                break
            elif s[s_index] == t[i]:
                s_index += 1
            else:
                pass
        return True if s_index == len(s) else False



        # Go through string t
        # if character in string t exist in string s we append to the result string
        # we compare it with string s
        # return true if string output and string s is equivant otherwise false
        output = ""
        for char in t:
            if char in s:
                output += char
            else:
                pass
        print(output)
        return True if s in output or output == s else False


                

        