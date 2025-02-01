class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        M = amount    
        memo = [[1]*(M+1) for _ in range(N+1)]
        memo[0][1:] = [0]*M
        
        for i in range(1, N+1):
            for j in range(1, M+1):
                k = j - coins[i-1]
                memo[i][j] = memo[i-1][j]
                if k < 0:
                    continue
                memo[i][j] += memo[i][k]
            
        return memo[-1][-1]