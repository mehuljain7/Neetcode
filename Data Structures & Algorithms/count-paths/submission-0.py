class Solution:
    def rec(self, i, j, m, n):
        if i == m - 1 and j == n - 1:
            return 1
        if i not in range(0, m) or j not in range(0, n):
            return 0
        down = self.rec(i + 1, j, m, n)
        right = self.rec(i, j + 1, m, n)
        return down + right
    def mem(self, i, j, m, n, dp = {}):
        if i == m - 1 and j == n - 1:
            return 1
        if i not in range(0, m) or j not in range(0, n):
            return 0
        down = self.mem(i + 1, j, m, n, dp)
        right = self.mem(i, j + 1, m, n, dp)
        dp[(i, j)] = down + right
        return dp[(i, j)]
    def tab(self, m, n):
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                dp[i][j] = up + left
        return dp[-1][-1]
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.rec(0, 0, m, n)
        # return self.mem(0, 0, m, n)
        return self.tab(m, n)