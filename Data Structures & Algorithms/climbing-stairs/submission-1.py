class Solution:
    def climbStairs(self, n: int) -> int:
        ways_mapping = {}
        def dfs(curr):
            if curr < 0: return 0

            if curr == 0: return 1

            if curr in ways_mapping:
                return ways_mapping[curr]

            ways_mapping[curr] = dfs(curr-1) + dfs(curr-2)

            return ways_mapping[curr]

        return dfs(n)