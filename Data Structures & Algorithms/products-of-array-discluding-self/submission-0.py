class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total_product = 1
        total_zeros = 0
        for num in nums:
            if num == 0:
                total_zeros += 1
            else:
                total_product *= num
        if total_zeros > 1:
            return [0] * len(nums)
        for num in nums:
            if total_zeros > 0:
                if num == 0:
                    res.append(total_product)
                else:
                    res.append(0)
            else:
                res.append(int(total_product/num))
        return res