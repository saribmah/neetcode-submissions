class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count = {}
        for w in s:
            if w not in word_count:
                word_count[w] = 0
            word_count[w] += 1
        for w in t:
            if w in word_count:
                word_count[w] -= 1
            else:
                return False
        if set(word_count.values()) == {0}:
            return True
        return False