class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n)
        
        for i in range(1, n + 1):
        # First check if s[0:i+1] is directly in dictionary
            if s[0:i] in wordDict:
                dp[i-1] = True
                continue
            
            # Otherwise, check all possible split points j before position i
            for j in range(1,i):
                # If s[0:j+1] can be segmented AND s[j+1:i+1] is a valid word
                if dp[j-1] and s[j:i] in wordDict:
                    dp[i-1] = True
                    break

        return dp[-1]
