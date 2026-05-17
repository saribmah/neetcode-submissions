class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, seen = set(), set()

        def dfs(r,c,node,word):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in seen or board[r][c] not in node.children:
                return

            seen.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.eow:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            seen.remove((r,c))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(res)