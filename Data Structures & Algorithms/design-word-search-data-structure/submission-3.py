class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root

        return self.search_word(word, curr)

    def search_word(self, word: str, curr: TrieNode) -> bool:
        if not word and curr.eow: return True

        if not word: return False

        c = word[0]

        if c in curr.children:
            return self.search_word(word[1:], curr.children[c])
        elif c == ".":
            # search in all children
            for child in curr.children:
                if self.search_word(word[1:], curr.children[child]):
                    return True
        return False