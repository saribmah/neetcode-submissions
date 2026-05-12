class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}
        for i in range(len(nums)):
            twoSums = self.twoSum(nums[i+1:], -nums[i])
            for s in twoSums:
                s.append(nums[i])
                s.sort()
                res[','.join(map(str, s))] = s
        return list(res.values())

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashm = {}
        res = []
        for i in range(len(nums)):
            hashm[nums[i]] = i
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashm and hashm[remainder] > i:
                res.append([nums[i], remainder])
        return res