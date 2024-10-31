class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for char in s.rsplit(" ")[::-1]:
            if(len(char) != 0):
                return len(char)

if __name__ == "__main__":
  s = Solution()
  print(s.lengthOfLastWord("Hello World"))  # Output: 5
  print(s.lengthOfLastWord("a "))  # Output: 1
  print(s.lengthOfLastWord(" "))  # Output: 0
  print(s.lengthOfLastWord("I am a programmer"))  # Output: 9
  print(s.lengthOfLastWord("I am a"))  # Output: 2