class Solution(object):
  def isValid(self, s):
    for i in range(len(s)):
      s = s.replace('{}', '').replace('[]', '').replace('()', '')
    return s == ''

if __name__ == '__main__':
  s = Solution()
  print(s.isValid('()'))  # True
  print(s.isValid('()[]{}'))  # True
  print(s.isValid('(]'))  # False
  print(s.isValid('([)]'))  # False
  print(s.isValid('{[]}'))  # True
  print(s.isValid('([)]'))  # False
  print(s.isValid(']'))  # False