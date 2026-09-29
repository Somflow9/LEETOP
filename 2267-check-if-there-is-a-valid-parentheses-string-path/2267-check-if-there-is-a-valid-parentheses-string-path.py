class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Path length is m + n - 1, must be even for valid parentheses
        if (m + n - 1) % 2 == 1:
            return False
        
        # Start must be '(' and end must be ')'
        if grid[0][0] != '(' or grid[m-1][n-1] != ')':
            return False
        
        memo = {}
        
        def dfs(i, j, balance):
            # balance = count of '(' minus count of ')'
            # If balance < 0, we have more ')' than '(', invalid
            if balance < 0:
                return False
            
            # If balance is too large, we can't close them all
            remaining = (m - 1 - i) + (n - 1 - j)
            if balance > remaining:
                return False
            
            # Reached the end
            if i == m - 1 and j == n - 1:
                return balance == 0
            
            # Check memo
            if (i, j, balance) in memo:
                return memo[(i, j, balance)]
            
            result = False
            
            # Try going down
            if i + 1 < m:
                next_char = grid[i + 1][j]
                new_balance = balance + (1 if next_char == '(' else -1)
                if dfs(i + 1, j, new_balance):
                    result = True
            
            # Try going right
            if not result and j + 1 < n:
                next_char = grid[i][j + 1]
                new_balance = balance + (1 if next_char == '(' else -1)
                if dfs(i, j + 1, new_balance):
                    result = True
            
            memo[(i, j, balance)] = result
            return result
        
        # Start at (0,0) with balance = 1
        return dfs(0, 0, 1)
        