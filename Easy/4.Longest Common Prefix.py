from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ""
    ans = ""

    # zip関数で全文字列の0番目から文字を取得
    for num in zip(*strs):
      print(num)
      # setでnumの集合を取るので、全て同じ文字なら1文字しか入らない
      # なのでlenが1になる
      if len(set(num)) == 1:
        ans += num[0]
      else:
        return ans
    return ans

strs = ["flower","flow","flight"]

s = Solution()

print(s.longestCommonPrefix(strs))