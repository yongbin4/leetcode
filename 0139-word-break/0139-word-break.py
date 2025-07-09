class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 0 - 7
        n = len(s)
        # 0 - 8
        dp = [False] * (n + 1)
        dp[0] = True

        # i: 1 - 8
        for i in range(1, n + 1):
            # j: 0 - 7
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1] 


        

        return dp[-1]
