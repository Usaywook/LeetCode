class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dp(m, n):
            if (m,n) in cache:
                return cache[(m,n)]
            if m==0 or n==0:
                return 0
            
            ans = dp(m-1, n-1) + 1 if text1[m-1] == text2[n-1] else max(dp(m-1, n), dp(m, n-1))                
            cache[(m,n)] = ans
            return ans
        
        return dp(len(text1), len(text2))