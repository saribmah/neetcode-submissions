class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            print(count)
            v = ",".join(str(x) for x in count) 
            if v not in hmap:
                hmap[v] = []
            hmap[v].append(s)

        return list(hmap.values())