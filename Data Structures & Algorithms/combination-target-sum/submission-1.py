class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index: int, nums: List[int], stack: List[int], target: int):
            if target == 0:
                res.append(stack.copy())
                return

            if index >= len(nums) or target < 0: return

            stack.append(nums[index])
            dfs(index, nums, stack, target-nums[index])
            stack.pop()
            dfs(index+1, nums, stack, target)

        dfs(0, nums, [], target)

        return res