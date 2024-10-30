from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keyとvalueになってる 例: {7 : 0}
        #! indexがvalueでindexの値がkeyなので注意
        hashmap = {}
        
        # 0からnumsまでループ
        for i in range(len(nums)):
            num = nums[i] # numsの値
            complement = target - num # 欲しい値からnumを引いた
            if num in hashmap: # hashmapにnumがある場合
                return [hashmap[num],i] #
            else: # 無い場合
                hashmap[complement] = i
                print(hashmap)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 17
    print(s.twoSum(nums, target))  # Output: [0, 1]