class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashm = {}
        for i in range(len(nums)):
            hashm[nums[i]] = i
        longest_seq = 0
        best_seq = 0
        for i in range(len(nums)):
            if nums[i] not in hashm: continue
            key = nums[i]
            if nums[i]-1 in hashm: continue
            while key in hashm:
                index = hashm[key]
                longest_seq += 1
                del hashm[key]
                key = nums[index] + 1
            best_seq = max(longest_seq, best_seq)
            longest_seq = 0
        return best_seq