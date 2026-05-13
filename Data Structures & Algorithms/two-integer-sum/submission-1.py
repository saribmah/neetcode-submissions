class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hmap:
                return [hmap[remainder], i]
            else:
                hmap[nums[i]] = i
        return []