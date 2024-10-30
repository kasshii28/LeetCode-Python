# 文字列変換なしver
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # xが0とxが0以外の時に10で割りきれるものは回文ではない
        if x < 0 or (x != 0 and x % 10 == 0):
          return False
        
        half = 0
        while x > half:
            print(half*10)
            print(x%10)
            half = (half * 10) + (x % 10)
            x = x // 10
            print(half, x)
        return x == half or x == half // 10

class StrSolution:
    def isPalindrome(self, x:int) -> bool:
      # [::-1]で配列を反転
      return False if x < 0 else str(x) == str(x)[::-1]

if __name__ == '__main__':
    s = Solution()
    str = StrSolution()
    print(s.isPalindrome(515))  # True
    print(s.isPalindrome(552))  # False

    print(str.isPalindrome(515))  # True
    print(str.isPalindrome(552))  # False