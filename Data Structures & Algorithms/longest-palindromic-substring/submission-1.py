class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest(left,right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        res = ""

        for i in range(len(s)):
            odd = longest(i,i)
            even = longest(i,i+1)
            curr = even
            if len(odd) > len(even):
                curr = odd
            if len(curr) > len(res):
                res = curr 

        return res