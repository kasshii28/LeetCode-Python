class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_A = list(a)[::-1]
        list_B = list(b)[::-1]
        result = []
        i=0
        while list_A and list_B:
          if (list_A[i] + list_B[i] == 2):
            return
        print(list_A, list_B)

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('10', '01'))  # Output: '100'