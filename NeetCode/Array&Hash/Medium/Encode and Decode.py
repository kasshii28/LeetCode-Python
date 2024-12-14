from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#neet4#code4#love3#you のような形式でencodeする
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l =  int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j
        return res