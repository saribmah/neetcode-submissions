class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 0
            hmap[c] += 1

        for c in t:
            if c not in hmap:
                return False
            hmap[c] -= 1
            if hmap[c] == 0:
                del hmap[c]
        return False if len(hmap) > 0 else True