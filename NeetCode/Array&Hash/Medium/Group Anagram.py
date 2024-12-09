from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # listが1以下の場合list返す
        if len(strs) <= 1:
            return [strs]
        
        # アナグラムをkeyにもつ辞書の初期化
        groupList = defaultdict(list)
        for str in strs:
            # ソートした文字列を繋げてkeyにする
            # keyのリストに文字列を追加
            groupList[''.join(sorted(str))].append(str)
        # valueを全て返す
        return groupList.values()