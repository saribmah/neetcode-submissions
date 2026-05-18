class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_two = 0
        prev_one = 0

        curr = 0

        for i in range(len(nums)):
            curr = max(prev_one, nums[i] + prev_two)
            temp = prev_one
            prev_one = curr
            prev_two = temp

        return curr