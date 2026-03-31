class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        mySet=set(nums)
        
        longestLength=0

        for n in mySet:
            if n-1 not in mySet:
                length=1
                
                while (n+length) in mySet:
                    print(n+length)
                    length+=1
                   
                longestLength=max(length,longestLength)
        
        return longestLength
            
