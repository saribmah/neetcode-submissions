class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for index, num in enumerate(nums):
            remainder = target-num
            if remainder in hmap:
                return [hmap[remainder], index]
            hmap[num] = index

        return []
        