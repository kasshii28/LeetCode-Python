from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tmp = []
        for i in range(len(nums)):
            value = 1
            tmp.append(nums[i])
            nums.pop(i)
            for j in range(len(nums)):
                value *= nums[j]
            res.append(value)
            nums.insert(i,tmp[i])
        return res