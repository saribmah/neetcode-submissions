class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        prev_two = 0
        prev_one = 0

        for i in range(len(nums)):
            curr = max(prev_one, nums[i] + prev_two)
            prev_two = prev_one
            prev_one = curr

        return prev_one