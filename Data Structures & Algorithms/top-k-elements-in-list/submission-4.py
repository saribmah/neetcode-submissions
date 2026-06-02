class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hmap.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)

        return res
