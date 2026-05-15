class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        seen = set()

        def dfs(r, c, index):
            if index >= len(word): return True
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in seen:
                return False

            seen.add((r,c))
            exists = False
            if board[r][c] == word[index]:
                exists = (dfs(r+1, c, index+1) or
                    dfs(r-1, c, index+1) or
                    dfs(r, c+1, index+1) or
                    dfs(r, c-1, index+1))

            seen.remove((r,c))

            return exists 

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    print(seen)
                    if dfs(i, j, 0):
                        return True

        return False