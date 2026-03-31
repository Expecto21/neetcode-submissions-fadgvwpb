class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        mySet=set()

        for num in nums:
            if num in mySet:
                dup=True
                break
            else:
                mySet.add(num)
        return dup
