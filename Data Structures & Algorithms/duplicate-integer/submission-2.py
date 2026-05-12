class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index,value in enumerate(nums):
            if index > 0 and nums[index-1] == value:
                return True
        return False