class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        max_str = 0

        chr_count = {}

        while r < len(s):
            chr_count[s[r]] = 1 + chr_count.get(s[r], 0)
            while chr_count[s[r]] > 1:
                chr_count[s[l]] -= 1
                l += 1
            max_str = max(r-l+1, max_str)
            r += 1
        return max_str

"""
s = zxyzxyz
l = 2
r = 5
max_str = 3
len(s) = 7

char_count = {z:1,x:1,y:1}


"""