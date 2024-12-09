from collections import Counter, defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        count_dict = defaultdict(list)

        for k,v in count.items():
            count_dict[k].append(v)
        k_max_count
        # mostNums = count.most_common(k)
        # for k ,_ in mostNums:
        #     res.append(k)
        # return res
            