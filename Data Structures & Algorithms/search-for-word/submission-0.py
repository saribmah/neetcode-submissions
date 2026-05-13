class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        paths = set()
        def dfs(r,c,i):
            if i == len(word):
                return True

            if (min(r,c) < 0 or
                r >= rows or 
                c >= cols or
                (r,c) in paths or
                board[r][c] != word[i]):
                return False

            paths.add((r,c))
            res = (dfs(r+1, c, i+1) or
                dfs(r-1,c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))

            paths.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True

        return False