from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 文字列の長さ判定
        if len(s) != len(t):
            return False
        # 文字列をソートして判定 True or False
        return sorted(s) == sorted(t)
