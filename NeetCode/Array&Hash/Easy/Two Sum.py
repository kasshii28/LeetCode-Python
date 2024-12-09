from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(0, len(nums)):
            num = nums[i]
            # 0になる値を計算
            ans = target - num
            # numがhashにあれば
            # 値のindexと現在のindexを返す
            if num in hash:
                return [hash[num], i]
            # なければhashに追加
            else:
                hash[ans] = i
