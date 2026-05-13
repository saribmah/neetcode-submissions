class Solution:
    def minWindow(self, s: str, t: str) -> str:
        desired_len = len(set(t))
        shortest_str = ""

        for i in range(len(s)):
            ch = s[i]

            if ch in t:
                ch_set = self.getMap(t)
                for j in range(i, len(s)):
                    if s[j] in ch_set and ch_set[s[j]] != 0:
                        ch_set[s[j]] -= 1
                    if sum(ch_set.values()) == 0:
                        if len(shortest_str) == 0 or len(shortest_str) > j-i+1:
                            shortest_str = s[i:j+1]
                        break
        return shortest_str

    def getMap(self, t: str):
        m = {}
        for i in t:
            m[i] = 1 + m.get(i, 0)

        return m