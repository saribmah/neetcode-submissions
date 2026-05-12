class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ledger = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in ledger:
                return [ledger[remainder], i]
            ledger[nums[i]] = i;
        return []