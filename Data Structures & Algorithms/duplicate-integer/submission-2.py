from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        myCounter=Counter(nums)
        print(myCounter)
        i=0
        for key in myCounter:
            if myCounter[key]>1:
                dup=True
                break
            i+=1

        return dup
