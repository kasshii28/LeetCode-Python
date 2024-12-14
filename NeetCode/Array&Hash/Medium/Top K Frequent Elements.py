from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        #各値をkey、出現回数をvalueとしたオブジェクトを生成
        count = Counter(nums)
        
        # countから降順でk個取り出す
        mostNums = count.most_common(k)
        # mostNumesからkeyだけを取り出して配列に追加
        for k ,_ in mostNums:
            res.append(k)
        return res
            