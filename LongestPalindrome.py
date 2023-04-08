# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        LEN = len(s)
        dp = [[False for c in range(LEN)] for r in range(LEN)]
        mLength = 1
        mString = s[0]
        for i in range(LEN):
            dp[i][i] = True
        for i in range(LEN - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                mString = s[i:i+2]
        for l in range(2, LEN):
            for i in range(LEN - l):
                length = l + 1
                j = i + l
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    mLength = length
                    mString = s[i:j+1]
                    continue
        return mString
