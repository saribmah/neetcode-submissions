class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in hmap:
                hmap[key] = []
            hmap[key].append(s)

        return list(hmap.values())