from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    list = []
    for i in range(0, len(nums)):
      if nums[i] != val:
        list.append(nums[i])
      else:
        print(list)
    return len(list)

if __name__ == "__main__":
   s = Solution()
   print(s.removeElement([3,2,2,3], 3))  # Output: 2