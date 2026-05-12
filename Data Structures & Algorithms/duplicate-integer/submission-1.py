class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = set()
        for index,value in enumerate(nums):
            if value in history:
                return True
            history.add(value)
        return False