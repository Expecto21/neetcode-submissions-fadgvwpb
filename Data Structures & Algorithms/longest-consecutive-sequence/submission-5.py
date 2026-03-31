class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        mySet=set(nums)
        myList=list(mySet)
        longestLength=0

        for n in range(len(myList)):
            if myList[n]-1 not in mySet:
                length=1
                curr=myList[n]
                while curr+1 in mySet:
                    print(curr)
                    length+=1
                    curr+=1
                longestLength=max(length,longestLength)
        
        return longestLength
            
