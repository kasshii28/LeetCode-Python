class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        # 要素-1までループ
        for i in range(len(s) - 1):
            # ローマ数字は"IV"のように小さい値の次に大きい値が来るとき
            # 小さい値を引くことで求めれる
            # 大きい値の次が小さい値の時はそのまま足す
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
            # 最後は次の値が無いのでそのまま足す
        return total + roman[s[-1]]

# best guess
class BestSolution:
    def romanToInt(self, s:str) -> int:
      roman = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000,
      }

      #romanToIntというfunctionは、number型で返される。この関数で使われる引数sはstring型である。
      integers = [roman[c] for c in s]
      return sum(-x if x < integers[i + 1] else x for i, x in enumerate(integers[:-1])) + integers[-1]
      # integers[:-1]では最後の要素を除外したリストを生成し、enumerateでインデックスと値を取り出します。
      # 現在の値が次の値より小さい場合、負の数として加算。
      # 最後の値（integers[-1]）はそのまま加算します。

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))  # Output: 3
    print(s.romanToInt('MCMXCIV'))  # Output: 4

    b = BestSolution()
    print(b.romanToInt('III'))  # Output: 3
    print(b.romanToInt('MCMXCIV'))  # Output: 4