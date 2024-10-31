from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

if __name__ == '__main__':
  s = Solution()
  print(s.searchInsert([1, 3, 5, 6], 5))  # Output: 2
  print(s.searchInsert([1, 3, 5, 6], 2))  # Output: 1
  print(s.searchInsert([1, 3, 5, 6], 7))  # Output: 4
  print(s.searchInsert([1, 3, 5, 6], 0))  # Output: 0