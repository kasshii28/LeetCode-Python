from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    list = []
    for i in range(0, len(nums)):
      num = nums[i]
      if num in list:
        continue
      else:
        list.append(num)
    return len(list)

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))  # Output: 2