class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        res = []
        for index, key in enumerate(sorted_frequency):
            if index < k:
                res.append(key)
            else:
                break
        return res