class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)
        memo = [[0]*(N+1) for _ in range(M+1)]
        for i in range(1,M+1):
            for j in range(1,N+1):                        
                memo[i][j] = memo[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(memo[i-1][j], memo[i][j-1])
        return memo[M][N]