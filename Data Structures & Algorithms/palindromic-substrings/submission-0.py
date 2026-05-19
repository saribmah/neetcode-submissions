class Solution:
    def countSubstrings(self, s: str) -> int:
        nop = 0
        def longest(l,r):
            nonlocal nop
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nop += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            longest(i,i)
            longest(i, i+1)

        return nop