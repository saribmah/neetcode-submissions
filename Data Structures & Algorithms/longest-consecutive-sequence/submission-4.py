class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0
        nums.sort()
        longest_seq = 0
        best_seq = 0
        print(nums)
        for i in range(len(nums)-1):
            print(f"checking {nums[i]} and {nums[i+1]}")
            if nums[i] == nums[i+1]:
                pass
            elif nums[i] + 1 == nums[i+1]:
                longest_seq += 1
            else:
                best_seq = max(longest_seq+1, best_seq)
                longest_seq = 0
        best_seq = max(longest_seq+1, best_seq)
        return best_seq