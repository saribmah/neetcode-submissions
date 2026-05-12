class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        total_strs = len(strs)
        encoded_str += str(total_strs) if total_strs >=10 else '0' + str(total_strs)
        print(encoded_str)
        for s in strs:
            lens = len(s);
            if lens < 10:
                encoded_str += '00' + str(lens)
            elif lens < 100:
                encoded_str += '0' + str(lens)
            else:
                encoded_str += str(lens)
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        total_strs = int(s[0:2])
        s = s[2:]
        res = []
        for i in range(total_strs):
            lens = int(s[0:3])
            s = s[3:]
            res.append(s[0:lens])
            s = s[lens:]
        return res