from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = ""
        for num in digits:
            total += str(num)
        total = int(total) + 1
        return [int(num) for num in list(str(total))]

if __name__ == "__main__":
  s = Solution()
  print(s.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
  print(s.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
  print(s.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]