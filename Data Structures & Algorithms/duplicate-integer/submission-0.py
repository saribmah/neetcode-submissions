class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = {}
        for index,value in enumerate(nums):
            if value in history:
                return True
            history[value] = index
        return False