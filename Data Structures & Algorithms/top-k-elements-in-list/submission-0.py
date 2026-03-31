from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter=Counter(nums)
        counts=myCounter.most_common(k)
        myList=[i[0] for i in counts]
        return myList
        
       