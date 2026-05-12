class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #For strings of length 0 and 1
        if (len(s) < 2): return len(s)
        char_count = {}
        maxF = 0
        l=0
        res = 0

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            maxF = max(maxF, char_count[s[r]])
            print(maxF)

            while (r-l+1) - maxF > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

"""
len(s) = 7
s = "AAABABB"
     0123456
l = 2
r = 5
max_substr = 3
k = 0

char_count = {A:1,B:1}
"""